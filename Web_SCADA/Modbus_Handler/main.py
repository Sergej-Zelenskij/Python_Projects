#_*_ coding: cp1251 _*_
from opcua import ua, Server, Client
from concurrent.futures import ThreadPoolExecutor
import modbus_tk
import modbus_tk.defines as cst
import modbus_tk.modbus_tcp as modbus_tcp
import confluent_kafka
config = {
    'bootstrap.servers': 'localhost:9092',    
    'group.id': 'mygroup',
    'auto.offset.reset': 'earliest'}
producer = confluent_kafka.Producer(config)
consumer = confluent_kafka.Consumer(config)
consumer.subscribe(['WA2','WA3','WA4','WA5','WA6','WA7','WA8','WA9'])
Signals_Last_State = [0,0,0,0,0,0,0,0]
server = Server()
Start_Flag_Read = False
server.set_endpoint("opc.tcp://127.0.0.1:4840")
server.set_server_name("FlowHandler")
uri = "http://FlowHandler"
idx = server.register_namespace(uri)
Node_1 = server.get_objects_node()
Device_1 = Node_1.add_object(idx, "110")
def StructCreator(Device_Name, Var_Name, Namespace):                        # Создание тегов ОПС
    return Device_Name.add_variable(Namespace, Var_Name, 0)
DO1_Set = StructCreator(Device_1, "DO1", idx)
DO1_Set.set_writable()
DO2_Set = StructCreator(Device_1, "DO2", idx)
DO2_Set.set_writable()
DO3_Set = StructCreator(Device_1, "DO3", idx)
DO3_Set.set_writable()
DO4_Set = StructCreator(Device_1, "DO4", idx)
DO4_Set.set_writable()
DO5_Set = StructCreator(Device_1, "DO5", idx)
DO5_Set.set_writable()
DO6_Set = StructCreator(Device_1, "DO6", idx)
DO6_Set.set_writable()
DO7_Set = StructCreator(Device_1, "DO7", idx)
DO7_Set.set_writable()
DO8_Set = StructCreator(Device_1, "DO8", idx)
DO8_Set.set_writable()
DI1_Set = StructCreator(Device_1, "DI1", idx)
DI2_Set = StructCreator(Device_1, "DI2", idx)
DI3_Set = StructCreator(Device_1, "DI3", idx)
DI4_Set = StructCreator(Device_1, "DI4", idx)
DI5_Set = StructCreator(Device_1, "DI5", idx)
DI6_Set = StructCreator(Device_1, "DI6", idx)
DI7_Set = StructCreator(Device_1, "DI7", idx)
DI8_Set = StructCreator(Device_1, "DI8", idx)
Out_Dev = StructCreator(Device_1, "Out_Val", idx)
In_Dev = StructCreator(Device_1, "In_Val", idx)
In_Dev.set_writable()
def Send_To_Handler(topic, message):                                        # Продюсер Кафки
    producer.produce(topic, value=message)
    producer.flush()
def Repacker(Package):                                                      # Распаовщик интов по битам в лист
    Formated_Str_List = list(format(Package, "b"))
    while len(Formated_Str_List) != 16:
          Formated_Str_List.insert(0, '0')
    return list(map(int, Formated_Str_List))
def Packer(Int_List):                                                       # Паковщик битов в инт
    Str_List = map(str, Int_List)
    return int(''.join(Str_List), 2)
def Discret_Read_Block(Data_Address, Flag):                                                            # Функция опроса инпут регистров
    global Start_Flag_Read
    try:    
        Package =  master.execute(1, cst.READ_INPUT_REGISTERS, Data_Address, 1)[0]
        Repacked_Data_R = Repacker(Package)
        with ThreadPoolExecutor(max_workers=16) as exexcutor:
            if not Flag:
                ThreadDO1 = exexcutor.submit(DO1_Set.set_value, Repacked_Data_R[15])
                ThreadDO2 = exexcutor.submit(DO2_Set.set_value, Repacked_Data_R[14])
                ThreadDO3 = exexcutor.submit(DO3_Set.set_value, Repacked_Data_R[13])
                ThreadDO4 = exexcutor.submit(DO4_Set.set_value, Repacked_Data_R[12])
                ThreadDO5 = exexcutor.submit(DO5_Set.set_value, Repacked_Data_R[11])
                ThreadDO6 = exexcutor.submit(DO6_Set.set_value, Repacked_Data_R[10])
                ThreadDO7 = exexcutor.submit(DO7_Set.set_value, Repacked_Data_R[9])
                ThreadDO8 = exexcutor.submit(DO8_Set.set_value, Repacked_Data_R[8])              
            ThreadDI1 = exexcutor.submit(DI1_Set.set_value, Repacked_Data_R[7])
            ThreadDI2 = exexcutor.submit(DI2_Set.set_value, Repacked_Data_R[6])
            ThreadDI3 = exexcutor.submit(DI3_Set.set_value, Repacked_Data_R[5])
            ThreadDI4 = exexcutor.submit(DI4_Set.set_value, Repacked_Data_R[4])
            ThreadDI5 = exexcutor.submit(DI5_Set.set_value, Repacked_Data_R[3])
            ThreadDI6 = exexcutor.submit(DI6_Set.set_value, Repacked_Data_R[2])
            ThreadDI7 = exexcutor.submit(DI7_Set.set_value, Repacked_Data_R[1])
            ThreadDI8 = exexcutor.submit(DI8_Set.set_value, Repacked_Data_R[0])
        if Flag == False:
            return True
        else:
            return False
    except Exception as ex1:
        print(ex1) 
def Discret_Write_Block(Data_Address):
    try:    
        with ThreadPoolExecutor(max_workers=16) as executor:
            DI8_exe = executor.submit(DI8_Set.get_value)
            DI8_State = DI8_exe.result()
            DI7_exe = executor.submit(DI7_Set.get_value)
            DI7_State = DI7_exe.result()
            DI6_exe = executor.submit(DI6_Set.get_value)
            DI6_State = DI6_exe.result()
            DI5_exe = executor.submit(DI5_Set.get_value)
            DI5_State = DI5_exe.result()
            DI4_exe = executor.submit(DI4_Set.get_value)
            DI4_State = DI4_exe.result()
            DI3_exe = executor.submit(DI3_Set.get_value)
            DI3_State = DI3_exe.result()
            DI2_exe = executor.submit(DI2_Set.get_value)
            DI2_State = DI2_exe.result()
            DI1_exe = executor.submit(DI1_Set.get_value)
            DI1_State = DI1_exe.result()
            DO8_exe = executor.submit(DO8_Set.get_value)
            DO8_State = DO8_exe.result()
            DO7_exe = executor.submit(DO7_Set.get_value)
            DO7_State = DO7_exe.result()
            DO6_exe = executor.submit(DO6_Set.get_value)
            DO6_State = DO6_exe.result()
            DO5_exe = executor.submit(DO5_Set.get_value)
            DO5_State = DO5_exe.result()
            DO4_exe = executor.submit(DO4_Set.get_value)
            DO4_State = DO4_exe.result()
            DO3_exe = executor.submit(DO3_Set.get_value)
            DO3_State = DO3_exe.result()
            DO2_exe = executor.submit(DO2_Set.get_value)
            DO2_State = DO2_exe.result()
            DO1_exe = executor.submit(DO1_Set.get_value)
            DO1_State = DO1_exe.result()
        Repacked_Datas = [DI8_State, DI7_State, DI6_State, DI5_State, DI4_State, DI3_State, DI2_State, DI1_State,
                          DO8_State, DO7_State, DO6_State, DO5_State, DO4_State, DO3_State, DO2_State, DO1_State]
        Value_To_Write = Packer(Repacked_Datas)
        master.execute(1, cst.WRITE_SINGLE_REGISTER, Data_Address, output_value=Value_To_Write)            # Запись запакованных битов в устройство
    except Exception as ex2:
        print(ex2) 
def Analog_Read_Block(Data_Address):
    try:    
        Readed_Var = master.execute(1, cst.READ_INPUT_REGISTERS, Data_Address, 1)[0]                       # Опрос устройства
        Out_Dev.set_value(Readed_Var)
    except Exception as ex3:
        print(ex3) 
def Analog_Write_Block(Data_Address):
    try:    
        Analog_From_Server = In_Dev.get_value()
        master.execute(1, cst.WRITE_SINGLE_REGISTER, Data_Address, output_value=Analog_From_Server)        # Запись числа в устройство 
    except Exception as ex4:
        print(ex4) 
def Value_From_Variable(Addr):                                                                         # Чтение данных из ОПС 
    Var = client.get_node(f"ns=2;i={Addr}")
    return Var.get_value()
def Value_To_Variable(Addr, Val):                                                                      # Запись данных в ОПС
    Var = client.get_node(f"ns=2;i={Addr}")
    Var.set_value(Val)
def Standart_R_MSG(Addr):                                                                              # Форматироване сообщения для кафки
    return f"R{Addr}V{Value_From_Variable(Addr)}"
def Get_From_Handler():                                                                                # Консьюмер и обработчик
    Msg = consumer.poll(timeout=1)
    Addr = 404
    Value = 404
    if Msg is None:
        pass
    else: 
        Data = Msg.value().decode('utf-8')
        if "W" in Data and "V" in Data:
            Space = Data.find('V')
            Addr = int(Data[1:Space])
            Value = int(Data[Space+1:])
        return Addr, Value 
def DI_Data_Handler(Data_Address, List_Index, Topic):
        Cur_Value = Value_From_Variable(Data_Address)
        if Cur_Value != Signals_Last_State[List_Index]:
            Send_To_Handler(Topic, Standart_R_MSG(Data_Address))   
            Signals_Last_State[List_Index] = Cur_Value
def DO_Data_Handler():                                                                                 # Исполнение команды из сети
        Addr, Value = Get_From_Handler()
        if Addr != 404 and Value != 404:
            Value_To_Variable(Addr, Value) 
server.start()
client = Client("opc.tcp://127.0.0.1:4840")
OPC_Flag = False
Server_Flag = False
print("Server Started")
master = modbus_tcp.TcpMaster("10.0.6.10", 502)
master.set_timeout(1.0)
while True:     
    try:       
        with ThreadPoolExecutor(max_workers=4) as executor:                                                           # Опрос инпутов в потоке           
            Discret_Reading = executor.submit(Discret_Read_Block, *[0, Start_Flag_Read])
            Flag_State = Discret_Reading.result()
            if Flag_State == False:
                pass
            else:
                Start_Flag_Read = Flag_State
            Discret_Writing = executor.submit(Discret_Write_Block, 0)
            Analog_Reading = executor.submit(Analog_Read_Block, 2)
            Analog_Writing = executor.submit(Analog_Write_Block, 1)
    except Exception as ex:
        master = modbus_tcp.TcpMaster("10.0.6.10", 502)
        master.set_timeout(1.0)
        print("Соединение разорвано", ex)
    try:
        if not OPC_Flag:
            client.connect()
            OPC_Flag = True
            print("OPC Connected") 
        with ThreadPoolExecutor(max_workers=9) as executor:
            Inp_1 = executor.submit(DI_Data_Handler, *[10, 0, 'RA10'])                             # Формирование сообщения в сеть
            Inp_2 = executor.submit(DI_Data_Handler, *[11, 1, 'RA11'])
            Inp_3 = executor.submit(DI_Data_Handler, *[12, 2, 'RA12'])
            Inp_4 = executor.submit(DI_Data_Handler, *[13, 3, 'RA13'])
            Inp_5 = executor.submit(DI_Data_Handler, *[14, 4, 'RA14'])
            Inp_6 = executor.submit(DI_Data_Handler, *[15, 5, 'RA15'])
            Inp_7 = executor.submit(DI_Data_Handler, *[16, 6, 'RA16'])
            Inp_8 = executor.submit(DI_Data_Handler, *[17, 7, 'RA17'])
            Msgs_Detector = executor.submit(DO_Data_Handler)  
    except Exception as _ex:
        print("OPC Connection Failed", _ex)