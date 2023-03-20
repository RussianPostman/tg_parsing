from pprint import pprint
from requests_html import HTMLSession


session = HTMLSession()

def main():
    main_dict = {}

    url = 'https://tgstat.ru/channel/@oper_goblin/stat/subscribers-days'
    payload = {
        "_tgstat_csrk": "PcZ5XqidJc0femy4WEOcfdm5nQ6OjcrpH-Wx19WYlq9MijYJ6vNUj3wpHuIKL_slm4uqacvfkrhAjOe1ovnJyQ==",
        "page": "1",
        "offset": "0"
    }
    headers = {
        # 'Cookie': '_tgstat_csrk=282384d25724d6b5e879be6164c5091d9859462ee2ad1629f38bd91e764e5480a%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22_tgstat_csrk%22%3Bi%3A1%3Bs%3A32%3A%22H-yTydTlsrkshPeLL1zICa8Tn765Jp5G%22%3B%7D',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
        'Accept': '*/*',
        # 'Accept-Encoding': 'br',
        'content-type': 'application/json',
        'Connection': 'keep-alive',
    }

    request = session.post(url=url, data=payload, headers=headers)
    list_dt = []

    sel = 'body > div > div > div.content.p-0.col > div.container-fluid.px-2.px-md-3 > div.modal.modal-background.m-0.modal-preopened > div > div'
    table = request.html.find(sel)[0]

    for i in table.find('li'):
        text = i.text.split('\n')
        print(text)
        list_dt.append(text)
    
    for i in list_dt:
        inside_dict = {}
        inside_dict['deta'] = i[0]
        inside_dict['subscribers'] = i[1]
        inside_dict['change'] = i[2]

        main_dict[inside_dict.get('deta')] = inside_dict
    
    # for one_dey in list_dt:
    #     one_dey.split('/')

    pprint(main_dict)
    return main_dict


if __name__ == '__main__':
    main()