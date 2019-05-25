#!/usr/bin/env python3

#author : Simran Kohli simran.kohli@colorado.edu
#name : obj3.py
#purpose : A script to find traps in a pcap file
#date : 2018.02.03
#version : 1.1

import os
import sys
from scapy.all import *
import smtplib

fileName = 'lab2tdump.pcap'

def checkFile(fileName):
    print("File name is: " + fileName)
    if os.path.isfile(fileName):
        print("File exists")
    else:
        print("File not found")
        sys.exit()

def read_file(fileName):
    data = " "
    trap = " "
    Trap = []
    try:
        pkts_list = rdpcap(fileName)
        print(len(pkts_list))
        for pkt in pkts_list:
            if (pkt.haslayer('SNMP')):
                print("This all the SNMP data")
                pkt.show()
                # data = str(pkt.show())
                #data = str(pkt.getlayer('SNMP'))
                #print(data)

                '''if "[SNMPtrapv2]" in data:
                    trap = data.split("")
                    Trap.append(trap)
                    print("This is the trap data")
                    print(Trap)'''

    except ImportError:
        print("Scapy module not found")
        sys.exit()

    try:
        print("Sending email")
        server = smtplib.SMTP('smtp.gmail.com', 587) #gmail server location and port
        server.starttls()
        server.login("simran.netman@gmail.com", "netmanLab2") # username and password
        msg = pkt.show()
        #print(msg)
        server.sendmail("simran.netman@gmail.com", "simran.netman@gmail.com", msg) #from, to, msg
        print("Mail sent successfully")
        server.quit()
    except Exception:
        print("Error. Unable to send email.")
        sys.exit()

'''def send_mail():
    try:
        print("Sending email")
        server = smtplib.SMTP('smtp.gmail.com', 587) #gmail server location and port
        server.starttls()
        server.login("simran.netman@gmail.com", "netmanLab2") # username and password
        msg = data
        print(msg)
        server.sendmail("simran.netman@gmail.com", "simran.netman@gmail.com", msg) #from, to, msg
        print("Mail sent successfully")
        server.quit()
    except Exception:
        print("Error. Unable to send email.")
        sys.exit()'''

checkFile(fileName)
read_file(fileName)
#send_mail()


