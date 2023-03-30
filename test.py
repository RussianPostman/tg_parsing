from pprint import pprint
import gspread
from google.oauth2.service_account import Credentials
import numpy as np

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


def get_or_create_ws(
        name: str,
        heads: list[str],
        rows: int = 3,
        cols: int = 10
        ) -> gspread.Worksheet:
    """
    Создать гугл таблицу
    :name:
    :heads:
    :rows:
    :cols:
    """
    gc = get_creds()
    ss = gc.open_by_url(URL)
    try:
        new_worksheet = ss.worksheet(name)
    except StopIteration:
        ss.add_worksheet(name, rows, cols)
        new_worksheet = ss.worksheet(name)
    except gspread.exceptions.WorksheetNotFound:
        ss.add_worksheet(name, rows, cols)
        new_worksheet = ss.worksheet(name)
    
    return new_worksheet # .append_row(heads)


def write_stat(tg_slug: str, data: list[dict]):
    write_list = []

    heads = list(data[0].keys())
    worksheet = get_or_create_ws(tg_slug, heads)

    for dey in data:
        values = list(dey.values())
        write_list.append(values)

    array = np.array(write_list, dtype=object)
    pprint(array.tolist())
    worksheet.update(array.tolist())

a ={
    'ERR': 28.9,
    'advertising_reach': '',
    'change': 16,
    'date': '26 Март 2023',
    'reach': 12094,
    'subscribers': 41900
    },

write_stat()