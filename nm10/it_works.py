#!/usr/bin/env python3

#author : Simran Kohli simran.kohli@colorado.edu
#name : it_works.py
#purpose : A script to get the running config of the router using nccleint
#date : 2018.13.04
#version : 1.1


from ncclient import manager
import xmltodict
import xml.dom.minidom
from prettytable import PrettyTable

def connect(): # to establish connectivity and check device capability

    try:       # try/except block for ncclient
        m = manager.connect(host='198.51.100.11', port=22, username='simran',
                            password='lab', device_params={'name': 'csr'})

        print(m.connected)

        for c in m.server_capabilities:
            print("Device capibilities", c)

    except Exception as ImportError:
        print("Error: ncclient module not found")

def edit1():        # to edit and view the updated running config of R1

    try:            # try/except block for ncclient and xmltodict
        m = manager.connect(host='198.51.100.11', port=22, username='simran',
                        password='lab', device_params={'name': 'csr'})

        UPDATE_CONFIG = """
              <config>
                 <cli-config-data>
                    <cmd>hostname Router1-siko0339</cmd>
                    <cmd>interface loopback99</cmd>
                    <cmd>ip address 10.1.1.1 255.255.255.0</cmd>
                    <cmd>router ospf 1</cmd>
                    <cmd>network 10.1.1.0 0.0.0.255 area 0</cmd>
                 </cli-config-data>
              </config>
        """

        conf_str = UPDATE_CONFIG

        m.edit_config(target='running', config=conf_str)

        running_config = m.get_config('running')

        #print(running_config)
        print(xml.dom.minidom.parseString(str(running_config)).toprettyxml())

    except Exception as a:
        print("Error: ", a)

def edit2():    # to edit and view updated running config of R2

    try:        # try/except block for ncclient and xmltodict
        m = manager.connect(host='198.51.100.12', port=22, username='simran',
                        password='lab', device_params={'name': 'csr'})

        UPDATE_CONFIG = """
              <config>
                 <cli-config-data>
                    <cmd>hostname Router2-siko0339</cmd>
                    <cmd>interface loopback99</cmd>
                    <cmd>ip address 10.1.2.1 255.255.255.0</cmd>
                    <cmd>router ospf 1</cmd>
                    <cmd>network 10.1.2.0 0.0.0.255 area 0</cmd>
                 </cli-config-data>
              </config>
        """

        conf_str = UPDATE_CONFIG

        m.edit_config(target='running', config=conf_str)

        running_config = m.get_config('running')

        #print(running_config)
        print(xml.dom.minidom.parseString(str(running_config)).toprettyxml())

    except Exception as a:
        print("Error: ", a)

def edit3():     # to edit and view the updated running config of R3

    try:        # try/except block for ncclient and xmltodict
        m = manager.connect(host='198.51.100.13', port=22, username='simran',
                        password='lab', device_params={'name': 'csr'})

        UPDATE_CONFIG = """
              <config>
                 <cli-config-data>
                    <cmd>hostname Router3-siko0339</cmd>
                    <cmd>interface loopback99</cmd>
                    <cmd>ip address 10.1.3.1 255.255.255.0</cmd>
                    <cmd>router ospf 1</cmd>
                    <cmd>network 10.1.3.0 0.0.0.255 area 0</cmd>
                 </cli-config-data>
              </config>
        """

        conf_str = UPDATE_CONFIG

        m.edit_config(target='running', config=conf_str)

        running_config = m.get_config('running')

        #print(running_config)
        print(xml.dom.minidom.parseString(str(running_config)).toprettyxml())

    except Exception as a:
        print("Error: ", a)

def edit4():    # to edit and view the updated running config of R4

    try:        # try/except block for ncclient and xmltodict
        m = manager.connect(host='198.51.100.14', port=22, username='simran',
                        password='lab', device_params={'name': 'csr'})

        UPDATE_CONFIG = """
              <config>
                 <cli-config-data>
                    <cmd>hostname Router4-siko0339</cmd>
                    <cmd>interface loopback99</cmd>
                    <cmd>ip address 10.1.4.1 255.255.255.0</cmd>
                    <cmd>router ospf 1</cmd>
                    <cmd>network 10.1.4.0 0.0.0.255 area 0</cmd>
                 </cli-config-data>
              </config>
        """

        conf_str = UPDATE_CONFIG

        m.edit_config(target='running', config=conf_str)

        running_config = m.get_config('running')

        #print(running_config)
        print(xml.dom.minidom.parseString(str(running_config)).toprettyxml())

    except Exception as a:
        print("Error: ", a)

def edit5():    # to edit and view the updated running config of R5

    try:        # try/except block for ncclient and xmltodict
        m = manager.connect(host='198.51.100.15', port=22, username='simran',
                        password='lab', device_params={'name': 'csr'})

        UPDATE_CONFIG = """
              <config>
                 <cli-config-data>
                    <cmd>hostname Router5-siko0339</cmd>
                    <cmd>interface loopback99</cmd>
                    <cmd>ip address 10.1.5.1 255.255.255.0</cmd>
                    <cmd>router ospf 1</cmd>
                    <cmd>network 10.1.5.0 0.0.0.255 area 0</cmd>
                 </cli-config-data>
              </config>
        """

        conf_str = UPDATE_CONFIG

        m.edit_config(target='running', config=conf_str)

        running_config = m.get_config('running')

        #print(running_config)
        print(xml.dom.minidom.parseString(str(running_config)).toprettyxml())

    except Exception as a:
        print("Error: ", a)

def run():      # to extract the running config of all routers

    try:        # try/except block for ncclient
        m1 = manager.connect(host='198.51.100.11', port=22, username='simran',
                            password='lab', device_params={'name': 'csr'})

        running_config1 = m1.get_config('running')

        with open('R1_lab10.txt', 'w') as f1:
            f1.write(str(running_config1))
            print("Config saved as: ", f1)

        m2 = manager.connect(host='198.51.100.12', port=22, username='simran',
                            password='lab', device_params={'name': 'csr'})

        running_config2 = m2.get_config('running')

        with open('R2_lab10.txt', 'w') as f2:
            f2.write(str(running_config2))
            print("Config saved as: ", f2)

        m3 = manager.connect(host='198.51.100.13', port=22, username='simran',
                            password='lab', device_params={'name': 'csr'})

        running_config3 = m3.get_config('running')

        with open('R3_lab10.txt', 'w') as f3:
            f3.write(str(running_config3))
            print("Config saved as: ", f3)

        m4 = manager.connect(host='198.51.100.14', port=22, username='simran',
                            password='lab', device_params={'name': 'csr'})

        running_config4 = m4.get_config('running')

        with open('R4_lab10.txt', 'w') as f4:
            f4.write(str(running_config4))
            print("Config saved as: ", f4)

        m5 = manager.connect(host='198.51.100.15', port=22, username='simran',
                            password='lab', device_params={'name': 'csr'})

        running_config5 = m5.get_config('running')

        with open('R5_lab10.txt', 'w') as f5:
            f5.write(str(running_config5))
            print("Config saved as: ", f5)

    except Exception as ImportError:
        print("Error: ncclient module not found")
    #print(running_config)
    #print(xml.dom.minidom.parseString(str(running_config)).toprettyxml())

def table():    # to parse the runnning configs and print relevant info in a table

    try:        # try/except block for pretty tables

        with open('R1_lab10.txt', 'r') as f1:
            for line in f1:
                #print(line)
                if 'hostname' in line:
                    name1 = line.split(' ')
                    #print(name1[1])

                if 'Loopback' in line:
                    loop1 = next(f1).split(' ')
                    #print(next(f1)) # prints the next iteration of a line after finding a match
                    #print(loop1[3], loop1[4])

                if 'router ospf 1' in line:
                    ospf1 = next(f1).split(' ')
                    #print(ospf1[2], ospf1[3])
                    #print(ospf1[5])

        with open('R2_lab10.txt', 'r') as f1:
            for line in f1:
                #print(line)
                if 'hostname' in line:
                    name2 = line.split(' ')
                    #print(name2[1])

                if 'Loopback' in line:
                    loop2 = next(f1).split(' ')
                    #print(next(f1)) # prints the next iteration of a line after finding a match
                    #print(loop2[3], loop2[4])

                if 'router ospf 1' in line:
                    ospf2 = next(f1).split(' ')
                    #print(ospf2[2], ospf2[3])
                    #print(ospf2[5])

        with open('R3_lab10.txt', 'r') as f1:
            for line in f1:
                #print(line)
                if 'hostname' in line:
                    name3 = line.split(' ')
                    #print(name3[1])

                if 'Loopback' in line:
                    loop3 = next(f1).split(' ')
                    #print(next(f1)) # prints the next iteration of a line after finding a match
                    #print(loop3[3], loop3[4])

                if 'router ospf 1' in line:
                    ospf3 = next(f1).split(' ')
                    #print(ospf3[2], ospf3[3])
                    #print(ospf3[5])

        with open('R4_lab10.txt', 'r') as f1:
            for line in f1:
                #print(line)
                if 'hostname' in line:
                    name4 = line.split(' ')
                    #print(name4[1])

                if 'Loopback' in line:
                    loop4 = next(f1).split(' ')
                    #print(next(f1)) # prints the next iteration of a line after finding a match
                    #print(loop4[3], loop4[4])

                if 'router ospf 1' in line:
                    ospf4 = next(f1).split(' ')
                    #print(ospf4[2], ospf4[3])
                    #print(ospf4[5])


        with open('R5_lab10.txt', 'r') as f1:
            for line in f1:
                #print(line)
                if 'hostname' in line:
                    name5 = line.split(' ')
                    #print(name5[1])

                if 'Loopback' in line:
                    loop5 = next(f1).split(' ')
                    #print(next(f1)) # prints the next iteration of a line after finding a match
                    #print(loop5[3], loop5[4])

                if 'router ospf 1' in line:
                    ospf5 = next(f1).split(' ')
                    #print(ospf5[2], ospf5[3])
                    #print(ospf5[5])


            table = PrettyTable(["Hostname", "Loopback99 IP", "OSPF area", "OSPF network to advertise"])
            table.add_row([name1[1], (loop1[3]+loop1[4]), ospf1[5], (ospf1[2]+ospf1[3])])
            table.add_row([name2[1], (loop2[3]+loop2[4]), ospf2[5], (ospf2[2]+ospf2[3])])
            table.add_row([name3[1], (loop3[3]+loop3[4]), ospf3[5], (ospf3[2]+ospf3[3])])
            table.add_row([name4[1], (loop4[3]+loop4[4]), ospf4[5], (ospf4[2]+ospf4[3])])
            table.add_row([name5[1], (loop5[3]+loop5[4]), ospf5[5], (ospf5[2]+ospf5[3])])

            print(table)

    except Exception as ImportError:
        print("Error: pretty tables module not found")


connect()
edit1()
edit2()
edit3()
edit4()
edit5()
run()
table()
