from datetime import date
import time
import csv
from pprint import pprint
from dateutil.relativedelta import relativedelta

from openpyxl import Workbook
from openpyxl.worksheet.worksheet import Worksheet

from scrap_data import post_reach, qotes_chart, advertising_reach, \
    err_chart, subscribers_chart
from scrap_data.attracting_subscribers import mentions
from scrap_data.advertising_effective import one_post_parser
from google_sheets import read, write


def get_mentions(tg_slug: str):
    out_list = []
    tuday = date.today()
    for _ in range(4):
        year_minth = tuday.strftime('%y:%m').split(':')
        out_list += mentions(tg_slug, year_minth[0], year_minth[1])
        tuday += relativedelta(months=-1)
    return out_list


def synchronization(
        inlist: list[dict],
        main_list: list[dict],
        value: int
        ):
    for i in inlist:
        for day in main_list:
            if day.get('date') == i.get('tt'):
                day[value] = i.get('y')


def custom_sync(
        inlist: list[dict],
        main_list: list[dict],
        value: str
        ):
    for day in main_list:
        day[value] = ''
    for i in inlist:
        for day in main_list:
            if day.get('date') == i.get('date'):
                text = (
                    f'| {i.get("tg_name")} - {i.get("tg_slug")} {i.get("subscribers")} '
                    + f' подпистчиков {i.get("action")}'
                    + f'{i.get("date")} в {i.get("time")}'
                    + f' ссылка: \n{i.get("post_url")} |\n'
                    )
                if dau_value := day.get(value):
                    day[value] = dau_value + text
                else:
                    day[value] = text



def main_csv(tg_slug: str = 'nashturist'):

    subscribers_с = subscribers_chart(tg_slug)[-101:-1]
    post_r = post_reach(tg_slug)[-101:-1]
    advertising_r = advertising_reach(tg_slug)[-101:-1]
    err = err_chart(tg_slug)[-101:-1]
    _mentions = get_mentions(tg_slug)

    w_list = []
    
    yesterday = None
    count = 0
    
    # тут формируется базовый словарь на основе графика подписчиков
    for day in subscribers_с:

        day: dict
        w_dict = {}

        if yesterday:
            w_dict['change'] = day.get('y') - yesterday
            yesterday = day.get('y')
        else:
            w_dict['change'] = 0
            yesterday = day.get('y')

        w_dict['date'] = day.get('tt')
        w_dict['subscribers'] = day.get('y')
        w_list.append(w_dict)
        count += 1
    
    synchronization(post_r, w_list, 'reach')
    synchronization(err, w_list, 'ERR')
    synchronization(advertising_r, w_list, 'advertising_reach')
    custom_sync(_mentions, w_list, 'mentions')

    return w_list

def file_write(tg_slug, w_list):
    columns_names = [
        'date', 'subscribers', 'change', 'reach', 'ERR', 'advertising_reach',
        'mentions']
    with open(tg_slug + '.csv', mode="w", encoding='utf-8') as w_file:
        file_writer = csv.DictWriter(
            w_file, delimiter = ",", lineterminator="\r", fieldnames=columns_names
            )
        file_writer.writeheader()

        for i in list(reversed(w_list)):
            file_writer.writerow(i)


def main_xlsx():
    data = one_post_parser('/channel/@nashturist/14127')
    wb = Workbook()
    ws: Worksheet = wb.active
    ws.append(data)
    wb.save("TreeData.xlsx")


# def main_gs():



if __name__ == '__main__':
    pprint(main_csv('nashturist'))
