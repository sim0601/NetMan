#!/usr/bin/env python3

#author : Simran Kohli simran.kohli@colorado.edu
#name : obj5.3py
#purpose : A script to start a cloudwatch session and get the instance metrics
#date : 2018.02.09
#version : 1.1

import sys
import boto3
import datetime

ec2 = boto3.resource('ec2')
cloud_client = boto3.client('cloudwatch')


def new_sess(): # start a cloudwatch session
    try:                                                            # try except block for boto3
        # to start a new aws session using keys
        session = boto3.Session(aws_access_key_id='AKIAIRV6EYEPR77TOYUQ',aws_secret_access_key='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', region_name='us-west')
        print("Session established:", session)
        # to start cloudwatch session
        print("Cloudwatch session initiated for:", cloud_client)

    except ImportError:
        print("boto3 module could not be imported")
        sys.exit()

def in_data(): # to get the details of the instances
    try:                                                             # try except block for boto3
        all_inst=[]
        instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name','Values': ['running']}])
        for instance in instances:
            all_inst.append(instance.id)
        print("Instance id's are:",all_inst)

        if all_inst[0] == 'i-08ded05a8005efe51':
            print("Instance id:", all_inst[0])
            '''for status in ec2.meta.client.describe_instance_status()['InstanceStatuses']:
                status_data = status
                #print(status_data)
                #print(status_data['InstanceStatus'])
                status_details = status_data['InstanceStatus']
                print("The instance status is:",status_details['Status'])'''

            try:                                                                                                # try/except block for datetime
                sess_cpu = cloud_client.get_metric_statistics(Namespace='AWS/EC2',MetricName='CPU Utilization',
                                                                  Dimensions=[{'Name':'CPU Utilization', 'Value': 'Percent'}],
                                                                  # the name and value should be refering to th instance id
                                                                  StartTime=datetime.datetime.utcnow()-datetime.timedelta(seconds=1800),EndTime=datetime.datetime.utcnow(),Period=60,
                                                                  Statistics=['Sum'])
                print(sess_cpu['Label'], sess_cpu['Datapoints'])

                net_in = cloud_client.get_metric_statistics(Namespace='AWS/EC2',MetricName='Network In',
                                                                  Dimensions=[{'Name': 'Network In','Value': 'Bytes'}],
                                                                  StartTime=datetime.datetime.utcnow()-datetime.timedelta(seconds=1800),EndTime=datetime.datetime.utcnow(),Period=60,
                                                                  Statistics=['Sum'])
                print(net_in['Label'], net_in['Datapoints'])

                net_out = cloud_client.get_metric_statistics(Namespace='AWS/EC2',MetricName='Network Out',
                                                                  Dimensions=[{'Name': 'Network Out','Value': 'Bytes'}],
                                                                  StartTime=datetime.datetime.utcnow()-datetime.timedelta(seconds=1800),EndTime=datetime.datetime.utcnow(),Period=60,
                                                                  Statistics=['Sum'])
                print(net_out['Label'], net_out['Datapoints'])

                stat_check = cloud_client.get_metric_statistics(Namespace='AWS/EC2',MetricName='Status Check Failed(Any)',
                                                                  Dimensions=[{'Name':'Status Check', 'Value': 'Count'}],
                                                                  StartTime=datetime.datetime.utcnow()-datetime.timedelta(seconds=1800),EndTime=datetime.datetime.utcnow(),Period=60,
                                                                  Statistics=['Sum'])
                print(stat_check['Label'], (stat_check['Datapoints']))

            except ImportError:
                print("Datetime module not imported")
                sys.exit()

    except ImportError:
        print("boto3 module could not be imported")
        sys.exit()

new_sess()
in_data()
