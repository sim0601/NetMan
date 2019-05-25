#!/usr/bin/env python3

#author : Simran Kohli simran.kohli@colorado.edu
#name : objexc.py
#purpose : A script to start a cloudwatch session and continuously get the instance metrics, start and terminate instances,
# and send emails
#date : 2018.02.09
#version : 1.1

import sys
import boto3
import datetime
from botocore.exceptions import ClientError

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
    global sess_cpu
    global n
    global all_inst
    try:                                                             # try except block for boto3
        all_inst=[]
        instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name','Values': ['running']}])
        for instance in instances:
            all_inst.append(instance.id)
        print("Instance id's are:",all_inst)

        while True:
            try:                                    # try/except block for datetime
                n = 0
                num = 2

                while n < num :
                    print("Instance id:", all_inst[n])
                    sess_cpu = cloud_client.get_metric_statistics(Namespace='AWS/EC2',MetricName='CPU Utilization',
                                                                      Dimensions=[{'Name':'CPU Utilization', 'Value': 'Percent'}],
                                                                      StartTime=datetime.datetime.utcnow()-datetime.timedelta(seconds=1800),EndTime=datetime.datetime.utcnow(),Period=60,
                                                                      Statistics=['Sum'])
                    print(sess_cpu['Label'], sess_cpu['Datapoints'])

                    n = n + 1

            except ImportError:
                print("Datetime module not imported")
                sys.exit()

    except ImportError:
        print("boto3 module could not be imported")
        sys.exit()

def thresh(sess_cpu):                                   # to terminate and create new sessions based on CPU utilization
    try:                                                # try except block for boto3
        if sess_cpu['Datapoints'] < 1:
            id = all_inst[n]
            ec2.instances.filter(InstanceIds=id).terminate()
            print("Threshold crossed, terminating instances")
            print("Creating new instances")
            ec2.create_instances(ImageId='ami-f2d3638a', MinCount=1, MaxCount=2)
            send_email()
            print("Alert mail sent to user")
        else:
            print("Utilization under threshold")

    except ImportError:
        print("boto3 module could not be imported")
        sys.exit()

def send_email():                                      # to send alert emails using amazon SES(Simple Email Service)

    SENDER = "simran.kohli@colorado.edu"

    RECIPIENT = "simran.kohli@colorado.edu"

    AWS_REGION = "us-west-2"

    # The subject line for the email.
    SUBJECT = "Amazon SES Lab"

    # The email body for recipients with non-HTML email clients.
    BODY_TEXT = ("Amazon SES Lab\r\n"
                 "This is an email alert for your instances. Please login to aws to check.")

    # The HTML body of the email.
    BODY_HTML = """<html>
    <head></head>
    <body>
      <h1>This is an email alert for your instances. Please login to aws to check.</h1>>
    </body>
    </html>
    """

    # The character encoding for the email.
    CHARSET = "UTF-8"

    # Create a new SES resource and specify a region.
    client = boto3.client('ses',region_name='us-west-2')

    # Try to send the email.
    try:                                                    # try/except block for boto email client
        #Provide the contents of the email.
        response = client.send_email(
                                        Destination={'ToAddresses': [RECIPIENT,],},
                                        Message={'Body': {'Html': {'Charset': CHARSET,'Data': BODY_HTML,},
                                        'Text': {'Charset': CHARSET,'Data': BODY_TEXT,},},
                                        'Subject': {'Charset': CHARSET,'Data': SUBJECT,},},
                                        Source=SENDER,)
        
    # Display an error if something goes wrong.
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['ResponseMetadata']['RequestId'])


new_sess()
in_data()
thresh(sess_cpu)

