from typing import List
import json
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials

def google_login(
    client_credentials_path:str = '',
    scopes:List[str] = []
    ) -> Credentials:

    with open(client_credentials_path, 'rb') as handle:
        client_credentials = json.load(handle)

    user_credentials = (
        InstalledAppFlow
        .from_client_config(client_credentials, scopes)
        .run_console()
    )

    return user_credentials

if __name__ == '__main__':
    google_login()