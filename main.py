import time
import csv
from pprint import pprint

from scrap_data import post_reach, qotes_chart, advertising_reach, \
    err_chart, subscribers_chart



def synchronization(
        inlist: list[dict],
        main_list: list[dict],
        value: int):
    for i in inlist:
        for day in main_list:
            if day.get('date') == i.get('tt'):
                day[value] = i.get('y')



def main_csv(tg_slug: str = 'nashturist'):

    subscribers_с = subscribers_chart(tg_slug)[-101:-1]
    post_r = post_reach(tg_slug)[-101:-1]
    time.sleep(2)
    advertising_r = advertising_reach(tg_slug)[-101:-1]
    err = err_chart(tg_slug)[-101:-1]

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
    
    # # добавление поля "охват"
    # for post in post_r:
    #     for day in w_list:
    #         if day.get('date') == post.get('tt'):
    #             day['reach'] = post.get('y')
    
    # # добавление поля "вовлеченность по просмотрам"
    # for post in err:
    #     for day in w_list:
    #         if day.get('date') == post.get('tt'):
    #             day['ERR'] = post.get('y')
    
    # # добавление поля "рекламный охват"
    # for post in advertising_r:
    #     for day in w_list:
    #         if day.get('date') == post.get('tt'):
    #             day['advertising_reach'] = post.get('y')

    

    # запись в файл
    columns_names = [
        'date', 'subscribers', 'change', 'reach', 'ERR', 'advertising_reach',
        ]
    with open(tg_slug + '.csv', mode="w", encoding='utf-8') as w_file:
        file_writer = csv.DictWriter(
            w_file, delimiter = ",", lineterminator="\r", fieldnames=columns_names
            )
        file_writer.writeheader()

        for i in list(reversed(w_list)):
            file_writer.writerow(i)


if __name__ == '__main__':
    main_csv('nashturist')