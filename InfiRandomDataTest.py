import gspread, datetime, time, random
from oauth2client.service_account import ServiceAccountCredentials

creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', ['https://spreadsheets.google.com/feeds'])
client = gspread.authorize(creds)

sheet = client.open("Temperature Sensing").sheet1

def updatesheet(temp1, temp2):
    values = [datetime.datetime.now(), temp1, temp2]
    sheet.append_row(values)

while True:
    probe1 = random.randint(0, 100)
    probe2 = random.randint(0, 100)
    updatesheet(probe1, probe2)
    print("Published succesfully.")
    time.sleep(15)
