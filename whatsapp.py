import os
from twilio.rest import Client

client = Client()

from_whatsapp_number='whatsapp:ADD_NUMBER'
to_whatsapp_number='whatsapp: add_number'

client.messages.create(body='INPUT MESSAGE', 
			from_=from_whatsapp_number,
			to=to_whatsapp_number)
