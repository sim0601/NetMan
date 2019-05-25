#!/usr/bin/env python3

#author : Simran Kohli simran.kohli@colorado.edu
#name : sshInfo.py
#purpose : A script to extract SSH info to connect to routers by parsing data from a json file
#date : 2018.03.06
#version : 1.1

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
def get_data(fileName):

    try:                                        # try/except block for json module
        with open(fileName) as file:
            data = json.load(file)

            print("This is the data for R1:", data['devices']['R1'])
            print("This is the data for R2:", data['devices']['R2'] , "\n")

            print("The required login credentials for R1 are: \n", "username is:", data['devices']['R1']['username'], ", password is:", data['devices']['R1']['password'])
            print("The IP for R1 is:", data['devices']['R1']['interfaces']['fa0/0'], "\n")

            print("The required login credentials for R2 are: \n", "username is:", data['devices']['R2']['username'], ", password is:", data['devices']['R2']['password'])
            print("The IP for R2 is:", data['devices']['R2']['interfaces']['fa0/0'], "\n")

    except ImportError:
        print("Import Error: json module not found")
        sys.exit()

#checkFile(fileName)
#get_data(fileName)
