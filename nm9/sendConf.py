#!/usr/bin/env python3

#author : Simran Kohli simran.kohli@colorado.edu
#name : sendConf.py
#purpose : A script to push config files to routers through netmiko
#date : 2018.04.06
#version : 1.1

import os
import sys
import netmiko
from netmiko import ConnectHandler


def send():

    try:                                        # try/except block for netmiko
        dev1 = {
                'device_type':  'cisco_ios',
                'ip':  '198.51.100.3',
                'username': 'simran',
                'password': 'lab',}

        dev2 = {
                'device_type':  'cisco_ios',
                'ip':   '198.51.100.4',
                'username': 'simran',
                'password': 'lab',}

        dev3 = {
                'device_type':  'cisco_ios',
                'ip':   '198.51.100.5',
                'username': 'simran',
                'password': 'lab',}


        net_connect1 = ConnectHandler(**dev1)
        net_connect2 = ConnectHandler(**dev2)
        net_connect3 = ConnectHandler(**dev3)

        p1 = net_connect1.find_prompt()
        #print(p1)

        p2 = net_connect2.find_prompt()
        #print(p2)

        p3 = net_connect3.find_prompt()
        #print(p3)

        with open('/etc/ansible/Configs/R1.txt') as f1:
            lines = f1.read().splitlines()
            output1= net_connect1.send_config_set(lines)
            print(output1)

        with open('/etc/ansible/Configs/R2.txt') as f2:
            lines = f2.read().splitlines()
            output2= net_connect2.send_config_set(lines)
            print(output2)

        with open('/etc/ansible/Configs/R3.txt') as f3:
            lines = f3.read().splitlines()
            output3= net_connect3.send_config_set(lines)
            print(output3)



    except Exception as a:
        print("Error: ", a)


send()
