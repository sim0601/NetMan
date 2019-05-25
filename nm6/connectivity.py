#!/usr/bin/env python3

#author : Simran Kohli simran.kohli@colorado.edu
#name : connectivty.py
#purpose : A script to SSH into the routers by parsing data from a json file
#date : 2018.03.09
#version : 1.2


import os
import sys
import json
import netmiko
from netmiko import ConnectHandler

fileName = "sshInfo.json"

# checks if the file exists
def checkFile(fileName):
    print("File name is: " + fileName)
    if os.path.isfile(fileName):
        print("File exists")
    else:
        print("File not found")
        sys.exit()


# gets the username, password and IPs from the file
def get_data_user(fileName):

    try:                                        # try/except block for json module
        with open(fileName) as file:
            global R1_int, R2_int, R1_loop1, R1_loop2, R2_int, R2_loop1, R2_loop2, user_1, pass_1, user_2, pass_2
            data = json.load(file)

            print("IP's for R1:")
            R1_int = (data['devices']['R1']['interfaces']['fa0/0'])
            print(R1_int)
            R1_loop1 = (data['devices']['R1']['interfaces']['loopback1'])
            print(R1_loop1)
            R1_loop2 = (data['devices']['R1']['interfaces']['loopback2'])
            print(R1_loop2, "\n")

            print("IP's for R2:")
            R2_int = (data['devices']['R2']['interfaces']['fa0/0'])
            print(R2_int)
            R2_loop1 = (data['devices']['R2']['interfaces']['loopback1'])
            print(R2_loop1)
            R2_loop2 = (data['devices']['R2']['interfaces']['loopback2'])
            print(R2_loop2, "\n")

            user_1 = data['devices']['R1']['username']
            pass_1 = data['devices']['R1']['password']
            print("The required login credentials for R1 are: \n", "username is:", user_1, ", password is:", pass_1)
            print("The IP for R1 is:", data['devices']['R1']['interfaces']['fa0/0'], "\n")

            user_2 = data['devices']['R2']['username']
            pass_2 = data['devices']['R2']['password']
            print("The required login credentials for R2 are: \n", "username is:", user_2, ", password is:", pass_2)
            print("The IP for R2 is:", data['devices']['R2']['interfaces']['fa0/0'], "\n")

    except ImportError:
        print("Import Error: json module not found")
        sys.exit()

def ping_test():        # to SSH into the devices and ping the interfaces to check IP connectivity

    error_string = "% Invalid input detected at '^' marker."
    exceptions = (netmiko.ssh_exception.NetMikoTimeoutException, netmiko.ssh_exception.NetMikoAuthenticationException)

    try:                                        # try/except block for netmiko
        dev1_int1 = {
                'device_type':  'cisco_ios',
                'ip':   R1_int,
                'username': user_1,
                'password': pass_1,}

        # establishes an SSH connection by passing in the device parameters
        net_connect1 = ConnectHandler(**dev1_int1)

        net_connect1.find_prompt()

        iplist=[R1_int, R2_int]
        for ip in iplist:
            p = net_connect1.send_command('ping ' + ip)
            print(p)

        dev2_int1 = {
                'device_type':  'cisco_ios',
                'ip':   R2_int,
                'username': user_2,
                'password': pass_2,}

        # establishes an SSH connection by passing in the device parameters
        net_connect2 = ConnectHandler(**dev2_int1)

        net_connect2.find_prompt()

        iplist1=[R1_int, R2_int]
        for ip in iplist1:
            p = net_connect2.send_command('ping ' + ip)
            print(p)

        # for graceful exit from SSH session
        net_connect1.disconnect()
        net_connect2.disconnect()

    except exceptions as a:
        print("Error occurred: ", a)
        sys.exit()


#checkFile(fileName)
#get_data_user(fileName)
#ping_test()
