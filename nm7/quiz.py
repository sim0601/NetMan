import sys
import netmiko
from netmiko import ConnectHandler


dev1 = {
            'device_type': 'cisco_ios',
            'ip':   '10.0.0.1',
            'username': 'simran',
            'password': 'lab',
}

net_connect1 = ConnectHandler(**dev1)

p = net_connect1.send_command('show ip dhcp binding')
with open('data.txt', 'w') as f1:
    f1.write(p)

with open('data.txt', 'r') as f2:
    for line in f2:
        #print(line)

        if '10.0.0.2' in line:
            ip = line.split(' ')
            print(ip[0])



dev2 = {
            'device_type': 'cisco_ios',
            'ip':   ip[0],
            'username': 'simran',
            'password': 'lab',
}


net_connect2 = ConnectHandler(**dev2)

p1 = net_connect2.send_command('show ip interface brief')
print(p1)
