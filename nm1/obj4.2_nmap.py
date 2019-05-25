#!/usr/bin/env python3

#author : Simran Kohli simran.kohli@colorado.edu
#name : 4.1.py
#purpose : A script to capture nmap results in a text/csv file
#date : 2018.01.26
#version : 1.1

import os
import sys
import subprocess

file1 = 'full1.txt'
file2 = 'full2.txt'
file3 = 'full3.txt'

def full_scan():
    if os.path.isfile(file1) and os.path.isfile(file2) and os.path.isfile(file3):
        print("Full scan results files found. Updating files")
    else:
        print("Full scan results not found on file")

        with open('full1.txt', 'wb') as out:
            print("Saving full scan results to text file")
            out.write(subprocess.check_output("nmap -p 80 172.20.74.0/24"))
            print("Results of full scan for port 80 are written")

        with open('full2.txt', 'wb') as out:
            print("Saving full scan results to text file")
            out.write(subprocess.check_output("nmap -p 8080 172.20.74.0/24"))
            print("Results of full scan for port 8080 are written")

        with open('full3.txt', 'wb') as out:
            print("Saving full scan results to text file")
            out.write(subprocess.check_output("nmap -p 443 172.20.74.0/24"))
            print("Results of full scan for port 443 are written")


    sys.exit()

def get_IP():
    octet= ""
    Octet1 = []
    Octet2 = []
    with open(file1, 'r') as out:
        for line in out:
            if "scan report" in line:
                if "(" in line:
                    octet = line.split(".")
                    #print(octet)
                    Octet1.append(octet)
                    Octet2.append(octet[6])
    print(Octet1)
    print(Octet2)
    rogue = str(Octet2).strip("[").strip("]").strip("'").split(")")
    #print(rogue[0])
    t_rogue = int(rogue[0])
    #print(t_rogue)
    if t_rogue > 10:
        with open('IP.txt', 'w') as out:
            out.write(str(Octet1))
            print("Writing rogue IP's to text file")

        with open('IP.csv', 'w') as out:
            out.write(str(Octet1))
            print("Writing rogue IP's to .csv file")
        sys.exit()


full_scan()
get_IP()
