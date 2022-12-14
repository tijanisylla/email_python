
from send_email import send_email
import requests
import os
from dotenv import load_dotenv
load_dotenv()

# API KEY

API_KEY = os.getenv('API_KEY')
url = f"https://newsapi.org/v2/everything?q=tesla&from=2022-11-14&sortBy=publishedAt&apiKey={API_KEY}"

request = requests.get(url)
content = request.json()

body = ""
for article in content['articles']:
    body = body + article['title'] + "\n" + article['description'] + 2*"\n"
body = body.encode("utf-8")
send_email(message=body)
# print(body)
    



