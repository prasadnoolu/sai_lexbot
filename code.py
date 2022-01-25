linux commands
download the python :  wget https://www.python.org/ftp/python/3.8.3/Python-3.8.3.tgz
unzip the python 3.8 using : ~$ tar -xf Python-3.8.3.tgz
open the folder : cd Python-3.8.3/
type: ./configure --enable-optimizations
type: sudo make altinstall
type: sudo make install
type : pip3 install simple-salesforce -t.
type : pip3 install pandas -t.
type : pip3 install paramiko -t.
-----------------------------------------------------------------------------------------------------------------------------------------
Salesforce data fetch
----------------------------------------------------------------------------------------------------------------------------------------
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


------------------------------------------------------------------------------------------------------------------------------------------------------
sms bot
------------------------------------------------------------------------------------------------------------------------------------------------------
import base64
import json
import os
import urllib
from urllib import request, parse


TWILIO_SMS_URL = "https://api.twilio.com/2010-04-01/Accounts/{}/Messages.json"
TWILIO_ACCOUNT_SID = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
TWILIO_AUTH_TOKEN = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"


def lambda_handler(event, context):
    respose={"dialogAction":{"type":"Close","fulfillmentState":"Fulfilled","message":{"contentType":"PlainText"}}}
    to_number=''
    if str(event["currentIntent"]["slots"]["mn"])=="+918328259947":
        to_number='xxxxxxxxxxxxxxxx'
        print("hi")
    elif str(event["currentIntent"]["slots"]["mn"])=="+919704193380":
        to_number='xxxxxxxxxxxxxxxxx'
        print("hello")
    print("to number = "+to_number)
    from_number = 'xxxxxxxxxxxxxx'
    print("from number = "+from_number)
    body = 'please download the ID card from this www.google.com'
    
    
    
    if not TWILIO_ACCOUNT_SID:
        return "Unable to access Twilio Account SID."
    elif not TWILIO_AUTH_TOKEN:
        return "Unable to access Twilio Auth Token."
    elif not to_number:
        return "The function needs a 'To' number in the format +12023351493"
    elif not from_number:
        return "The function needs a 'From' number in the format +19732644156"
    elif not body:
        return "The function needs a 'Body' message to send."

    # insert Twilio Account SID into the REST API URL
    populated_url = TWILIO_SMS_URL.format(TWILIO_ACCOUNT_SID)
    post_params = {"To": to_number, "From": from_number, "Body": body}

    # encode the parameters for Python's urllib
    data = parse.urlencode(post_params).encode()
    req = request.Request(populated_url)

    # add authentication header to request based on Account SID + Auth Token
    authentication = "{}:{}".format(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    base64string = base64.b64encode(authentication.encode('utf-8'))
    req.add_header("Authorization", "Basic %s" % base64string.decode('ascii'))

    try:
        # perform HTTP POST request
        with request.urlopen(req, data) as f:
            print("Twilio returned {}".format(str(f.read().decode('utf-8'))))
            respose['dialogAction']['message']['content'] = "SMS sent successfully!"
    except Exception as e:
        # something went wrong!
        respose['dialogAction']['message']['content'] = e
    
    return respose

-----------------Test case-------------------
{
  "currentIntent": {
    "name": "smsservice",
    "slots": {
      "mn": "+918328259947"
    },
    "slotDetails": {
      "mn": "+918328259947"
    }
  }
}
-------------------------------------------------------------------------------------------------------
email bot
-------------------------------------------------------------------------------------------------------
var aws = require("aws-sdk");
var ses = new aws.SES({ region: "us-east-1" });


exports.handler = async function (event) {
  
    
  var params = {
    Destination: {
      ToAddresses: [event.currentIntent.slots.em],
    },
    Message: {
      Body: {
        Text: { Data: "Download the Auto ID from this link wwww.googledrivelink.com" },
      },

      Subject: { Data: "Download the Auto ID " },
    },
    Source: "eliveprasad@gmail.com"
  };
  
  const  k=await sms(event,params);
   var response = {
        sessionAttributes: event.sessionAttributes,
        dialogAction: {
            type: "Close",
            fulfillmentState: "Fulfilled",
            message: {
                "contentType": "PlainText",
                "content": "Email send Successfully"
            }
        }
    };
    
   
    return response;
    
    
};

function sms(event,params){
  return ses.sendEmail(params).promise();
  
}





-------------------testcase----------------------
{
  "currentIntent": {
    "name": "emailservice",
    "slots": {
      "em": "varaprasad239@gmail.com"
    },
    "slotDetails": {
      "em": "varaprasad239@gmail.com"
    }
  }
}
-----------------------------------------------------------------------------------------------------------------------------------------
Working page of visual salesforce is 
---------------------------------------------------------------------------------------------------------------------------------

<apex:page sidebar="false" >
    <apex:iframe height="400" width="300" src="https://d13qqkftmzwn75.cloudfront.net/" scrolling="true"/>
</apex:page>
