from flask import Flask, render_template, request
from twilio.rest import TwilioRestClient

app = Flask(__name__)
account = "ACf65d7f6a52e562109340437ab8dc2829"
token = "9c7237a15b4c3bdc49574898232e79d5"
client = TwilioRestClient(account, token)

@app.route('/')
def ReturnForm():
	return render_template('form.html')

@app.route('/', methods=['POST'])
def FormPost():
	message = client.sms.messages.create(to="+18179460792", from_="+16176064716", body=request.form['Message'])
	return render_template('success.html')

	if __name__ == '__main__':
		app.run(host='0.0.0.0', port=5000)
		