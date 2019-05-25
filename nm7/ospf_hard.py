#!/usr/bin/env python3

#author : Simran Kohli simran.kohli@colorado.edu
#name : ospfconfig.py
#purpose : A script to configure the routers
#date : 2018.03.16
#version : 1.1

import os
import sys
import netmiko
from netmiko import ConnectHandler
from prettytable import PrettyTable


def ospf_conf1():

        exceptions = (netmiko.ssh_exception.NetMikoTimeoutException, netmiko.ssh_exception.NetMikoAuthenticationException)
        try:                                    # try/except block for netmiko
            #R1
            dev1 = {
                'device_type': 'cisco_ios',
                'ip':   '198.51.101.1',
                'username': 'simran',
                'password': 'lab1',
            }

            # establishes an SSH connection by passing in the device parameters

            net_connect1 = ConnectHandler(**dev1)

            # for R1
            config_commands1 = ['router ospf 1',
                    'network '+ ' 198.51.100.0 0.0.0.255 ' + ' area 1 ',
                    'network '+ ' 198.51.101.0 0.0.0.255 ' + ' area 1 ',
                    'network '+ ' 10.0.0.1 0.0.0.0 ' + ' area 1 ',
                    ]
            output1 = net_connect1.send_config_set(config_commands1)
            print(output1)

            # for graceful exit from SSH session
            net_connect1.disconnect()

        except exceptions as b:
            print("Error occurred ", b)
            sys.exit()

def ospf_conf2():

        exceptions = (netmiko.ssh_exception.NetMikoTimeoutException, netmiko.ssh_exception.NetMikoAuthenticationException)
        try:                                    # try/except block for netmiko

            #R2
            dev2 = {
                'device_type': 'cisco_ios',
                'ip':   '198.51.101.2',
                'username': 'simran',
                'password': 'lab2',
            }

            # establishes an SSH connection by passing in the device parameters

            net_connect2 = ConnectHandler(**dev2)

            #for R2
            config_commands2 = ['router ospf 1',
                    'network '+ ' 198.51.101.0 0.0.0.255 ' + ' area 1 ',
                    'network '+ ' 172.16.1.0 0.0.0.255 ' + ' area 0 ',
                    'network '+ ' 20.0.0.1 0.0.0.0 ' + ' area 0 ',
                    ]
            output2 = net_connect2.send_config_set(config_commands2)
            print(output2)

            config_commands3 = ['int f0/0 ',
                    'ip ospf cost ' + ' 10 ',
                    ]
            output3 = net_connect2.send_config_set(config_commands3)
            print(output3)

            # for graceful exit from SSH session
            net_connect2.disconnect()

        except exceptions as b:
            print("Error occurred ", b)
            sys.exit()


def ospf_conf3():
        exceptions = (netmiko.ssh_exception.NetMikoTimeoutException, netmiko.ssh_exception.NetMikoAuthenticationException)
        try:                                    # try/except block for netmiko

            #R3
            dev4 = {
                'device_type': 'cisco_ios',
                'ip':   '172.16.1.1',
                'username': 'simran',
                'password': 'lab3',
            }

            # establishes an SSH connection by passing in the device parameters

            net_connect4 = ConnectHandler(**dev4)

            # for R3
            config_commands6 = ['router ospf 1',
                    'network '+ ' 172.16.1.0 0.0.0.255 ' + ' area 0 ',
                    'network '+ ' 30.0.0.1 0.0.0.0 ' + ' area 0 ',
                    ]
            output6 = net_connect4.send_config_set(config_commands6)
            print(output6)

            # for graceful exit from SSH session
            net_connect4.disconnect()

        except exceptions as b:
            print("Error occurred ", b)
            sys.exit()



def ospf_conf4():
        exceptions = (netmiko.ssh_exception.NetMikoTimeoutException, netmiko.ssh_exception.NetMikoAuthenticationException)
        try:                                    # try/except block for netmiko
            #R4
            dev3 = {
                'device_type': 'cisco_ios',
                'ip':   '198.51.101.3',
                'username': 'simran',
                'password': 'lab4',
            }

            # establishes an SSH connection by passing in the device parameters

            net_connect3 = ConnectHandler(**dev3)

            #for R4
            config_commands4 = ['router ospf 1',
                    'network '+ ' 198.51.101.0 0.0.0.255 ' + ' area 1 ',
                    'network '+ ' 172.16.1.0 0.0.0.255 ' + ' area 0 ',
                    'network '+ ' 40.0.0.1 0.0.0.0 ' + ' area 0 ',
                    ]
            output4 = net_connect3.send_config_set(config_commands4)
            print(output4)

            config_commands5 = ['int f0/0 ',
                    'ip ospf cost ' + ' 10 ',
                    ]
            output5 = net_connect3.send_config_set(config_commands5)
            print(output5)

            # for graceful exit from SSH session
            net_connect3.disconnect()

        except exceptions as b:
            print("Error occurred ", b)
            sys.exit()

def check_ospf():

    exceptions = (netmiko.ssh_exception.NetMikoTimeoutException, netmiko.ssh_exception.NetMikoAuthenticationException)

    try:                                    # try/except block for netmiko

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

        # establishes an SSH connection by passing in the device parameters

        net_connect1 = ConnectHandler(**dev1)
        net_connect2 = ConnectHandler(**dev2)
        net_connect3 = ConnectHandler(**dev3)
        net_connect4 = ConnectHandler(**dev4)

        # for R1
        output1 = net_connect1.send_command('show ip ospf neighbor')
        print("OSPF neighbors for R1")
        print(output1)

        #for R2
        output2 = net_connect2.send_command('show ip ospf neighbor')
        print("OSPF neighbors for R2")
        print(output2)

        #for R4
        output3 = net_connect3.send_command('show ip ospf neighbor')
        print("OSPF neighbors for R4")
        print(output3)

        # for R3
        output4 = net_connect4.send_command('show ip ospf neighbor')
        print("OSPF neighbors for R3")
        print(output4)

        with open('ospfdata.txt', 'a+') as f:
            f.write("Neighborship for R1 \n")
            f.write(output1+ "\n")
            f.write("Neighborship for R2 \n")
            f.write(output2+ "\n")
            f.write("Neighborship for R3 \n")
            f.write(output3+ "\n")
            f.write("Neighborship for R4 \n")
            f.write(output4+ "\n")

        file = 'ospfdata.txt'

        with open(file, 'r') as f:
            for line in f:

                #print(line)

                if 'Neighbor ID' in line:
                    title = line.split(' ')
                    print(title[0], title[1], title[9].rjust(11), title[33].strip('\n').rjust(14))

                if '10.0.0.1' in line:
                    data1 = line.split(' ')
                    print(data1[0], data1[13].rjust(16),data1[25].rjust(18))


                if '20.0.0.1' in line:
                    data2 = line.split(' ')
                    print(data2[0], data2[13].rjust(17), data2[27].rjust(18))

                if '30.0.0.1' in line:
                    data3 = line.split(' ')
                    print(data3[0], data3[13].rjust(17), data3[31].rjust(18))


                if '40.0.0.1' in line:
                    data4 = line.split(' ')
                    print(data4[0], data4[13].rjust(16), data4[30].rjust(18))

        # for graceful exit from SSH session
        net_connect1.disconnect()
        net_connect2.disconnect()
        net_connect3.disconnect()
        net_connect4.disconnect()

    except exceptions as b:
        print("Error occurred ", b)
        sys.exit()



def ping_test():

    exceptions = (netmiko.ssh_exception.NetMikoTimeoutException, netmiko.ssh_exception.NetMikoAuthenticationException)

    try:                                        # try/except block for netmiko
        dev1 = {
            'device_type': 'cisco_ios',
            'ip':   '10.0.0.1',
            'username': 'simran',
            'password': 'lab1',
        }

        dev2 = {
            'device_type': 'cisco_ios',
            'ip':   '30.0.0.1',
            'username': 'simran',
            'password': 'lab3',
        }
        # establishes an SSH connection by passing in the device parameters
        net_connect1 = ConnectHandler(**dev1)
        net_connect2 = ConnectHandler(**dev2)

        net_connect1.find_prompt()
        net_connect2.find_prompt()

        p1 = net_connect1.send_command('ping 30.0.0.1' )
        print(p1)

        p2 = net_connect2.send_command('ping 10.0.0.1' )
        print(p2)

        if p1 != '' and p2 != '':
            print("OSPF has been successfully configured")

        else:
            print("OSPF failed")


        # for graceful exit from SSH session
        net_connect1.disconnect()
        net_connect2.disconnect()

    except exceptions as a:
        print("Error occurred: ", a)
        sys.exit()


check_ospf()
ping_test()
