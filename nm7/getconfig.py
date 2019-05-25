#!/usr/bin/env python3

#author : Simran Kohli simran.kohli@colorado.edu
#name : getconfig.py
#purpose : A script to get the running configs
#date : 2018.03.16
#version : 1.1

import sys
import netmiko
from netmiko import ConnectHandler
import datetime


try:                                # try/except block for datetime
    stamp = datetime.datetime.now()

    time = str(stamp)

except ImportError:
    print("Error: Could not import datetime")


def save_run():             # to save ths running config on the routers locally

    exceptions = (netmiko.ssh_exception.NetMikoTimeoutException, netmiko.ssh_exception.NetMikoAuthenticationException)

    global filename1,filename2,filename3,filename4
    global files
    filename1="R1_%s.txt" % time
    filename2="R2_%s.txt" % time
    filename3="R3_%s.txt" % time
    filename4="R4_%s.txt" % time

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


        print("Saving running config for R1")
        p1 = net_connect1.send_command('show run')
        with open(filename1, 'w') as f1:
            f1.write(p1)
            print("Saved file as:", filename1)

        print("Saving running config for R2")
        p2 = net_connect2.send_command('show run')
        with open(filename2, 'w') as f2:
            f2.write(p2)
            print("Saved file as:", filename2)

        print("Saving running config for R3")
        p3 = net_connect3.send_command('show run')
        with open(filename3, 'w') as f3:
            f3.write(p3)
            print("Saved file as:", filename3)

        print("Saving running config for R4")
        p4 = net_connect4.send_command('show run')
        with open(filename4, 'w') as f4:
            f4.write(p4)
            print("Saved file as:", filename4)

        files = [filename1,filename2,filename3,filename4]
        print(files)
        return files

        # for graceful exit from SSH session
        net_connect1.disconnect()
        net_connect2.disconnect()
        net_connect3.disconnect()
        net_connect4.disconnect()

    except exceptions as b:
        print("Error occurred ", b)
        sys.exit()


save_run()



