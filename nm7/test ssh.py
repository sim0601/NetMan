from netmiko import ConnectHandler

dev1 = {
    'device_type': 'cisco_ios',
    'ip':   '198.51.101.1',
    'username': 'simran',
    'password': 'lab1',
}

dev2 = {
    'device_type': 'cisco_ios',
    'ip':   '198.51.101.2',
    'username': 'simran',
    'password': 'lab2',
}

dev3 = {
    'device_type': 'cisco_ios',
    'ip':   '198.51.101.3',
    'username': 'simran',
    'password': 'lab4',
}

dev4 = {
    'device_type': 'cisco_ios',
    'ip':   '172.16.1.1',
    'username': 'simran',
    'password': 'lab3',
}

net_connect1 = ConnectHandler(**dev1)
net_connect1.find_prompt()
out1 = net_connect1.send_command('show ip int brief')
print(out1)


net_connect2 = ConnectHandler(**dev2)
net_connect2.find_prompt()
out2 = net_connect2.send_command('show ip int brief')
print(out2)


net_connect3 = ConnectHandler(**dev3)
net_connect3.find_prompt()
out3 = net_connect3.send_command('show ip int brief')
print(out3)

net_connect4 = ConnectHandler(**dev4)
net_connect4.find_prompt()
out4 = net_connect4.send_command('show ip int brief')
print(out4)




