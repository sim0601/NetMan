#!/usr/bin/env python3

#author : Simran Kohli simran.kohli@colorado.edu
#name : obj6.3_w.py
#purpose : A script to find the IP's in a pcap file
#date : 2018.01.28
#version : 1.2

import os
import sys
from scapy.all import rdpcap

fileName = 'obj6.pcap'

def checkFile(fileName):
    print("File name is: " + fileName)
    if os.path.isfile(fileName):
        print("File exists")
    else:
        print("File not found")
        sys.exit()

def read_file(fileName):
    try:
        pkts_list = rdpcap(fileName)

        n = len(pkts_list)
        num = 0

        print("No of pkts in file is", n)

        while num < n:
            print(pkts_list[num]['IP'].src, "This is the source IP for packet no:", num)
            #print("This is the source IP for packet no:", num)

            print(pkts_list[num]['IP'].dst, "This is the destination IP for packet no:", num)
            #print("This is the destination IP for packet no:", num)
            num = num + 1
        sys.exit()

    except ImportError:
        print("Scapy module not found")
        sys.exit()

checkFile(fileName)
read_file(fileName)
