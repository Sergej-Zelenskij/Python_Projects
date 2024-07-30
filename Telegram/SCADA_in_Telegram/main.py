#_*_ coding: cp1251 _*_
from ast import main
from gc import callbacks
from msilib import Table
from turtle import setpos
import telebot
from telebot import types
from telebot.types import Message
from telebot import custom_filters
from telebot.handler_backends import State, StatesGroup
from telebot.storage import StateMemoryStorage
import sqlite3
import time
state_storage = StateMemoryStorage()
API_Token = '6990401912:AAHR8pfQjk77mGS-XRjWeoEWitcE1B5PELM'
bot = telebot.TeleBot(API_Token, state_storage = state_storage)
class BotStates(StatesGroup):
    SetSP = State()
    SysCmd = State()
    GroupSysControl = State()
    EditSeason = State()
    EntName = State()
    EntSurname = State()
    EndReg = State()
    EditN = State()
    EditS = State()
    EntPass = State()
    EditLevel = State()
    AdmUsers = State()
    UsersControl = State()
    PassControl = State()
    AddAdm = State()
    AddMAdm = State()
    DelAdm = State()
    DelMAdm = State()
    DelUser = State()
    EditPassUser = State()
    EditPassAdmin = State()
    EditPassMAdmin = State()
SystemToWork = 0
SetPoint_Files = []
Reset_Files = []
Mode_Files = []
System_Files = []
Table_Datas = []
Table_Alarms = []
Table_Control = []
sysname = []
schemes = []
sysnameshort = ['cruch']
Names_Data_For_Sel = []
Name_Alarm_For_Sel = []
Knc1Datas = []
Knc1Alarm = []
Abk1Datas = []
Abk1Alarms = []
Abk2Datas = []
Abk2Alarms = []
Abk3Datas = []
Abk3Alarms = []
Abk4Datas = []
Abk4Alarms = []
Knc2Datas = []
Knc2Alarm = []
Abk1WDatas = []
Abk1WAlarms = []
Abk2WDatas = []
Abk2WAlarms = []
Abk3WDatas = []
Abk3WAlarms = []
Abk4WDatas = []
Abk4WAlarms = []
Itp_Data_Tag_Name = ['������� ��������:', '�������� �����������:', '����� 1 ���. � ������:', '����� 1 ���. � ������:', '����� 2 ���. � ������:', '����� 2 ���. � ������:',
                     '������ �������� 1:', '������ �������� 2:', '������ �������� 1:', '������ �������� 2:', '������ �������� 3:', '������ �������� 4:', '����������� � ���������:',
                     '����������� �� ���������:', '����������� �������� ��������� 1:', '����������� �������� ��������� 2:', '����������� ������� ��������� 1:', '����������� ������� ��������� 2:',
                     '����������� ������� 1:', '����������� ������� 2:', '����������� ������� 1:', '����������� ������� 2:', '�������� �������:', '�������� �������:']
Itp_Alarm_Tag_Name = ['����������� ������:', '������ ������ 1 ���.:', '������ ������ 1 ���.:', '������ ������ 2 ���.:', '������ ������ 2 ���.:', '������ �� �������:', '�������� ������:',
                      '������ �� ������ 1 ���.:', '������ �� ������ 1 ���.:', '������ �� ������ 2 ���.:', '������ ������ 2 ���.:', '������ �� ����. ������ 1 ���:', '������ �� ����. ������ 1 ���.:', '������ �� ����. ������ 2 ���.:',
                     '������ �� ����. ������ 2 ���.:', '������ QF ������ 1 ���.:', '������ QF ������ 1 ���.:', '������ QF ������ 2 ���.:', '������ QF ������ 2 ���.:', '����. ������ 1 �������:', '����. ������ 2 �������:']
Pv4_Data_Tag_Name = ['������� ��������:', '���������� �������:', '���������� �������:', '���������� ������� ����.:', '����. ������:',
                     '����������� �������:', '�������� ������� � �������:', '�������� ������������:', '������� �������:']
Pv4_Alarm_Tag_Name = ['����������� ������:', '������ ��������:', '�������� ������:', '������ �� ����. �������:', '������ �� ����. �������:', '������ ���������:', '������ ������� ����������� �������:', '������ �� �������:']
Abk_E_Data_Tag_Name = ['��������:', '����. ������� ���.:', '����. ������� ���.:', '�����������:', '������� ��������:', '����������� �������:', '������� �������:']
Abk_E_Alarm_Tag_Name = ['�������� ������:', '������ �� ����. �������:', '������ �����������:', '������ ���������:', '������ ������� ����������� �������:', '������ �������:', '����������� ������:']
Abk_W_Data_Tag_Name = ['��������:', '����. �������:', '�����:', '������� ��������:', '����������� �������:', '���������:', '�������� �����������:', '����������� ����:', '����:', '������ �����������:']
Abk_W_Alarm_Tag_Name = ['�������� ������:', '������ ���������:', '������ ������� ����������� �������:', '������ �������:', '����������� ������:', '������ ��������� ������� �����������:', '������ ������� ����������� ����:', '������ �� ���������� �����������:']
Knc_Data_Tag_Name = ['����� 1 � ������:', '����� 1 � ����:', '����� 2 � ������:', '����� 2 � ����:', 'Inp1', 'F1', 'F2', 'F3', 'F4']
Knc_Alarm_Tag_Name = ['������ ������ 1:', '������ ������ 2:']
systemsel = types.InlineKeyboardMarkup()
systemsel.add(types.InlineKeyboardButton('��� 1', callback_data='1'))
systemsel.add(types.InlineKeyboardButton('���', callback_data='2'))
systemsel.add(types.InlineKeyboardButton('�� 4', callback_data='3'))
systemsel.add(types.InlineKeyboardButton('��� 1 �������������', callback_data='4'))
systemsel.add(types.InlineKeyboardButton('��� 2 �������������', callback_data='5'))
systemsel.add(types.InlineKeyboardButton('��� 3 �������������', callback_data='6'))
systemsel.add(types.InlineKeyboardButton('��� 4 �������������', callback_data='7'))
systemsel.add(types.InlineKeyboardButton('��� 1 ������� ������', callback_data='8'))
systemsel.add(types.InlineKeyboardButton('��� 2 ������� ������', callback_data='9'))
systemsel.add(types.InlineKeyboardButton('��� 3 ������� ������', callback_data='10'))
systemsel.add(types.InlineKeyboardButton('��� 4 ������� ������', callback_data='11'))
systemsel.add(types.InlineKeyboardButton('��� 2', callback_data='12'))
systemsel.add(types.InlineKeyboardButton('�������� �����', callback_data='13'))
systemsel.add(types.InlineKeyboardButton('������', callback_data='14'))
systemsel.add(types.InlineKeyboardButton('������', callback_data='15'))
canselcontrol = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
canselcontrol.add(types.KeyboardButton('������'))
#
mainmenukeyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
mainmenukeyboard.add(types.KeyboardButton('������� ������� ��� ������'))
mainmenukeyboard.add(types.KeyboardButton('�������� ������� �������'))
#
useradministrationkbrd = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
useradministrationkbrd.add(types.KeyboardButton('���������� ��������������'), types.KeyboardButton('����������� ��������'))
useradministrationkbrd.add(types.KeyboardButton('������� ����'))
#
editpasskbrd = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
editpasskbrd.add(types.KeyboardButton('�������� �������'), types.KeyboardButton('������� ������ ������������'))
editpasskbrd.add(types.KeyboardButton('�������� ������ ��������������'), types.KeyboardButton('������� ������ ��. ��������������'))
editpasskbrd.add(types.KeyboardButton('������'))
#
deleteuserkbrd = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
deleteuserkbrd.add(types.KeyboardButton('�������� �������������'), types.KeyboardButton('������� ������������'))
deleteuserkbrd.add(types.KeyboardButton('������ ��������������'), types.KeyboardButton('������ ��. ��������������'))
deleteuserkbrd.add(types.KeyboardButton('������� �� ���������������'), types.KeyboardButton('������� �� ��. ���������������'))
deleteuserkbrd.add(types.KeyboardButton('������'))
#
mainmenuadminkeyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
mainmenuadminkeyboard.add(types.KeyboardButton('������� ������� ��� ������'))
mainmenuadminkeyboard.add(types.KeyboardButton('���������� �������������� � ��������'))
#
groupukeyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
groupukeyboard.add(types.KeyboardButton(f"���������� � ��������"))
groupukeyboard.add(types.KeyboardButton('����� ������'), types.KeyboardButton('������ ������'), types.KeyboardButton('������� ����'))
groupakeyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
groupakeyboard.add(types.KeyboardButton(f"���������� � ��������"), types.KeyboardButton('����� ������ ������'))
groupakeyboard.add(types.KeyboardButton(f"���������� ���������"), types.KeyboardButton('�������� �������'))
groupakeyboard.add(types.KeyboardButton('����� ������'), types.KeyboardButton('������ ������'), types.KeyboardButton('������� ����'))
groupmakeyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
groupmakeyboard.add(types.KeyboardButton(f"���������� � ��������"), types.KeyboardButton('����� ������ ������'))
groupmakeyboard.add(types.KeyboardButton(f"���������� ���������"), types.KeyboardButton('�������� �������'))
groupmakeyboard.add(types.KeyboardButton('����� ������'), types.KeyboardButton('������ ������'), types.KeyboardButton('������� ����'))
@bot.message_handler(commands=['start'])
def registration(message):
    id_con = sqlite3.connect(r"C:\ProgramData\InSAT\MasterOPC Universal Modbus Server\Users_ID_Data.sqlite3")
    cursor_IDs = id_con.cursor()
    cursor_IDs.execute('''CREATE TABLE IF NOT EXISTS User_Level (
                        id INTEGER PRIMARY KEY, surname TEXT, name TEXT, user_id TEXT)''')
    cursor_IDs.execute('''CREATE TABLE IF NOT EXISTS Admin_Level (
                        id INTEGER PRIMARY KEY, surname TEXT, name TEXT, user_id TEXT)''')
    cursor_IDs.execute('''CREATE TABLE IF NOT EXISTS MainAdmin_Level (
                        id INTEGER PRIMARY KEY, surname TEXT, name TEXT, user_id TEXT)''')
    cursor_IDs.execute('''CREATE TABLE IF NOT EXISTS Passwords (
                        id INTEGER PRIMARY KEY, level TEXT, pass TEXT)''')
    cursor_IDs.execute('SELECT * FROM User_Level')
    users = cursor_IDs.fetchall()
    dname = 'NoOne'
    duplicate_id = False
    for i in users:
         if f"{message.chat.id}" in i[3]:
            duplicate_id = True
            dname = i[2]
    if duplicate_id:
        bot.send_message(message.chat.id, f"{dname}, �� ��� ������ �������������, ��������� ��������� ����� �� ���������.")
        bot.delete_state(message.from_user.id, message.chat.id)
    else:
        bot.send_message(message.chat.id, '�������, ��� ���������� ������� ������������ ����������! ��� ������������� ������� ���� ���������� ������ ��������� �������������.')
        bot.send_message(message.chat.id, '������� ������.')
        bot.set_state(message.from_user.id, BotStates.EntPass, message.chat.id)
    id_con.close()
@bot.message_handler(state=BotStates.EntPass)
def passenter(message):
    duplicate_id = False
    dname = 'NoOne'
    id_con = sqlite3.connect(r"C:\ProgramData\InSAT\MasterOPC Universal Modbus Server\Users_ID_Data.sqlite3")
    cursor_IDs = id_con.cursor()
    cursor_IDs.execute('SELECT * FROM User_Level')
    ids = cursor_IDs.fetchall()
    cursor_IDs.execute('SELECT * FROM Passwords')
    pass_s = cursor_IDs.fetchall()
    user_id = message.chat.id
    password = message.text
    ids_value = len(ids)
    if ids_value == 0:
        if password == ''.join(pass_s[0][2]):
            cursor_IDs.execute('INSERT INTO User_Level VALUES (NULL, NULL, NULL, ?);', (f"{user_id}",))  
            id_con.commit()
            bot.send_message(message.chat.id, '��� ��� ����� ������� ������������.')
            bot.send_message(message.chat.id, '������� ���� ���.')
            bot.set_state(message.from_user.id, BotStates.EntName, message.chat.id)
        elif password == ''.join(pass_s[1][2]):
            cursor_IDs.execute('INSERT INTO User_Level VALUES (NULL, NULL, NULL, ?);', (f"{user_id}",))
            id_con.commit()
            cursor_IDs.execute('INSERT INTO Admin_Level VALUES (NULL, NULL, NULL, ?);', (f"{user_id}",))
            id_con.commit()
            bot.send_message(message.chat.id, '��� ��� ����� ������� ��������������.')
            bot.send_message(message.chat.id, '������� ���� ���.')
            bot.set_state(message.from_user.id, BotStates.EntName, message.chat.id)
        elif password == ''.join(pass_s[2][2]):
            cursor_IDs.execute('INSERT INTO User_Level VALUES (NULL, NULL, NULL, ?);', (f"{user_id}",))
            id_con.commit()
            cursor_IDs.execute('INSERT INTO Admin_Level VALUES (NULL, NULL, NULL, ?);', (f"{user_id}",))
            id_con.commit()
            cursor_IDs.execute('INSERT INTO MainAdmin_Level VALUES (NULL, NULL, NULL, ?);', (f"{user_id}",))
            id_con.commit()
            bot.send_message(message.chat.id, '��� ��� ����� ������� �������� ��������������.')
            bot.send_message(message.chat.id, '������� ���� ���.')
            bot.set_state(message.from_user.id, BotStates.EntName, message.chat.id)
        else:
            bot.send_message(message.chat.id, '�������� ������.')
    else:
        for i in ids:
            if f"{user_id}" in i[3]:
                duplicate_id = True
                dname = i[2]
        if duplicate_id:
            bot.send_message(user_id, f"{dname}, �� ��� ������ �������������, ��������� ��������� ����� �� ���������.")
            bot.delete_state(message.from_user.id, message.chat.id)
        else:
            if password == ''.join(pass_s[0][2]):
                cursor_IDs.execute('INSERT INTO User_Level VALUES (NULL, NULL, NULL, ?);', (f"{user_id}",))  
                id_con.commit()
                bot.send_message(message.chat.id, '��� ��� ����� ������� ������������.')
                bot.send_message(message.chat.id, '������� ���� ���.')
                bot.set_state(message.from_user.id, BotStates.EntName, message.chat.id)
            elif password == ''.join(pass_s[1][2]):
                cursor_IDs.execute('INSERT INTO User_Level VALUES (NULL, NULL, NULL, ?);', (f"{user_id}",))
                id_con.commit()
                cursor_IDs.execute('INSERT INTO Admin_Level VALUES (NULL, NULL, NULL, ?);', (f"{user_id}",))
                id_con.commit()
                bot.send_message(message.chat.id, '��� ��� ����� ������� ��������������.')
                bot.send_message(message.chat.id, '������� ���� ���.')
                bot.set_state(message.from_user.id, BotStates.EntName, message.chat.id)
            elif password == ''.join(pass_s[2][2]):
                cursor_IDs.execute('INSERT INTO User_Level VALUES (NULL, NULL, NULL, ?);', (f"{user_id}",))
                id_con.commit()
                cursor_IDs.execute('INSERT INTO Admin_Level VALUES (NULL, NULL, NULL, ?);', (f"{user_id}",))
                id_con.commit()
                cursor_IDs.execute('INSERT INTO MainAdmin_Level VALUES (NULL, NULL, NULL, ?);', (f"{user_id}",))
                id_con.commit()
                bot.send_message(message.chat.id, '��� ��� ����� ������� �������� ��������������.')
                bot.send_message(message.chat.id, '������� ���� ���.')
                bot.set_state(message.from_user.id, BotStates.EntName, message.chat.id)
            else:
                bot.send_message(message.chat.id, '�������� ������.')
    ids = cursor_IDs.fetchall()
    ids_value = len(ids)
    id_con.close()
@bot.message_handler(state=BotStates.EntName)
def entername(message):
    users_con = sqlite3.connect(r"C:\ProgramData\InSAT\MasterOPC Universal Modbus Server\Users_ID_Data.sqlite3")
    users_cursor = users_con.cursor()
    users_cursor.execute('UPDATE User_Level SET name = ? WHERE user_id = ?;', (f"{message.text}", f"{message.chat.id}",))
    users_con.commit()
    users_cursor.execute('SELECT * FROM Admin_Level')
    usersa = users_cursor.fetchall()
    for a in usersa:
        if f"{message.chat.id}" in a[3]:
            users_cursor.execute('UPDATE Admin_Level SET name = ? WHERE user_id = ?;', (f"{message.text}", f"{message.chat.id}",))
            users_con.commit()
    users_cursor.execute('SELECT * FROM MainAdmin_Level')
    usersma = users_cursor.fetchall()
    for m in usersma:
        if f"{message.chat.id}" in m[3]:
            users_cursor.execute('UPDATE MainAdmin_Level SET name = ? WHERE user_id = ?;', (f"{message.text}", f"{message.chat.id}",))
            users_con.commit()
    bot.send_message(message.chat.id, f"�������, {message.text}, ������ ������� ���� �������.")
    bot.set_state(message.from_user.id, BotStates.EntSurname, message.chat.id)
    users_con.close()
@bot.message_handler(state=BotStates.EntSurname)
def entersurname(message):
    users_con = sqlite3.connect(r"C:\ProgramData\InSAT\MasterOPC Universal Modbus Server\Users_ID_Data.sqlite3")
    users_cursor = users_con.cursor()
    users_cursor.execute('UPDATE User_Level SET surname = ? WHERE user_id = ?;', (f"{message.text}", f"{message.chat.id}",))
    users_con.commit()
    users_cursor.execute('SELECT * FROM Admin_Level')
    usersa = users_cursor.fetchall()
    for a in usersa:
        if f"{message.chat.id}" in a[3]:
            users_cursor.execute('UPDATE Admin_Level SET surname = ? WHERE user_id = ?;', (f"{message.text}", f"{message.chat.id}",))
            users_con.commit()
    users_cursor.execute('SELECT * FROM MainAdmin_Level')
    usersma = users_cursor.fetchall()
    for m in usersma:
        if f"{message.chat.id}" in m[3]:
            users_cursor.execute('UPDATE MainAdmin_Level SET surname = ? WHERE user_id = ?;', (f"{message.text}", f"{message.chat.id}",))
            users_con.commit()
    firstkeyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    firstkeyboard.add(types.KeyboardButton('�������� ���'), types.KeyboardButton('�������� �������'))
    firstkeyboard.add(types.KeyboardButton('��������� �����������'))
    users_cursor.execute(f"SELECT name FROM User_Level WHERE user_id = {message.chat.id}")
    namef = users_cursor.fetchall()
    name = namef[0]
    users_cursor.execute(f"SELECT surname FROM User_Level WHERE user_id = {message.chat.id}")
    surnamef = users_cursor.fetchall()
    surname = surnamef[0]
    bot.send_message(message.chat.id, f"��������� ���� ������, ���� ��� �����, ������� ������ '��������� �����������'. ���� ������: {''.join(name)} {''.join(surname)}.", reply_markup=firstkeyboard)
    bot.set_state(message.from_user.id, BotStates.EndReg, message.chat.id)
    users_con.close()
@bot.message_handler(state=BotStates.EndReg)
def endorsel(message):
    users_con = sqlite3.connect(r"C:\ProgramData\InSAT\MasterOPC Universal Modbus Server\Users_ID_Data.sqlite3")
    users_cursor = users_con.cursor()
    if message.text == '��������� �����������':
        users_cursor.execute("SELECT * FROM User_Level")
        users = users_cursor.fetchall()
        users_cursor.execute("SELECT * FROM Admin_Level")
        admins = users_cursor.fetchall()
        users_cursor.execute("SELECT * FROM MainAdmin_Level")
        mainadmins = users_cursor.fetchall()
        madm = False
        adm = False
        for m in mainadmins:
            if f"{message.chat.id}" in m[3]:
                bot.send_message(message.chat.id, '����������� ���������, ��� ��� ����� ������ ������ �������� �������������.', reply_markup=mainmenuadminkeyboard)
                bot.delete_state(message.from_user.id, message.chat.id)
                madm = True
        for a in admins:
            if f"{message.chat.id}" in a[3]:
                if not madm:
                    bot.send_message(message.chat.id, '����������� ���������, ��� ��� ����� ������ ������ �������������.', reply_markup=mainmenukeyboard)
                    bot.delete_state(message.from_user.id, message.chat.id)
                    adm = True
        for u in users:
            if f"{message.chat.id}" in u[3]:
                if not adm and not madm:
                    bot.send_message(message.chat.id, '����������� ���������, ��� ��� ����� ������ ������ ������������.', reply_markup=mainmenukeyboard)
                    bot.delete_state(message.from_user.id, message.chat.id)
    elif message.text == '�������� ���':
        bot.send_message(message.chat.id, '������� ����� ���:')
        bot.set_state(message.from_user.id, BotStates.EditN, message.chat.id)
    elif message.text == '�������� �������':
        bot.send_message(message.chat.id, '������� ����� �������:')
        bot.set_state(message.from_user.id, BotStates.EditS, message.chat.id)
    else:
        bot.send_message(message.chat.id, '������������ ����')
    users_con.close()
@bot.message_handler(state=BotStates.EditN)
def neditor(message):
    users_con = sqlite3.connect(r"C:\ProgramData\InSAT\MasterOPC Universal Modbus Server\Users_ID_Data.sqlite3")
    users_cursor = users_con.cursor()
    users_cursor.execute('UPDATE User_Level SET name = ? WHERE user_id = ?;', (f"{message.text}", f"{message.chat.id}",))
    users_con.commit()
    users_cursor.execute('SELECT * FROM Admin_Level')
    usersa = users_cursor.fetchall()
    for a in usersa:
        if f"{message.chat.id}" in a[3]:
            users_cursor.execute('UPDATE Admin_Level SET name = ? WHERE user_id = ?;', (f"{message.text}", f"{message.chat.id}",))
            users_con.commit()
    users_cursor.execute('SELECT * FROM MainAdmin_Level')
    usersma = users_cursor.fetchall()
    for m in usersma:
        if f"{message.chat.id}" in m[3]:
            users_cursor.execute('UPDATE MainAdmin_Level SET name = ? WHERE user_id = ?;', (f"{message.text}", f"{message.chat.id}",))
            users_con.commit()
    bot.send_message(message.chat.id, "��� ���������.")
    users_con.close()
    bot.set_state(message.from_user.id, BotStates.EndReg, message.chat.id)
@bot.message_handler(state=BotStates.EditS)
def seditor(message):
    users_con = sqlite3.connect(r"C:\ProgramData\InSAT\MasterOPC Universal Modbus Server\Users_ID_Data.sqlite3")
    users_cursor = users_con.cursor()
    users_cursor.execute('UPDATE User_Level SET surname = ? WHERE user_id = ?;', (f"{message.text}", f"{message.chat.id}",))
    users_con.commit()
    users_cursor.execute('SELECT * FROM Admin_Level')
    usersa = users_cursor.fetchall()
    for a in usersa:
        if f"{message.chat.id}" in a[3]:
            users_cursor.execute('UPDATE Admin_Level SET surname = ? WHERE user_id = ?;', (f"{message.text}", f"{message.chat.id}",))
            users_con.commit()
    users_cursor.execute('SELECT * FROM MainAdmin_Level')
    usersma = users_cursor.fetchall()
    for m in usersma:
        if f"{message.chat.id}" in m[3]:
            users_cursor.execute('UPDATE MainAdmin_Level SET surname = ? WHERE user_id = ?;', (f"{message.text}", f"{message.chat.id}",))
            users_con.commit()
    bot.send_message(message.chat.id, "������� ���������.")
    users_con.close()
    bot.set_state(message.from_user.id, BotStates.EndReg, message.chat.id)
@bot.message_handler(state=BotStates.SetSP)
def getsp(message):
    NewSetPoint = message.text
    if NewSetPoint.replace(".", "", 1).lstrip("-").isdigit():
        spvalue = float(NewSetPoint)
        if spvalue <= 100 and spvalue >= -100:
            for t in range(0,len(Table_Control)):
                if Table_Control[t] != 'Itp_Control' and Table_Control[t] != 'Knc2_Control' and Table_Control[t] != 'Knc1_Control':
                    filteredsp = round(spvalue, 2)
                    con_ws = sqlite3.connect(f"C:\ProgramData\InSAT\MasterOPC Universal Modbus Server\Data_Set{SetPoint_Files[t]}.sqlite3")
                    cursor_ws = con_ws.cursor()
                    cursor_ws.execute(f"UPDATE {Table_Control[t]} SET Value = 'true' WHERE id = 2")
                    cursor_ws.execute(f"UPDATE {Table_Control[t]} SET Value = ? WHERE id = 1", (f"{filteredsp}",))
                    con_ws.commit()
                    bot.send_message(message.chat.id, "��������������� ����� �������� �������, ���������.")
                    con_ws.close()
            for t in range(0,len(Table_Control)):
                if Table_Control[t] != 'Itp_Control' and Table_Control[t] != 'Knc2_Control' and Table_Control[t] != 'Knc1_Control':
                    con_ws = sqlite3.connect(f"C:\ProgramData\InSAT\MasterOPC Universal Modbus Server\Data_Set{SetPoint_Files[t]}.sqlite3")
                    cursor_ws = con_ws.cursor()
                    Sucsessful_change = False
                    timeout = 0
                    while not Sucsessful_change:
                        time.sleep(1)
                        cursor_ws.execute(f"SELECT * FROM {Table_Control[t]} WHERE id =2")
                        cycle_check = cursor_ws.fetchall()
                        if cycle_check[0][2] == 'false':
                            Sucsessful_change = True
                        timeout +=1
                        if timeout == 10:
                            break
                    if Sucsessful_change:
                        if len(Table_Control) > 1:
                            con_ws.close()
                            bot.send_message(message.chat.id, f"����� �������� ����������� ��� ������� {sysname[t]}.")
                        else:
                            bot.send_message(message.chat.id, f"����� �������� ����������� ��� ������� {sysname[t]}.", reply_markup=akeyboard)
                            con_ws.close()
                            bot.delete_state(message.from_user.id, message.chat.id)
                    else:
                        cursor_ws.execute(f"UPDATE {Table_Control[t]} SET Value = 'false' WHERE id = 2")
                        con_ws.commit()
                        con_ws.close()
                        bot.send_message(message.chat.id, f"�� ������� �������� ������� ��� ������� {sysname[t]}.")
            if len(Table_Control) > 1:
                bot.send_message(message.chat.id, "���������� �������� ������� ����������� ������� ��� ������ ������ ���������.", reply_markup=groupakeyboard)        
            bot.delete_state(message.from_user.id, message.chat.id)
        else:
           bot.send_message(message.chat.id, "������� �������� � ��������� �� -100 �� 100.")
    elif NewSetPoint == '������':
        if len(Table_Control) > 1:
            bot.send_message(message.chat.id, "�������� ��������.", reply_markup=groupakeyboard)
        else:    
            bot.send_message(message.chat.id, "�������� ��������.", reply_markup=akeyboard)
        bot.delete_state(message.from_user.id, message.chat.id)
    else:
         bot.send_message(message.chat.id, "������� ����� ��� ������� '������' ��� ������ ��������.")
@bot.message_handler(state=BotStates.SysCmd)
def syscommand(message):
    con_ws = sqlite3.connect(f"C:\ProgramData\InSAT\MasterOPC Universal Modbus Server\Data_Set{System_Files[0]}.sqlite3")
    cursor_ws = con_ws.cursor()
    cursor_ws.execute(f"SELECT * FROM {Table_Control[0]} WHERE id = 1")
    rows_ws = cursor_ws.fetchall()
    if message.text == '��������� �������':
        if rows_ws[0][2] == 'false':
            cursor_ws.execute(f"UPDATE {Table_Control[0]} SET Value = 'true' WHERE id = 2")
            cursor_ws.execute(f"UPDATE {Table_Control[0]} SET Value = 'true' WHERE id = 1")
            con_ws.commit()
            bot.send_message(message.chat.id, "������� �����������, ���������.")            
            Sucsessful_change = False
            timeout = 0
            while not Sucsessful_change:
                time.sleep(1)
                cursor_ws.execute(f"SELECT * FROM {Table_Control[0]} WHERE id =2")
                cycle_check = cursor_ws.fetchall()
                if cycle_check[0][2] == 'false':
                    Sucsessful_change = True
                timeout +=1
                if timeout == 10:
                    break
            if Sucsessful_change:
                bot.send_message(message.chat.id, "������� ��������.", reply_markup=akeyboard)            
                bot.delete_state(message.from_user.id, message.chat.id)
            else:
                cursor_ws.execute(f"UPDATE {Table_Control[0]} SET Value = 'false' WHERE id = 2")
                con_ws.commit()
                bot.send_message(message.chat.id, "�� ������� ��������� �������.") 
        elif rows_ws[0][2] == 'true':
            bot.send_message(message.chat.id, "������� ��� ��������� � ������.")
    elif message.text == '���������� �������':
        if rows_ws[0][2] == 'true':
            cursor_ws.execute(f"UPDATE {Table_Control[0]} SET Value = 'true' WHERE id = 2")
            cursor_ws.execute(f"UPDATE {Table_Control[0]} SET Value = 'false' WHERE id = 1")
            con_ws.commit()
            bot.send_message(message.chat.id, "������� ���������������, ���������.")
            Sucsessful_change = False
            timeout = 0
            while not Sucsessful_change:
                time.sleep(1)
                cursor_ws.execute(f"SELECT * FROM {Table_Control[0]} WHERE id =2")
                cycle_check = cursor_ws.fetchall()
                if cycle_check[0][2] == 'false':
                    Sucsessful_change = True
                timeout +=1
                if timeout == 10:
                    break
            if Sucsessful_change:
                bot.send_message(message.chat.id, "������� �����������.", reply_markup=akeyboard)
                bot.delete_state(message.from_user.id, message.chat.id)
            else:
                cursor_ws.execute(f"UPDATE {Table_Control[0]} SET Value = 'false' WHERE id = 2")
                con_ws.commit()
                bot.send_message(message.chat.id, "�� ������� ���������� �������.")
        elif rows_ws[0][2] == 'false':
           bot.send_message(message.chat.id, "������� ��� ���� �����������.")        
    elif message.text == '������':
        bot.send_message(message.chat.id, "�������� ��������.", reply_markup=akeyboard)
        con_ws.close()
        bot.delete_state(message.from_user.id, message.chat.id)
    else:
        con_ws.close()
        bot.send_message(message.chat.id, '������������ �������.')
@bot.message_handler(state=BotStates.EditSeason)
def seasoneditor(message):
    somechange = False
    if message.text == '����':
        for t in range(0,len(Table_Control)):
            if Table_Control[t] != 'Itp_Control' and Table_Control[t] != 'Knc2_Control' and Table_Control[t] != 'Knc1_Control' and Table_Control[t] != 'Pv4_Control' and Table_Control[t] != 'Abk1_E_Control' and Table_Control[t] != 'Abk2_E_Control' and Table_Control[t] != 'Abk3_E_Control' and Table_Control[t] != 'Abk4_E_Control':
                con_ws = sqlite3.connect(f"C:\ProgramData\InSAT\MasterOPC Universal Modbus Server\Data_Set{Mode_Files[t]}.sqlite3")
                cursor_ws = con_ws.cursor()
                cursor_ws.execute(f"SELECT * FROM {Table_Control[t]} WHERE id = 1")
                rows_ws = cursor_ws.fetchall()
                if rows_ws[0][2] == '0':
                    con_ws.close()
                    bot.send_message(message.chat.id, f"����� '����' ��� ���������� � ������� {sysname[t]}, �������� ������ ����� ��� ������ '������'.")
                else:
                    cursor_ws.execute(f"UPDATE {Table_Control[t]} SET Value = 'true' WHERE id = 2")
                    cursor_ws.execute(f"UPDATE {Table_Control[t]} SET Value = '0' WHERE id = 1")
                    con_ws.commit()
                    if len(Table_Control) > 1:
                        somechange = True
                        con_ws.close()
                        bot.send_message(message.chat.id, f"��������������� ����� '����' ��� ������� {sysname[t]}, ���������.")
                    else:
                        bot.send_message(message.chat.id, f"��������������� ����� '����' ��� ������� {sysname[t]}, ���������.")
                        Sucsessful_change = False
                        timeout = 0
                        while not Sucsessful_change:
                            time.sleep(1)
                            cursor_ws.execute(f"SELECT * FROM {Table_Control[t]} WHERE id =2")
                            cycle_check = cursor_ws.fetchall()
                            if cycle_check[0][2] == 'false':
                                Sucsessful_change = True
                            timeout +=1
                            if timeout == 10:
                                break
                        if Sucsessful_change:
                            bot.send_message(message.chat.id, f"���������� ����� '����' ��� ������� {sysname[t]}.", reply_markup=akeyboard)
                            con_ws.close()
                            bot.delete_state(message.from_user.id, message.chat.id)
                        else:
                            cursor_ws.execute(f"UPDATE {Table_Control[t]} SET Value = 'false' WHERE id = 2")
                            con_ws.commit()
                            bot.send_message(message.chat.id, f"�� ������� ���������� ����� '����' ��� ������� {sysname[t]}.")
                            con_ws.close()
        if somechange:
            for t in range(0,len(Table_Control)):
                if Table_Control[t] != 'Itp_Control' and Table_Control[t] != 'Knc2_Control' and Table_Control[t] != 'Knc1_Control' and Table_Control[t] != 'Pv4_Control' and Table_Control[t] != 'Abk1_E_Control' and Table_Control[t] != 'Abk2_E_Control' and Table_Control[t] != 'Abk3_E_Control' and Table_Control[t] != 'Abk4_E_Control':
                    con_ws = sqlite3.connect(f"C:\ProgramData\InSAT\MasterOPC Universal Modbus Server\Data_Set{Mode_Files[t]}.sqlite3")
                    cursor_ws = con_ws.cursor()
                    Sucsessful_change = False
                    timeout = 0
                    while not Sucsessful_change:
                        time.sleep(1)
                        cursor_ws.execute(f"SELECT * FROM {Table_Control[t]} WHERE id =2")
                        cycle_check = cursor_ws.fetchall()
                        if cycle_check[0][2] == 'false':
                            Sucsessful_change = True
                        timeout +=1
                        if timeout == 10:
                            break
                    if Sucsessful_change:
                        con_ws.close()
                        bot.send_message(message.chat.id, f"���������� ����� '����' ��� ������� {sysname[t]}.")
                    else:
                        cursor_ws.execute(f"UPDATE {Table_Control[t]} SET Value = 'false' WHERE id = 2")
                        con_ws.commit()
                        con_ws.close()
                        bot.send_message(message.chat.id, f"�� ������� ���������� ����� '����' ��� ������� {sysname[t]}.")            
            somechange = False
            bot.send_message(message.chat.id, "���������� ������� ����������� ������ ���������. ��� ��������� ��� �������� ������� ��� ��������� ����� '����'.", reply_markup=groupakeyboard)
            bot.delete_state(message.from_user.id, message.chat.id)
        elif not somechange and len(Table_Control) > 1:
            bot.send_message(message.chat.id, "�� ���� ��������� ��� �������� ������� ��� ����� ����� '����'.")   
    elif message.text == '����':
        for t in range(0,len(Table_Control)):
            if Table_Control[t] != 'Itp_Control' and Table_Control[t] != 'Knc2_Control' and Table_Control[t] != 'Knc1_Control' and Table_Control[t] != 'Pv4_Control' and Table_Control[t] != 'Abk1_E_Control' and Table_Control[t] != 'Abk2_E_Control' and Table_Control[t] != 'Abk3_E_Control' and Table_Control[t] != 'Abk4_E_Control':
                con_ws = sqlite3.connect(f"C:\ProgramData\InSAT\MasterOPC Universal Modbus Server\Data_Set{Mode_Files[t]}.sqlite3")
                cursor_ws = con_ws.cursor()
                cursor_ws.execute(f"SELECT * FROM {Table_Control[t]} WHERE id = 1")
                rows_ws = cursor_ws.fetchall()
                if rows_ws[0][2] == '1':
                    con_ws.close()
                    bot.send_message(message.chat.id, f"����� '����' ��� ���������� � ������� {sysname[t]}, �������� ������ ����� ��� ������ '������'.")
                else:
                    cursor_ws.execute(f"UPDATE {Table_Control[t]} SET Value = 'true' WHERE id = 2")
                    cursor_ws.execute(f"UPDATE {Table_Control[t]} SET Value = '1' WHERE id = 1")
                    con_ws.commit()
                    if len(Table_Control) > 1:
                        somechange = True
                        con_ws.close()
                        bot.send_message(message.chat.id, f"��������������� ����� '����' ��� ������� {sysname[t]}, ���������.")
                    else:
                        bot.send_message(message.chat.id, f"��������������� ����� '����' ��� ������� {sysname[t]}, ���������.")
                        Sucsessful_change = False
                        timeout = 0
                        while not Sucsessful_change:
                            time.sleep(1)
                            cursor_ws.execute(f"SELECT * FROM {Table_Control[t]} WHERE id =2")
                            cycle_check = cursor_ws.fetchall()
                            if cycle_check[0][2] == 'false':
                                Sucsessful_change = True
                            timeout +=1
                            if timeout == 10:
                                break
                        if Sucsessful_change:
                            bot.send_message(message.chat.id, f"���������� ����� '����' ��� ������� {sysname[t]}.", reply_markup=akeyboard)
                            con_ws.close()
                            bot.delete_state(message.from_user.id, message.chat.id)
                        else:
                            cursor_ws.execute(f"UPDATE {Table_Control[t]} SET Value = 'false' WHERE id = 2")
                            con_ws.commit()
                            bot.send_message(message.chat.id, f"�� ������� ���������� ����� '����' ��� ������� {sysname[t]}.")
                            con_ws.close()        
        if somechange:
            for t in range(0,len(Table_Control)):
                if Table_Control[t] != 'Itp_Control' and Table_Control[t] != 'Knc2_Control' and Table_Control[t] != 'Knc1_Control' and Table_Control[t] != 'Pv4_Control' and Table_Control[t] != 'Abk1_E_Control' and Table_Control[t] != 'Abk2_E_Control' and Table_Control[t] != 'Abk3_E_Control' and Table_Control[t] != 'Abk4_E_Control':
                    con_ws = sqlite3.connect(f"C:\ProgramData\InSAT\MasterOPC Universal Modbus Server\Data_Set{Mode_Files[t]}.sqlite3")
                    cursor_ws = con_ws.cursor()
                    Sucsessful_change = False
                    timeout = 0
                    while not Sucsessful_change:
                        time.sleep(1)
                        cursor_ws.execute(f"SELECT * FROM {Table_Control[t]} WHERE id =2")
                        cycle_check = cursor_ws.fetchall()
                        if cycle_check[0][2] == 'false':
                            Sucsessful_change = True
                        timeout +=1
                        if timeout == 10:
                            break
                    if Sucsessful_change:
                        con_ws.close()
                        bot.send_message(message.chat.id, f"���������� ����� '����' ��� ������� {sysname[t]}.")
                    else:
                        cursor_ws.execute(f"UPDATE {Table_Control[t]} SET Value = 'false' WHERE id = 2")
                        con_ws.commit()
                        con_ws.close()
                        bot.send_message(message.chat.id, f"�� ������� ���������� ����� '����' ��� ������� {sysname[t]}.")                      
            somechange = False
            bot.send_message(message.chat.id, "���������� ������� ����������� ������ ���������. ��� ��������� ��� �������� ������� ��� ��������� ����� '����'.", reply_markup=groupakeyboard)
            bot.delete_state(message.from_user.id, message.chat.id)
        elif not somechange and len(Table_Control) > 1:
            bot.send_message(message.chat.id, "�� ���� ��������� ��� �������� ������� ��� ����� ����� '����'.")
    elif message.text == '����':
        for t in range(0,len(Table_Control)):
            if Table_Control[t] != 'Itp_Control' and Table_Control[t] != 'Knc2_Control' and Table_Control[t] != 'Knc1_Control' and Table_Control[t] != 'Pv4_Control' and Table_Control[t] != 'Abk1_E_Control' and Table_Control[t] != 'Abk2_E_Control' and Table_Control[t] != 'Abk3_E_Control' and Table_Control[t] != 'Abk4_E_Control':
                con_ws = sqlite3.connect(f"C:\ProgramData\InSAT\MasterOPC Universal Modbus Server\Data_Set{Mode_Files[t]}.sqlite3")
                cursor_ws = con_ws.cursor()
                cursor_ws.execute(f"SELECT * FROM {Table_Control[t]} WHERE id = 1")
                rows_ws = cursor_ws.fetchall()
                if rows_ws[0][2] == '2':
                    con_ws.close()
                    bot.send_message(message.chat.id, f"����� '����' ��� ���������� � ������� {sysname[t]}, �������� ������ ����� ��� ������ '������'.")
                else:
                    cursor_ws.execute(f"UPDATE {Table_Control[t]} SET Value = 'true' WHERE id = 2")
                    cursor_ws.execute(f"UPDATE {Table_Control[t]} SET Value = '2' WHERE id = 1")
                    con_ws.commit()                  
                    if len(Table_Control) > 1:
                        somechange = True
                        con_ws.close()
                        bot.send_message(message.chat.id, f"��������������� ����� '����' ��� ������� {sysname[t]}, ���������.")
                    else:
                        bot.send_message(message.chat.id, f"��������������� ����� '����' ��� ������� {sysname[t]}, ���������.")
                        Sucsessful_change = False
                        timeout = 0
                        while not Sucsessful_change or timeout <= 10:
                            time.sleep(1)
                            cursor_ws.execute(f"SELECT * FROM {Table_Control[t]} WHERE id =2")
                            cycle_check = cursor_ws.fetchall()
                            if cycle_check[0][2] == 'false':
                                Sucsessful_change = True
                            timeout +=1
                            if timeout == 10:
                                break
                        if Sucsessful_change:
                            bot.send_message(message.chat.id, f"���������� ����� '����' ��� ������� {sysname[t]}.", reply_markup=akeyboard)
                            con_ws.close()
                            bot.delete_state(message.from_user.id, message.chat.id)
                        else:
                            cursor_ws.execute(f"UPDATE {Table_Control[t]} SET Value = 'false' WHERE id = 2")
                            con_ws.commit()
                            bot.send_message(message.chat.id, f"�� ������� ���������� ����� '����' ��� ������� {sysname[t]}.")
                            con_ws.close()
        if somechange:
            for t in range(0,len(Table_Control)):
                if Table_Control[t] != 'Itp_Control' and Table_Control[t] != 'Knc2_Control' and Table_Control[t] != 'Knc1_Control' and Table_Control[t] != 'Pv4_Control' and Table_Control[t] != 'Abk1_E_Control' and Table_Control[t] != 'Abk2_E_Control' and Table_Control[t] != 'Abk3_E_Control' and Table_Control[t] != 'Abk4_E_Control':
                    con_ws = sqlite3.connect(f"C:\ProgramData\InSAT\MasterOPC Universal Modbus Server\Data_Set{Mode_Files[t]}.sqlite3")
                    cursor_ws = con_ws.cursor()
                    Sucsessful_change = False
                    timeout = 0
                    while not Sucsessful_change:
                        time.sleep(1)
                        cursor_ws.execute(f"SELECT * FROM {Table_Control[t]} WHERE id =2")
                        cycle_check = cursor_ws.fetchall()
                        if cycle_check[0][2] == 'false':
                            Sucsessful_change = True
                        timeout +=1
                        if timeout == 10:
                            break
                    if Sucsessful_change:
                        con_ws.close()
                        bot.send_message(message.chat.id, f"���������� ����� '����' ��� ������� {sysname[t]}.")
                    else:
                        cursor_ws.execute(f"UPDATE {Table_Control[t]} SET Value = 'false' WHERE id = 2")
                        con_ws.commit()
                        con_ws.close()
                        bot.send_message(message.chat.id, f"�� ������� ���������� ����� '����' ��� ������� {sysname[t]}.")            
            somechange = False
            bot.send_message(message.chat.id, "���������� ������� ����������� ������ ���������. ��� ��������� ��� �������� ������� ��� ��������� ����� '����'.", reply_markup=groupakeyboard)
            bot.delete_state(message.from_user.id, message.chat.id)
        elif not somechange and len(Table_Control) > 1:
            bot.send_message(message.chat.id, "�� ���� ��������� ��� �������� ������� ��� ����� ����� '����'.")
    elif message.text == '������':
        if len(Table_Control) > 1:
            bot.send_message(message.chat.id, "�������� ��������.", reply_markup=groupakeyboard)
        else:    
            bot.send_message(message.chat.id, "�������� ��������.", reply_markup=akeyboard)
        bot.delete_state(message.from_user.id, message.chat.id)
@bot.message_handler(state=BotStates.GroupSysControl)
def groupsyscontrol(message):   
    if message.text == '��������� �������':
        somestart = False
        for t in range(0,len(Table_Datas)):
            if Table_Control[t] != 'Itp_Control' and Table_Control[t] != 'Knc2_Control' and Table_Control[t] != 'Knc1_Control':           
                con_ws = sqlite3.connect(f"C:\ProgramData\InSAT\MasterOPC Universal Modbus Server\Data_Set{System_Files[t]}.sqlite3")
                cursor_ws = con_ws.cursor()
                cursor_ws.execute(f"SELECT * FROM {Table_Control[t]} WHERE id = 1")
                rows_ws = cursor_ws.fetchall()
                if rows_ws[0][2] == 'false':
                    cursor_ws.execute(f"UPDATE {Table_Control[t]} SET Value = 'true' WHERE id = 2")
                    cursor_ws.execute(f"UPDATE {Table_Control[t]} SET Value = 'true' WHERE id = 1")
                    con_ws.commit()
                    somestart = True
                    con_ws.close()
                    bot.send_message(message.chat.id, f"������� {sysname[t]} �����������, ���������.")                    
                elif rows_ws[0][2] == 'true':
                    con_ws.close()
                    bot.send_message(message.chat.id, "������� ��� ��������� � ������.")  
        if somestart:
            for t in range(0,len(Table_Datas)):
                if Table_Control[t] != 'Itp_Control' and Table_Control[t] != 'Knc2_Control' and Table_Control[t] != 'Knc1_Control':
                    con_ws = sqlite3.connect(f"C:\ProgramData\InSAT\MasterOPC Universal Modbus Server\Data_Set{System_Files[t]}.sqlite3")
                    cursor_ws = con_ws.cursor()
                    Sucsessful_change = False
                    timeout = 0
                    while not Sucsessful_change:
                        time.sleep(1)
                        cursor_ws.execute(f"SELECT * FROM {Table_Control[t]} WHERE id =2")
                        cycle_check = cursor_ws.fetchall()
                        if cycle_check[0][2] == 'false':
                            Sucsessful_change = True
                        timeout +=1
                        if timeout == 10:
                            break
                    if Sucsessful_change:
                        con_ws.close()
                        bot.send_message(message.chat.id, "������� ��������.")            
                    else:
                        cursor_ws.execute(f"UPDATE {Table_Control[t]} SET Value = 'false' WHERE id = 2")
                        con_ws.commit()
                        con_ws.close()
                        bot.send_message(message.chat.id, "�� ������� ��������� �������.") 
            somestart = False
            bot.send_message(message.chat.id, "��� ������� �� ������ ���� ��������.", reply_markup=groupakeyboard)
            bot.delete_state(message.from_user.id, message.chat.id)
        else:
            bot.send_message(message.chat.id, "��� ������� �� ������ ��� ��������� � ������.")
    elif message.text == '���������� �������':
        somestop = False
        for t in range(0,len(Table_Datas)):
            if Table_Control[t] != 'Itp_Control' and Table_Control[t] != 'Knc2_Control' and Table_Control[t] != 'Knc1_Control':          
                con_ws = sqlite3.connect(f"C:\ProgramData\InSAT\MasterOPC Universal Modbus Server\Data_Set{System_Files[t]}.sqlite3")
                cursor_ws = con_ws.cursor()
                cursor_ws.execute(f"SELECT * FROM {Table_Control[t]} WHERE id = 1")
                rows_ws = cursor_ws.fetchall()
                if rows_ws[0][2] == 'true':
                    cursor_ws.execute(f"UPDATE {Table_Control[t]} SET Value = 'true' WHERE id = 2")
                    cursor_ws.execute(f"UPDATE {Table_Control[t]} SET Value = 'false' WHERE id = 1")
                    con_ws.commit()
                    somestop = True
                    con_ws.close()
                    bot.send_message(message.chat.id, f"������� {sysname[t]} ���������������, ���������.")
                elif rows_ws[0][2] == 'false':
                    con_ws.close()
                    bot.send_message(message.chat.id, f"������� {sysname[t]} ��� ���� �����������.")    
        if somestop:
            for t in range(0,len(Table_Datas)):
                if Table_Control[t] != 'Itp_Control' and Table_Control[t] != 'Knc2_Control' and Table_Control[t] != 'Knc1_Control':
                    con_ws = sqlite3.connect(f"C:\ProgramData\InSAT\MasterOPC Universal Modbus Server\Data_Set{System_Files[t]}.sqlite3")
                    cursor_ws = con_ws.cursor()
                    Sucsessful_change = False
                    timeout = 0
                    while not Sucsessful_change:
                        time.sleep(1)
                        cursor_ws.execute(f"SELECT * FROM {Table_Control[t]} WHERE id =2")
                        cycle_check = cursor_ws.fetchall()
                        if cycle_check[0][2] == 'false':
                            Sucsessful_change = True
                        timeout +=1
                        if timeout == 10:
                            break
                    if Sucsessful_change:
                        con_ws.close()
                        bot.send_message(message.chat.id, "������� �����������.")            
                    else:
                        cursor_ws.execute(f"UPDATE {Table_Control[t]} SET Value = 'false' WHERE id = 2")
                        con_ws.commit()
                        con_ws.close()
                        bot.send_message(message.chat.id, "�� ������� ���������� �������.") 
            somestop = False
            bot.send_message(message.chat.id, "��� ������� �� ������ ���� �����������.", reply_markup=groupakeyboard)
            bot.delete_state(message.from_user.id, message.chat.id)
        else:
            bot.send_message(message.chat.id, "��� ������� �� ������ ��� ����������.")            
    elif message.text == '������':
        bot.send_message(message.chat.id, "�������� ��������.", reply_markup=groupakeyboard)
        bot.delete_state(message.from_user.id, message.chat.id)
    else:
        bot.send_message(message.chat.id, '������������ �������.')   
@bot.message_handler(state=BotStates.EditLevel)
def edlevel(message):
    id_con = sqlite3.connect(r"C:\ProgramData\InSAT\MasterOPC Universal Modbus Server\Users_ID_Data.sqlite3")
    cursor_IDs = id_con.cursor()
    cursor_IDs.execute('SELECT * FROM Passwords')
    pas = cursor_IDs.fetchall()
    cursor_IDs.execute('SELECT * FROM User_Level WHERE user_id = ?', (f"{message.chat.id}",))
    user = cursor_IDs.fetchall()
    admin = False
    madmin = False
    if message.text == pas[1][2]:
        cursor_IDs.execute('SELECT * FROM Admin_Level')
        admins = cursor_IDs.fetchall()
        for a in admins:
            if f"{message.chat.id}" in a[3]:
                bot.send_message(message.chat.id, '� ��� ��� ���� ������ ������� �������.')
                admin = True
        if not admin:
            cursor_IDs.execute('INSERT INTO Admin_Level VALUES (NULL, ?, ?, ?);', (f"{user[0][1]}", f"{user[0][2]}", f"{user[0][3]}",))
            id_con.commit()
            bot.send_message(message.chat.id, '��� ������� ������� ��� �������� �� ��������������.', reply_markup=mainmenukeyboard)
            bot.delete_state(message.from_user.id, message.chat.id)
    elif message.text == pas[2][2]:
        cursor_IDs.execute('SELECT * FROM Admin_Level')
        admins = cursor_IDs.fetchall()
        for a in admins:
            if f"{message.chat.id}" in a[3]:
                admin = True
        if not admin:
            cursor_IDs.execute('INSERT INTO Admin_Level VALUES (NULL, ?, ?, ?);', (f"{user[0][1]}", f"{user[0][2]}", f"{user[0][3]}",))
            id_con.commit()
        cursor_IDs.execute('SELECT * FROM MainAdmin_Level')
        madmins = cursor_IDs.fetchall()
        for m in madmins:
            if f"{message.chat.id}" in m[3]:
                madmin = True
        if not madmin:
            cursor_IDs.execute('INSERT INTO MainAdmin_Level VALUES (NULL, ?, ?, ?);', (f"{user[0][1]}", f"{user[0][2]}", f"{user[0][3]}",))
            id_con.commit()
            bot.send_message(message.chat.id, '��� ������� ������� ��� �������� �� �������� ��������������.', reply_markup=mainmenuadminkeyboard)
            bot.delete_state(message.from_user.id, message.chat.id)
    elif message.text == pas[0][2]:
        bot.send_message(message.chat.id, '� ��� ��� ���� ������ ������� �������.')
    elif message.text == '������':
        bot.send_message(message.chat.id, '�������� ��������.', reply_markup=mainmenukeyboard)
        bot.delete_state(message.from_user.id, message.chat.id)
    else:
        bot.send_message(message.chat.id, '�������� ������.')
    id_con.close()
@bot.message_handler(state=BotStates.AdmUsers)
def usersadministration(message):
    if message.text == '���������� ��������������':
        bot.send_message(message.chat.id, '������� � ����� ���������� ��������������.', reply_markup=deleteuserkbrd)
        bot.set_state(message.from_user.id, BotStates.UsersControl, message.chat.id)
    elif message.text == '����������� ��������':
        bot.send_message(message.chat.id, '������� � ����� ���������� ��������.', reply_markup=editpasskbrd)
        bot.set_state(message.from_user.id, BotStates.PassControl, message.chat.id)
    elif message.text == '������� ����':
        bot.send_message(message.chat.id, '������� � ������� ����.', reply_markup=mainmenuadminkeyboard)
        bot.delete_state(message.from_user.id, message.chat.id)
@bot.message_handler(state=BotStates.UsersControl)
def usercontrol(message):
    if message.text == '�������� �������������':
        id_con = sqlite3.connect(r"C:\ProgramData\InSAT\MasterOPC Universal Modbus Server\Users_ID_Data.sqlite3")
        cursor_IDs = id_con.cursor()
        cursor_IDs.execute('SELECT * FROM MainAdmin_Level')
        madmins = cursor_IDs.fetchall()
        madmins_len = len(madmins)
        bot.send_message(message.chat.id, '������� ��������������:')
        for m in range(0,madmins_len):           
            bot.send_message(message.chat.id, f"{madmins[m][1]} {madmins[m][2]}, ID ������������: {madmins[m][3]}")
        cursor_IDs.execute('SELECT * FROM Admin_Level')
        admins = cursor_IDs.fetchall()
        admins_len = len(admins)
        bot.send_message(message.chat.id, '��������������:')
        for a in range(0,admins_len):           
            bot.send_message(message.chat.id, f"{admins[a][1]} {admins[a][2]}, ID ������������: {admins[a][3]}")
        cursor_IDs.execute('SELECT * FROM User_Level')
        users = cursor_IDs.fetchall() 
        users_len = len(users)
        bot.send_message(message.chat.id, '������������:')
        for u in range(0,users_len):           
            bot.send_message(message.chat.id, f"{users[u][1]} {users[u][2]}, ID ������������: {users[u][3]}")
        id_con.close()
    elif message.text == '������� ������������':
        bot.send_message(message.chat.id, '������� ������� ������������:', reply_markup=canselcontrol)
        bot.set_state(message.from_user.id, BotStates.DelUser, message.chat.id)
    elif message.text == '������ ��������������':
        bot.send_message(message.chat.id, '������� ������� ������������:', reply_markup=canselcontrol)
        bot.set_state(message.from_user.id, BotStates.AddAdm, message.chat.id)
    elif message.text == '������� �� ���������������':
        bot.send_message(message.chat.id, '������� ������� ������������:', reply_markup=canselcontrol)
        bot.set_state(message.from_user.id, BotStates.DelAdm, message.chat.id)
    elif message.text == '������ ��. ��������������':
        bot.send_message(message.chat.id, '������� ������� ������������:', reply_markup=canselcontrol)
        bot.set_state(message.from_user.id, BotStates.AddMAdm, message.chat.id)
    elif message.text == '������� �� ��. ���������������':
        bot.send_message(message.chat.id, '������� ������� ������������:', reply_markup=canselcontrol)
        bot.set_state(message.from_user.id, BotStates.DelMAdm, message.chat.id)
    elif message.text == '������':
        bot.send_message(message.chat.id, '�������� ��������.', reply_markup=useradministrationkbrd)
        bot.set_state(message.from_user.id, BotStates.AdmUsers, message.chat.id)
@bot.message_handler(state=BotStates.DelUser)
def deluser(message):
    id_con = sqlite3.connect(r"C:\ProgramData\InSAT\MasterOPC Universal Modbus Server\Users_ID_Data.sqlite3")
    cursor_IDs = id_con.cursor()
    cursor_IDs.execute('SELECT * FROM MainAdmin_Level')
    madmins = cursor_IDs.fetchall()
    mainadmin = False
    cursor_IDs.execute('SELECT * FROM Admin_Level')
    admins = cursor_IDs.fetchall()
    admin = False
    cursor_IDs.execute('SELECT * FROM User_Level')
    users = cursor_IDs.fetchall()
    user = False
    deldone = False
    for m in madmins:
        if f"{message.text}" in m[1]:             
            mainadmin = True
    for a in admins:
        if f"{message.text}" in a[1]:             
            admin = True
    for u in users:
        if f"{message.text}" in u[1]:
            selsecteduser = u
            user = True
    if message.text == '������':
        bot.send_message(message.chat.id, '�������� ��������.', reply_markup=deleteuserkbrd)
        bot.set_state(message.from_user.id, BotStates.UsersControl, message.chat.id)
    else:
        if user:
            if selsecteduser[3] == str(message.chat.id):
                bot.send_message(message.chat.id, '�� �� ������ �������� ������ �������� ��� �����, ���������� �� ������� � ������� �������� ���������������, ���� �������� ���, �������� ���.')
            else:
                if mainadmin:
                    cursor_IDs.execute('DELETE FROM MainAdmin_Level WHERE surname = ?', (f"{message.text}",))
                    id_con.commit()
                    deldone = True
                if admin:
                    cursor_IDs.execute('DELETE FROM Admin_Level WHERE surname = ?', (f"{message.text}",))
                    id_con.commit()
                    deldone = True
                if user:
                    cursor_IDs.execute('DELETE FROM User_Level WHERE surname = ?', (f"{message.text}",))
                    id_con.commit()
                    deldone = True
                if deldone:
                    bot.send_message(message.chat.id, '������ ������������ ������ �� ���� ������.', reply_markup=deleteuserkbrd)
                    bot.send_message(selsecteduser[3], '�� ���� ������� �� ���� ������ ������� ���������������.')
                    bot.set_state(message.from_user.id, BotStates.UsersControl, message.chat.id)
        else:
            bot.send_message(message.chat.id, '������� ������������ �� ���������� � ���� ������.')
    id_con.close()
@bot.message_handler(state=BotStates.AddAdm)
def addadmin(message):
    id_con = sqlite3.connect(r"C:\ProgramData\InSAT\MasterOPC Universal Modbus Server\Users_ID_Data.sqlite3")
    cursor_IDs = id_con.cursor()
    cursor_IDs.execute('SELECT * FROM MainAdmin_Level')
    madmins = cursor_IDs.fetchall()
    mainadmin = False
    cursor_IDs.execute('SELECT * FROM Admin_Level')
    admins = cursor_IDs.fetchall()
    admin = False
    cursor_IDs.execute('SELECT * FROM User_Level')
    users = cursor_IDs.fetchall()
    user = False
    for m in madmins:
        if f"{message.text}" in m[1]:             
            mainadmin = True
    for a in admins:
        if f"{message.text}" in a[1]:             
            admin = True
    for u in users:
        if f"{message.text}" in u[1]:
            selsecteduser = u
            user = True 
    if message.text == '������':
        bot.send_message(message.chat.id, '�������� ��������.', reply_markup=deleteuserkbrd)
        bot.set_state(message.from_user.id, BotStates.UsersControl, message.chat.id)
    else:    
        if user:
            if selsecteduser[3] == str(message.chat.id):
                bot.send_message(message.chat.id, '�� �� ������ �������� ������ �������� ��� �����, ���������� �� ������� � ������� �������� ���������������, ���� �������� ���, �������� ���.')
            else:    
                if not admin:
                    cursor_IDs.execute('INSERT INTO Admin_Level VALUES (NULL, ?, ?, ?)', (f"{selsecteduser[1]}", f"{selsecteduser[2]}", f"{selsecteduser[3]}",))
                    id_con.commit()
                    bot.send_message(message.chat.id, '������� ������������ ��� ����� ������� ��������������.', reply_markup=deleteuserkbrd)
                    bot.send_message(selsecteduser[3], '��� ��� ����� ������� �������������� ������� ���������������.')
                    bot.set_state(message.from_user.id, BotStates.UsersControl, message.chat.id)
                else:
                    bot.send_message(message.chat.id, '������ ������������ ��� �������� ���������������.')
        else:
            bot.send_message(message.chat.id, '������� ������������ �� ���������� � ���� ������.')
    id_con.close()
@bot.message_handler(state=BotStates.DelAdm)
def deladmin(message):
    id_con = sqlite3.connect(r"C:\ProgramData\InSAT\MasterOPC Universal Modbus Server\Users_ID_Data.sqlite3")
    cursor_IDs = id_con.cursor()
    cursor_IDs.execute('SELECT * FROM MainAdmin_Level')
    madmins = cursor_IDs.fetchall()
    mainadmin = False
    cursor_IDs.execute('SELECT * FROM Admin_Level')
    admins = cursor_IDs.fetchall()
    admin = False
    cursor_IDs.execute('SELECT * FROM User_Level')
    users = cursor_IDs.fetchall()
    user = False
    for m in madmins:
        if f"{message.text}" in m[1]:             
            mainadmin = True
    for a in admins:
        if f"{message.text}" in a[1]:             
            admin = True
    for u in users:
        if f"{message.text}" in u[1]:
            selsecteduser = u
            user = True
    if message.text == '������':
        bot.send_message(message.chat.id, '�������� ��������.', reply_markup=deleteuserkbrd)
        bot.set_state(message.from_user.id, BotStates.UsersControl, message.chat.id)
    else:    
        if user:        
            if selsecteduser[3] == str(message.chat.id):
                bot.send_message(message.chat.id, '�� �� ������ �������� ������ �������� ��� �����, ���������� �� ������� � ������� �������� ���������������, ���� �������� ���, �������� ���.')
            else:        
                if not mainadmin:
                    if admin:
                        cursor_IDs.execute('DELETE FROM Admin_Level WHERE surname = ?', (f"{message.text}",))             
                        id_con.commit() 
                        bot.send_message(message.chat.id, '������ ������������ ��� ������� �� ������ ������������.', reply_markup=deleteuserkbrd)
                        bot.send_message(selsecteduser[3], '��� ������� ��� ������� �� ������ ������������ ������� ���������������.')
                        bot.set_state(message.from_user.id, BotStates.UsersControl, message.chat.id)
                    else:
                        bot.send_message(message.chat.id, '� ������� ������������ ����������� ������� ��������������.')
                else:
                    bot.send_message(message.chat.id, '������ ������������ �������� ������� ���������������, �������� ��� �� ������ ��������������, ����� ��������� ������ ��������.')
        else:
            bot.send_message(message.chat.id, '������� ������������ �� ���������� � ���� ������.')
    id_con.close()
@bot.message_handler(state=BotStates.AddMAdm)
def addmainadmin(message):
    id_con = sqlite3.connect(r"C:\ProgramData\InSAT\MasterOPC Universal Modbus Server\Users_ID_Data.sqlite3")
    cursor_IDs = id_con.cursor()
    cursor_IDs.execute('SELECT * FROM MainAdmin_Level')
    madmins = cursor_IDs.fetchall()
    mainadmin = False
    cursor_IDs.execute('SELECT * FROM Admin_Level')
    admins = cursor_IDs.fetchall()
    admin = False
    cursor_IDs.execute('SELECT * FROM User_Level')
    users = cursor_IDs.fetchall()
    user = False
    for m in madmins:
        if f"{message.text}" in m[1]:             
            mainadmin = True
    for a in admins:
        if f"{message.text}" in a[1]:             
            admin = True
    for u in users:
        if f"{message.text}" in u[1]:
            selsecteduser = u
            user = True 
    if message.text == '������':
        bot.send_message(message.chat.id, '�������� ��������.', reply_markup=deleteuserkbrd)
        bot.set_state(message.from_user.id, BotStates.UsersControl, message.chat.id)
    else:    
        if user:
            if selsecteduser[3] == str(message.chat.id):
                bot.send_message(message.chat.id, '�� �� ������ �������� ������ �������� ��� �����, ���������� �� ������� � ������� �������� ���������������, ���� �������� ���, �������� ���.')
            else:      
                if admin:
                    if not mainadmin:
                        cursor_IDs.execute('INSERT INTO MainAdmin_Level VALUES (NULL, ?, ?, ?)', (f"{selsecteduser[1]}", f"{selsecteduser[2]}", f"{selsecteduser[3]}",))
                        id_con.commit()
                        bot.send_message(message.chat.id, '������� ������������ ��� ����� ������� �������� ��������������.', reply_markup=deleteuserkbrd)
                        bot.send_message(selsecteduser[3], '��� ��� ����� ������� �������� �������������� ������� ���������������.')
                        bot.set_state(message.from_user.id, BotStates.UsersControl, message.chat.id)
                    else:
                        bot.send_message(message.chat.id, '������ ������������ ��� �������� ������� ���������������.')
                else:
                    cursor_IDs.execute('INSERT INTO Admin_Level VALUES (NULL, ?, ?, ?)', (f"{selsecteduser[1]}", f"{selsecteduser[2]}", f"{selsecteduser[3]}",))
                    id_con.commit()
                    bot.send_message(message.chat.id, '������� ������������ ��� ����� ������� ��������������.')
                    bot.send_message(selsecteduser[3], '��� ��� ����� ������� �������������� ������� ���������������.')
                    cursor_IDs.execute('INSERT INTO MainAdmin_Level VALUES (NULL, ?, ?, ?)', (f"{selsecteduser[1]}", f"{selsecteduser[2]}", f"{selsecteduser[3]}",))
                    id_con.commit()
                    bot.send_message(message.chat.id, '������� ������������ ��� ����� ������� �������� ��������������.', reply_markup=deleteuserkbrd)
                    bot.send_message(selsecteduser[3], '��� ��� ����� ������� �������� �������������� ������� ���������������.')
                    bot.set_state(message.from_user.id, BotStates.UsersControl, message.chat.id)
        else:
            bot.send_message(message.chat.id, '������� ������������ �� ���������� � ���� ������.')
    id_con.close()
@bot.message_handler(state=BotStates.DelMAdm)
def delmainadmin(message):
    id_con = sqlite3.connect(r"C:\ProgramData\InSAT\MasterOPC Universal Modbus Server\Users_ID_Data.sqlite3")
    cursor_IDs = id_con.cursor()
    cursor_IDs.execute('SELECT * FROM MainAdmin_Level')
    madmins = cursor_IDs.fetchall()
    mainadmin = False
    cursor_IDs.execute('SELECT * FROM Admin_Level')
    admins = cursor_IDs.fetchall()
    admin = False
    cursor_IDs.execute('SELECT * FROM User_Level')
    users = cursor_IDs.fetchall()
    user = False
    for m in madmins:
        if f"{message.text}" in m[1]:             
            mainadmin = True
    for a in admins:
        if f"{message.text}" in a[1]:             
            admin = True
    for u in users:
        if f"{message.text}" in u[1]:
            selsecteduser = u
            user = True
    if message.text == '������':
        bot.send_message(message.chat.id, '�������� ��������.', reply_markup=deleteuserkbrd)
        bot.set_state(message.from_user.id, BotStates.UsersControl, message.chat.id)
    else:    
        if user:
            if selsecteduser[3] == str(message.chat.id):
                bot.send_message(message.chat.id, '�� �� ������ �������� ������ �������� ��� �����, ���������� �� ������� � ������� �������� ���������������, ���� �������� ���, �������� ���.')
            else:     
                if admin:
                    if mainadmin:
                        cursor_IDs.execute('DELETE FROM MainAdmin_Level WHERE surname = ?', (f"{message.text}",))             
                        id_con.commit() 
                        bot.send_message(message.chat.id, '������ ������������ ��� ������� �� ������ ��������������.', reply_markup=deleteuserkbrd)
                        bot.send_message(selsecteduser[3], '��� ������� ��� ������� �� ������ �������������� ������� ���������������.')
                        bot.set_state(message.from_user.id, BotStates.UsersControl, message.chat.id)
                    else:
                        bot.send_message(message.chat.id, '������ ������������ ��� �������� ���������������.')
                else:
                    bot.send_message(message.chat.id, '������ ������������ �������� �������������.')
        else:
            bot.send_message(message.chat.id, '������� ������������ �� ���������� � ���� ������.')
    id_con.close()
@bot.message_handler(state=BotStates.PassControl)
def passcontrol(message):
    if message.text == '�������� �������':
        id_con = sqlite3.connect(r"C:\ProgramData\InSAT\MasterOPC Universal Modbus Server\Users_ID_Data.sqlite3")
        cursor_IDs = id_con.cursor()
        cursor_IDs.execute('SELECT * FROM Passwords')
        pas = cursor_IDs.fetchall()
        bot.send_message(message.chat.id, f"����������������: {pas[0][2]}")
        bot.send_message(message.chat.id, f"�����������������: {pas[1][2]}")
        bot.send_message(message.chat.id, f"������� �����������������: {pas[2][2]}")
        id_con.close()
    elif message.text == '������� ������ ������������':
        bot.send_message(message.chat.id, '������� ����� ������:', reply_markup=canselcontrol)
        bot.set_state(message.from_user.id, BotStates.EditPassUser, message.chat.id)
    elif message.text == '�������� ������ ��������������':
        bot.send_message(message.chat.id, '������� ����� ������:', reply_markup=canselcontrol)
        bot.set_state(message.from_user.id, BotStates.EditPassAdmin, message.chat.id)
    elif message.text == '������� ������ ��. ��������������':
        bot.send_message(message.chat.id, '������� ����� ������:', reply_markup=canselcontrol)
        bot.set_state(message.from_user.id, BotStates.EditPassMAdmin, message.chat.id)
    elif message.text == '������':
        bot.send_message(message.chat.id, '�������� ��������.', reply_markup=useradministrationkbrd)
        bot.set_state(message.from_user.id, BotStates.AdmUsers, message.chat.id)
@bot.message_handler(state=BotStates.EditPassUser)
def edituserpass(message):
    if message.text == '������':
        bot.send_message(message.chat.id, '�������� ��������.', reply_markup=editpasskbrd)
        bot.set_state(message.from_user.id, BotStates.PassControl, message.chat.id)
    else:    
        id_con = sqlite3.connect(r"C:\ProgramData\InSAT\MasterOPC Universal Modbus Server\Users_ID_Data.sqlite3")
        cursor_IDs = id_con.cursor()
        cursor_IDs.execute('UPDATE Passwords SET pass = ? WHERE id = 1;', (f"{message.text}",))
        id_con.commit()
        bot.send_message(message.chat.id, '������ ������������ ��������.', reply_markup=editpasskbrd)
        bot.set_state(message.from_user.id, BotStates.PassControl, message.chat.id)
        id_con.close()
@bot.message_handler(state=BotStates.EditPassAdmin)
def editadminpass(message):
    if message.text == '������':
        bot.send_message(message.chat.id, '�������� ��������.', reply_markup=editpasskbrd)
        bot.set_state(message.from_user.id, BotStates.PassControl, message.chat.id)
    else:    
        id_con = sqlite3.connect(r"C:\ProgramData\InSAT\MasterOPC Universal Modbus Server\Users_ID_Data.sqlite3")
        cursor_IDs = id_con.cursor()
        cursor_IDs.execute('UPDATE Passwords SET pass = ? WHERE id = 2;', (f"{message.text}",))
        id_con.commit()
        bot.send_message(message.chat.id, '������ �������������� ��������.', reply_markup=editpasskbrd)
        bot.set_state(message.from_user.id, BotStates.PassControl, message.chat.id)
        id_con.close()
@bot.message_handler(state=BotStates.EditPassMAdmin)
def editmadminpass(message):
    if message.text == '������':
        bot.send_message(message.chat.id, '�������� ��������.', reply_markup=editpasskbrd)
        bot.set_state(message.from_user.id, BotStates.PassControl, message.chat.id)
    else:    
        id_con = sqlite3.connect(r"C:\ProgramData\InSAT\MasterOPC Universal Modbus Server\Users_ID_Data.sqlite3")
        cursor_IDs = id_con.cursor()
        cursor_IDs.execute('UPDATE Passwords SET pass = ? WHERE id = 3;', (f"{message.text}",))
        id_con.commit()
        bot.send_message(message.chat.id, '������ �������� �������������� ��������.', reply_markup=editpasskbrd)
        bot.set_state(message.from_user.id, BotStates.PassControl, message.chat.id)
        id_con.close()
@bot.callback_query_handler(func=lambda call: True)
def getsystem(call):
    id_con = sqlite3.connect(r"C:\ProgramData\InSAT\MasterOPC Universal Modbus Server\Users_ID_Data.sqlite3")
    cursor_IDs = id_con.cursor()
    cursor_IDs.execute('SELECT * FROM MainAdmin_Level')
    madmins = cursor_IDs.fetchall()
    mainadmin = False
    admin = False
    global System_Files
    global Reset_Files
    global SetPoint_Files
    global Table_Datas
    global Table_Alarms
    global Table_Control
    global Names_Data_For_Sel
    global Name_Alarm_For_Sel
    global sysname
    global sysnameshort
    global ukeyboard
    global akeyboard
    global makeyboard
    global Knc1Datas
    global Knc1Alarm
    global Abk1Datas
    global Abk1Alarms
    global Abk2Datas
    global Abk2Alarms
    global Abk3Datas
    global Abk3Alarms
    global Abk4Datas
    global Abk4Alarms
    global Knc2Datas
    global Knc2Alarm
    global Abk1WDatas
    global Abk1WAlarms
    global Abk2WDatas
    global Abk2WAlarms
    global Abk3WDatas
    global Abk3WAlarms
    global Abk4WDatas
    global Abk4WAlarms
    global schemes
    if call.data == '1':
        if not (('Knc1_Datas' in Table_Datas) and ('Knc1_Alarms' in Table_Alarms) and ('Knc1_Control' in Table_Control)):
            System_Files.append('_KNC1')
            Reset_Files.append('NO_RESETK1')
            SetPoint_Files.append('NO_SPK1')
            Mode_Files.append('NO_MODEK1')
            Table_Datas.append('Knc1_Datas')
            Table_Alarms.append('Knc1_Alarms')
            Table_Control.append('Knc1_Control')
            schemes.append("NO_SCHEME1")
            Knc1Datas = Knc_Data_Tag_Name
            Knc1Alarm = Knc_Alarm_Tag_Name
            Names_Data_For_Sel.append(Knc1Datas)
            Name_Alarm_For_Sel.append(Knc1Alarm)
            sysname.append('��� 1')
            sysnameshort.append('��� 1')
            ukeyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
            ukeyboard.add(types.KeyboardButton(f"���������� � {sysnameshort[1]}"))
            ukeyboard.add(types.KeyboardButton('������ ������'), types.KeyboardButton('������� ����'))
            akeyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
            akeyboard.add(types.KeyboardButton(f"���������� � {sysnameshort[1]}"))
            akeyboard.add(types.KeyboardButton('������ ������'), types.KeyboardButton('������� ����'))
            makeyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
            makeyboard.add(types.KeyboardButton(f"���������� � {sysnameshort[1]}"))
            makeyboard.add(types.KeyboardButton('������ ������'), types.KeyboardButton('������� ����'))
            bot.send_message(call.message.chat.id, '������� ��� 1 �������� � ������ ��� ������.')
        else:
            System_Files.remove('_KNC1')
            Reset_Files.remove('NO_RESETK1')
            SetPoint_Files.remove('NO_SPK1')
            Mode_Files.remove('NO_MODEK1')
            Table_Datas.remove('Knc1_Datas')
            Table_Alarms.remove('Knc1_Alarms')
            Table_Control.remove('Knc1_Control')
            schemes.remove("NO_SCHEME1")
            Names_Data_For_Sel.remove(Knc1Datas)
            Name_Alarm_For_Sel.remove(Knc1Alarm)
            sysname.remove('��� 1')
            sysnameshort.remove('��� 1')
            bot.send_message(call.message.chat.id, '������� ��� 1 ������� �� ������ ��� ������.')
    elif call.data == '2':
        if not (('Itp_Datas' in Table_Datas) and ('Itp_Alarms' in Table_Alarms) and ('Itp_Control' in Table_Control)):
            System_Files.append('_ITP')
            Reset_Files.append('_ITP_R')
            SetPoint_Files.append('NO_SPI')
            Mode_Files.append('NO_MODEI')
            Table_Datas.append('Itp_Datas')
            Table_Alarms.append('Itp_Alarms')
            Table_Control.append('Itp_Control')
            schemes.append("C:\ProgramData\InSAT\ITP.pdf")
            Names_Data_For_Sel.append(Itp_Data_Tag_Name)
            Name_Alarm_For_Sel.append(Itp_Alarm_Tag_Name)
            sysname.append('���')
            sysnameshort.append('���')
            ukeyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
            ukeyboard.add(types.KeyboardButton(f"���������� � {sysnameshort[1]}"))
            ukeyboard.add(types.KeyboardButton('����� ������'), types.KeyboardButton('������ ������'), types.KeyboardButton('������� ����'))
            akeyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
            akeyboard.add(types.KeyboardButton(f"���������� � {sysnameshort[1]}"))
            akeyboard.add(types.KeyboardButton('����� ������'), types.KeyboardButton('������ ������'), types.KeyboardButton('������� ����'))
            makeyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
            makeyboard.add(types.KeyboardButton(f"���������� � {sysnameshort[1]}"))
            makeyboard.add(types.KeyboardButton('����� ������'), types.KeyboardButton('������ ������'), types.KeyboardButton('������� ����'))
            bot.send_message(call.message.chat.id, '������� ��� �������� � ������ ��� ������.')
        else:
            System_Files.remove('_ITP')
            Reset_Files.remove('_ITP_R')
            SetPoint_Files.remove('NO_SPI')
            Mode_Files.remove('NO_MODEI')
            Table_Datas.remove('Itp_Datas')
            Table_Alarms.remove('Itp_Alarms')
            Table_Control.remove('Itp_Control')
            schemes.remove("C:\ProgramData\InSAT\ITP.pdf")
            Names_Data_For_Sel.remove(Itp_Data_Tag_Name)
            Name_Alarm_For_Sel.remove(Itp_Alarm_Tag_Name)
            sysname.remove('���')
            sysnameshort.remove('���')
            bot.send_message(call.message.chat.id, '������� ��� ������� �� ������ ��� ������.')
    elif call.data == '3':
        if not (('Pv4_Datas' in Table_Datas) and ('Pv4_Alarms' in Table_Alarms) and ('Pv4_Control' in Table_Control)):
            System_Files.append('_PV4')
            Reset_Files.append('_PV4_R')
            SetPoint_Files.append('_PV4_S')
            Mode_Files.append('NO_MODEP')
            Table_Datas.append('Pv4_Datas')
            Table_Alarms.append('Pv4_Alarms')
            Table_Control.append('Pv4_Control')
            schemes.append("C:\ProgramData\InSAT\PV4.pdf")
            Names_Data_For_Sel.append(Pv4_Data_Tag_Name)
            Name_Alarm_For_Sel.append(Pv4_Alarm_Tag_Name)
            sysname.append('�� 4')
            sysnameshort.append('�� 4')
            ukeyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
            ukeyboard.add(types.KeyboardButton(f"���������� � {sysnameshort[1]}"))
            ukeyboard.add(types.KeyboardButton('����� ������'), types.KeyboardButton('������ ������'), types.KeyboardButton('������� ����'))
            akeyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
            akeyboard.add(types.KeyboardButton(f"���������� � {sysnameshort[1]}"))
            akeyboard.add(types.KeyboardButton(f"���������� {sysnameshort[1]}"), types.KeyboardButton('�������� �������'))
            akeyboard.add(types.KeyboardButton('����� ������'), types.KeyboardButton('������ ������'), types.KeyboardButton('������� ����'))
            makeyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
            makeyboard.add(types.KeyboardButton(f"���������� � {sysnameshort[1]}"))
            makeyboard.add(types.KeyboardButton(f"���������� {sysnameshort[1]}"), types.KeyboardButton('�������� �������'))
            makeyboard.add(types.KeyboardButton('����� ������'), types.KeyboardButton('������ ������'), types.KeyboardButton('������� ����'))
            bot.send_message(call.message.chat.id, '������� �� 4 �������� � ������ ��� ������.')
        else:
            System_Files.remove('_PV4')
            Reset_Files.remove('_PV4_R')
            SetPoint_Files.remove('_PV4_S')
            Mode_Files.remove('NO_MODEP')
            Table_Datas.remove('Pv4_Datas')
            Table_Alarms.remove('Pv4_Alarms')
            Table_Control.remove('Pv4_Control')
            schemes.remove("C:\ProgramData\InSAT\PV4.pdf")
            Names_Data_For_Sel.remove(Pv4_Data_Tag_Name)
            Name_Alarm_For_Sel.remove(Pv4_Alarm_Tag_Name)
            sysname.remove('�� 4')
            sysnameshort.remove('�� 4')
            bot.send_message(call.message.chat.id, '������� �� 4 ������� �� ������ ��� ������.')
    elif call.data == '4':
        if not (('Abk1_E_Datas' in Table_Datas) and ('Abk1_E_Alarms' in Table_Alarms) and ('Abk1_E_Control' in Table_Control)):
            System_Files.append('_ABK1E')
            Reset_Files.append('_ABK1E_R')
            SetPoint_Files.append('_ABK1E_S')
            Mode_Files.append('NO_MODEA1')
            Table_Datas.append('Abk1_E_Datas')
            Table_Alarms.append('Abk1_E_Alarms')
            Table_Control.append('Abk1_E_Control')
            schemes.append("C:\ProgramData\InSAT\E1.pdf")
            Abk1Datas = Abk_E_Data_Tag_Name
            Abk1Alarms = Abk_E_Alarm_Tag_Name
            Names_Data_For_Sel.append(Abk1Datas)
            Name_Alarm_For_Sel.append(Abk1Alarms)
            sysname.append('��� 1 ��������������')
            sysnameshort.append('��� 1 �.')
            ukeyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
            ukeyboard.add(types.KeyboardButton(f"���������� � {sysnameshort[1]}"))
            ukeyboard.add(types.KeyboardButton('����� ������'), types.KeyboardButton('������ ������'), types.KeyboardButton('������� ����'))
            akeyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
            akeyboard.add(types.KeyboardButton(f"���������� � {sysnameshort[1]}"))
            akeyboard.add(types.KeyboardButton(f"���������� {sysnameshort[1]}"), types.KeyboardButton('�������� �������'))
            akeyboard.add(types.KeyboardButton('����� ������'), types.KeyboardButton('������ ������'), types.KeyboardButton('������� ����'))
            makeyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
            makeyboard.add(types.KeyboardButton(f"���������� � {sysnameshort[1]}"))
            makeyboard.add(types.KeyboardButton(f"���������� {sysnameshort[1]}"), types.KeyboardButton('�������� �������'))
            makeyboard.add(types.KeyboardButton('����� ������'), types.KeyboardButton('������ ������'), types.KeyboardButton('������� ����'))
            bot.send_message(call.message.chat.id, '������� ��� 1 �������������� �������� � ������ ��� ������.')
        else:
            System_Files.remove('_ABK1E')
            Reset_Files.remove('_ABK1E_R')
            SetPoint_Files.remove('_ABK1E_S')
            Mode_Files.append('NO_MODEA1')
            Table_Datas.remove('Abk1_E_Datas')
            Table_Alarms.remove('Abk1_E_Alarms')
            Table_Control.remove('Abk1_E_Control')
            schemes.remove("C:\ProgramData\InSAT\E1.pdf")
            Names_Data_For_Sel.remove(Abk1Datas)
            Name_Alarm_For_Sel.remove(Abk1Alarms)
            sysname.remove('��� 1 ��������������')
            sysnameshort.remove('��� 1 �.')
            bot.send_message(call.message.chat.id, '������� ��� 1 �������������� ������� �� ������ ��� ������.')
    elif call.data == '5':
        if not (('Abk2_E_Datas' in Table_Datas) and ('Abk2_E_Alarms' in Table_Alarms) and ('Abk2_E_Control' in Table_Control)):
            System_Files.append('_ABK2E')
            Reset_Files.append('_ABK2E_R')
            SetPoint_Files.append('_ABK2E_S')
            Mode_Files.append('NO_MODEA2')
            Table_Datas.append('Abk2_E_Datas')
            Table_Alarms.append('Abk2_E_Alarms')
            Table_Control.append('Abk2_E_Control')
            schemes.append("C:\ProgramData\InSAT\E2.pdf")
            Abk2Datas = Abk_E_Data_Tag_Name
            Abk2Alarms = Abk_E_Alarm_Tag_Name
            Names_Data_For_Sel.append(Abk2Datas)
            Name_Alarm_For_Sel.append(Abk2Alarms)
            sysname.append('��� 2 ��������������')
            sysnameshort.append('��� 2 �.')
            ukeyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
            ukeyboard.add(types.KeyboardButton(f"���������� � {sysnameshort[1]}"))
            ukeyboard.add(types.KeyboardButton('����� ������'), types.KeyboardButton('������ ������'), types.KeyboardButton('������� ����'))
            akeyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
            akeyboard.add(types.KeyboardButton(f"���������� � {sysnameshort[1]}"))
            akeyboard.add(types.KeyboardButton(f"���������� {sysnameshort[1]}"), types.KeyboardButton('�������� �������'))
            akeyboard.add(types.KeyboardButton('����� ������'), types.KeyboardButton('������ ������'), types.KeyboardButton('������� ����'))
            makeyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
            makeyboard.add(types.KeyboardButton(f"���������� � {sysnameshort[1]}"))
            makeyboard.add(types.KeyboardButton(f"���������� {sysnameshort[1]}"), types.KeyboardButton('�������� �������'))
            makeyboard.add(types.KeyboardButton('����� ������'), types.KeyboardButton('������ ������'), types.KeyboardButton('������� ����'))
            bot.send_message(call.message.chat.id, '������� ��� 2 �������������� �������� � ������ ��� ������.')
        else:
            System_Files.remove('_ABK2E')
            Reset_Files.remove('_ABK2E_R')
            SetPoint_Files.remove('_ABK2E_S')
            Mode_Files.remove('NO_MODEA2')
            Table_Datas.remove('Abk2_E_Datas')
            Table_Alarms.remove('Abk2_E_Alarms')
            Table_Control.remove('Abk2_E_Control')
            schemes.remove("C:\ProgramData\InSAT\E2.pdf")
            Names_Data_For_Sel.remove(Abk2Datas)
            Name_Alarm_For_Sel.remove(Abk2Alarms)
            sysname.remove('��� 2 ��������������')
            sysnameshort.remove('��� 2 �.')
            bot.send_message(call.message.chat.id, '������� ��� 2 �������������� ������� �� ������ ��� ������.')
    elif call.data == '6':
        if not (('Abk3_E_Datas' in Table_Datas) and ('Abk3_E_Alarms' in Table_Alarms) and ('Abk3_E_Control' in Table_Control)):
            System_Files.append('_ABK3E')
            Reset_Files.append('_ABK3E_R')
            SetPoint_Files.append('_ABK3E_S')
            Mode_Files.append('NO_MODEA3')
            Table_Datas.append('Abk3_E_Datas')
            Table_Alarms.append('Abk3_E_Alarms')
            Table_Control.append('Abk3_E_Control')
            schemes.append("C:\ProgramData\InSAT\E3.pdf")
            Abk3Datas = Abk_E_Data_Tag_Name
            Abk3Alarms = Abk_E_Alarm_Tag_Name
            Names_Data_For_Sel.append(Abk3Datas)
            Name_Alarm_For_Sel.append(Abk3Alarms)
            sysname.append('��� 3 ��������������')
            sysnameshort.append('��� 3 �.')
            ukeyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
            ukeyboard.add(types.KeyboardButton(f"���������� � {sysnameshort[1]}"))
            ukeyboard.add(types.KeyboardButton('����� ������'), types.KeyboardButton('������ ������'), types.KeyboardButton('������� ����'))
            akeyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
            akeyboard.add(types.KeyboardButton(f"���������� � {sysnameshort[1]}"))
            akeyboard.add(types.KeyboardButton(f"���������� {sysnameshort[1]}"), types.KeyboardButton('�������� �������'))
            akeyboard.add(types.KeyboardButton('����� ������'), types.KeyboardButton('������ ������'), types.KeyboardButton('������� ����'))
            makeyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
            makeyboard.add(types.KeyboardButton(f"���������� � {sysnameshort[1]}"))
            makeyboard.add(types.KeyboardButton(f"���������� {sysnameshort[1]}"), types.KeyboardButton('�������� �������'))
            makeyboard.add(types.KeyboardButton('����� ������'), types.KeyboardButton('������ ������'), types.KeyboardButton('������� ����'))
            bot.send_message(call.message.chat.id, '������� ��� 3 �������������� �������� � ������ ��� ������.')
        else:
            System_Files.remove('_ABK3E')
            Reset_Files.remove('_ABK3E_R')
            SetPoint_Files.remove('_ABK3E_S')
            Mode_Files.remove('NO_MODEA3')
            Table_Datas.remove('Abk3_E_Datas')
            Table_Alarms.remove('Abk3_E_Alarms')
            Table_Control.remove('Abk3_E_Control')
            schemes.remove("C:\ProgramData\InSAT\E3.pdf")
            Names_Data_For_Sel.remove(Abk3Datas)
            Name_Alarm_For_Sel.remove(Abk3Alarms)
            sysname.remove('��� 3 ��������������')
            sysnameshort.remove('��� 3 �.')
            bot.send_message(call.message.chat.id, '������� ��� 3 �������������� ������� �� ������ ��� ������.')
    elif call.data == '7':
        if not (('Abk4_E_Datas' in Table_Datas) and ('Abk4_E_Alarms' in Table_Alarms) and ('Abk4_E_Control' in Table_Control)):
            System_Files.append('_ABK4E')
            Reset_Files.append('_ABK4E_R')
            SetPoint_Files.append('_ABK4E_S')
            Mode_Files.append('NO_MODEA4')
            Table_Datas.append('Abk4_E_Datas')
            Table_Alarms.append('Abk4_E_Alarms')
            Table_Control.append('Abk4_E_Control')
            schemes.append("C:\ProgramData\InSAT\E4.pdf")
            Abk4Datas = Abk_E_Data_Tag_Name
            Abk4Alarms = Abk_E_Alarm_Tag_Name
            Names_Data_For_Sel.append(Abk4Datas)
            Name_Alarm_For_Sel.append(Abk4Alarms)
            sysname.append('��� 4 ��������������')
            sysnameshort.append('��� 4 �.')
            ukeyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
            ukeyboard.add(types.KeyboardButton(f"���������� � {sysnameshort[1]}"))
            ukeyboard.add(types.KeyboardButton('����� ������'), types.KeyboardButton('������ ������'), types.KeyboardButton('������� ����'))
            akeyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
            akeyboard.add(types.KeyboardButton(f"���������� � {sysnameshort[1]}"))
            akeyboard.add(types.KeyboardButton(f"���������� {sysnameshort[1]}"), types.KeyboardButton('�������� �������'))
            akeyboard.add(types.KeyboardButton('����� ������'), types.KeyboardButton('������ ������'), types.KeyboardButton('������� ����'))
            makeyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
            makeyboard.add(types.KeyboardButton(f"���������� � {sysnameshort[1]}"))
            makeyboard.add(types.KeyboardButton(f"���������� {sysnameshort[1]}"), types.KeyboardButton('�������� �������'))
            makeyboard.add(types.KeyboardButton('����� ������'), types.KeyboardButton('������ ������'), types.KeyboardButton('������� ����'))
            bot.send_message(call.message.chat.id, '������� ��� 4 �������������� �������� � ������ ��� ������.')
        else:
            System_Files.remove('_ABK4E')
            Reset_Files.remove('_ABK4E_R')
            SetPoint_Files.remove('_ABK4E_S')
            Mode_Files.remove('NO_MODEA4')
            Table_Datas.remove('Abk4_E_Datas')
            Table_Alarms.remove('Abk4_E_Alarms')
            Table_Control.remove('Abk4_E_Control')
            schemes.remove("C:\ProgramData\InSAT\E4.pdf")
            Names_Data_For_Sel.remove(Abk4Datas)
            Name_Alarm_For_Sel.remove(Abk4Alarms)
            sysname.remove('��� 4 ��������������')
            sysnameshort.remove('��� 4 �.')
            bot.send_message(call.message.chat.id, '������� ��� 4 �������������� ������� �� ������ ��� ������.')
    elif call.data == '8':
        if not (('Abk1_W_Datas' in Table_Datas) and ('Abk1_W_Alarms' in Table_Alarms) and ('Abk1_W_Control' in Table_Control)):
            System_Files.append('_ABK1W')
            Reset_Files.append('_ABK1W_R')
            SetPoint_Files.append('_ABK1W_S')
            Mode_Files.append('_ABK1W_M')
            Table_Datas.append('Abk1_W_Datas')
            Table_Alarms.append('Abk1_W_Alarms')
            Table_Control.append('Abk1_W_Control')
            schemes.append("C:\ProgramData\InSAT\W1.pdf")
            Abk1WDatas = Abk_W_Data_Tag_Name
            Abk1WAlarms = Abk_W_Alarm_Tag_Name
            Names_Data_For_Sel.append(Abk1WDatas)
            Name_Alarm_For_Sel.append(Abk1WAlarms)
            sysname.append('��� 1 �������� �������')
            sysnameshort.append('��� 1 �.')
            ukeyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
            ukeyboard.add(types.KeyboardButton(f"���������� � {sysnameshort[1]}"))
            ukeyboard.add(types.KeyboardButton('����� ������'), types.KeyboardButton('������ ������'), types.KeyboardButton('������� ����'))
            akeyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
            akeyboard.add(types.KeyboardButton(f"���������� � {sysnameshort[1]}"), types.KeyboardButton('����� ������ ������'))
            akeyboard.add(types.KeyboardButton(f"���������� {sysnameshort[1]}"), types.KeyboardButton('�������� �������'))
            akeyboard.add(types.KeyboardButton('����� ������'), types.KeyboardButton('������ ������'), types.KeyboardButton('������� ����'))
            makeyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
            makeyboard.add(types.KeyboardButton(f"���������� � {sysnameshort[1]}"), types.KeyboardButton('����� ������ ������'))
            makeyboard.add(types.KeyboardButton(f"���������� {sysnameshort[1]}"), types.KeyboardButton('�������� �������'))
            makeyboard.add(types.KeyboardButton('����� ������'), types.KeyboardButton('������ ������'), types.KeyboardButton('������� ����'))
            bot.send_message(call.message.chat.id, '������� ��� 1 �������� ������� �������� � ������ ��� ������.')
        else:
            System_Files.remove('_ABK1W')
            Reset_Files.remove('_ABK1W_R')
            SetPoint_Files.remove('_ABK1W_S')
            Mode_Files.remove('_ABK1W_M')
            Table_Datas.remove('Abk1_W_Datas')
            Table_Alarms.remove('Abk1_W_Alarms')
            Table_Control.remove('Abk1_W_Control')
            schemes.remove("C:\ProgramData\InSAT\W1.pdf")
            Names_Data_For_Sel.remove(Abk1WDatas)
            Name_Alarm_For_Sel.remove(Abk1WAlarms)
            sysname.remove('��� 1 �������� �������')
            sysnameshort.remove('��� 1 �.')
            bot.send_message(call.message.chat.id, '������� ��� 1 �������� ������� ������� �� ������ ��� ������.')
    elif call.data == '9':
        if not (('Abk2_W_Datas' in Table_Datas) and ('Abk2_W_Alarms' in Table_Alarms) and ('Abk2_W_Control' in Table_Control)):
            System_Files.append('_ABK2W')
            Reset_Files.append('_ABK2W_R')
            SetPoint_Files.append('_ABK2W_S')
            Mode_Files.append('_ABK2W_M')
            Table_Datas.append('Abk2_W_Datas')
            Table_Alarms.append('Abk2_W_Alarms')
            Table_Control.append('Abk2_W_Control')
            schemes.append("C:\ProgramData\InSAT\W2.pdf")
            Abk2WDatas = Abk_W_Data_Tag_Name
            Abk2WAlarms = Abk_W_Alarm_Tag_Name
            Names_Data_For_Sel.append(Abk2WDatas)
            Name_Alarm_For_Sel.append(Abk2WAlarms)
            sysname.append('��� 2 �������� �������')
            sysnameshort.append('��� 2 �.')
            ukeyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
            ukeyboard.add(types.KeyboardButton(f"���������� � {sysnameshort[1]}"))
            ukeyboard.add(types.KeyboardButton('����� ������'), types.KeyboardButton('������ ������'), types.KeyboardButton('������� ����'))
            akeyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
            akeyboard.add(types.KeyboardButton(f"���������� � {sysnameshort[1]}"), types.KeyboardButton('����� ������ ������'))
            akeyboard.add(types.KeyboardButton(f"���������� {sysnameshort[1]}"), types.KeyboardButton('�������� �������'))
            akeyboard.add(types.KeyboardButton('����� ������'), types.KeyboardButton('������ ������'), types.KeyboardButton('������� ����'))
            makeyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
            makeyboard.add(types.KeyboardButton(f"���������� � {sysnameshort[1]}"), types.KeyboardButton('����� ������ ������'))
            makeyboard.add(types.KeyboardButton(f"���������� {sysnameshort[1]}"), types.KeyboardButton('�������� �������'))
            makeyboard.add(types.KeyboardButton('����� ������'), types.KeyboardButton('������ ������'), types.KeyboardButton('������� ����'))
            bot.send_message(call.message.chat.id, '������� ��� 2 �������� ������� �������� � ������ ��� ������.')
        else:
            System_Files.remove('_ABK2W')
            Reset_Files.remove('_ABK2W_R')
            SetPoint_Files.remove('_ABK2W_S')
            Mode_Files.remove('_ABK2W_M')
            Table_Datas.remove('Abk2_W_Datas')
            Table_Alarms.remove('Abk2_W_Alarms')
            Table_Control.remove('Abk2_W_Control')
            schemes.remove("C:\ProgramData\InSAT\W2.pdf")
            Names_Data_For_Sel.remove(Abk2WDatas)
            Name_Alarm_For_Sel.remove(Abk2WAlarms)
            sysname.remove('��� 2 �������� �������')
            sysnameshort.remove('��� 2 �.')
            bot.send_message(call.message.chat.id, '������� ��� 2 �������� ������� ������� �� ������ ��� ������.')
    elif call.data == '10':
        if not (('Abk3_W_Datas' in Table_Datas) and ('Abk3_W_Alarms' in Table_Alarms) and ('Abk3_W_Control' in Table_Control)):
            System_Files.append('_ABK3W')
            Reset_Files.append('_ABK3W_R')
            SetPoint_Files.append('_ABK3W_S')
            Mode_Files.append('_ABK3W_M')
            Table_Datas.append('Abk3_W_Datas')
            Table_Alarms.append('Abk3_W_Alarms')
            Table_Control.append('Abk3_W_Control')
            schemes.append("C:\ProgramData\InSAT\W3.pdf")
            Abk3WDatas = Abk_W_Data_Tag_Name
            Abk3WAlarms = Abk_W_Alarm_Tag_Name
            Names_Data_For_Sel.append(Abk3WDatas)
            Name_Alarm_For_Sel.append(Abk3WAlarms)
            sysname.append('��� 3 �������� �������')
            sysnameshort.append('��� 3 �.')
            ukeyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
            ukeyboard.add(types.KeyboardButton(f"���������� � {sysnameshort[1]}"), types.KeyboardButton('�������� �����������'))
            ukeyboard.add(types.KeyboardButton('����� ������'), types.KeyboardButton('������ ������'), types.KeyboardButton('������� ����'))
            akeyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
            akeyboard.add(types.KeyboardButton(f"���������� � {sysnameshort[1]}"), types.KeyboardButton('����� ������ ������'))
            akeyboard.add(types.KeyboardButton(f"���������� {sysnameshort[1]}"), types.KeyboardButton('�������� �������'))
            akeyboard.add(types.KeyboardButton('����� ������'), types.KeyboardButton('������ ������'), types.KeyboardButton('������� ����'))
            makeyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
            makeyboard.add(types.KeyboardButton(f"���������� � {sysnameshort[1]}"), types.KeyboardButton('����� ������ ������'))
            makeyboard.add(types.KeyboardButton(f"���������� {sysnameshort[1]}"), types.KeyboardButton('�������� �������'))
            makeyboard.add(types.KeyboardButton('����� ������'), types.KeyboardButton('������ ������'), types.KeyboardButton('������� ����'))
            bot.send_message(call.message.chat.id, '������� ��� 3 �������� ������� �������� � ������ ��� ������.')
        else:
            System_Files.remove('_ABK3W')
            Reset_Files.remove('_ABK3W_R')
            SetPoint_Files.remove('_ABK3W_S')
            Mode_Files.remove('_ABK3W_M')
            Table_Datas.remove('Abk3_W_Datas')
            Table_Alarms.remove('Abk3_W_Alarms')
            Table_Control.remove('Abk3_W_Control')
            schemes.remove("C:\ProgramData\InSAT\W3.pdf")
            Names_Data_For_Sel.remove(Abk3WDatas)
            Name_Alarm_For_Sel.remove(Abk3WAlarms)
            sysname.remove('��� 3 �������� �������')
            sysnameshort.remove('��� 3 �.')
            bot.send_message(call.message.chat.id, '������� ��� 3 �������� ������� ������� �� ������ ��� ������.')
    elif call.data == '11':
        if not (('Abk4_W_Datas' in Table_Datas) and ('Abk4_W_Alarms' in Table_Alarms) and ('Abk4_W_Control' in Table_Control)):
            System_Files.append('_ABK4W')
            Reset_Files.append('_ABK4W_R')
            SetPoint_Files.append('_ABK4W_S')
            Mode_Files.append('_ABK4W_M')
            Table_Datas.append('Abk4_W_Datas')
            Table_Alarms.append('Abk4_W_Alarms')
            Table_Control.append('Abk4_W_Control')
            schemes.append("C:\ProgramData\InSAT\W4.pdf")
            Abk4WDatas = Abk_W_Data_Tag_Name
            Abk4WAlarms = Abk_W_Alarm_Tag_Name
            Names_Data_For_Sel.append(Abk4WDatas)
            Name_Alarm_For_Sel.append(Abk4WAlarms)
            sysname.append('��� 4 �������� �������')
            sysnameshort.append('��� 4 �.')
            ukeyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
            ukeyboard.add(types.KeyboardButton(f"���������� � {sysnameshort[1]}"))
            ukeyboard.add(types.KeyboardButton('����� ������'), types.KeyboardButton('������ ������'), types.KeyboardButton('������� ����'))
            akeyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
            akeyboard.add(types.KeyboardButton(f"���������� � {sysnameshort[1]}"), types.KeyboardButton('����� ������ ������'))
            akeyboard.add(types.KeyboardButton(f"���������� {sysnameshort[1]}"), types.KeyboardButton('�������� �������'))
            akeyboard.add(types.KeyboardButton('����� ������'), types.KeyboardButton('������ ������'), types.KeyboardButton('������� ����'))
            makeyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
            makeyboard.add(types.KeyboardButton(f"���������� � {sysnameshort[1]}"), types.KeyboardButton('����� ������ ������'))
            makeyboard.add(types.KeyboardButton(f"���������� {sysnameshort[1]}"), types.KeyboardButton('�������� �������'))
            makeyboard.add(types.KeyboardButton('����� ������'), types.KeyboardButton('������ ������'), types.KeyboardButton('������� ����'))
            bot.send_message(call.message.chat.id, '������� ��� 4 �������� ������� �������� � ������ ��� ������.')
        else:
            System_Files.remove('_ABK4W')
            Reset_Files.remove('_ABK4W_R')
            SetPoint_Files.remove('_ABK4W_S')
            Mode_Files.remove('_ABK4W_M')
            Table_Datas.remove('Abk4_W_Datas')
            Table_Alarms.remove('Abk4_W_Alarms')
            Table_Control.remove('Abk4_W_Control')
            schemes.remove("C:\ProgramData\InSAT\W4.pdf")
            Names_Data_For_Sel.remove(Abk4WDatas)
            Name_Alarm_For_Sel.remove(Abk4WAlarms)
            sysname.remove('��� 4 �������� �������')
            sysnameshort.remove('��� 4 �.')
            bot.send_message(call.message.chat.id, '������� ��� 4 �������� ������� ������� �� ������ ��� ������.')
    elif call.data == '12':
        if not (('Knc2_Datas' in Table_Datas) and ('Knc2_Alarms' in Table_Alarms) and ('Knc2_Control' in Table_Control)):
            System_Files.append('_KNC2')
            Reset_Files.append('NO_RESETK2')
            SetPoint_Files.append('NO_SPK2')
            Mode_Files.append('NO_MODEK2')
            Table_Datas.append('Knc2_Datas')
            Table_Alarms.append('Knc2_Alarms')
            Table_Control.append('Knc2_Control')
            schemes.append("NO_SCHEME2")
            Knc2Datas = Knc_Data_Tag_Name
            Knc2Alarm = Knc_Alarm_Tag_Name
            Names_Data_For_Sel.append(Knc2Datas)
            Name_Alarm_For_Sel.append(Knc2Alarm)
            sysname.append('��� 2')
            sysnameshort.append('��� 2')
            ukeyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
            ukeyboard.add(types.KeyboardButton(f"���������� � {sysnameshort[1]}"))
            ukeyboard.add(types.KeyboardButton('������ ������'), types.KeyboardButton('������� ����'))
            akeyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
            akeyboard.add(types.KeyboardButton(f"���������� � {sysnameshort[1]}"))
            akeyboard.add(types.KeyboardButton('������ ������'), types.KeyboardButton('������� ����'))
            makeyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
            makeyboard.add(types.KeyboardButton(f"���������� � {sysnameshort[1]}"))
            makeyboard.add(types.KeyboardButton('������ ������'), types.KeyboardButton('������� ����'))
            bot.send_message(call.message.chat.id, '������� ��� 2 �������� � ������ ��� ������.')
        else:
            System_Files.remove('_KNC2')
            Reset_Files.remove('NO_RESETK2')
            SetPoint_Files.remove('NO_SPK2')
            Mode_Files.remove('NO_MODEK2')
            Table_Datas.remove('Knc2_Datas')
            Table_Alarms.remove('Knc2_Alarms')
            Table_Control.remove('Knc2_Control')
            schemes.remove("NO_SCHEME2")
            Names_Data_For_Sel.remove(Knc2Datas)
            Name_Alarm_For_Sel.remove(Knc2Alarm)
            sysname.remove('��� 2')
            sysnameshort.remove('��� 2')
            bot.send_message(call.message.chat.id, '������� ��� 2 ������� �� ������ ��� ������.')
    elif call.data == '13':
        if len(schemes) != 0:
            for t in range(0,len(schemes)):
                if schemes[t] == "NO_SCHEME2" or schemes[t] == "NO_SCHEME1":
                    bot.send_message(call.message.chat.id, f"�� ������� {sysname[t]} ������ �������� �����.")
                else:
                    bot.send_document(call.message.chat.id, open(schemes[t], 'rb'), caption=f"{sysname[t]}")
        else:
            bot.send_message(call.message.chat.id, "�������� �������, �� ������� ������ �������� �����.")
    elif call.data == '14':
        schemes.clear()
        if 'cruch' in sysnameshort:
            sysnameshort.remove('cruch')
        if len(Table_Datas) == 1 and len(Table_Alarms) == 1 and len(Table_Control) == 1:
            for m in madmins:    
                if f"{call.message.chat.id}" in m[3]:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=f"������ ����� ������ � ������� {sysname[0]}.")
                    bot.send_message(call.message.chat.id, f"������� � ����� ���������� ������� {sysname[0]} �� ������ �������� ��������������.", reply_markup=makeyboard)
                    mainadmin = True
            if not mainadmin:
                cursor_IDs.execute('SELECT * FROM Admin_Level')
                admins = cursor_IDs.fetchall()
                for a in admins:
                    if f"{call.message.chat.id}" in a[3]:
                        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=f"������ ����� ������ � ������� {sysname[0]}.")
                        bot.send_message(call.message.chat.id, f"������� � ����� ���������� ������� {sysname[0]} �� ������ ��������������.", reply_markup=akeyboard)
                        admin = True
            if not mainadmin and not admin:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=f"������ ����� ������ � ������� {sysname[0]}.")
                bot.send_message(call.message.chat.id, f"������� � ����� ���������� ������� {sysname[0]} �� ������ �����������.", reply_markup=ukeyboard)
        elif len(Table_Datas) == 0 and len(Table_Alarms) == 0 and len(Table_Control) == 0:
            bot.send_message(call.message.chat.id, "�� �� ������� �� ����� �������, �������� ���� ��� ��������� ������ � ������� '������' ��� ������� '������' ��� �������� ����.")
        elif len(Table_Datas) > 1 and len(Table_Alarms) > 1 and len(Table_Control) > 1:
            for m in madmins:    
                if f"{call.message.chat.id}" in m[3]:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="������ ����� ������ � ������� �����.")
                    bot.send_message(call.message.chat.id, "������� � ����� ���������� ������� ����� �� ������ �������� ��������������.", reply_markup=groupmakeyboard)
                    mainadmin = True
            if not mainadmin:
                cursor_IDs.execute('SELECT * FROM Admin_Level')
                admins = cursor_IDs.fetchall()
                for a in admins:
                    if f"{call.message.chat.id}" in a[3]:
                        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="������ ����� ������ � ������� �����.")
                        bot.send_message(call.message.chat.id, "������� � ����� ���������� ������� ����� �� ������ ��������������.", reply_markup=groupakeyboard)
                        admin = True
            if not mainadmin and not admin:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="������ ����� ������ � ������� �����.")
                bot.send_message(call.message.chat.id, "������� � ����� ���������� ������� ����� �� ������ �����������.", reply_markup=groupukeyboard)
    elif call.data == '15':
        System_Files.clear()
        Reset_Files.clear()
        SetPoint_Files.clear()
        Mode_Files.clear()
        Table_Datas.clear()
        Table_Alarms.clear()
        Table_Control.clear()
        sysname.clear()
        schemes.clear()
        sysnameshort.clear()
        sysnameshort.append('cruch')
        Names_Data_For_Sel.clear()
        Name_Alarm_For_Sel.clear()
        for m in madmins:    
            if f"{call.message.chat.id}" in m[3]:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="������ ��������.")
                    bot.send_message(call.message.chat.id, "�������� ��������.", reply_markup=mainmenuadminkeyboard)
                    mainadmin = True
            if not mainadmin:
                cursor_IDs.execute('SELECT * FROM Admin_Level')
                admins = cursor_IDs.fetchall()
                for a in admins:
                    if f"{call.message.chat.id}" in a[3]:
                        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="������ ��������.")
                        bot.send_message(call.message.chat.id, "�������� ��������.", reply_markup=mainmenukeyboard)
                        admin = True
            if not mainadmin and not admin:
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="������ ��������.")
                bot.send_message(call.message.chat.id, "�������� ��������.", reply_markup=groupukeyboard)
    id_con.close()
@bot.message_handler(content_types=['text'])
def main_menu(message):
    id_con = sqlite3.connect(r"C:\ProgramData\InSAT\MasterOPC Universal Modbus Server\Users_ID_Data.sqlite3")
    cursor_IDs = id_con.cursor()
    cursor_IDs.execute('SELECT * FROM MainAdmin_Level')
    madmins = cursor_IDs.fetchall()
    mainadmin = False
    cursor_IDs.execute('SELECT * FROM Admin_Level')
    admins = cursor_IDs.fetchall()
    admin = False
    cursor_IDs.execute('SELECT * FROM User_Level')
    users = cursor_IDs.fetchall()
    user = False
    for m in madmins:
        if f"{message.chat.id}" in m[3]:             
            mainadmin = True
    for a in admins:
        if f"{message.chat.id}" in a[3]:             
            admin = True
    for u in users:
        if f"{message.chat.id}" in u[3]:             
            user = True        
    if message.text == f"���������� � {sysnameshort[0]}" or message.text == '���������� � ��������':
        if user or admin or mainadmin:
            if len(Table_Datas) != 0:
                for t in range(0,len(Table_Datas)):
                    con_def = sqlite3.connect(f"C:\ProgramData\InSAT\MasterOPC Universal Modbus Server\Data_Set{System_Files[t]}.sqlite3")
                    cursor_def = con_def.cursor()
                    cursor_def.execute(f"SELECT * FROM {Table_Datas[t]}")
                    rows_def = cursor_def.fetchall()
                    rows_def_value = len(rows_def)
                    cursor_def.execute(f"SELECT * FROM {Table_Alarms[t]}")
                    rows_alms = cursor_def.fetchall()
                    rows_alms_value = len(rows_alms)
                    noalms = False
                    value = '*_*'
                    bot.send_message(message.chat.id, f"���������� �� ������ {sysname[t]}:")
                    bot.send_message(message.chat.id, "___________________________________")
                    for i in range(0,rows_def_value):
                        if rows_def[i][2] == 'false':
                            value = '���'
                        elif rows_def[i][2] == 'true':
                            value = '��'
                        else:
                            val_float = float(rows_def[i][2])
                            value = round(val_float, 2)
                        bot.send_message(message.chat.id, f"{Names_Data_For_Sel[t][i]} {value}")
                    for a in range(0,rows_alms_value):
                        if rows_alms[a][2] == 'false':
                            noalms = False
                        elif rows_alms[a][2] == 'true':
                            noalms = True
                            bot.send_message(message.chat.id, "� ������� ������������ ������, ������� '������ ������' ��� ��������� ����������.")
                            break            
                    if not noalms:
                        bot.send_message(message.chat.id, "������ � ������� ���.")
                    bot.send_message(message.chat.id, "___________________________________")
                    if len(Table_Datas) > 1:
                        time.sleep(2)
                    con_def.close()
            else:
                bot.send_message(message.chat.id, "��� ������ ���������� ������� �������(�) ��� ������.")
        else:
            bot.send_message(message.chat.id, "�� ������������ � ����, ������� ������� '/start' ��� ��������� �����������.")
    elif message.text == '������ ������':
        if user or admin or mainadmin:
            if len(Table_Alarms) != 0:
                for t in range(0,len(Table_Alarms)):
                    con_def = sqlite3.connect(f"C:\ProgramData\InSAT\MasterOPC Universal Modbus Server\Data_Set{System_Files[t]}.sqlite3")
                    cursor_def = con_def.cursor()
                    cursor_def.execute(f"SELECT * FROM {Table_Alarms[t]}")
                    rows_alms = cursor_def.fetchall()
                    rows_alms_value = len(rows_alms)
                    noalms = False   
                    bot.send_message(message.chat.id, f"�������� ������ ������ {sysname[t]}:")
                    bot.send_message(message.chat.id, "___________________________________")
                    for a in range(0,rows_alms_value):
                        if rows_alms[a][2] == 'true':
                            noalms = True
                            bot.send_message(message.chat.id, f"{Name_Alarm_For_Sel[t][a]} ��")          
                    if not noalms:
                        bot.send_message(message.chat.id, "������ � ������� ���.")
                    bot.send_message(message.chat.id, "___________________________________")    
                    con_def.close()
            else:
                bot.send_message(message.chat.id, "��� ������ ���������� ������� �������(�) ��� ������.")       
        else:
            bot.send_message(message.chat.id, "�� ������������ � ����, ������� ������� '/start' ��� ��������� �����������.")
    elif message.text == f"���������� {sysnameshort[0]}":
        if admin or mainadmin:
            if len(Table_Alarms) != 0:
                if len(Table_Control) == 1:
                    if Table_Control[0] == 'Itp_Control' or Table_Control[0] == 'Knc2_Control' or Table_Control[0] == 'Knc1_Control':
                        bot.send_message(message.chat.id, f"������� {sysname[0]} �� ����� ������� ������� � ���������.")
                    else:
                        con_w = sqlite3.connect(f"C:\ProgramData\InSAT\MasterOPC Universal Modbus Server\Data_Set{System_Files[0]}.sqlite3")
                        cursor_w = con_w.cursor()
                        cursor_w.execute(f"SELECT * FROM {Table_Control[0]} WHERE id = 1")
                        rows_w = cursor_w.fetchall()
                        if rows_w[0][2] == 'false':
                            syskbrdstart = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
                            syskbrdstart.add(types.KeyboardButton('������'), types.KeyboardButton('��������� �������'))
                            bot.send_message(message.chat.id, f"������� {sysname[0]} �����������, ������� '��������� �������', ����� �� ��������� ��� '������', ����� �������� ��������.", reply_markup=syskbrdstart)
                        elif rows_w[0][2] == 'true':
                            syskbrdstop = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
                            syskbrdstop.add(types.KeyboardButton('������'), types.KeyboardButton('���������� �������'))
                            bot.send_message(message.chat.id, f"������� {sysname[0]} ��������, ������� '����������', ����� �� ���������� ��� '������', ����� �������� ��������.", reply_markup=syskbrdstop)
                        con_w.close()
                        bot.set_state(message.from_user.id, BotStates.SysCmd, message.chat.id)
                else:
                    bot.send_message(message.chat.id, "������ ������� ����������� ��� ���������� ��������� ��������.")
            else:
                bot.send_message(message.chat.id, "��� ������ ���������� ������� 1 ������� ��� ������.")    
        else:
            bot.send_message(message.chat.id, '� ��� ������������ ���� ��� ������������� ������ ��������, ���������� � �������� �������������� �� ��������.')
    elif message.text == '���������� ���������':
        systemtocontrol = False
        groupsyscontrolkbrd = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        groupsyscontrolkbrd.add(types.KeyboardButton('��������� �������'), types.KeyboardButton('���������� �������'))
        groupsyscontrolkbrd.add(types.KeyboardButton('������'))
        if admin or mainadmin:
            if len(Table_Alarms) != 0:
                if len(Table_Control) > 1:
                    for t in range(0,len(Table_Control)):
                        if Table_Control[t] == 'Itp_Control' or Table_Control[t] == 'Knc2_Control' or Table_Control[t] == 'Knc1_Control':
                            bot.send_message(message.chat.id, f"������� {sysname[t]} �� ����� ������� ������� � ���������.")
                        else:
                            con_w = sqlite3.connect(f"C:\ProgramData\InSAT\MasterOPC Universal Modbus Server\Data_Set{System_Files[t]}.sqlite3")
                            cursor_w = con_w.cursor()
                            cursor_w.execute(f"SELECT * FROM {Table_Control[t]} WHERE id = 1")
                            rows_w = cursor_w.fetchall()
                            if rows_w[0][2] == 'false':
                                bot.send_message(message.chat.id, f"������� {sysname[t]} �����������, ������� '��������� �������', ����� �� ��������� ��� '������', ����� �������� ��������.")
                            elif rows_w[0][2] == 'true':
                                bot.send_message(message.chat.id, f"������� {sysname[t]} ��������, ������� '����������', ����� �� ���������� ��� '������', ����� �������� ��������.")
                            con_w.close()
                            systemtocontrol = True
                    if systemtocontrol:
                        systemtocontrol = False
                        bot.send_message(message.chat.id, "������� � ���� ���������� ������� ������.", reply_markup=groupsyscontrolkbrd)
                        bot.set_state(message.from_user.id, BotStates.GroupSysControl, message.chat.id)
                    else:
                        bot.send_message(message.chat.id, "����� ��������� ������ ���� ���, �������� ����� ���������.")
                else:
                    bot.send_message(message.chat.id, "������ ������� ����������� ��� 1 ��������� �������.")
            else:
                bot.send_message(message.chat.id, "���������� ������� ������ ������ ��� ������.")    
        else:
            bot.send_message(message.chat.id, '� ��� ������������ ���� ��� ������������� ������ ��������, ���������� � �������� �������������� �� ��������.')
    elif message.text == '����� ������':
        if user or admin or mainadmin:
            just1reset = False
            if len(Table_Control) != 0:
                for t in range(0,len(Table_Control)):
                    if Table_Control[t] == 'Knc2_Control' or Table_Control[t] == 'Knc1_Control':
                        bot.send_message(message.chat.id, f"������� {sysname[t]} �� ����� ������� ������ ������.")
                    else:
                        con_w = sqlite3.connect(f"C:\ProgramData\InSAT\MasterOPC Universal Modbus Server\Data_Set{Reset_Files[t]}.sqlite3")
                        cursor_w = con_w.cursor()
                        cursor_w.execute(f"UPDATE {Table_Control[t]} SET Value = 'true' WHERE id = 2;")
                        cursor_w.execute(f"UPDATE {Table_Control[t]} SET Value = 'true' WHERE id = 1;")
                        con_w.commit()
                        bot.send_message(message.chat.id, '���� ����� ������, ���������.')
                        just1reset = True
                        con_w.close()
                if just1reset:   
                    if 'Itp_Control' in Table_Control:
                        time.sleep(60)
                    else:
                        time.sleep(7)
                    for t in range(0,len(Table_Control)): 
                        if Table_Control[t] != 'Knc2_Control' and Table_Control[t] != 'Knc1_Control': 
                            con_w = sqlite3.connect(f"C:\ProgramData\InSAT\MasterOPC Universal Modbus Server\Data_Set{Reset_Files[t]}.sqlite3")
                            cursor_w = con_w.cursor()
                            cursor_w.execute(f"UPDATE {Table_Control[t]} SET Value = 'false' WHERE id = 1;")
                            con_w.commit()
                            con_w.close()
                    for t in range(0,len(Table_Control)): 
                        if Table_Control[t] != 'Knc2_Control' and Table_Control[t] != 'Knc1_Control':
                            con_w = sqlite3.connect(f"C:\ProgramData\InSAT\MasterOPC Universal Modbus Server\Data_Set{Reset_Files[t]}.sqlite3")
                            cursor_w = con_w.cursor()
                            Sucsessful_change = False
                            timeout = 0
                            while not Sucsessful_change:
                                time.sleep(1)
                                cursor_w.execute(f"SELECT * FROM {Table_Control[t]} WHERE id =2")
                                cycle_check = cursor_w.fetchall()
                                if cycle_check[0][2] == 'false':
                                    Sucsessful_change = True
                                timeout +=1
                                if 'Itp_Control' in Table_Control:                                 
                                    if timeout == 60:
                                        break
                                else:
                                    if timeout == 10:
                                        break        
                            if Sucsessful_change:
                                con_w.close()
                                bot.send_message(message.chat.id, '����� ������ ��������.')
                            else:
                                cursor_w.execute(f"UPDATE {Table_Control[t]} SET Value = 'false' WHERE id = 2;")
                                con_w.commit()
                                con_w.close()
                                bot.send_message(message.chat.id, '�� ������� �������� ������.')
                        just1reset = False
                else:
                    bot.send_message(message.chat.id, '����� ��������� ������ ��� ���, �� ������� ����� �������� ������.')
            else:
                bot.send_message(message.chat.id, "��� ������ ���������� ������� �������(�) ��� ������.")            
        else:
            bot.send_message(message.chat.id, "�� ������������ � ����, ������� ������� '/start' ��� ��������� �����������.")
    elif message.text == '�������� �������':
        if admin or mainadmin:
            just1editsp = False
            if len(Table_Control) != 0:
                for t in range(0,len(Table_Control)):
                    if Table_Control[t] == 'Itp_Control' or Table_Control[t] == 'Knc2_Control' or Table_Control[t] == 'Knc1_Control':
                        bot.send_message(message.chat.id, f"������� {sysname[t]} �� ����� ������� ��������� ������� ����������� �������.")
                    else:
                        canselkbrd = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
                        canselkbrd.add(types.KeyboardButton('������'))
                        con_w = sqlite3.connect(f"C:\ProgramData\InSAT\MasterOPC Universal Modbus Server\Data_Set{SetPoint_Files[t]}.sqlite3")
                        cursor_w = con_w.cursor()
                        cursor_w.execute(f"SELECT * FROM {Table_Control[t]} WHERE id = 1")
                        rows_w = cursor_w.fetchall()    
                        bot.send_message(message.chat.id, f"������� ����� �������� ������� ����������� ������� ��� ������� {sysname[t]}, ������� ��������: {rows_w[0][2]}.", reply_markup=canselkbrd)
                        con_w.close()
                        just1editsp = True
                if len(Table_Control) > 1 and just1editsp:        
                    bot.send_message(message.chat.id, "��������! ��������� ������� ����������� ������� ��� ���������� ��������� �������� �������� � ��������� �� ���� ��������� ��������.")     
                if just1editsp:
                    just1editsp = False
                    bot.set_state(message.from_user.id, BotStates.SetSP, message.chat.id)
                else:
                    bot.send_message(message.chat.id, '����� ��������� ������ ��� ���, �� ������� ����� �������� ������� ����������� �������.')
            else:
                bot.send_message(message.chat.id, "��� ������ ���������� ������� �������(�) ��� ������.")    
        else:
            bot.send_message(message.chat.id, '� ��� ������������ ���� ��� ������������� ������ ��������, ���������� � �������� �������������� �� ��������.')
    elif message.text == '����� ������ ������':
        if admin or mainadmin:
            just1editmode = False
            if len(Table_Control) != 0:
                for t in range(0,len(Table_Control)):
                    if Table_Control[t] == 'Itp_Control' or Table_Control[t] == 'Knc2_Control' or Table_Control[t] == 'Knc1_Control' or Table_Control[t] == 'Pv4_Control' or Table_Control[t] == 'Abk1_E_Control' or Table_Control[t] == 'Abk2_E_Control' or Table_Control[t] == 'Abk3_E_Control' or Table_Control[t] == 'Abk4_E_Control':
                        bot.send_message(message.chat.id, f"������� {sysname[t]} �� ����� ������� ������ ������ ������.")
                    else:
                        modeskbrd = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
                        modeskbrd.add(types.KeyboardButton('����'), types.KeyboardButton('����'))
                        modeskbrd.add(types.KeyboardButton('������'), types.KeyboardButton('����'))
                        con_w = sqlite3.connect(f"C:\ProgramData\InSAT\MasterOPC Universal Modbus Server\Data_Set{Mode_Files[t]}.sqlite3")
                        cursor_w = con_w.cursor()
                        cursor_w.execute(f"SELECT * FROM {Table_Control[t]} WHERE id = 1")
                        rows_w = cursor_w.fetchall()  
                        seasmode = '*_*'
                        if rows_w[0][2] == '0':
                            seasmode = "'����'"
                        elif rows_w[0][2] == '1':
                            seasmode = "'����'"
                        elif rows_w[0][2] == '2':
                            seasmode = "'����'"
                        bot.send_message(message.chat.id, f"�������� ����� ����������� ������ ��� ������� {sysname[t]}, ������� �����: {seasmode}.", reply_markup=modeskbrd)
                        just1editmode = True
                        con_w.close()
                if len(Table_Control) > 1 and just1editmode:        
                    bot.send_message(message.chat.id, "��������! ��������� ������ ����������� ������ ��� ���������� ��������� �������� �������� ��� ��������� �� ���� ��������� ��������.") 
                if just1editmode:  
                    just1editmode = False
                    bot.set_state(message.from_user.id, BotStates.EditSeason, message.chat.id)
                else:
                    bot.send_message(message.chat.id, '����� ��������� ������ ��� ���, �� ������� ����� �������� ����� ������ ������.')    
            else:
                bot.send_message(message.chat.id, "��� ������ ���������� ������� �������(�) ��� ������.")    
        else:
            bot.send_message(message.chat.id, '� ��� ������������ ���� ��� ������������� ������ ��������, ���������� � �������� �������������� �� ��������.')
    elif message.text == '������� ������� ��� ������':
        if user or admin or mainadmin:
            bot.send_message(message.chat.id, '�������� ������� � ������� ����� ����������� ������.', reply_markup=systemsel)
        else:
            bot.send_message(message.chat.id, "�� ������������ � ����, ������� ������� '/start' ��� ��������� �����������.")
    elif message.text == '������� ����':
        System_Files.clear()
        Reset_Files.clear()
        SetPoint_Files.clear()
        Mode_Files.clear()
        Table_Datas.clear()
        Table_Alarms.clear()
        Table_Control.clear()
        sysname.clear()
        sysnameshort.clear()
        sysnameshort.append('cruch')
        Names_Data_For_Sel.clear()
        Name_Alarm_For_Sel.clear()
        if mainadmin:                       
            bot.send_message(message.chat.id, '������� � ������� ����.', reply_markup=mainmenuadminkeyboard)
        elif not mainadmin and (user or admin):
            bot.send_message(message.chat.id, '������� � ������� ����.', reply_markup=mainmenukeyboard)
        elif not user:
            bot.send_message(message.chat.id, "�� ������������ � ����, ������� ������� '/start' ��� ��������� �����������.")
    elif message.text == '�������� ������� �������':
        if mainadmin:
            bot.send_message(message.chat.id, "� ��� ��� ������������ ������� �������.")
        elif not mainadmin and (user or admin):
            cansellevelkbrd = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
            cansellevelkbrd.add(types.KeyboardButton('������'))
            bot.send_message(message.chat.id, "������� ������ ��� ������� ������ '������'.", reply_markup=cansellevelkbrd)
            bot.set_state(message.from_user.id, BotStates.EditLevel, message.chat.id)
        elif not user:
            bot.send_message(message.chat.id, "�� ������������ � ����, ������� ������� '/start' ��� ��������� �����������.")
    elif message.text == '���������� �������������� � ��������':
        if mainadmin:
            bot.send_message(message.chat.id, '������� � ����� ����������������� �������������.', reply_markup=useradministrationkbrd)
            bot.set_state(message.from_user.id, BotStates.AdmUsers, message.chat.id)
        else:
            bot.send_message(message.chat.id, '� ��� ������������ ���� ��� ������������� ������ ��������, ���������� � �������� �������������� �� ��������.')
    id_con.close()          
bot.add_custom_filter(custom_filters.StateFilter(bot))
bot.add_custom_filter(custom_filters.IsDigitFilter())
bot.polling(none_stop=True)