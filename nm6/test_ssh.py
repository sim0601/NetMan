#!/usr/bin/env python3

#author : Simran Kohli simran.kohli@colorado.edu
#name :osshInfi.py
#purpose : A script to SSH into the routers by parsing data from a csv file
#date : 2018.03.06
#version : 1.1

import csv
import os
import sys
from prettytable import PrettyTable

fileName = "sshInfo.csv"

# checks if the file exists
def checkFile(fileName):
    print("File name is: " + fileName)
    if os.path.isfile(fileName):
        print("File exists")
    else:
        print("File not found")
        sys.exit()


# gets the username, password and IPs from the file
def get_data(fileName):
    with open(fileName) as file:
        reader = csv.reader(file)
        column = []

        for column in reader:
            # checks for blank lines
            if column:
                device = []
                username = []
                password = []
                interface = []
                ip = []

                device = column[0]
                #print(device)

                username = column[1]
                #print(username)

                password = column[2]
                #print(password)

                interface = column[3]
                #print(interface)

                ip = column[4]
                #print(ip)

                R1 = []
                #R1 = R1.append(device).append(username)
                print(type(R1))
                #print("Device:", column[0], "User:", column[1].rjust(10))

checkFile(fileName)
get_data(fileName)
