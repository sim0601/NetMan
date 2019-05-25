'''from netmiko import Netmiko

dev1 = {'device_type': 'cisco_ios',
        'ip': '198.51.100.1',
        'username': 'simran',
        'password': 'LAB',}

net_connect = Netmiko(**dev1)
print(net_connect.find_prompt())'''


from netmiko import ConnectHandler

dev1 = {'device_type': 'cisco_ios',
        'ip': '198.51.100.1',
        'username': 'simran',
        'password': 'LAB',}

# establishes an SSH connection by passing in the device parameters
net_connect = ConnectHandler(**dev1)

output = net_connect.send_command('show ip int brief')
print(output)


