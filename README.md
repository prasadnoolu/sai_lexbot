# sai_lexbot
linum commands
download the python :  wget https://www.python.org/ftp/python/3.8.3/Python-3.8.3.tgz
unzip the python 3.8 using : ~$ tar -xf Python-3.8.3.tgz
open the folder : cd Python-3.8.3/
type: ./configure --enable-optimizations
type: sudo make altinstall
type: sudo make install
type : pip3 install simple-salesforce -t.
type : pip3 install pandas -t.
type : pip3 install paramiko -t.
code :
import json
from simple_salesforce import Salesforce,SalesforceLogin
import pandas as pd
pd.set_option('display.max_column',100)


def lambda_handler(event, context):
    response = {"dialogAction":{"type": "Close","fulfillmentState": "Fulfilled","message":{"contentType": "PlainText"}}}
    sf = Salesforce(username='xxxxxxxxxxxx', password='xxxxxxxxxxxxxx', security_token='xxxxxxxxxxxxxxxxxx')
    responses = sf.query("SELECT id,Name,City__c FROM Patient__c")
    Rec=responses.get('records')
    df=pd.DataFrame(Rec)
    if event["currentIntent"]["name"]=="steve":
        for i in range (0,len(df)):
            if df['Name'][i]=='steve':
                response["dialogAction"]["message"]["content"]=df['City__c'][i]
                print("success")
    print(response)
    return response

