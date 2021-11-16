# datetime, time

from datetime import datetime, timedelta, timezone

my_date = datetime(2019,11,11,18,15,25) #2019/11/11 18:15:25
print(my_date, type(my_date))
now_date = datetime.now()
now_date = datetime.utcnow()
print(now_date)
print(now_date.year, now_date.month, now_date.microsecond)
time_str = '2019/12/12 16:40'
dt = datetime.strptime(time_str, '%Y/%m/%d %H:%M')
print(type(dt), dt)
date_str = datetime.now().strftime('%Y %m %d')
print(date_str, type(date_str))
print(datetime.now() - timedelta(days=10))
my_date = datetime(2019,11,11,18,15,25)

local_date = my_date.replace(tzinfo=timezone.utc).astimezone()
print(local_date)

from datetime import date

date_obj = date.today()
to_datetime = datetime(date_obj.year, date_obj.month, date_obj.day) # date => datetime
print(to_datetime)

date_obj = datetime.now().date()
print(date_obj)

import time

for x in range(10):
    print(x)
    time.sleep(1)