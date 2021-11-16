# date, timedelta

from datetime import date, timedelta

my_date = date(1000,1,1)
print(my_date < date.today()) # 古ければTrue, 新しければFalse

my_date = my_date.replace(year=2000, month=12)
print(my_date)

my_date_2 = date.today() - timedelta(days=10) # 10日前の日付
print(my_date_2)    

str_date = my_date_2.strftime('%Y/%m/%d')
print(str_date)
print(type(str_date))