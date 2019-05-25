#!/usr/bin/env python3

#author : Simran Kohli simran.kohli@colorado.edu
#name : NMsnmp.py
#purpose : A script to access data from SNMP agents
#date : 2018.02.27
#version : 1.2


import easysnmp
from easysnmp import Session
import sys
import time
import matplotlib.pyplot as plt

def do_it_all():

    try:                                                                                        # try except block for easysnmp

        # creating sessions to access data from OID's
        session1 = Session(hostname='10.0.0.1', community='public', version=1) # for R1
        session2 = Session(hostname='10.0.0.2', community='public', version=1) # for R2
        session3 = Session(hostname='192.168.1.5', community='public', version=1) # for R2
        session4 = Session(hostname='10.0.0.3', community='public', version=1)  # for R3
        session5 = Session(hostname='192.168.1.4', community='public', version=1) # for R3
        session6 = Session(hostname='192.168.1.6', community='public', version=1) # for R4
        session7 = Session(hostname='198.51.100.3', community='public', version=1) # for R4
        session8 = Session(hostname='192.168.1.1', community='public', version=1) # for R5

        # to create a dictionary for all the router interface statuses
        int_status = {}
        # creates dicts for router IP's to store data in json format
        ip_add = {}
        ip_add['R1'] = {}
        ip_add['R1']['Addresses'] = {}
        ip_add['R1']['Addresses']['v4'] = {}
        ip_add['R1']['Addresses']['mac'] = {}

        ip_add['R5'] = {}
        ip_add['R5']['Addresses'] = {}
        ip_add['R5']['Addresses']['v4'] = {}
        ip_add['R5']['Addresses']['mac'] = {}

        ip_add['R2'] = {}
        ip_add['R2']['Addresses'] = {}
        ip_add['R2']['Addresses']['v4'] = {}
        ip_add['R2']['Addresses']['mac'] = {}

        ip_add['R3'] = {}
        ip_add['R3']['Addresses'] = {}
        ip_add['R3']['Addresses']['v4'] = {}
        ip_add['R3']['Addresses']['mac'] = {}

        ip_add['R4'] = {}
        ip_add['R4']['Addresses'] = {}
        ip_add['R4']['Addresses']['v4'] = {}
        ip_add['R4']['Addresses']['mac'] = {}

        # to get data from OIDs

        #R1 int 1
        # interface status
        int_stat1 = session1.get('ifOperStatus.1')

        # IP address
        ip_add1 = session1.get('ipAdEntAddr.10.0.0.1')
        ip_add['R1']['Addresses']['v4']['fa0/0'] = {ip_add1}

        # mac address
        mac_add1 = session1.get('ifPhysAddress.1')
        ip_add['R1']['Addresses']['mac']['fa0/0'] = {mac_add1}

        # int stat dict for R1
        int_status['R1'] = {int_stat1}

        #R2 int 1
        # interface status
        int_stat2 = session2.get('ifOperStatus.1')

        # IP address
        ip_add2 = session2.get('ipAdEntAddr.10.0.0.2')
        ip_add['R2']['Addresses']['v4']['fa0/0'] = {ip_add2}

        # mac address
        mac_add2 = session2.get('ifPhysAddress.1')
        ip_add['R2']['Addresses']['mac']['fa0/0'] = {mac_add2}

        #R2 int 2
        # interface status
        int_stat3 = session3.get('ifOperStatus.2')

        # IP address
        ip_add3 = session3.get('ipAdEntAddr.192.168.1.5')
        ip_add['R2']['Addresses']['v4']['fa0/1'] = {ip_add3}

        # mac address
        mac_add3 = session3.get('ifPhysAddress.2')
        ip_add['R2']['Addresses']['mac']['fa0/1'] = {mac_add3}

        # int stat dict for R2
        int_status['R2'] = {int_stat2, int_stat3}

        # R3 int 1
        # interface status
        int_stat4 = session4.get('ifOperStatus.1')

        # IP address
        ip_add4 = session4.get('ipAdEntAddr.10.0.0.3')
        ip_add['R3']['Addresses']['v4']['fa0/0'] = {ip_add4}
        # mac address
        mac_add4 = session4.get('ifPhysAddress.1')
        ip_add['R3']['Addresses']['mac']['fa0/0'] = {mac_add4}

        # R3 int 2
        # interface status
        int_stat5 = session5.get('ifOperStatus.1')

        # IP address
        ip_add5 = session5.get('ipAdEntAddr.192.168.1.4')
        ip_add['R3']['Addresses']['v4']['fa0/1'] = {ip_add5}

        # mac address
        mac_add5 = session5.get('ifPhysAddress.1')
        ip_add['R3']['Addresses']['mac']['fa0/1'] = {mac_add5}

        # int stat dict for R3
        int_status['R3'] = {int_stat4, int_stat5}

        # R4 int 1
        # interface status
        int_stat6 = session6.get('ifOperStatus.1')

        # IP address
        ip_add6 = session6.get('ipAdEntAddr.192.168.1.6')
        ip_add['R4']['Addresses']['v4']['fa0/0'] = {ip_add6}

        # mac address
        mac_add6 = session6.get('ifPhysAddress.1')
        ip_add['R4']['Addresses']['mac']['fa0/0'] = {mac_add6}

        # R4 int 2
        # interface status
        int_stat7= session7.get('ifOperStatus.2')

        # IP address
        ip_add7 = session7.get('ipAdEntAddr.198.51.100.3')
        ip_add['R4']['Addresses']['v4']['fa0/1'] = {}

        # mac address
        mac_add7 = session7.get('ifPhysAddress.2')
        ip_add['R4']['Addresses']['mac']['fa0/1'] = {mac_add7}

        # int stat dict for R4
        int_status['R4'] = {int_stat6, int_stat7}

        # R5 int 1
        # interface status
        int_stat8 = session8.get('ifOperStatus.1')

        # IP address
        ip_add8 = session8.get('ipAdEntAddr.192.168.1.1')
        ip_add['R5']['Addresses']['v4']['fa0/0'] = {ip_add8}

        # mac address
        mac_add8 = session8.get('ifPhysAddress.1')
        ip_add['R5']['Addresses']['mac']['fa0/0'] = {mac_add8}

        # int stat dict for R5
        int_status['R5'] = {int_stat8}

        # display the interface status data
        print("This is the interface status data: \n", int_status)

        # store and ip addresses in json format
        print(ip_add)

        with open('ip_add.txt', 'w') as f:
            f.write(str(ip_add))


        #cpu utilization/ processor RAM
        #cpu1 = session1.get('1.3.6.1.4.1.9.3.6.6.0')
        CPU=[]

        print("Getting CPU utilization for 5 mins. Please wait...")

        try:                                                            # try/except block for time, matplotlib and pillow modules
            for i in range(60):
                CPU.append((session1.get('1.3.6.1.4.1.9.3.6.6.0')))
                time.sleep(5)

            print(CPU)
            plt.plot(CPU)
            plt.margins(0.025)
            plt.legend(['CPU Utilization'], loc='upper left')
            plt.savefig("CPU.jpg")
            plt.show()

        except ImportError as a:
            print("Time module not found", a)
            sys.exit()
        except ImportError as b:
            print("Matplotlib module not found", b)
            sys.exit()
        except ImportError as c:
            print("Pillow module to support .jpg function not found", c)
            sys.exit()


    except ImportError:
            print("Easysnmp module not found")
            sys.exit()
