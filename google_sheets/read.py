import gspread
from google.oauth2.service_account import Credentials

URL = 'https://docs.google.com/spreadsheets/d/1FKaBTRApPnxXq9OoChi6pOj__3kgom5HLBzHu21H6mI/edit#gid=0'


def get_creds():
    scopes = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
    ]

    credentials = Credentials.from_service_account_file(
        'docs/creds.json',
        scopes=scopes
    )
    gc = gspread.authorize(credentials)
    return gc

def read():
    gc = get_creds()
    sht = gc.open_by_url(URL)
    ws = sht.worksheet('Ввод')
    channels = ws.col_values(1)
    print(channels)


if __name__ == '__main__':
    read()
