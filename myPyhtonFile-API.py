from __future__ import print_function

import json
import urllib
from lambda_packages import lambda_packages
import psycopg2
def lambda_handler(event, context):
	
    # a = int(event['a'])
    # b = int(event['b'])
    c = None
    # op = event['op']
    
    # if op == "+": c = a + b
    # print(c)
    # if op == "-": c = a - b
    # print(c)
    # if op == "*": c = a * b
    # print(c)
    # if op == "/": c = a / b
    # print(c)
    
    con=psycopg2.connect(dbname= 'dev', host='redshift-cluster-1.czutp277tj2a.us-east-2.redshift.amazonaws.com', port= '5439', user= 'awsuser', password= 'Michael1')
    cur = con.cursor()
    cur.execute("select * from public.demo")
    rows = cur.fetchall()
    print (rows)
    i = 0
    for item in rows:
        print(str(item)[:-1][1:])
        if i == 0:
            c = str(item)[:-1][1:]
        else:
            c = c + ", " + str(item)[:-1][1:]
        i = i + 1
    
    print(c)
    return{
        'c':c
    }
