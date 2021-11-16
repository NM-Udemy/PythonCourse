# 辞書の関数

car = {'brand': 'Toyota', 'model': 'Prius', 'year': 2015}

tmp_dict = {'country': 'Japan', 'prefecture': 'Aichi', 'model': 'カローラ'}
car.update(tmp_dict)
print(car)
car['city'] = 'Toyota-shi'
car['year'] = 2017
print(car)

value = car.popitem()
print(car)
print(value)

value = car.pop('model')
print(car)
print(value)

car.clear()
print(car)
del car
print(car)
