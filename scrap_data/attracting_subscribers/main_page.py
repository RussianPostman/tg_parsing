from pprint import pprint
import time
import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup
from bs4.element import Tag

from mentions import mentions 


session = HTMLSession()

months = {
    'Декабрь': '12',
    'Ноябрь': '11',
    'Октябрь': '10',
    'Сентябрь': '9',
    'Август': '8',
    'Июль': '7',
    'Июнь': '6',
    'Май': '5',
    'Апрель': '4',
    'Март': '3',
    'Февраль': '2',
    'Январь': '1',
}

def main(tg_slug: str = 'nashturist'):
    response: requests.Response = session.get(url=f'https://tgstat.ru/channel/@{tg_slug}/stat/members-attraction')
    soup = BeautifulSoup(response.text, 'html.parser')
    output_list = []

    data_list = soup.find_all('li', 'list-group-item list-group-item-action list-group-item-body py-1')

    for row in data_list:
        out_dict = {}
        row: Tag
        deta = row.find('div', 'col-4 col-sm 2 text-left text-truncate').text
        deta = " ".join(deta.split())
        mentions = row.find('div', 'col-8 col-sm-3 text-left text-truncate').text
        mentions = " ".join(mentions.split())
        coverage = row.find_all('div', 'col-6 col-sm-3 d-flex align-items-center')
        sumar_coverage = " ".join(coverage[0].text.split())
        new_subscribers = " ".join(coverage[1].text.split())

        out_dict['deta'] = deta
        out_dict['mentions'] = mentions
        out_dict['sumar_coverage'] = sumar_coverage
        out_dict['new_subscribers'] = new_subscribers

        output_list.append(out_dict)

    return output_list



if __name__ == '__main__':
    pprint(main('nashturist'))
