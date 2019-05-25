#!/usr/bin/env python3

#author : Simran Kohli simran.kohli@colorado.edu
#name : test.py
#purpose : A script to get the running config of the router using nccleint
#date : 2018.13.04
#version : 1.1

#Note: netconf over ssh uses port 830

from ncclient import manager
import sys

''''def run():
    try:
        host='Lab10Router'
        with manager.connect(host='Lab10Router', port=830, username='simran', hostkey_verify=False) as m:
            c = m.get_config(source='running').data_xml
            with open("%s.xml" % host, 'w') as f:
                f.write(c)
                print("File saved as: ", f)

    except Exception as a:
        print("Error: ", a)

def run():
    try:
        host='Lab10Router'
        with manager.connect_ssh(host, username='simran', hostkey_verify=False) as m:
            c = m.get_config(source='running', filter=None)
            print(c)

    except Exception as a:
        print("Error: ", a)

def run():
    try:
        with manager.connect(host='Lab10Router',
                             port = 830,
                             username='simran',
                             password='lab',
                             hostkey_verify=False,
                             #device_params={'name': '7206VXR'},
                             allow_agent=False,
                             look_for_keys=False) as m:
            c = m.get_config(source='running')
            print(c)
            sys.exit()

    except Exception as a:
        print("Error: ", a)
run()'''

def connect():

    m = manager.connect(host='198.51.100.3', port=22, username='simran',
                        password='lab', device_params={'name': 'csr'})

    print(m.connected)

    for c in m.server_capabilities:
        print(c)


connect()
