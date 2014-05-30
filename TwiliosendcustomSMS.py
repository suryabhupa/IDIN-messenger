from flask import Flask, render_template, request
from twilio.rest import TwilioRestClient

from local_settings import *

app = Flask(__name__)
client = TwilioRestClient(account, token)

@app.route('/')
def ReturnForm():
  return render_template('form.html')
 
@app.route('/', methods=['POST'])
def FormPost():
  sendto = request.values.get('to-number', None)
  message = client.sms.messages.create(to=request.form['to-number'], from_="+16176064716",
                                     body=request.form['Message'])
  return render_template('success.html')
 
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
		
