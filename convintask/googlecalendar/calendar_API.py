from datetime import datetime
import os
import json
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build

def test_calendar():
    print("RUNNING TEST_CALENDAR()")
    test_event1 = {"start": {"date": "2022-01-01"}, "end": {"date": "2022-01-07"}, "summary":"test event 1"}
    test_event2 = {"start": {"date": "2022-02-01"}, "end": {"date": "2022-02-07"}, "summary":"test event 2"}
    events = [test_event1, test_event2]

    return events

SCOPES = ['https://www.googleapis.com/auth/calendar']
OAUTH_CREDS = "D:\Coding\Web Projects\Convin\convintask\client_secret_310383752013-506oo8sq2hbofh3bnheb1g4eav4p0j6v.apps.googleusercontent.com.json"
CREDS = None
# SERVICE_ACCOUNT_FILE = './calendar-347410-8643619bfa06.json'
# OAUTH_CREDS = "./client_secret_310383752013-506oo8sq2hbofh3bnheb1g4eav4p0j6v.apps.googleusercontent.com.json"

def get_token(creds):
    global CREDS
    CREDS = creds
    if CREDS:
        CREDS = Credentials.from_authorized_user_info(json.loads(CREDS))
        if CREDS.expired and CREDS.refresh_token:
            print('refreshing token!')
            CREDS.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(OAUTH_CREDS, SCOPES, redirect_uri="http://localhost:8080/gcal/api/redirect/")
        CREDS = flow.run_local_server()
    return CREDS

def get_events():
    global CREDS
    try:
        service = build('calendar', 'v3', credentials=CREDS)
        print("Getting Events...")
        print('---')
        event_res = service.events().list(calendarId='primary').execute()
        events = event_res.get('items', [])

    except HttpError as error:
        print(f'An Http Error Occured : {error}')
    
    return events