# You will find your ACCOUNT SID, AUTH TOKEN, twilio PHONE NUMBER on the twilio dashboard..

from twilio.rest import Client

# Your Account SID
account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXX"  # ACCOUNT SID
# Your Auth Token
auth_token  = "8XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"  # AUTH TOKEN

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+913874020472", 
    from_="+6547385345", # PHONE NUMBER
    # Enter your message in body
    body="Hello from Python!\nTwilio api is working!!!! :)")

print(message.sid)
