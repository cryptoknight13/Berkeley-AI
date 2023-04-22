import twilio
# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import random # generate random number
otp = random.randint(1000,9999)
print("Your OTP is - ",otp)
# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC99cd312bf5cc5ffdce7d63cd7a2f1426'
auth_token = 'd760c87f123e565e4a07138a4e1067b3'
client = Client(account_sid, auth_token)

message = client.messages.create(
         body='Hello Mr. Mayur Your Secure Device OTP is - ' + str(otp) + 'now your mobile is hacked!\n Byby...',
         from_='+19707328524',
         to='+919661204904'
     )

print(message.sid)