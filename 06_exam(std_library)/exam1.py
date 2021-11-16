# 1
from datetime import date, datetime
my_date = date.today() # 現在日付

#2
my_datetime = datetime(my_date.year, my_date.month, my_date.day, 15, 0, 0)

# print(my_date)
# print(my_datetime)
# 3
now_datetime = datetime.now()

# 4
print(now_datetime if now_datetime > my_datetime else my_datetime)

#5
import math
print(math.pow(16, 5))

# 6
from decimal import Decimal, ROUND_HALF_UP
print(Decimal('2') * Decimal('2') * Decimal(str(math.pi)))

# 7
print(Decimal(Decimal('10.586') / Decimal('12.124')).quantize(Decimal('0.00'), ROUND_HALF_UP))

# 8
import random

answer = random.randint(1,100)
while True:
    user_input = input('数値を入力してください: ')
    if int(user_input) == answer:
        print('正解です')
        break
    elif int(user_input) > answer:
        print('大きいです')
    else:
        print('小さいです')
