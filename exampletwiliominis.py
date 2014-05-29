# API Credentials
from twilio.rest import TwilioRestClient
account = "ACf65d7f6a52e562109340437ab8dc2829"
token = "9c7237a15b4c3bdc49574898232e79d5"
client = TwilioRestClient(account, token)

# Make a Call
from twilio.rest import TwilioRestClient

account = "ACf65d7f6a52e562109340437ab8dc2829"
token = "9c7237a15b4c3bdc49574898232e79d5"
client = TwilioRestClient(account, token)

call = client.calls.create(to="9991231234",
						   from_="9991231234",
						   url ="http://twimlets.com/holdmusic?Bucket=com. twilio.music.ambient")
print call.sid

# Send an SMS
from twilio.net import TwilioRestClient

account = "ACf65d7f6a52e562109340437ab8dc2829"
token = "9c7237a15b4c3bdc49574898232e79d5"
client = TwilioRestClient(account, token)

message = client.messages.create(to="+1236851234, from_="+15555555555",
								 body="Hello there!")

# Handling a call using TwiML
from twilio import TwiML
r = twiml.Response()
r.say("Welcome to twilio!")
print str(r)

# Send message from Twilio
from twilio.rest import TwilioRestClient 
 
# put your own credentials here 
ACCOUNT_SID = "ACf65d7f6a52e562109340437ab8dc2829" 
AUTH_TOKEN = "9c7237a15b4c3bdc49574898232e79d5" 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
 
client.messages.create( 
	to="+18179460792",
	from_="+16176064716", 
	body="Welcome to the IDIN 2014 Phone List", 
	media_url="d-lab.mit.edu/idin", 
)