#_*_ coding: cp1251 _*_
import numbers
import telebot
import sqlite3
import time
API_Token = '6990401912:AAHR8pfQjk77mGS-XRjWeoEWitcE1B5PELM'
bot = telebot.TeleBot(API_Token)
counter = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
knc1 = []
itp = []
pv4 = []
e1 = []
e2 = []
e3 = []
e4 = []
w1 = []
w2 = []
w3 = []
w4 = []
knc2 = []
numbers = [knc1, itp, pv4, e1, e2, e3, e4, w1, w2, w3, w4, knc2]
systems = ['��� 1', '���', '�� 4', '��� 1 ��������������', '��� 2 ��������������', '��� 3 ��������������', '��� 4 ��������������', '��� 1 �������� �������', '��� 2 �������� �������', '��� 3 �������� �������', '��� 4 �������� �������', '��� 2']
Itp_Alarm_Tag_Name = ['����������� ������', '������ ������ 1 ���.', '������ ������ 1 ���.', '������ ������ 2 ���.', '������ ������ 2 ���.', '������ �� �������', '�������� ������',
                      '������ �� ������ 1 ���.', '������ �� ������ 1 ���.', '������ �� ������ 2 ���.', '������ ������ 2 ���.', '������ �� ����. ������ 1 ���', '������ �� ����. ������ 1 ���.', '������ �� ����. ������ 2 ���.',
                     '������ �� ����. ������ 2 ���.', '������ QF ������ 1 ���.', '������ QF ������ 1 ���.', '������ QF ������ 2 ���.', '������ QF ������ 2 ���.', '����. ������ 1 �������', '����. ������ 2 �������', '������ � �������']
Pv4_Alarm_Tag_Name = ['����������� ������', '������ ��������', '�������� ������', '������ �� ����. �������', '������ �� ����. �������', '������ ���������', '������ ������� ����������� �������', '������ �� �������']
Abk_E_Alarm_Tag_Name = ['�������� ������', '������ �� ����. �������', '������ �����������', '������ ���������', '������ ������� ����������� �������', '������ �������', '����������� ������']
Abk_W_Alarm_Tag_Name = ['�������� ������', '������ ���������', '������ ������� ����������� �������', '������ �������', '����������� ������', '������ ��������� ������� �����������', '������ ������� ����������� ����', '������ �� ���������� �����������']
Knc_Alarm_Tag_Name = ['������ ������ 1', '������ ������ 2']
Names =[]
Names.append(Knc_Alarm_Tag_Name)
Names.append(Itp_Alarm_Tag_Name)
Names.append(Pv4_Alarm_Tag_Name)
Names.append(Abk_E_Alarm_Tag_Name)
Names.append(Abk_E_Alarm_Tag_Name)
Names.append(Abk_E_Alarm_Tag_Name)
Names.append(Abk_E_Alarm_Tag_Name)
Names.append(Abk_W_Alarm_Tag_Name)
Names.append(Abk_W_Alarm_Tag_Name)
Names.append(Abk_W_Alarm_Tag_Name)
Names.append(Abk_W_Alarm_Tag_Name)
Names.append(Knc_Alarm_Tag_Name)
Files = ['_KNC1', '_ITP', '_PV4', '_ABK1E', '_ABK2E', '_ABK3E', '_ABK4E', '_ABK1W', '_ABK2W', '_ABK3W', '_ABK4W', '_KNC2']
Tables = ['Knc1_Alarms', 'Itp_Alarms', 'Pv4_Alarms', 'Abk1_E_Alarms', 'Abk2_E_Alarms', 'Abk3_E_Alarms', 'Abk4_E_Alarms', 'Abk1_W_Alarms', 'Abk2_W_Alarms', 'Abk3_W_Alarms', 'Abk4_W_Alarms', 'Knc2_Alarms',]
while True:
    for s in range(0, len(Files)):   
        con = sqlite3.connect(f"C:\ProgramData\InSAT\MasterOPC Universal Modbus Server\Data_Set{Files[s]}.sqlite3")
        cursor_main = con.cursor()
        cursor_main.execute(f"SELECT * FROM {Tables[s]}")
        rows = cursor_main.fetchall()
        ids_for_newsletters = sqlite3.connect(r"C:\ProgramData\InSAT\MasterOPC Universal Modbus Server\Users_ID_Data.sqlite3")
        cursor_newletters = ids_for_newsletters.cursor()
        cursor_newletters.execute('SELECT * FROM User_Level')
        newletters_ids = cursor_newletters.fetchall()
        if len(rows) !=0:
            while counter[s]<=len(rows):
                numbers[s].append(False)
                counter[s] += 1            
            for i in range(0, len(rows)):
                if rows[i][2] == 'false':
                    if numbers[s][i] == False:
                        for j in range(0, len(newletters_ids)):
                            bot.send_message(newletters_ids[j][3], f"{Names[s][i]} � ������� {systems[s]}.")
                        numbers[s][i] = True
                else:
                    numbers[s][i] = False
        con.close() 
        ids_for_newsletters.close()
        time.sleep(1)
