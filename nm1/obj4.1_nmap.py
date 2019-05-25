#!/usr/bin/env python3

#author : Simran Kohli simran.kohli@colorado.edu
#name : 4.1.py
#purpose : A script to capture nmap results in a text/csv file
#date : 2018.01.28
#version : 1.2

import os
import sys
import subprocess
import time

file1 = 'output1.txt'
file2 = 'output1.csv'

def ping_sweep():

    num = 1

    if os.path.isfile(file1) and os.path.isfile(file2):
        print("Ping sweep results files found. Updating files")
    else:
        while num <=1:
            print("Ping sweep results not found on file")

            with open('output1.txt', 'wb') as out:
                print("Saving ping sweep results to text file")
                out.write(subprocess.check_output("nmap -sP 172.20.74.0/24")) # writes the data from the ping sweep to the file
                print("Results of ping sweep saved to text file")

            with open('output1.csv', 'wb') as out:
                print("Saving ping sweep results to .csv file")
                out.write(subprocess.check_output("nmap -sP 172.20.74.0/24"))
                print("Results of ping sweep saved to .csv file")

            num = num + 1

            print(num)

            time.sleep(600) # sleeps for 10 mins

    sys.exit()

def get_IP():
    octet= ""
    Octet = []
    with open(file1, 'r') as out:
        for line in out:
            if "scan report" in line:
                octet = line.split(".")
                #print(octet)
                Octet.append(octet)
            else:
                print("No hosts were found")
    #print(Octet)
    with open('IP.txt', 'w') as out:
        out.write(str(Octet))
        print("Writing IP's to text file")

    with open('IP.csv', 'w') as out:
        out.write(str(Octet))
        print("Writing IP's to .csv file")
    sys.exit()


ping_sweep()
get_IP()
