from __future__ import print_function

import json
import urllib
from lambda_packages import lambda_packages
import psycopg2
import boto3

s3 = boto3.client('s3')
def lambda_handler(event, context):
    print("I'm being triggered!")
    print('starting connection')
    con=psycopg2.connect(dbname= 'dev', host='redshift-cluster-1.czutp277tj2a.us-east-2.redshift.amazonaws.com', port= '5439', user= 'awsuser', password= 'Michael1')
    cur = con.cursor()
    cur.execute("select * from public.demo")
    rows = cur.fetchall()
    
    
    #email_content = ''
    ## retrieve bucket name and file_key from the S3 event
    #bucket_name = event['Records'][0]['s3']['bucket']['name']
    #file_key = event['Records'][0]['s3']['object']['key']
    ## get the object
    #obj = s3.get_object(Bucket=bucket_name, Key=file_key)
    ## get lines inside the csv
    #lines = obj['Body'].read().split(b'\n')
    #print(lines)
    #for col in lines[0].split(','):
    #    print(col)
    
    #cur.copy_from(obj, 'demo', columns=('primary_key', 'name', 'user_id', 'city', 'state', 'timezone_offset', 'zip_code'))
    cur.execute("copy demo from 's3://econetteam5' credentials 'aws_access_key_id=AKIAJBWEBWNOC2ROLBMQ;aws_secret_access_key=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' csv")
    con.commit()
    #sql = """INSERT INTO public.demo(lastname) VALUES(%s);"""
    
    #for r in lines:
    #   email_content = email_content + '\n' + r.decode()
    #   cur.execute(sql, (str(r.decode()),))
    #   con.commit()
    #cur.execute("select * from public.demo")
    #rows = cur.fetchall()
    
    #cur.close()
    return 'Hello from Lambda'
