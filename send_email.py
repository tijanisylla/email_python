import smtplib, ssl
from dotenv import load_dotenv
import os
load_dotenv()

MY_PASSWORD = os.getenv('MY_PASSWORD')

def send_email(message):
    host = "Tijani.sylla1@gmail.com"
    port = 465
    username = "Tijani.sylla1@gmail.com"
    password = MY_PASSWORD
    receiver = "Tijani.sylla1@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
         server.login(username, password)
         server.send_email(username,receiver, message)
   
