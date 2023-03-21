from datetime import date, datetime, timedelta
from pprint import pprint

from dateutil.relativedelta import relativedelta

# six_months = date.today() + relativedelta(months=-4)
# print(six_months.strftime('%y:%m'))


def get_mentions(tg_slug: str):
    out_list = []
    tuday = date.today()
    for _ in range(3):
        print(tuday)
        year_minth = tuday.strftime('%y:%m').split(':')
        tuday += relativedelta(months=-1)
    print(tuday)


get_mentions('sdfs')