from __future__ import print_function

import json
import urllib
import boto3
from lambda_packages import lambda_packages

def lambda_handler(event, context):
    print("I'm being triggered!")
    print('starting connection')
	print (lambda_packages['psycopg2'])
	#con=psycopg2.connect(dbname= 'dev', host='redshift-cluster-1.c5xtuwdo1luu.us-east-2.redshift.amazonaws.com',
    #port= '5439', user= 'awsuser', password= 'Michael1')
    print('connected')
    return 'Hello from Lambda'
