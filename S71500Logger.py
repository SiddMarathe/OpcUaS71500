from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.payload import BinaryPayloadBuilder
import datetime as dt
import time
from pymodbus.client.sync import ModbusTcpClient as delta
import tkinter
import excel
import text
from opcua import Client
from opcua import ua

# import logging
# logging.basicConfig()
# log = logging.getLogger()
# log.setLevel(logging.INFO)

def Today():
    strDt = str(dt.datetime.now())
    T = dt.datetime.strptime(strDt,"%Y-%m-%d %H:%M:%S.%f")
    return T 
inthour=int(Today().hour)
#print(Today().time())
#print(type(inthour))
#welcome to file generator
wish=str()
if inthour<12 :
	wish='Good Morning\n'
elif 18>inthour>=12:
	wish='Good Afternoon\n'
elif inthour>=18:
	wish='Good Evening\n'
input(wish+'Welcome to file generator\nPress enter to start ')
filename=input("Enter file name: ")
filepath=input("Enter file path: ")
#'/storage/emulated/0/'


txt_jalvis=text.text_edit(filepath,filename)	    
ex_jalvis = excel.excel_edit(filepath,filename)
#MODE
options="1:TXT Log\n2:CSV Log\n3:Change file name\n4:Change File path\n5:Exit\
    \nEnter the mode:\n"
a=input(options)
option_dict={'0':"Invalid Input", '1': "TXT Log", '2':'CSV Log', \
                '3':'Change file name', '4':'Change file path', '5':'Exit & Start Logging.'}
while a!='5':                 
    while a in option_dict:
        if a=='1':
            start_txt_log = True
            start_csv_log = False
            a=input(options)
                    
        if a=='2':
            start_csv_log = True
            start_txt_log = False
            a=input(options)
            
        if a=='3':
            filename=input("Enter file name: ")
            a=input(options)

        if a=='4':     
            filepath=input("Enter file path: ")
            a=input(options)
        
        if a=='5':
            break

    while a not in option_dict:
        print(option_dict['0'])
        a=input(options)
        if a=='6':
            break

if a=='6':
    print ("Thank you")
nodes = ['ns=3; s="opcua_DB"."real"','ns=3; s="opcua_DB"."real_1"','ns=3; s="opcua_DB"."real_2"','ns=3; s="opcua_DB"."real_3"']
ex_headers = ['Date','Time','OpcDbReal','OpcDbReal_1','OpcDbReal_2','OpcDbReal_3','OpcDbReal_4']
ex_jalvis.write_excel_header(ex_headers) 
#display
def csv_file():
    try:
        from opcua import Client
        OpcPort = "opc.tcp://192.168.0.1:4840"
        client = Client(OpcPort)
        client.connect()
        Object = client.get_objects_node()
        Plc = Object.get_children()[2]
        GlobalDB = Plc.get_children()[1]
        OpcDB = GlobalDB.get_children()[3]
        while True:
            LogButton = client.get_node('ns=3; s="opcua_DB"."CsvLogButton"')
            trigger = LogButton.get_value()
            if trigger : 
                Res1=client.get_node('ns=3; s="opcua_DB"."real"')
                Res1Val=Res1.get_value()
                Res2=client.get_node('ns=3; s="opcua_DB"."real_1"')
                Res2Val=Res2.get_value()
                Res3=client.get_node('ns=3; s="opcua_DB"."real_2"')
                Res3Val=Res3.get_value()
                Res4=client.get_node('ns=3; s="opcua_DB"."real_3"')
                Res4Val=Res4.get_value()
                ClientNewVar= client.get_node('ns=3; s="NewDb"."NewVar"')  
                print(ClientNewVar)                                              
                ex_data=[Today().date(),Today().time(),Res1Val,Res2Val,Res3Val,Res4Val]
                ex_headers=['Date','Time','OpcDbReal','OpcDbReal_1','OpcDbReal_2','OpcDbReal_3','OpcDbReal_4']
                ex_jalvis.append_excel(ex_data,ex_headers)
                print(trigger)
                time.sleep(0.8)
                var.set_attribute(ua.AttributeIds.Value, ua.DataValue(False))
                print(trigger)
                trigger = False
            time.sleep(0.1)
        client.disconnect()
    except:
        ex_data=[Today().date(),str(Today().hour)+':'+str(Today().minute),"com fail"]
        ex_headers=['Date','Time','OpcDbReal']
        ex_jalvis.append_excel(ex_data,ex_headers)
        time.sleep(1)
        csv_file()
try:       
    if start_csv_log : csv_file()			
except:
    pass