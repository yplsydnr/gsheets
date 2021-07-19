#commenting this out to instead use gspread library

from googleapiclient.discovery import build
from google.oauth2 import service_account
import gsheet

SERVICE_ACCOUNT_FILE = 'C:/authkeys/googlesheets/keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = service_account.Credentials.from_service_account_file(
       SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID and range of a sample spreadsheet.
SPREADSHEET_ID = '1AO1-ySXp4Gk-Z0lqS6p-59xBLnAvKrf6lcqME3WyGvc'


service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
portfolio = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
    range="primary!A1:BB180").execute()


#write "new" data to spreadsheet
request = service.spreadsheets().values().update(spreadsheetId=SPREADSHEET_ID,
    range="primary!A100", valueInputOption="USER_ENTERED",
    body={"values": "new"}).execute()