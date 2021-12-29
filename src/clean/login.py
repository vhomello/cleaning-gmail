import json
import pathlib
import os
from typing import List
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials

from constants import CLIENT_SECRET_FILE, SCOPES

def google_login(
    client_secret_file:str = CLIENT_SECRET_FILE,
    scopes:List[str] = SCOPES
    ) -> Credentials:

    here = pathlib.Path(__file__).parent.resolve()
    with open(os.path.join(here, client_secret_file), 'rb') as handle:
        client_secret = json.load(handle)

    user_credentials = (
        InstalledAppFlow
        .from_client_config(client_secret, scopes)
        .run_console()
    )

    return user_credentials
