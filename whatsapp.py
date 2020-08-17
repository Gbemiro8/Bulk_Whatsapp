import os
from twilio.rest import Client

client = Client()

from_whatsapp_number='whatsapp:ADD_NUMBER'
to_whatsapp_number='whatsapp: add_number'

message = 'YOUR MESSAGE HERE'

client.messages.create(body=message, 
			from_=from_whatsapp_number,
			to=to_whatsapp_number)
