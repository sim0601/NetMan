#!/usr/bin/env python3

#author : Simran Kohli simran.kohli@colorado.edu
#name : makeYML.py
#purpose : A script to create a YAML file after reading data from a CSV
#date : 2018.04.03
#version : 1.1


import csv
import os
import sys
import yaml

fileName = "confRequirements.csv"

def checkFile(fileName):
    print("File name is: " + fileName)
    if os.path.isfile(fileName):
        print("File exists")
    else:
        print("File not found")
        sys.exit()

def get_data():

    try:                                        # try/except block for all modules

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


            #print(hostname, "\n", int_type, "\n", int_name, "\n", ip_sub, "\n", ospf_stat, "\n", ospf_id, "\n", ospf_area)

            data = {}
            data['R1']= {}
            data['R1']['Hostname'] = hostname[1]
            data['R1']['LoopbackName'] = int_type[1] + int_name[1]
            data['R1']['LoopbackIP'] = ip_sub[1]
            data['R1']['Inteface1 Name'] = int_type[2] + int_name[2]
            data['R1']['Inteface1 IP'] = ip_sub[2]
            data['R1']['Inteface2 Name'] = int_type[3] + int_name[3]
            data['R1']['Inteface2 IP'] = ip_sub[3]
            data['R1']['Inteface3 Name'] = int_type[4] + int_name[4]
            data['R1']['Inteface3 IP'] = ip_sub[4]
            data['R1']['ProcessID'] = ospf_id[1]
            data['R1']['OSPF Area'] = ospf_area[1]

            data['R2']= {}
            data['R2']['Hostname'] = hostname[5]
            data['R2']['LoopbackName'] = int_type[5] + int_name[5]
            data['R2']['LoopbackIP'] = ip_sub[5]
            data['R2']['Inteface1 Name'] = int_type[6] + int_name[6]
            data['R2']['Inteface1 IP'] = ip_sub[6]
            data['R2']['Inteface2 Name'] = int_type[7] + int_name[7]
            data['R2']['Inteface2 IP'] = ip_sub[7]
            data['R2']['ProcessID'] = ospf_id[5]
            data['R2']['OSPF Area'] = ospf_area[5]

            data['R3']= {}
            data['R3']['Hostname'] = hostname[8]
            data['R3']['LoopbackName'] = int_type[8] + int_name[8]
            data['R3']['LoopbackIP'] = ip_sub[8]
            data['R3']['Inteface1 Name'] = int_type[9] + int_name[9]
            data['R3']['Inteface1 IP'] = ip_sub[9]
            data['R3']['Inteface2 Name'] = int_type[10] + int_name[10]
            data['R3']['Inteface2 IP'] = ip_sub[10]
            data['R3']['ProcessID'] = ospf_id[8]
            data['R3']['OSPF Area'] = ospf_area[8]

            #print(data)
            print(data['R1'])
            print(data['R2'])
            print(data['R3'])

        with open('main.yml', 'w') as out:
            out.write('---- #this is a playbook containing the variables\n')
            out.write('routers:\n')
            out.write(' - ')
            yaml.dump(data, out, default_flow_style=False)
            print("Yaml file created as: ", out)


    except Exception as a:
        print("Error: ", a)

checkFile(fileName)
get_data()
