car = {
    'brand': 'Toyota',
    'model': 'Prius',
    'year': 2050
}

car['year'] = 2040
# car.get('year') = 2040
car['city'] = 'Toyota'
print(car)

# update
tmp_dict = {
    'country': 'Japan',
    'prefecture': 'Aichi',
    'city': 'Toyota city'
}
car.update(tmp_dict)
print(car)
# modelの内容を取得して、元の辞書から削除
value = car.pop('model') 
print(car, value)

# 中身からcityだけ削除
del car['city']
print(car)

# 中身を全削除
car.clear()
print(car)