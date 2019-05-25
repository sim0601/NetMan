#!/usr/bin/env python3

#author : Simran Kohli simran.kohli@colorado.edu
#name : NMtcpdump.py
#purpose : A script to parse and extract MAC
#date : 2018.02.23
#version : 1.2

import os
import sys
from scapy.all import *

fileName = 'lab5obj2.pcap' # replace with required .pcap file

def checkFile(fileName):                # checks to see if file exists
    print("File name is: " + fileName)
    if os.path.isfile(fileName):
        print("File exists")
    else:
        print("File not found")
        sys.exit()

def read_file(fileName):                # reads the files to extract MAC
    try:                                # try and except block for scapy module
        pkts_list = rdpcap(fileName)

        n = len(pkts_list)
        num = 0

        print("No of pkts in file is", n)

        #while num < n:
        while num < n:
            #print(pkts_list[num].summary())
            if num == 2 or num == 16:
                if 'ICMPv6 Echo Request' in pkts_list[num].summary():
                    # determines the src IP
                    a = pkts_list[num]['IPv6'].src
                    print("This is the source IP",a, "for packet no:", num)
                    parts = a.split(':')
                    # determines the MAC from the IP address(converts back from the EUI 64 format)
                    print("This is the source MAC for packet no:", num)
                    print(parts[4].replace('e','c'),".0",parts[5].replace('f',''),parts[6].replace('fe',''),".00",parts[7])            #print(type(parts[4]))

                    if num ==2:
                        print("This is the MAC of R2")
                    else:
                        print("This is the MAC of R3")

            num = num + 1
        sys.exit()

    except ImportError:
        print("Scapy module not found")
        sys.exit()

#checkFile(fileName)
#read_file(fileName)
