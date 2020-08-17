# Bulk_Whatsapp created by Peculiar Oluwagbemiro
Send messages to thousands of people on whatsapp using at once

## Instructions to use:
* Set up your twilio account -> https://www.twilio.com/try-twilio
* Enable Whatsapp in your twilio account dashboard

* Go to a terminal and type
  `pip install twilio`
  
* Clone the repository by typing `git clone https://github.com/Gbemiro8/Bulk_Whatsapp.git`

* Set up your environment variables that will contain `TWILIO_ACCOUNT_SID` and `TWILIO_AUTH_TOKEN`
    * To create environment variables
    * type `sudo vim /etc/environment` or replace vim with any text editor of your choice and press enter
    * Type `TWILIO_ACCOUNT_SID="your account id"` and `TWILIO_AUTH_TOKEN="your_auth_token"` on a new line

* include your phone phone number in the `from_whatsapp_number` and the number you're sending to in the `to_whatsapp_number`

* include your message in the message string `message`

* Run whatsapp.py in your terminal and you're good to go.
