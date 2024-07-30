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
systems = ['КНС 1', 'ИТП', 'ПВ 4', 'АБК 1 Электронагрева', 'АБК 2 Электронагрева', 'АБК 3 Электронагрева', 'АБК 4 Электронагрева', 'АБК 1 Водяного нагрева', 'АБК 2 Водяного нагрева', 'АБК 3 Водяного нагрева', 'АБК 4 Водяного нагрева', 'КНС 2']
Itp_Alarm_Tag_Name = ['Критическая авария', 'Авария насоса 1 осн.', 'Авария насоса 1 рез.', 'Авария насоса 2 осн.', 'Авария насоса 2 рез.', 'Авария по системе', 'Пожарная авария',
                      'Авария ТК насоса 1 осн.', 'Авария ТК насоса 1 рез.', 'Авария ТК насоса 2 осн.', 'Авария насоса 2 рез.', 'Ааврия по давл. насоса 1 осн', 'Ааврия по давл. насоса 1 рез.', 'Авария по давл. насоса 2 осн.',
                     'Авария по давл. насоса 2 рез.', 'Авария QF насоса 1 осн.', 'Авария QF насоса 1 рез.', 'Авария QF насоса 2 осн.', 'Авария QF насоса 2 рез.', 'Крит. авария 1 контура', 'Крит. авария 2 контура', 'Авария в системе']
Pv4_Alarm_Tag_Name = ['Критическая авария', 'Авария протечки', 'Пожарная авария', 'Авария ТК вент. притока', 'Авария ТК вент. вытяжки', 'Фильтр загрязнен', 'Авария датчика температуры притока', 'Авария по системе']
Abk_E_Alarm_Tag_Name = ['Пожарная авария', 'Авария ТК вент. притока', 'Авария нагревателя', 'Фильтр загрязнен', 'Авария датчика температуры притока', 'Авария системы', 'Критическая авария']
Abk_W_Alarm_Tag_Name = ['Пожарная авария', 'Фильтр загрязнен', 'Авария датчика температуры притока', 'Авария системы', 'Критическая авария', 'Авария наружнего датчика температуры', 'Авария датчика температуры воды', 'Авария ТК приточного вентилятора']
Knc_Alarm_Tag_Name = ['Авария насоса 1', 'Авария насоса 2']
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
                            bot.send_message(newletters_ids[j][3], f"{Names[s][i]} в системе {systems[s]}.")
                        numbers[s][i] = True
                else:
                    numbers[s][i] = False
        con.close() 
        ids_for_newsletters.close()
        time.sleep(1)
