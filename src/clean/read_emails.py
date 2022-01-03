from googleapiclient.discovery import build, Resource
from google.oauth2.credentials import Credentials

from login import google_login

def read_emails(
    creds: Credentials
    ):

    service: Resource = build('gmail', 'v1', credentials=creds)
    
    return 
