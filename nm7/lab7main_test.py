#!/usr/bin/env python3

#author : Simran Kohli simran.kohli@colorado.edu
#name : lab7main.py
#purpose : A script to create a web server in flask that will get and display OSPF config info based on user input data
#date : 2018.03.17
#version : 1.1


from flask import Flask, render_template, request
import getconfig
import diffconfig
import ospfconfig
import netmiko
from netmiko import ConnectHandler
import sys


app = Flask(__name__)

@app.route('/') # the route decorator tells flask which URL you should trigger our function
def Index(): # the function is given a name which is used to gernerate URLs for that function
    return render_template('Index.html')

@app.route('/GET_config', methods=['GET','POST'])   # to save the configs and display the name of saved files
def GET_config():
    data1 = getconfig.save_run()
    print(data1)
    if request.method == 'GET':
        bodyText = data1 # replace with list containing filenames of saved files
        return render_template('GET_config.html', bodyText=bodyText)


@app.route('/OSPF_config',methods=['GET','POST'])   # diplays the form for user input
def OSPF_config():
    return render_template('OSPF_config.html')


@app.route('/Diff_config',methods=['GET','POST'])   # comapres the running and saved config files
def Diff_config():
    data1 = diffconfig.save_run()
    #print(data1[0])
    data2 = diffconfig.get_run()
    #print(data2[0])
    data3 = diffconfig.compare(data1[0], data2[0])
    data4 = diffconfig.compare(data1[1], data2[1])
    data5 = diffconfig.compare(data1[2], data2[2])
    data6 = diffconfig.compare(data1[3], data2[3])
    if request.method == 'GET':
        bodyText = [data3,data4,data5,data6] # list containing filenames of saved files
        return render_template('Diff_config.html', bodyText=bodyText)


@app.route('/formData1', methods=['GET','POST'])    # ospf config user input for R1
def formData1():

    if request.method == 'POST':
        user1 = request.form['username1']
        pass1 = request.form['password1']
        process1 = request.form['process_id1']
        area1 = request.form['area_id1']
        loop1 = request.form['loopback_IP1']
        net1_1 = request.form['network1_1']
        net1_2 = request.form['network1_2']

        exceptions = (netmiko.ssh_exception.NetMikoTimeoutException, netmiko.ssh_exception.NetMikoAuthenticationException)
        try:                                    # try/except block for netmiko
            #R1
            dev1 = {
                'device_type': 'cisco_ios',
                'ip':   loop1,
                'username': user1,
                'password': pass1,
            }

            # establishes an SSH connection by passing in the device parameters

            net_connect1 = ConnectHandler(**dev1)

            # for R1
            config_commands1 = ['router ospf ' + process1,
                    'network '+ net1_1 + ' 0.0.0.255 ' + ' area ' + area1,
                    'network '+ net1_2 + ' 0 0.0.0.255 ' + ' area ' + area1,
                    'network '+ loop1 + ' 0.0.0.0 ' + ' area ' + area1,
                    ]
            output1 = net_connect1.send_config_set(config_commands1)
            print(output1)

            # for graceful exit from SSH session
            net_connect1.disconnect()

        except exceptions as b:
            print("Error occurred ", b)

        return ("Data entered successfully.", ospfconfig.check_ospf())

    else:
        return("Please enter data to configure")



@app.route('/formData2', methods=['GET','POST'])        # ospf config user input for R2
def formData2():

    if request.method == 'POST':
        user2 = request.form['username2']
        pass2 = request.form['password2']
        process2 = request.form['process_id2']
        area2_1 = request.form['area_id21']
        area2_2 = request.form['area_id22']
        loop2 = request.form['loopback_IP2']
        cost1 = request.form['int_cost1']
        net2_1 = request.form['network2_1']
        net2_2 = request.form['network2_2']

        exceptions = (netmiko.ssh_exception.NetMikoTimeoutException, netmiko.ssh_exception.NetMikoAuthenticationException)
        try:                                    # try/except block for netmiko

            #R2
            dev2 = {
                'device_type': 'cisco_ios',
                'ip':   loop2,
                'username': user2,
                'password': pass2,
            }

            # establishes an SSH connection by passing in the device parameters

            net_connect2 = ConnectHandler(**dev2)

            #for R2
            config_commands2 = ['router ospf ' + process2,
                    'network '+ net2_1 + ' 0.0.0.255 ' + ' area ' + area2_1,
                    'network '+ net2_2 + ' 0.0.0.255 ' + ' area ' + area2_2,
                    'network '+ loop2 + ' 0.0.0.0 ' + ' area ' + area2_2,
                    ]
            output2 = net_connect2.send_config_set(config_commands2)
            print(output2)

            config_commands3 = ['int f0/0 ',
                    'ip ospf cost ' + cost1,
                    ]
            output3 = net_connect2.send_config_set(config_commands3)
            print(output3)

            # for graceful exit from SSH session
            net_connect2.disconnect()

        except exceptions as b:
            print("Error occurred ", b)


        return ("Data entered successfully.")

    else:
        return("Please enter data to configure")


@app.route('/formData3', methods=['GET','POST'])    # ospf config user input for R3
def formData3():

    if request.method == 'POST':
        user3 = request.form['username3']
        pass3 = request.form['password3']
        process3 = request.form['process_id3']
        area3 = request.form['area_id3']
        loop3 = request.form['loopback_IP3']
        net3_1 = request.form['network3_1']

        exceptions = (netmiko.ssh_exception.NetMikoTimeoutException, netmiko.ssh_exception.NetMikoAuthenticationException)
        try:                                    # try/except block for netmiko

            #R3
            dev4 = {
                'device_type': 'cisco_ios',
                'ip':   loop3,
                'username': user3,
                'password': pass3,
            }

            # establishes an SSH connection by passing in the device parameters

            net_connect4 = ConnectHandler(**dev4)

            # for R3
            config_commands6 = ['router ospf ' + process3,
                    'network '+ net3_1 + ' 0.0.0.255 ' + ' area ' + area3,
                    'network '+ loop3 + ' 0.0.0.0 ' + ' area ' + area3,
                    ]
            output6 = net_connect4.send_config_set(config_commands6)
            print(output6)

            # for graceful exit from SSH session
            net_connect4.disconnect()

        except exceptions as b:
            print("Error occurred ", b)

        return ("Data entered successfully.")

    else:
        return("Please enter data to configure")


@app.route('/formData4', methods=['GET','POST'])    # ospf config user input for R4
def formData4():

    if request.method == 'POST':
        user4 = request.form['username4']
        pass4 = request.form['password4']
        process4 = request.form['process_id4']
        area4_1 = request.form['area_id41']
        area4_2 = request.form['area_id42']
        loop4 = request.form['loopback_IP4']
        cost2 = request.form['int_cost2']
        net4_1 = request.form['network4_1']
        net4_2 = request.form['network4_2']

        exceptions = (netmiko.ssh_exception.NetMikoTimeoutException, netmiko.ssh_exception.NetMikoAuthenticationException)
        try:                                    # try/except block for netmiko
            #R4
            dev3 = {
                'device_type': 'cisco_ios',
                'ip':   loop4,
                'username': user4,
                'password': pass4,
            }

            # establishes an SSH connection by passing in the device parameters

            net_connect3 = ConnectHandler(**dev3)

            #for R4
            config_commands4 = ['router ospf ' + process4,
                    'network '+ net4_1 + ' 0.0.0.255 ' + ' area ' + area4_1,
                    'network '+ net4_2 + ' 0.0.0.255 ' + ' area ' + area4_2,
                    'network '+ loop4 + ' 0.0.0.0 ' + ' area ' + area4_2,
                    ]
            output4 = net_connect3.send_config_set(config_commands4)
            print(output4)

            config_commands5 = ['int f0/0 ',
                    'ip ospf cost ' + cost2,
                    ]
            output5 = net_connect3.send_config_set(config_commands5)
            print(output5)

            # for graceful exit from SSH session
            net_connect3.disconnect()

        except exceptions as b:
            print("Error occurred ", b)

        return ("Data entered successfully.")

    else:
        return("Please enter data to configure")

# function calls to verify ospf was configured successfully
#ospfconfig.check_ospf()
#ospfconfig.ping_test()


if __name__=='__main__':
    app.debug = True
    app.run(host='127.0.0.1', port =8080)
