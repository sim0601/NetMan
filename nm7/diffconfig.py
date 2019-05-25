#!/usr/bin/env python3

#author : Simran Kohli simran.kohli@colorado.edu
#name : diffconfig.py
#purpose : A script to compare the running and saved configs
#date : 2018.03.16
#version : 1.2

import os
import sys
import netmiko
from netmiko import ConnectHandler
import datetime

try:                                # try/except block for datetime
    stamp = datetime.datetime.now()

    time = str(stamp)

except ImportError:
    print("Error: Could not import datetime")


def get_run(): # to save ths running config on the routers locally

    exceptions = (netmiko.ssh_exception.NetMikoTimeoutException, netmiko.ssh_exception.NetMikoAuthenticationException)

    global filename5, filename6, filename7,filename8

    filename5="R1_%s.txt" % time # appends the datetime string to the file name
    filename6="R2_%s.txt" % time
    filename7="R3_%s.txt" % time
    filename8="R4_%s.txt" % time


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


        print("Extracting running config for R1")
        p1 = net_connect1.send_command('show run')
        with open(filename5, 'w') as f1:
            f1.write(p1)
            print("Saved file as:", filename5)

        print("Extracting running config for R2")
        p2 = net_connect2.send_command('show run')
        with open(filename6, 'w') as f2:
            f2.write(p2)
            print("Saved file as:", filename6)

        print("Extracting running config for R3")
        p3 = net_connect3.send_command('show run')
        with open(filename7, 'w') as f3:
            f3.write(p3)
            print("Saved file as:", filename7)

        print("Extracting running config for R4")
        p4 = net_connect4.send_command('show run')
        with open(filename8, 'w') as f4:
            f4.write(p4)
            print("Saved file as:", filename8)


        files = [filename5,filename6,filename7,filename8]
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


def save_run(): # to save ths running config on the routers locally

    exceptions = (netmiko.ssh_exception.NetMikoTimeoutException, netmiko.ssh_exception.NetMikoAuthenticationException)

    global filename1,filename2,filename3,filename4

    filename1="R1_%s.txt" % time
    filename2="R2_%s.txt" % time
    filename3="R3_%s.txt" % time
    filename4="R4_%s.txt" % time

    # the parameters will be user inputs extracted from the flask webpage

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

        files = [filename1,filename2,filename3,filename4]
        print(files)
        return files
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

        # for graceful exit from SSH session
        net_connect1.disconnect()
        net_connect2.disconnect()
        net_connect3.disconnect()
        net_connect4.disconnect()

    except exceptions as b:
        print("Error occurred ", b)
        sys.exit()


def checkFile(fileName):                # checks to see if file exists
    print("File name is: " + fileName)
    if os.path.isfile(fileName):
        print("File exists")
    else:
        print("File not found")
        sys.exit()

def compare(file1, file2):              # to compare the saved and running config files

    f1 = open(file1)
    f2 = open(file2)

    print("*"*20)
    print("Comparing files ", file1, " with ", file2, "\n")
    print("*"*20)

    # Reads the first line from the files
    f1_line = f1.readline()
    f2_line = f2.readline()

    line_count = 1

    # checks the file contents till EOF
    while f1_line != '' or f2_line != '':

        # Strip the leading whitespaces
        f1_line = f1_line.rstrip()
        f2_line = f2_line.rstrip()

        if f1_line != f2_line:

            # If a line does not exist on file2 then mark the output with + sign
            if f2_line == '' and f1_line != '':
                print("file1+", "Line-" , line_count, f1_line)
                return("file1+", "Line-" , line_count, f1_line)
            # otherwise output the line on file1 and mark it with ok
            elif f1_line != '':
                print("file1ok", "Line-" , line_count, f1_line)
                return("file1ok", "Line-" , line_count, f1_line)
            # If a line does not exist on file1 then mark the output with + sign
            if f1_line == '' and f2_line != '':
                print("file2+", "Line-" , line_count, f2_line)
                return("file2+", "Line-" , line_count, f2_line)
            # otherwise output the line on file2 and mark it with ok
            elif f2_line != '':
                print("file2ok", "Line-" ,  line_count, f2_line)
                return("file2ok", "Line-" ,  line_count, f2_line)

        #Read the next line from the file
        f1_line = f1.readline()
        f2_line = f2.readline()


        #Increment line counter
        line_count = +1

    else:
        print("The lines match")
        return("The lines match")


    # Close the files
    f1.close()
    f2.close()

save_run()
get_run()
checkFile(filename1)
checkFile(filename2)
checkFile(filename3)
checkFile(filename4)
checkFile(filename5)
checkFile(filename6)
checkFile(filename7)
checkFile(filename8)
compare(filename1,filename5)
compare(filename2,filename6)
compare(filename3,filename7)
compare(filename4,filename8)

