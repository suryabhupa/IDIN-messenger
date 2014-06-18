# This component handles outbound messaging.

from flask import Flask, render_template, request, redirect
from twilio.rest import TwilioRestClient
import twilio.twiml
import sendgrid
import json
import plivo

import os

if os.environ.has_key('twilio_account') and os.environ.has_key('twilio_token') and os.environ.has_key('SENDGRID_USERNAME') and os.environ.has_key('SENDGRID_PASSWORD'):
    account = os.environ['twilio_account']
    token = os.environ['twilio_token']
    username = os.environ['SENDGRID_USERNAME']
    password = os.environ['SENDGRID_PASSWORD']
    placcount = os.environ['plivo_account']
    pltoken = os.environ['plivo_token']

else:
    from local_settings import *


app = Flask(__name__)
client = TwilioRestClient(account, token)
sendgrid_api = sendgrid.SendGridClient(username, password)
plivo_api = plivo.RestAPI(placcount, pltoken)

plivo_number = 14842027664

@app.route('/')
def ReturnForm():
  return render_template('form.html')
 
@app.route('/', methods=['GET','POST'])
def FormPost():
  sendto = request.form['to-number']
  at_symbol = "@"
  brazil_code = "+55"
  usa_code = "+1"
  if at_symbol in sendto:
    message = sendgrid.Mail(to=request.form['to-number'], subject='Test email from IDIN web app', html=request.form['Message'], text=request.form['Message'], from_email='16176064716@sms.idinmessagetest.cf')
    status, msg = sendgrid_api.send(message)
    return render_template('success.html')
  if brazil_code in sendto:
    text = request.form['Message']
    message_params = {
        'src':plivo_number,
        'dst':sendto,
        'text':text,
        }
    print plivo_api.send_message(message_params)
    return render_template('success.html')
  if usa_code in sendto:
    text = request.form['Message']
    message_params = {
       'src':plivo_number,
       'dst':sendto,
       'text':text,
        }
    print plivo_api.send_message(message_params)
    return render_template('success.html')
  else:
    message = client.sms.messages.create(to=request.form['to-number'], from_="+16176064716",
                                     body=request.form['Message'])
    return render_template('success.html')
		
# This component handles incoming messages.

callers = {
  "+18179460792": "Amber",
  "+5511982023271": "Miguel",
  "+13474462905": "Jona"
}

@app.route("/handle-sms", methods=['GET', 'POST'])
def response_text():
  from_number = request.values.get('From', None)
  if from_number in callers:
      response_text = "Hi " + callers[from_number] + ", thanks for the message!"
  else: response_text = "Hello! Thank you for the message!"    
  
  r = plivo.XML.Response()
  r.addMessage(response_text)
  return r

  resp = twilio.twiml.Response()
  resp.message(response_text)
  return str(resp)


  params = {
  'src': '14842027664', # Caller Id
  'dst' : '18179460792', # User Number to Call
  'text' : "Hi, message from Plivo",
  'type' : "sms",
  }
  
  response = plivo_api.send_message(params)
  


 

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
