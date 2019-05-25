#!/usr/bin/env python3

#author : Simran Kohli simran.kohli@colorado.edu
#name : lab7main.py
#purpose : A script to create a web server in flask that will get and display OSPF config info based on user input data
#date : 2018.03.17
#version : 1.1


from flask import Flask, render_template, request
import getconfig
import diffconfig
import sys

app = Flask(__name__)

@app.route('/') # the route decorator tells flask which URL you should trigger our function
def Index(): # the function is given a name which is used to gernerate URLs for that function
    return render_template('Index.html')

@app.route('/GET_config', methods=['GET','POST'])
def GET_config():
    data1 = getconfig.save_run()
    print(data1)
    if request.method == 'GET':
        bodyText = data1 # replace with list containing filenames of saved files
        return render_template('GET_config.html', bodyText=bodyText)

# diplays the form for user input
@app.route('/OSPF_config',methods=['GET','POST'])
def OSPF_config():
    return render_template('OSPF_config.html')

@app.route('/Diff_config',methods=['GET','POST'])
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
        bodyText = [data3,data4,data5,data6] # replace with list containing filenames of saved files
        return render_template('Diff_config.html', bodyText=bodyText)


@app.route('/formData', methods=['GET','POST'])
def formData():
    if request.method == 'POST':
        user1 = request.form['username1']
        pass1 = request.form['password1']
        process1 = request.form['process_id1']
        area1 = request.form['area_id1']
        loop1 = request.form['loopback_IP1']

        return ("Data entered successfully. \n"
                "Data for R1:", user1, pass1,process1,area1,loop1, "\n")

    else:
        return("Please enter data to configure")


if __name__=='__main__':
    app.debug = True
    app.run(host='127.0.0.1', port =8080)
