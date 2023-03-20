from pprint import pprint
import requests
from requests import Response



def qotes_chart(tg_slug: str) -> Response:
    """
    Динамика репостов и упоминаний
    tg_slug: Без "@", только буквы
    """
    cookies = {
        '_tgstat_csrk': 'cd2a6ef1320042a5ef090f4b891af3bab8697ab37dfa0d648649503aaced57c2a%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22_tgstat_csrk%22%3Bi%3A1%3Bs%3A32%3A%22qLOWBnqBcSrZRlgXB27gERXQ_iVbwa_f%22%3B%7D',
        '_ym_uid': '1677178234702463738',
        '_ym_d': '1677178234',
        '_tgstat_userlang': 'a9c55d7d0ccdcd622b74ac6715f1b7fc3c850f3b8cb694e2ce0421457145cd18a%3A2%3A%7Bi%3A0%3Bs%3A16%3A%22_tgstat_userlang%22%3Bi%3A1%3Bs%3A2%3A%22ru%22%3B%7D',
        '_gid': 'GA1.2.812962157.1678692837',
        '_ga_ZEKJ7V8PH3': 'GS1.1.1678783839.21.1.1678783844.0.0.0',
        '_ga': 'GA1.2.1070164511.1677178230',
        '_ym_isad': '2',
    }
    
    headers = {
        'authority': 'tgstat.ru',
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': '_tgstat_csrk=cd2a6ef1320042a5ef090f4b891af3bab8697ab37dfa0d648649503aaced57c2a%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22_tgstat_csrk%22%3Bi%3A1%3Bs%3A32%3A%22qLOWBnqBcSrZRlgXB27gERXQ_iVbwa_f%22%3B%7D; _ym_uid=1677178234702463738; _ym_d=1677178234; _tgstat_userlang=a9c55d7d0ccdcd622b74ac6715f1b7fc3c850f3b8cb694e2ce0421457145cd18a%3A2%3A%7Bi%3A0%3Bs%3A16%3A%22_tgstat_userlang%22%3Bi%3A1%3Bs%3A2%3A%22ru%22%3B%7D; _gid=GA1.2.812962157.1678692837; _ga_ZEKJ7V8PH3=GS1.1.1678783839.21.1.1678783844.0.0.0; _ga=GA1.2.1070164511.1677178230; _ym_isad=2',
        'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjM0NTMyNzEiLCJhcCI6IjMyODAxMDQxNyIsImlkIjoiY2M0NmM2YTEwZDA5ODJiMiIsInRyIjoiNDY5YWJmOWIxMGFlMDFmMDZkOGUwOTk1OWZmZWM5YjAiLCJ0aSI6MTY3ODc4NDE2MzIxMH19',
        'origin': 'https://tgstat.ru',
        'referer': f'https://tgstat.ru/channel/@{tg_slug}/stat/citation',
        'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'traceparent': '00-469abf9b10ae01f06d8e09959ffec9b0-cc46c6a10d0982b2-01',
        'tracestate': '3453271@nr=0-1-3453271-328010417-cc46c6a10d0982b2----1678784163210',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        'x-newrelic-id': 'VwICUlRUCRADVVhXDwYAU1I=',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        '_tgstat_csrk': 'IOt_R2A9AfPhroJH3re0h3Y_e2fQTx8S9j2RXIDBXvJRpzAQIlNwsYL98B2M29PfNA1MAJUdR0OpVMc-96ABlA==',
        'interval': 'total',
        'group': 'day',
        'startTs': '',
        'endTs': '',
    }

    response = requests.post(f'https://tgstat.ru/channel/@{tg_slug}/stat/quotes-chart', cookies=cookies, headers=headers, data=data)
    return response


if __name__ == '__main__':
    pprint(qotes_chart('rian_ru').json())