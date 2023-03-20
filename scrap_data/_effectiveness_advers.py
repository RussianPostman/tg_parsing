from pprint import pprint
import requests
import json
from pprint import pprint
from requests_html import HTMLSession


session = HTMLSession()

cookies = {
    '_tgstat_csrk': 'cd2a6ef1320042a5ef090f4b891af3bab8697ab37dfa0d648649503aaced57c2a%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22_tgstat_csrk%22%3Bi%3A1%3Bs%3A32%3A%22qLOWBnqBcSrZRlgXB27gERXQ_iVbwa_f%22%3B%7D',
    '_ym_uid': '1677178234702463738',
    '_ym_d': '1677178234',
    '_tgstat_userlang': 'a9c55d7d0ccdcd622b74ac6715f1b7fc3c850f3b8cb694e2ce0421457145cd18a%3A2%3A%7Bi%3A0%3Bs%3A16%3A%22_tgstat_userlang%22%3Bi%3A1%3Bs%3A2%3A%22ru%22%3B%7D',
    '_gid': 'GA1.2.812962157.1678692837',
    '_ym_isad': '2',
    '_gat_gtag_UA_104082833_1': '1',
    '_ga': 'GA1.1.1070164511.1677178230',
    '_ga_ZEKJ7V8PH3': 'GS1.1.1678799279.25.1.1678802417.0.0.0',
}

headers = {
    'authority': 'tgstat.ru',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': '_tgstat_csrk=cd2a6ef1320042a5ef090f4b891af3bab8697ab37dfa0d648649503aaced57c2a%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22_tgstat_csrk%22%3Bi%3A1%3Bs%3A32%3A%22qLOWBnqBcSrZRlgXB27gERXQ_iVbwa_f%22%3B%7D; _ym_uid=1677178234702463738; _ym_d=1677178234; _tgstat_userlang=a9c55d7d0ccdcd622b74ac6715f1b7fc3c850f3b8cb694e2ce0421457145cd18a%3A2%3A%7Bi%3A0%3Bs%3A16%3A%22_tgstat_userlang%22%3Bi%3A1%3Bs%3A2%3A%22ru%22%3B%7D; _gid=GA1.2.812962157.1678692837; _ym_isad=2; _gat_gtag_UA_104082833_1=1; _ga=GA1.1.1070164511.1677178230; _ga_ZEKJ7V8PH3=GS1.1.1678799279.25.1.1678802417.0.0.0',
    'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjM0NTMyNzEiLCJhcCI6IjMyODAxMDQxNyIsImlkIjoiZjQ3MWMwZmRjNmE2ZThhYiIsInRyIjoiNjM0NjY1MWI1ZTkxNjk3YzhiZTVkNjNkZTczMDc4ODAiLCJ0aSI6MTY3ODgwMjQyMjkxMH19',
    'origin': 'https://tgstat.ru',
    'referer': 'https://tgstat.ru/channel/@rian_ru/stat/ads-efficiency',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'traceparent': '00-6346651b5e91697c8be5d63de7307880-f471c0fdc6a6e8ab-01',
    'tracestate': '3453271@nr=0-1-3453271-328010417-f471c0fdc6a6e8ab----1678802422910',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'x-newrelic-id': 'VwICUlRUCRADVVhXDwYAU1I=',
    'x-requested-with': 'XMLHttpRequest',
}

data = {
    '_tgstat_csrk': 'MMEIdZtG9WM0YxslC2WDewptm9AIEE4Tm5i3vJ-5qLRBjUci2SiEIVcwaX9ZCeQjSF-st01CFkLE8eHe6Nj30g==',
    'hideCross': '1',
    'page': '0',
    'offset': '0',
}

response = session.post(
    'https://tgstat.ru/channel/@rian_ru/stat/ads-efficiency/list',
    cookies=cookies,
    headers=headers,
    data=data,
)


list_dt = []

sel = 'body'
table = response.html.find(sel)[0]

for i in table.find('li'):
    text = i.text.split('\n')
    print(text)
    list_dt.append(text)