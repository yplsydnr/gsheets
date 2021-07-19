from oauth2client.service_account import ServiceAccountCredentials
import gspread
import finviz as fv
import yfinance as yf
import time

#time.sleep(1)

scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive.file',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('C:/authkeys/googlesheets/keys.json', scope)
client = gspread.authorize(creds)

portfolio = client.open('overall tracker').worksheet('code test primary')

#get all tickers
tickers = portfolio.col_values(1)
for t in tickers[1:]:
    print(t)