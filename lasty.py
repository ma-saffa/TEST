!/usr/bin/env python
from netmiko import ConnectHandler
nx_os = {
'device_type': 'cisco_ios',
'ip': 'sbx-nxos-mgmt.cisco.com',
'username': 'admin',
'password': 'Admin_1234!',
'port': 8181
}
net_connect = ConnectHandler(**nx_os)
config_commands = ['no int lo100']
output = net_connect.send_config_set(config_commands)
print (output)

