# This component handles outbound messaging.

from flask import render_template, request
from flask.ext.restless import APIManager
from app import app, db
from .models import Message

from twilio.rest import TwilioRestClient
import twilio.twiml
import sendgrid
import json
import plivo
import plivoxml as XML
import requests

import os

if 'twilio_account' in os.environ and 'twilio_token' in os.environ and 'SENDGRID_USERNAME' in os.environ and 'SENDGRID_PASSWORD' in os.environ:
    account = os.environ['twilio_account']
    token = os.environ['twilio_token']
    username = os.environ['SENDGRID_USERNAME']
    password = os.environ['SENDGRID_PASSWORD']
    placcount = os.environ['plivo_account']
    pltoken = os.environ['plivo_token']

else:
    from .local_settings import *

client = TwilioRestClient(account, token)
sendgrid_api = sendgrid.SendGridClient(username, password)
plivo_api = plivo.RestAPI(placcount, pltoken)

plivo_number = "14842027664"

# REST API

manager = APIManager(app, flask_sqlalchemy_db=db)
manager.create_api(Message, methods=['GET'])

@app.route('/')
def ReturnForm():
    return render_template('form.html')

@app.route('/', methods=['GET', 'POST'])
def FormPost():
    sendto = request.form['to-number']
    at_symbol = "@"
    brazil_code = "+55"
    usa_code = "+1"
    if at_symbol in sendto:
        message = sendgrid.Mail(
            to=request.form['to-number'],
            subject='Test email from IDIN web app',
            html=request.form['Message'],
            text=request.form['Message'],
            from_email='16176064716@sms.idinmessagetest.cf')
        status, msg = sendgrid_api.send(message)

    # if brazil_code in sendto:
    else:
        text = request.form['Message']
        message_params = {
            'src': plivo_number,
            'dst': sendto,
            'text': text}
        print plivo_api.send_message(message_params)
        m = Message(
            to_number=message_params['dst'],
            from_number=message_params['src'],
            text=message_params['text'])
        db.session.add(m)
        db.session.commit()
    messages = Message.query.all()
    messages.reverse()
    print "messages", messages
    return render_template('table.html', messages=messages)

# This component handles incoming messages.

callers = {
    "+18179460792": "Amber",
    "+5511982023271": "Miguel",
    "+13474462905": "Jona"
}

@app.route("/handle-sms", methods=['GET', 'POST'])
def response_text():
    from_number = request.values.get('From', '')
    print "received sms"
    print "From: ", from_number
    params = {
        'src': plivo_number,  # Caller Id
        'dst': from_number,  # User Number to Call
        'text': "It works! Hello.",
        'type': "sms",
    }

    recd = Message(
        to_number=params['src'],
        from_number=params['dst'],
        text=request.values.get(
            'Text',
            ''))
    db.session.add(recd)
    db.session.commit()

    response = plivo_api.send_message(params)

    autresp = Message(
        to_number=params['dst'],
        from_number=params['src'],
        text=params['text'])
    db.session.add(autresp)
    db.session.commit()
    return "success"
