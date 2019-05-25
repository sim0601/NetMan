#!/usr/bin/env python3

#author : Simran Kohli simran.kohli@colorado.edu
#name : validateIP.py
#purpose : A script to check the validity of extracted IP's
#date : 2018.03.06
#version : 1.1

'''import sshInfo

fileName = "sshInfo.json"

sshInfo.checkFile(fileName)
sshInfo.get_data(fileName)'''


import os
import sys
import json

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
def get_data_IP(fileName):

    try:                                        # try/except block for json module
        with open(fileName) as file:
            global R1_int, R2_int, R1_loop1, R1_loop2, R2_int, R2_loop1, R2_loop2
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

    except ImportError:
        print("Import Error: json module not found")
        sys.exit()

# checks the validity of the IP's obtained
def val_IP():

    try:                                # try/except block for json module
        print("IP's for R1:")
        print(R1_int)
        print(R1_loop1)
        print(R1_loop2)

        print("IP's for R2:")
        print(R2_int)
        print(R2_loop1)
        print(R2_loop2)

        #test_IP = '256.124.257.238'
        #octets_test = test_IP.split('.')

        octetsR1_int = R1_int.split('.')
        octetsR1_loop1 = R1_loop1.split('.')
        octetsR1_loop2 = R1_loop2.split('.')

        octetsR2_int = R2_int.split('.')
        octetsR2_loop1 = R2_loop1.split('.')
        octetsR2_loop2 = R2_loop2.split('.')
        #print(octetsR2_loop2)

        print("Validating IP's for R1")
        for n in range (0,4):
            if int(octetsR1_int[n]) >= 0 and int(octetsR1_int[n]) <= 255:
                print("Octet ", n, "is valid", octetsR1_int[n])
            else:
                print("Octet ", n, "is invalid", octetsR1_int[n])
                sys.exit()

            if int(octetsR1_loop1[n]) >= 0 and int(octetsR1_loop1[n]) <= 255:
                print("Octet ", n, "is valid", octetsR1_loop1[n])
            else:
                print("Octet ", n, "is invalid", octetsR1_loop1[n])
                sys.exit()

            if int(octetsR1_loop2[n]) >= 0 and int(octetsR1_loop2[n]) <= 255:
                print("Octet ", n, "is valid", octetsR1_loop2[n])
            else:
                print("Octet ", n, "is invalid", octetsR1_loop2[n])
                sys.exit()

        print("Validating IP's for R2")
        for n in range (0,4):
            if int(octetsR2_int[n]) >= 0 and int(octetsR2_int[n]) <= 255:
                print("Octet ", n, "is valid", octetsR2_int[n])
            else:
                print("Octet ", n, "is invalid", octetsR2_int[n])
                sys.exit()

            if int(octetsR2_loop1[n]) >= 0 and int(octetsR2_loop1[n]) <= 255:
                print("Octet ", n, "is valid", octetsR2_loop1[n])
            else:
                print("Octet ", n, "is invalid", octetsR2_loop1[n])
                sys.exit()

            if int(octetsR2_loop2[n]) >= 0 and int(octetsR2_loop2[n]) <= 255:
                print("Octet ", n, "is valid", octetsR2_loop2[n])
            else:
                print("Octet ", n, "is invalid", octetsR2_loop2[n])
                sys.exit()

            '''if int(octets_test[n]) >= 0 and int(octets_test[n]) <= 255:
                print("Octet is valid", octets_test[n])
            else:
                print("Octet is invalid", octets_test[n])'''

    except ImportError:
        print("Import Error: json module not found")
        sys.exit()

#checkFile(fileName)
#get_data_IP(fileName)
#val_IP()
