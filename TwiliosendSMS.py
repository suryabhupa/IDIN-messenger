from twilio.rest import TwilioRestClient
 
account = "ACf65d7f6a52e562109340437ab8dc2829"
token = "9c7237a15b4c3bdc49574898232e79d5"
client = TwilioRestClient(account, token)
 
def SendSMS():
  message = client.sms.messages.create(to="+18179460792", from_="+16176064716",
                                     body="Hello, World!")
 
if __name__ == '__main__':
  SendSMS()