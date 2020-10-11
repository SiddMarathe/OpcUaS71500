from opcua import Client

def get_index(node_array,element):
    for o in node_array:
        if str(element) in str(o):
            return node_array.index(o)


OpcPort = "opc.tcp://192.168.0.1:4840"
client = Client(OpcPort)
client.connect()
Object = client.get_objects_node()
# print(type(client.get_objects_node()))
PlcIndex = get_index(Object.get_children(),"PLC")
Plc = Object.get_children()[PlcIndex]
DBIndex = get_index(Plc.get_children(),"DataBlocksGlobal")
GlobalDB = Plc.get_children()[DBIndex]
OpcDBIndex = get_index(GlobalDB.get_children(),"OpcuaDb")
OpcDB = GlobalDB.get_children()[OpcDBIndex]
VarValueList=[]
for Var in OpcDB.get_children():
    StrVar = str(Var)
    SplitIndex = StrVar.index('.')
    VarValueList.append(Var.get_value())
    VarName = StrVar[SplitIndex+1 : ]
    print("Values in {} is {}".format(VarName,Var.get_value()))
client.disconnect()
print(VarValueList)

