#!/usr/bin/env python3

#author : Simran Kohli simran.kohli@colorado.edu
#name : NMtcpdump.py
#purpose : A script to parse and extract MAC
#date : 2018.02.20
#version : 1.1

import os
import sys
from scapy.all import *

fileName = 'obj6.pcap' # replace with required .pcap file

def checkFile(fileName):                # checks to see if file exists
    print("File name is: " + fileName)
    if os.path.isfile(fileName):
        print("File exists")
    else:
        print("File not found")
        sys.exit()

def read_file(fileName):                # reads the files to extract MAC
    try:                                # try and except block for scapy
        pkts_list = rdpcap(fileName)

        n = len(pkts_list)
        num = 0

        print("No of pkts in file is", n)

        #while num < n:
        while num < 1:
            print(pkts_list[num]['IP'].src)
            print("This is the source IP for packet no:", num)
            #print(pkts_list[num].summary())
            #print(pkts_list[num].show())
            print("This is the ethernet data: Src MAC")
            #print(pkts_list[0].getlayer('Ethernet'))
            print(pkts_list[num]['Ethernet'].src)
            print("This is the ethernet data: Dst MAC")
            print(pkts_list[num]['Ethernet'].dst)
            #print(pkts_list[num]['IP'].dst)
            #print("This is the destination IP for packet no:", num)
            num = num + 1
        sys.exit()

    except ImportError:
        print("Scapy module not found")
        sys.exit()

checkFile(fileName)
read_file(fileName)
