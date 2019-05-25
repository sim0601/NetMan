#!/usr/bin/env python3

#author : Simran Kohli simran.kohli@colorado.edu
#name : obj5.2py
#purpose : A script to control EC2 instances
#date : 2018.02.09
#version : 1.1

import sys
import boto3

ec2 = boto3.resource('ec2')

def create(): # to create 2 new ec2 instances
    try:                                                                         # try except block for boto3
        ec2.create_instances(ImageId='ami-f2d3638a', MinCount=1, MaxCount=2)
        print("New EC2 instances created")

    except ImportError:
        print("boto3 module could not be imported")
        sys.exit()

def stop_in(): # to stop one of the instances
    try:                                                                        # try except block for boto3
        id = ['i-04ea9d0de25ee028b']
        ec2.instances.filter(InstanceIds=id).stop()
        print("Instance", id, "has/have been stopped")

    except ImportError:
        print("boto3 module could not be imported")
        sys.exit()

def in_data(): # to get the details of the instances
    try:                                                                        # try except block for boto3
        instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name','Values': ['running', 'stopped']}])
        for instance in instances:
            state_info = instance.state
            state_name = state_info['Name']
            #print(state_name)
            print("Instance id is:",instance.id, "Instance type is:",instance.instance_type, "Instance IP is:", instance.public_ip_address, "Instance state is:", state_name)

    except ImportError:
        print("boto3 module could not be imported")
        sys.exit()

create()
stop_in()
in_data()

