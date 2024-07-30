import asyncio
import websockets
import confluent_kafka
config = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'mygroup',
    'auto.offset.reset': 'earliest'}
producer = confluent_kafka.Producer(config)
consumer = confluent_kafka.Consumer(config)
consumer.subscribe(['RA10','RA11','RA12','RA13','RA14','RA15','RA16','RA17'])
def Handler_R_Datas():
    Msg = consumer.poll(timeout=0)
    Addr = 404
    Value = 404
    if Msg is None:
        pass
    else:  
        Data = Msg.value().decode('utf-8')
        if "R" in Data and "V" in Data:
            Space = Data.find('V')
            Addr = int(Data[1:Space])
            Value = int(Data[Space+1:])
    return f"{Addr}_{Value}"
def Messages_Handler(Msg):
    Topic = "None"
    if 'W' in Msg and 'V' in Msg:
        Space = Msg.find('V')
        Addr = int(Msg[1:Space])
        Topic = f"WA{Addr}"
    return Topic, Msg
async def Sender():
    uri = "ws://192.168.1.56:8000"
    while True:
        async with websockets.connect(uri) as websocket:
            Data = Handler_R_Datas()
            if Data != "404_404":
                await websocket.send(Data)
                print(Data)
            else:
                await asyncio.sleep(0.01)
async def Reader():  
    uri = "ws://192.168.1.56:8000"
    while True:
        async with websockets.connect(uri) as websocket:
            Message = await websocket.recv()
            Topic, Msg = Messages_Handler(Message)
            if Topic != "None":
                codedmsg = Msg.encode()
                producer.produce(Topic, value=codedmsg)
                producer.flush()
            print(f"<<< {Message}")
async def main():
    while True:
        S = loop.create_task(Sender())
        R = loop.create_task(Reader())
        await asyncio.wait([S, R])
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
