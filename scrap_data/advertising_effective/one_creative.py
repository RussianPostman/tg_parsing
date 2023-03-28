from bs4 import BeautifulSoup
import requests


def request(url: str):
    cookies = {
        '_tgstat_csrk': 'cd2a6ef1320042a5ef090f4b891af3bab8697ab37dfa0d648649503aaced57c2a%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22_tgstat_csrk%22%3Bi%3A1%3Bs%3A32%3A%22qLOWBnqBcSrZRlgXB27gERXQ_iVbwa_f%22%3B%7D',
        '_ym_uid': '1677178234702463738',
        '_ym_d': '1677178234',
        '_tgstat_userlang': 'a9c55d7d0ccdcd622b74ac6715f1b7fc3c850f3b8cb694e2ce0421457145cd18a%3A2%3A%7Bi%3A0%3Bs%3A16%3A%22_tgstat_userlang%22%3Bi%3A1%3Bs%3A2%3A%22ru%22%3B%7D',
        '_ym_isad': '2',
        '_gid': 'GA1.2.566002959.1679670097',
        '_gat_gtag_UA_104082833_1': '1',
        '_ga': 'GA1.1.1070164511.1677178230',
        '_ga_ZEKJ7V8PH3': 'GS1.1.1679676128.44.1.1679676315.0.0.0',
    }

    headers = {
        'authority': 'tgstat.ru',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        # 'cookie': '_tgstat_csrk=cd2a6ef1320042a5ef090f4b891af3bab8697ab37dfa0d648649503aaced57c2a%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22_tgstat_csrk%22%3Bi%3A1%3Bs%3A32%3A%22qLOWBnqBcSrZRlgXB27gERXQ_iVbwa_f%22%3B%7D; _ym_uid=1677178234702463738; _ym_d=1677178234; _tgstat_userlang=a9c55d7d0ccdcd622b74ac6715f1b7fc3c850f3b8cb694e2ce0421457145cd18a%3A2%3A%7Bi%3A0%3Bs%3A16%3A%22_tgstat_userlang%22%3Bi%3A1%3Bs%3A2%3A%22ru%22%3B%7D; _ym_isad=2; _gid=GA1.2.566002959.1679670097; _gat_gtag_UA_104082833_1=1; _ga=GA1.1.1070164511.1677178230; _ga_ZEKJ7V8PH3=GS1.1.1679676128.44.1.1679676315.0.0.0',
        'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    }

    return requests.get(f'https://tgstat.ru{url}', cookies=cookies, headers=headers)
    


def one_post_parser(url: str) -> list[str]:

    response = request(url)
    output_list = []
    

    soup = BeautifulSoup(response.text, 'html.parser')

    # with open(f"{url.replace('/', '_')}.html", "w", encoding="utf-8") as file:
    #     file.write(str(soup))
    
    table = soup.find('div', 'modal-content bg-transparent')

    img_list = ''
    pictures = table.find_all('img')
    for pictur in pictures:
        url: str = pictur.get('src')
        if url.startswith('https'):
            img_list += f'{url}\n '
    output_list.append(img_list)
    
    text = table.find('div', 'post-text')
    output_list.append(text.text)

    views = table.find_all(
        'a',
        'btn btn-light btn-rounded py-05 px-13 mr-1 popup_ajax font-12 font-sm-13'
        )
    output_list.append(views[0].text.strip())
    # shared_in_public
    output_list.append(views[1].text.strip())
    all_shared = table.find(
        'span',
        'btn btn-light btn-rounded py-05 px-13 mr-1 font-12 font-sm-13'
        )
    output_list.append(all_shared.text.strip())

    return output_list

if __name__ == '__main__':
    one_post_parser(request('/channel/@nashturist/14127'))
