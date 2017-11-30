import csv

import gspread
from oauth2client.service_account import ServiceAccountCredentials


# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("BoardGames").sheet1

# Extract and print all of the values
board_games = []
with open('./data/board_games.csv', 'r') as f:
    reader = csv.reader(f, delimiter=';')

    for row in reader:
        board_games.append(row)

for row_num, row in enumerate(board_games):
    for column, item in enumerate(row):
        print(item)
        sheet.update_cell(row_num + 1, column + 1, item)
