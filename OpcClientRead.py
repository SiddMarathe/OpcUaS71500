from opcua import Client
from opcua import ua
import time
OpcUaPlcT1="opc.tcp://192.168.0.1:4840"
client = Client(OpcUaPlcT1)
print('Connect to: {}'.format(OpcUaPlcT1))
client.connect()
if True:
    BoolTemp = client.get_node('ns=3; s="opcua_DB"."bool"')
    BoolTempVal = BoolTemp.get_value()
    print(BoolTempVal)
    if BoolTempVal :
        var1 = client.get_node('ns=3; s="opcua_DB"."real_1"')
        # var1.get_data_value() # get value of node as a DataValue object
        temp1=var1.get_value() # get value of node as a python builtin
        print(temp1)
        var2 = client.get_node('ns=3; s="opcua_DB"."real_2"')
        # var2.get_data_value() # get value of node as a DataValue object
        temp2=var2.get_value() # get value of node as a python builtin
        print(temp2)
        var3 = client.get_node('ns=3; s="opcua_DB"."real_3"')
        # var3.get_data_value() # get value of node as a DataValue object
        temp3=var3.get_value() # get value of node as a python builtin
        print(temp3)
        l1=[temp1,temp2,temp3]
        print(l1)
    time.sleep(1)
client.disconnect()
