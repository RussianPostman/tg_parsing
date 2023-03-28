from datetime import datetime
from pprint import pprint
import time
import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup
from bs4.element import Tag


def all_request(
    tg_slug: str = 'nashturist',
    page: int = 0
    ):
    """
    Эффективность рекламы (полный список)
    tg_slug: Без "@", только буквы
    """
    cookies = {
        '_tgstat_csrk': 'cd2a6ef1320042a5ef090f4b891af3bab8697ab37dfa0d648649503aaced57c2a%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22_tgstat_csrk%22%3Bi%3A1%3Bs%3A32%3A%22qLOWBnqBcSrZRlgXB27gERXQ_iVbwa_f%22%3B%7D',
        '_ym_uid': '1677178234702463738',
        '_ym_d': '1677178234',
        '_tgstat_userlang': 'a9c55d7d0ccdcd622b74ac6715f1b7fc3c850f3b8cb694e2ce0421457145cd18a%3A2%3A%7Bi%3A0%3Bs%3A16%3A%22_tgstat_userlang%22%3Bi%3A1%3Bs%3A2%3A%22ru%22%3B%7D',
        '_ym_isad': '2',
        '_gid': 'GA1.2.566002959.1679670097',
        '_ga': 'GA1.2.1070164511.1677178230',
        '_ga_ZEKJ7V8PH3': 'GS1.1.1679673225.43.0.1679673225.0.0.0',
    }

    headers = {
        'authority': 'tgstat.ru',
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': '_tgstat_csrk=cd2a6ef1320042a5ef090f4b891af3bab8697ab37dfa0d648649503aaced57c2a%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22_tgstat_csrk%22%3Bi%3A1%3Bs%3A32%3A%22qLOWBnqBcSrZRlgXB27gERXQ_iVbwa_f%22%3B%7D; _ym_uid=1677178234702463738; _ym_d=1677178234; _tgstat_userlang=a9c55d7d0ccdcd622b74ac6715f1b7fc3c850f3b8cb694e2ce0421457145cd18a%3A2%3A%7Bi%3A0%3Bs%3A16%3A%22_tgstat_userlang%22%3Bi%3A1%3Bs%3A2%3A%22ru%22%3B%7D; _ym_isad=2; _gid=GA1.2.566002959.1679670097; _ga=GA1.2.1070164511.1677178230; _ga_ZEKJ7V8PH3=GS1.1.1679673225.43.0.1679673225.0.0.0',
        'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjM0NTMyNzEiLCJhcCI6IjMyODAxMDQxNyIsImlkIjoiYTI4OGIxNzI3MGQ1MDgwMyIsInRyIjoiNWVjZDkxZGU3ZTkwZTMxY2NhZWYyMzI2Y2ViZGFmMDAiLCJ0aSI6MTY3OTY3MzIyNjQzMH19',
        'origin': 'https://tgstat.ru',
        'referer': f'https://tgstat.ru/channel/@{tg_slug}/stat/ads-efficiency',
        'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'traceparent': '00-5ecd91de7e90e31ccaef2326cebdaf00-a288b17270d50803-01',
        'tracestate': '3453271@nr=0-1-3453271-328010417-a288b17270d50803----1679673226430',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        'x-newrelic-id': 'VwICUlRUCRADVVhXDwYAU1I=',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        '_tgstat_csrk': 'lwg956ESO5i1y7R_Lp9aDFZFxDSPsWQR6_k1QgBBurnmRHKw43xK2taYxiV88z1UFHfzU8rjPEC0kGMgdyDl3w==',
        'page': str(page),
        'offset': '0',
    }

    response = requests.post(
        f'https://tgstat.ru/channel/@{tg_slug}/stat/ads-efficiency/list',
        cookies=cookies,
        headers=headers,
        data=data,
    )

    
    data = response.json()
    text = data['html']
    return BeautifulSoup(text, 'lxml')

def get_all_creative(response: BeautifulSoup) -> list[str]:
    out_list = [] 

    resp_list = response.find_all('a', 'popup_ajax btn btn-block btn-light px-2 py-1 font-14')
    for i in resp_list:
        out_list.append(i.get('href'))
    return(out_list)


    # with open("output1.html", "w", encoding="utf-8") as file:
    #     file.write(str(soup))




if __name__ == '__main__':
    print(get_all_creative(all_request()))
