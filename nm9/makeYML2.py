#!/usr/bin/env python3

#author : Simran Kohli simran.kohli@colorado.edu
#name : makeYML.py
#purpose : A script to create a YAML file after reading data from a CSV
#date : 2018.04.05
#version : 1.2


import csv
import os
import sys


fileName = "confRequirements.csv"

def checkFile(fileName):
    print("File name is: " + fileName)
    if os.path.isfile(fileName):
        print("File exists")
    else:
        print("File not found")
        sys.exit()

def get_data():

    try:                                        # try/except block for all errors

        with open('confRequirements.csv') as file:
            reader = csv.reader(file)
            column = []
            hostname = []
            int_type = []
            int_name = []
            ip_sub = []
            ospf_stat = []
            ospf_id = []
            ospf_area = []
            for column in reader:
                #checks for blank lines
                if column:
                    hostname.append(column[0])
                    int_type.append(column[1])
                    int_name.append(column[2])
                    ip_sub.append(column[3])
                    ospf_stat.append(column[4])
                    ospf_id.append(column[5])
                    ospf_area.append(column[6])


        yml_file = 'main.yml'
        path = "/etc/ansible/Templates/roles/router/vars/"

        #if os.path.exists(path):
        with open(os.path.join(path + yml_file), 'w') as out:
            # for router1
            out.write('--- #this is a playbook containing the variables\n')
            out.write('routers:\n')
            out.write(' - ')
            out.write('hostname: ' + hostname[1] + "\n")
            out.write('   loopbackName: ' + int_type[1] + int_name[1] + "\n")
            out.write('   loopbackIP: ' + ip_sub[1] + "\n")
            out.write('   interfaceName1: ' + int_type[2] + int_name[2] + "\n")
            out.write('   interfaceIP1: ' + ip_sub[2] + "\n")
            out.write('   interfaceName2: ' + int_type[3] + int_name[3] + "\n")
            out.write('   interfaceIP2: ' + ip_sub[3] + "\n")
            out.write('   interfaceName3: ' + int_type[4] + int_name[4] + "\n")
            out.write('   interfaceIP3: ' + ip_sub[4] + "\n")
            out.write('   processID: ' + ospf_id[5] + "\n")
            out.write('   ospfNetwork1: ' + ip_sub[1][:-4] + '0 0.0.0.0' + "\n")
            out.write('   ospfNetwork2: ' + ip_sub[2][:-4] + '0 0.0.0.255' + "\n")
            out.write('   ospfNetwork3: ' + ip_sub[3][:-4] + '0 0.0.0.255' + "\n")
            out.write('   ospfNetwork4: ' + ip_sub[4][:-4] + '0 0.0.0.255' + "\n")
            out.write('   ospfArea: ' + ospf_area[5] + "\n")


            # for router 2
            out.write(' - ')
            out.write('hostname: ' + hostname[5] + "\n")
            out.write('   loopbackName: ' + int_type[5] + int_name[5] + "\n")
            out.write('   loopbackIP: ' + ip_sub[5] + "\n")
            out.write('   interfaceName1: ' + int_type[6] + int_name[6] + "\n")
            out.write('   interfaceIP1: ' + ip_sub[6] + "\n")
            out.write('   interfaceName2: ' + int_type[7] + int_name[7] + "\n")
            out.write('   interfaceIP2: ' + ip_sub[7] + "\n")
            out.write('   processID: ' + ospf_id[1] + "\n")
            out.write('   ospfNetwork1: ' + ip_sub[5][:-4] + '0 0.0.0.0' + "\n")
            out.write('   ospfNetwork2: ' + ip_sub[6][:-4] + '0 0.0.0.255' + "\n")
            out.write('   ospfNetwork3: ' + ip_sub[7][:-4] + '0 0.0.0.255' + "\n")
            out.write('   ospfArea: ' + ospf_area[1] + "\n")

            # for router 3
            out.write(' - ')
            out.write('hostname: ' + hostname[8] + "\n")
            out.write('   loopbackName: ' + int_type[8] + int_name[8] + "\n")
            out.write('   loopbackIP: ' + ip_sub[8] + "\n")
            out.write('   interfaceName1: ' + int_type[9] + int_name[9] + "\n")
            out.write('   interfaceIP1: ' + ip_sub[9] + "\n")
            out.write('   interfaceName2: ' + int_type[10] + int_name[10] + "\n")
            out.write('   interfaceIP2: ' + ip_sub[10] + "\n")
            out.write('   processID: ' + ospf_id[8] + "\n")
            out.write('   ospfNetwork1: ' + ip_sub[8][:-4] + '0 0.0.0.0' + "\n")
            out.write('   ospfNetwork2: ' + ip_sub[9][:-4] + '0 0.0.0.255' + "\n")
            out.write('   ospfNetwork3: ' + ip_sub[10][:-4] + '0 0.0.0.255' + "\n")
            out.write('   ospfArea: ' + ospf_area[8] + "\n")

            print("Yaml file created as: ", out)


    except Exception as a:
        print("Error: ", a)

checkFile(fileName)
get_data()
