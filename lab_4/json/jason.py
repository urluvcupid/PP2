import json

file = open('sample-data.json')
json_data = json.loads(file.read())
print('Interface status')
print('================================================================================')
print('DN                                                 Description           Speed    MTU  ')
print('-------------------------------------------------- --------------------  ------  ------')
for i in json_data["imdata"]:
    if i["l1PhysIf"]["attributes"]['dn'] == 'topology/pod-1/node-201/sys/phys-[eth1/1]':
        break
    print(i["l1PhysIf"]["attributes"]['dn'], '                              ', i["l1PhysIf"]["attributes"]['descr'], i["l1PhysIf"]["attributes"]["speed"], '   ', i["l1PhysIf"]["attributes"]["mtu"], sep = '')
file.close()
