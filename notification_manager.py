from email import message
from twilio.rest import Client
import smtplib


class NotificationManager:
    def __init__(self) -> None:
        self.twilio_account_sid = "YOUR_TWILIO_SID"
        self.twilio_auth_token = "YOUR_TWILIO_TOKEN"
        self.client = Client(self.twilio_account_sid,self.twilio_auth_token)

        # email account
        self.my_email = "YOUR EMAIL"
        self.password = "YOUR PASSWORD"
    
    def sent_message (self,from_iata, to_iata, from_city,to_city,price,depart_date,return_date):
        self.message = self.client.messages.create(
                                                    body = f"Low price alert! Only ${price} to fly from {from_city}-{from_iata} to {to_city}-{to_iata}, from {depart_date} to {return_date}",
                                                    from_ = '+TWILIO_PHONE',
                                                    to = 'YOUR_MOBILE'
                                                 )
        print(self.message.status)

    def sent_message_stepover (self,from_iata, to_iata, from_city,to_city,price,depart_date,return_date,via_city):
        self.message = self.client.messages.create(
                                                    body = f"Low price alert! Only ${price} to fly from {from_city}-{from_iata} to {to_city}-{to_iata}, from {depart_date} to {return_date}\n\nFlight has 1 stepover, via city {via_city}",
                                                    from_ = '+TWILIO PHONE',
                                                    to = 'YOUR_MOBILE'
                                                 )
        print(self.message.status)
    
    def sent_email(self,email,from_city,from_iata,to_city,to_iata,price,depart_date,return_date):
        with smtplib.SMTP("smtp.mail.yahoo.com",587) as connection:
            connection.starttls()
            connection.login(user=self.my_email, password=self.password)
            connection.sendmail(from_addr = self.my_email,
                                to_addrs = email,
                                msg = f"Subject: New Low Flight Price! \n\nLow price alert! Only ${price} to fly from {from_city}-{from_iata} to {to_city}-{to_iata}, from {depart_date} to {return_date}\nhttps://www.google.co.uk/flights?hl=en#flt={from_iata}.{to_iata}.{depart_date}*{to_iata}.{from_iata}.{return_date}"
                                )
            connection.close()
                                

