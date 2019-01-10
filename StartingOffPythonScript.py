import requests
import boto
import boto.s3.connection
from boto.s3.key import Key
import os
def econetAPI():
    head = {'Referer': 'http://econetreg.myrheem.com/login', 'Origin': 'http://econetreg.myrheem.com/login', 'Content-Type': 'application/x-www-form-urlencoded', 'Accept': 'application/json, text/plain, */*', 'Authorization': 'Basic Y29tLnJoZWVtLmVjb25ldF9hcGk6c3RhYmxla2VybmVs'}
    bod = {'grant_type':'password', 'username':'rheeminternal@rheem.com', 'password':'rheem123'}
    r = requests.post('http://econet-uat-api.rheemcert.com/auth/token', headers=head, data=bod)
    head2 = {'Content-Type':'application/json', 'Accept':'application/json', 'Authorization':'Bearer ' + r.json().get('access_token')}
    r2 = requests.get('http://econet-uat-api.rheemcert.com/locations', headers=head2)
    return r2.json()
newDict = {}
newDict = econetAPI()
print(econetAPI())
#print(newDict[0])
#print(newDict[0]['name'])
i = 0
for element in range(0,len(newDict)):
    print(newDict[i])
    print(i)
    i = i + 1

f= open("myEconetFile1.json","w+")
for i in range(1):
    f.write("0003, Andrew, 4545, Auburn, Al, -5, 36832")
f.close()

conn = boto.s3.connect_to_region('us-east-2',
    aws_access_key_id = 'AKIAJ6QKO3GDWE7INWAA',
    aws_secret_access_key = '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',
    # host = 's3-website-us-east-1.amazonaws.com',
    # is_secure=True,               # uncomment if you are not using ssl
    calling_format = boto.s3.connection.OrdinaryCallingFormat(),
)

bucket = conn.get_bucket('econetteam5')
key_name = 'myEconetFile1.json'
path = '' #Directory Under which file should get upload
full_key_name = os.path.join(path, key_name)
k = bucket.new_key(full_key_name)
k.set_contents_from_filename(key_name)

