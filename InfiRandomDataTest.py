import gspread, datetime, time
from oauth2client.service_account import ServiceAccountCredentials
from random import randint

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("TemperatureSensing").sheet1

def updatesheet():
    temp1 = randint(0, 100)
    temp2 = randint(0, 100)
    values = [datetime.datetime.now(), temp1, temp2]

    sheet.append_row(values)

while True:
    updatesheet()
    time.sleep(15)
