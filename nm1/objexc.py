#!/usr/bin/env python3

#author : Simran Kohli simran.kohli@colorado.edu
#name : objexc.py
#purpose : A script to find A records in a pcap file
#date : 2018.01.26
#version : 1.1

import os
import sys
from scapy.all import *

fileName = 'lab1.pcap'

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

        for pkt in pkts_list:
            if (pkt.haslayer('DNS')):
                data = str((pkt.getlayer('DNS')))
                print(data)
                #print(type(data))
                #data_true = str(data)
                #print(data_true)

    except ImportError:
        print("Scapy module not found")
        sys.exit()

checkFile(fileName)
read_file(fileName)




