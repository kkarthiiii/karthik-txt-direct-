#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "23269372"))
API_HASH = environ.get("API_HASH", "ad1257b0704ddbd536a0a11723fbdc4f")
BOT_TOKEN = environ.get("BOT_TOKEN", "8087601529:AAG_00BkRwo8K-1gbqv5yy_ehx74d7msbgI")
OWNER = int(environ.get("OWNER", "7373747071"))
CREDIT = "KARTHIK"
AUTH_USER = os.environ.get('AUTH_USERS', '7373747071').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
