from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

from twilio.rest import Client
import os

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACd706c06d3b5fab9df94f1bf8a760f773'
auth_token = '7b7ce1f377bd494a0e55b2c39865b3de'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              from_='whatsapp:+14155238886',
                              body='Welcome to the .... App. Please enter your Account Number to start Transaction',
                              to='whatsapp:+2349013775931'
                          )

print(message.sid)

app = Flask(__name__)


GOOD_BOY_URL = "https://images.unsplash.com/photo-1518717758536-85ae29035b6d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80"


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if 'quote' in incoming_msg:
        # return a quote
        r = request.get('https://api.quotable.io/random')
        if r.status_code == 200:
            data = r.json()
            quote = f'{data["content"]} ({data["author"]})'
        else:
            quote = 'I could not retrieve a quote at this time, sorry.'
        msg.body(quote)
        responded = True
    if '1234567' in incoming_msg:
        # return a cat pic
        msg.body('Welcome Gain John\nPress 1 to perform addition Operation \n Press 2 to perform subtraction Operation \nPress 3 to perform Multiplication Operation')
        responded = True
         
    if not responded:
        msg.body('I could not retrieve your Account Number at this time, Sorry')


    if 'cat' in incoming_msg:
        # return a cat pic
        msg.media('https://cataas.com/cat')
        responded = True
    # if not responded:
    #     msg.body('I only know about famous quotes and cats, sorry!')
    return str(resp)


if __name__ == "__main__":
    app.run()



# from twilio.rest import Client
# import os

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
# account_sid = 'ACd706c06d3b5fab9df94f1bf8a760f773'
# auth_token = '7b7ce1f377bd494a0e55b2c39865b3de'
# client = Client(account_sid, auth_token)

# message = client.messages.create(
#                               from_='whatsapp:+14155238886',
#                               body='Press 1 to check account balance',
#                               to='whatsapp:+2349013775931'
#                           )

# print(message.sid)










