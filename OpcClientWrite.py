from opcua import Client
from opcua import ua
import time
OpcUaPlcT1="opc.tcp://192.168.0.1:4840"
client = Client(OpcUaPlcT1)
print('Connect to: {}'.format(OpcUaPlcT1))
client.connect()
while True:
    BoolVal=bool(input())
    var1 = client.get_node('ns=3; s="opcua_DB"."bool"')
    var1.get_data_value() # get value of node as a DataValue object
    temp1=var1.get_value() # get value of node as a python builtin
    print(temp1)
    var1.set_attribute(ua.AttributeIds.Value, ua.DataValue(BoolVal))
    temp1=var1.get_value() # get value of node as a python builtin
    print(temp1)
    time.sleep(1)
# var.set_attribute(ua.AttributeIds.Value, ua.DataValue(True))
client.disconnect()
