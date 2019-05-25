#!/usr/bin/env python3

#author : Simran Kohli simran.kohli@colorado.edu
#name : bgp.py
#purpose : A script to configure BGP after parsing the bgp.conf file
#date : 2018.03.09
#version : 1.1

import os
import sys
import json
import netmiko
from netmiko import ConnectHandler
from prettytable import PrettyTable

fileName2 = "bgp.conf"
fileName3 = "sshInfo.json"

# checks if the file exists
def checkFile2(fileName2):
    print("File name is: " + fileName2)
    if os.path.isfile(fileName2):
        print("File exists")
    else:
        print("File not found")
        sys.exit()

def checkFile3(fileName3):
    print("File name is: " + fileName3)
    if os.path.isfile(fileName3):
        print("File exists")
    else:
        print("File not found")
        sys.exit()


def get_data_bgp(fileName2):        # gets the IP and relevant data for BGP configs

    try:
        with open(fileName2, 'r') as file:
            for line in file:
                global AS_num, AS_num2, routerID, routerID2, neighborIP, neighborIP2, neighborAS, neighborAS2, net_list, net_list2, neighborIP_list,neighborIP2_list, net_list_IP, net_list2_IP

                if 'R1' in line and 'LocalAS_Number' in line:
                    AS_num = line.split(':')
                    print("AS no. for R1: ", AS_num[2])

                if 'R1' in line and 'MyRouterID' in line:
                    routerID = line.split(':')
                    print("Router ID for R1: ", routerID[2])

                if 'R1' in line and 'NeighborIP' in line:
                    neighborIP = line.split(':')
                    neighborIP_list = neighborIP[2].split(',')
                    print("Neighbor IP's for R1: ", neighborIP_list[0], neighborIP_list[1])

                if 'R1' in line and 'NeighborRemoteAS' in line:
                    neighborAS = line.split(':')
                    print("Neighbor AS for R1: ",neighborAS[2])

                if 'R1' in line and 'NetworkListToAdvertise' in line:
                    net_list = line.split(':')
                    net_list_IP = net_list[2].split(',')
                    print("Network list for R1: ", net_list_IP[0], net_list_IP[1], net_list_IP[2])

                if 'R2' in line and 'LocalAS_Number' in line:
                    AS_num2 = line.split(':')
                    print("AS no. for R2: ", AS_num2[2])

                if 'R2' in line and 'MyRouterID' in line:
                    routerID2 = line.split(':')
                    print("Router ID for R2: ", routerID2[2])

                if 'R2' in line and 'NeighborIP' in line:
                    neighborIP2 = line.split(':')
                    neighborIP2_list = neighborIP2[2].split(',')
                    print("Neighbor IP's for R2: ", neighborIP2_list[0], neighborIP2_list[1])

                if 'R2' in line and 'NeighborRemoteAS' in line:
                    neighborAS2 = line.split(':')
                    print("Neighbor AS for R2: ",neighborAS2[2])

                if 'R2' in line and 'NetworkListToAdvertise' in line:
                    net_list2 = line.split(':')
                    net_list2_IP = net_list2[2].split(',')
                    print("Network list for R2: ", net_list2_IP[0], net_list2_IP[1], net_list2_IP[2])

                    print(neighborIP2_list[1].split('\n'))

    except Exception as a:
        print("Exception occurred: ",a )
        sys.exit()


def get_data_user2(fileName3):          # gets the username, password and IPs from the file

    try:                                        # try/except block for json module
        with open(fileName3) as file:
            global R1_int, R2_int, R1_loop1, R1_loop2, R2_int, R2_loop1, R2_loop2, user_1, pass_1, user_2, pass_2
            data = json.load(file)

            #print("IP's for R1:")
            R1_int = (data['devices']['R1']['interfaces']['fa0/0'])
            #print(R1_int)
            R1_loop1 = (data['devices']['R1']['interfaces']['loopback1'])
            #print(R1_loop1)
            R1_loop2 = (data['devices']['R1']['interfaces']['loopback2'])
            #print(R1_loop2, "\n")

            #print("IP's for R2:")
            R2_int = (data['devices']['R2']['interfaces']['fa0/0'])
            #print(R2_int)
            R2_loop1 = (data['devices']['R2']['interfaces']['loopback1'])
            #print(R2_loop1)
            R2_loop2 = (data['devices']['R2']['interfaces']['loopback2'])
            #print(R2_loop2, "\n")

            user_1 = data['devices']['R1']['username']
            pass_1 = data['devices']['R1']['password']
            #print("The required login credentials for R1 are: \n", "username is:", user_1, ", password is:", pass_1)
            #print("The IP for R1 is:", data['devices']['R1']['interfaces']['fa0/0'], "\n")

            user_2 = data['devices']['R2']['username']
            pass_2 = data['devices']['R2']['password']
            #print("The required login credentials for R2 are: \n", "username is:", user_2, ", password is:", pass_2)
            #print("The IP for R2 is:", data['devices']['R2']['interfaces']['fa0/0'], "\n")

    except ImportError:
        print("Import Error: json module not found")
        sys.exit()

def config_ibgp(): # to configure iBGP on the routers

    exceptions = (netmiko.ssh_exception.NetMikoTimeoutException, netmiko.ssh_exception.NetMikoAuthenticationException)

    error_string = "% Unknown command or computer name, or unable to find computer address"

    try:                                        # try/except block for netmiko
        dev1_int1 = {
                'device_type':  'cisco_ios',
                'ip':   R1_int,
                'username': user_1,
                'password': pass_1,}

        dev2_int1 = {
                'device_type':  'cisco_ios',
                'ip':   R2_int,
                'username': user_2,
                'password': pass_2,}

        global net_connect1, net_connect2
        # establishes an SSH connection by passing in the device parameters

        net_connect1 = ConnectHandler(**dev1_int1)
        net_connect2 = ConnectHandler(**dev2_int1)


        config_commands1 = ['router bgp ' + AS_num[2],
                            'neighbor '+ neighborIP_list[0] + ' remote-as ' + AS_num[2],
                            'neighbor '+ neighborIP_list[1] + ' remote-as ' + AS_num[2],
                            'neighbor ' + neighborIP_list[0] + ' update-source loopback1',
                            'neighbor ' + neighborIP_list[1] + ' update-source loopback2',
                            ]
        config_commands2 = ['ip route ' + neighborIP_list[0] + ' 255.255.255.255 ' + R2_int,
                            'ip route ' + neighborIP_list[1] + ' 255.255.255.255 ' + R2_int]

        output1 = net_connect1.send_config_set(config_commands1)
        output2 = net_connect1.send_config_set(config_commands2)
        print(output1)
        print(output2)

        config_commands3 = ['router bgp ' + AS_num2[2],
                            'neighbor '+ neighborIP2_list[0] + ' remote-as ' + AS_num2[2],
                            'neighbor '+ neighborIP2_list[1] + ' remote-as ' + AS_num2[2],
                            'neighbor ' + neighborIP2_list[0] + ' update-source loopback1',
                            'neighbor ' + neighborIP2_list[1] + ' update-source loopback2',
                            ]
        config_commands4 = ['ip route ' + neighborIP2_list[0] + ' 255.255.255.255 ' + R1_int,
                            'ip route ' + neighborIP2_list[1] + ' 255.255.255.255 ' + R1_int]

        output3 = net_connect2.send_config_set(config_commands3)
        output4 = net_connect2.send_config_set(config_commands4)
        print(output3)
        print(output4)

        # for graceful exit from SSH session
        net_connect1.disconnect()
        net_connect2.disconnect()

    except exceptions as b:
        print("Error occurred ", b)
        sys.exit()

    if error_string in output1 or error_string in output2 or error_string in output3 or error_string in output4:
        print("Invalid command entered")
        sys.exit()

def sh_nei(): # to extract the important neoghborship information

    exceptions = (netmiko.ssh_exception.NetMikoTimeoutException, netmiko.ssh_exception.NetMikoAuthenticationException)

    error_string = "% Unknown command or computer name, or unable to find computer address"

    try:                                    # try/except block for pretty table

        iplist=[R1_int, R2_int]


        for ip in iplist:
            print("This is bgp neighborship for R1")
            p1 = net_connect1.send_command('show ip bgp neighbors')
            print(p1)
            print("This is bgp neighborship for R2")
            p2 = net_connect2.send_command('show ip bgp neighbors')
            print(p2)

            with open('bgpdata.txt', 'a+') as f:
                f.write(p1+"\n")
                f.write(p2)

            file = 'bgpdata.txt'

            with open(file, 'r') as f:
                for line in f:
                    if 'BGP neighbor' in line:
                        neig_data = line.split(' ')
                        #print(neig_data)
                        nei_IP = neig_data[3].split(',')
                        #print(nei_IP[0])
                        nei_AS = neig_data[7].split(',')
                        #print(nei_AS[0])
                    if 'BGP state' in line:
                        state_data = line.split(' ')
                        #print(state_data)
                        state = state_data[5].split(',')
                        #print(state[0])

                        table = PrettyTable(["BGP neighbor IP", "BGP neighbor AS", "BGP neighbor state"])
                        table.add_row([nei_IP[0], nei_AS[0],state[0]])
                        print(table)

    except Exception as ImportError:
        print("Import Error: Pretty tables module not found")

    except exceptions as b:
        print("Error occurred ", b)
        sys.exit()

    if error_string in p1 or p2:
        print("Invalid command entered")
        sys.exit()

def get_run(): # to save ths running config on the routers locally

    exceptions = (netmiko.ssh_exception.NetMikoTimeoutException, netmiko.ssh_exception.NetMikoAuthenticationException)

    error_string = "% Unknown command or computer name, or unable to find computer address"


    try:                                    # try/except block for netmiko

        iplist=[R1_int, R2_int]

        for ip in iplist:
            print("Extracting running config for R1")
            p1 = net_connect1.send_command('show run')
            with open('run1.txt', 'w') as f1:
                f1.write(p1)

            print("Extracting running config for R2")
            p2 = net_connect2.send_command('show run')
            with open('run2.txt', 'w') as f2:
                f2.write(p2)

    except exceptions as b:
        print("Error occurred ", b)
        sys.exit()

    if error_string in p1 or p2: # to handle invalid commands
        print("Invalid command entered")
        sys.exit()


#checkFile2(fileName2)
#checkFile3(fileName3)
#get_data_bgp(fileName2)
#get_data_user2(fileName3)
#config_ibgp()
#sh_nei()
#get_run()
