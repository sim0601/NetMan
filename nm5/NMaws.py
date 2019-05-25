#!/usr/bin/env python3

#author : Simran Kohli simran.kohli@colorado.edu
#name : NMaws.py
#purpose : A script to create and manipulate S3 buckets
#date : 2018.02.26
#version : 1.2

import sys
import boto3
import datetime

s3 = boto3.client('s3') # create an S3 client

def create():
    try:                    #create a S3 bucket                                                                                # try except block for boto3
        s3.create_bucket(Bucket='netmanlab5.2', CreateBucketConfiguration={'LocationConstraint': 'us-west-2'})
        print("Bucket created successfully")

    except ImportError:
        print("boto3 module could not be imported")
        sys.exit()

def list_buckets():
    try:                    # list the buckets                                                                                          # try except block for boto3
        result = s3.list_buckets()
        buckets = [bucket['Name'] for bucket in result['Buckets']]
        print("Bucket list: ", buckets)

    except ImportError:
        print("boto3 module could not be imported")
        sys.exit()

def push():
    try:                  # push/upload files to the bucket                                                                                  # try except block for boto3
        current_time = datetime.datetime.now()
        file1 = 'mac extraction'
        file2 = 'CPU.jpg'
        bucket_name = 'netmanlab5.2'


        s3.upload_file(file1, bucket_name, file1)
        s3.upload_file(file2, bucket_name, file2)
        print("Files:", file1, file2, "have been pushed to the bucket")

    except ImportError:
        print("boto3 module could not be imported")
        sys.exit()

def list_con_del():
    try:                             # list the bucket contents                                                  # try except block for boto3
        bucket_name = 'netmanlab5.2'
        result = s3.list_objects_v2(Bucket = bucket_name)

        content = result['Contents']

        print("The contents of the bucket are:")
        #print(content)
        print(content[0]['Key'])
        print(content[1]['Key'])

        file1_time = content[0]['LastModified']
        print(content[0]['Key'], " was last modified ", file1_time)

        file2_time = content[1]['LastModified']
        print(content[1]['Key'], " was last modified ", file2_time)

    except ImportError:
        print("boto3 module could not be imported")
        sys.exit()


    try:                                # delete files according to the time
        StartTime = file1_time.utcnow()
        EndTime=file1_time.utcnow() + datetime.timedelta(seconds=300)
        print(StartTime)
        print(EndTime)

        if file1_time.utcnow() < EndTime:
            print("Deleting files now")
            
            s3.delete_objects(Bucket = bucket_name, Delete= {'Objects': [{'Key': 'test.jpg'}]})
            
            print("Deletion successful for first file")
            
        else:
            print("File time not expired")


        if file2_time.utcnow() < EndTime:
            print("Deleting files now")

            s3.delete_objects(Bucket = bucket_name, Delete= {'Objects': [{'Key': 'mac extraction'}]})

            print("Deletion successful for second file" )

        else:
            print("File time not expired")


    except ImportError:
        print("boto3 module could not be imported")
        sys.exit()

#create()
#list_buckets()
#list_con_del()
#push()
