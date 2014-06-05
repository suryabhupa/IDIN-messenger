from flask import Flask, render_template, request
from twilio.rest import TwilioRestClient
import sendgrid
import json

import os

if os.environ.has_key('twilio_account') and os.environ.has_key('twilio_token') and os.environ.has_key('SENDGRID_USERNAME') and os.environ.has_key('SENDGRID_PASSWORD'):
    account = os.environ['twilio_account']
    token = os.environ['twilio_token']
    username = os.environ['SENDGRID_USERNAME']
    password = os.environ['SENDGRID_PASSWORD']
else:
    from local_settings import *


app = Flask(__name__)
client = TwilioRestClient(account, token)
sendgrid_api = sendgrid.SendGridClient(username, password)

@app.route('/')
def ReturnForm():
  return render_template('form.html')
 
@app.route('/', methods=['POST'])
def FormPost():
  sendto = request.form['to-number']
  at_symbol = "@"
  if at_symbol in sendto:
    message = sendgrid.Mail(to=request.form['to-number'], subject='Test email from IDIN web app', html=request.form['Message'], text=request.form['Message'], from_email='16176064716@sms.idinmessagetest.cf')
    status, msg = sendgrid_api.send(message)
    return render_template('success.html')
  else:
    message = client.sms.messages.create(to=request.form['to-number'], from_="+16176064716",
                                     body=request.form['Message'])
    return render_template('success.html')
 
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
		
