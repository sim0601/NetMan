#!/usr/bin/env python3

#author : Simran Kohli simran.kohli@colorado.edu
#name : obj3final.py
#purpose : A script to find traps in a pcap file
#date : 2018.02.03
#version : 1.1

import os
import sys
from scapy.all import *
import smtplib

fileName = 'lab2tdump.pcap'
data = " "
def checkFile(fileName):
    print("File name is: " + fileName)
    if os.path.isfile(fileName):
        print("File exists")
    else:
        print("File not found")
        sys.exit()

def read_send(fileName):
    try:
        pkts_list = rdpcap(fileName)
        print(len(pkts_list))
        for pkt in pkts_list:
            if (pkt.haslayer('SNMP')):
                print("This is all the SNMP data")
                pkt.show()
                data = str((pkt.getlayer('UDP')))
                print("Sending emails with snmp data encoded in byte strings")
                server = smtplib.SMTP('smtp.gmail.com', 587) #gmail server location and port
                server.starttls()
                server.login("simran.netman@gmail.com", "netmanLab2") # username and password
                msg = data
                server.sendmail("simran.netman@gmail.com", "simran.netman@gmail.com", msg) #from, to, msg
                print("Mail sent successfully")
                server.quit()

    except ImportError:
        print("Scapy module not found")
        sys.exit()
    except Exception:
        print("Error. Unable to send email.")
        sys.exit()

checkFile(fileName)
read_send(fileName)
