from pprint import pprint
import time
import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup
from bs4.element import Tag


def main(tg_slug: str = 'nashturist', page: int = 0):
    """
    Получить упомянания
    tg_slug: Без "@", только буквы
    """
    session = HTMLSession()

    cookies = {
        '_tgstat_csrk': 'cd2a6ef1320042a5ef090f4b891af3bab8697ab37dfa0d648649503aaced57c2a%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22_tgstat_csrk%22%3Bi%3A1%3Bs%3A32%3A%22qLOWBnqBcSrZRlgXB27gERXQ_iVbwa_f%22%3B%7D',
        '_ym_uid': '1677178234702463738',
        '_ym_d': '1677178234',
        '_tgstat_userlang': 'a9c55d7d0ccdcd622b74ac6715f1b7fc3c850f3b8cb694e2ce0421457145cd18a%3A2%3A%7Bi%3A0%3Bs%3A16%3A%22_tgstat_userlang%22%3Bi%3A1%3Bs%3A2%3A%22ru%22%3B%7D',
        '_gid': 'GA1.2.812962157.1678692837',
        '_ym_isad': '2',
        '_ga_ZEKJ7V8PH3': 'GS1.1.1678884519.28.1.1678886491.0.0.0',
        '_ga': 'GA1.2.1070164511.1677178230',
    }

    headers = {
        'authority': 'tgstat.ru',
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': '_tgstat_csrk=cd2a6ef1320042a5ef090f4b891af3bab8697ab37dfa0d648649503aaced57c2a%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22_tgstat_csrk%22%3Bi%3A1%3Bs%3A32%3A%22qLOWBnqBcSrZRlgXB27gERXQ_iVbwa_f%22%3B%7D; _ym_uid=1677178234702463738; _ym_d=1677178234; _tgstat_userlang=a9c55d7d0ccdcd622b74ac6715f1b7fc3c850f3b8cb694e2ce0421457145cd18a%3A2%3A%7Bi%3A0%3Bs%3A16%3A%22_tgstat_userlang%22%3Bi%3A1%3Bs%3A2%3A%22ru%22%3B%7D; _gid=GA1.2.812962157.1678692837; _ym_isad=2; _ga_ZEKJ7V8PH3=GS1.1.1678884519.28.1.1678886491.0.0.0; _ga=GA1.2.1070164511.1677178230',
        'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjM0NTMyNzEiLCJhcCI6IjMyODAxMDQxNyIsImlkIjoiZjE3NjYxM2ZjYjE4YTk3NSIsInRyIjoiODYxMmQ1MmJlNDdiODM2M2ZmOTgwMzhjYzAyYTcwOTAiLCJ0aSI6MTY3ODg4NzIwNjg3Mn19',
        'origin': 'https://tgstat.ru',
        'referer': f'https://tgstat.ru/quotes/@{tg_slug}/list/m-2303',
        'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'traceparent': '00-8612d52be47b8363ff98038cc02a7090-f176613fcb18a975-01',
        'tracestate': '3453271@nr=0-1-3453271-328010417-f176613fcb18a975----1678887206872',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
        'x-newrelic-id': 'VwICUlRUCRADVVhXDwYAU1I=',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        '_tgstat_csrk': 'hWX3zMqA5VGTPPzh6BjXvDvKXwmeSteX1lt3e9lhBlD0KbibiO6UE_Bvjru6dLDkefhobtsYj8aJMiEZrgBZNg==',
        'page': str(page),
        'offset': '0',
    }

    response: requests.Response = session.post(f'https://tgstat.ru/quotes/@{tg_slug}/list-all/m-2302', cookies=cookies, headers=headers, data=data)


    data = response.json()
    text = data['html']
    soup = BeautifulSoup(text, 'lxml')

    text_list = soup.find_all('li')

    input_list = []

    for i in text_list:
        i: Tag    
        inside_dict = {}

        url = i.find('a', 'text-dark')
        tg_slug = url.get('href').split('/')[-2]
        tg_name =  url.text.strip()
        subscribers = i.find('b').text.strip()
        pre_action = i.find('div', 'col col-5 align-items-center text-right')
        action = pre_action.find('a').text.strip()
        date = pre_action.find('small').text.strip()

        inside_dict['tg_slug'] = tg_slug
        inside_dict['tg_name'] = tg_name
        inside_dict['subscribers'] = subscribers
        inside_dict['action'] = action
        inside_dict['date'] = date

        input_list.append(inside_dict)

    return input_list 


def cycle():
    for i in range(0, 10):
        data = main(page=i)
        pprint(data)
        if not data:
            return
        time.sleep(2)


if __name__ == '__main__':
    cycle()
