# 辞書型
car = {
    'brand': 'Toyota',
    'model': 'Prius',
    'year': 2050,
}

print(car['brand']) # Toyota
# print(car['manufacturer']) # KeyError
brand = car.get('manufacturer') # エラーがない場合はNone
print(brand, type(brand))

brand = car.get('manufacturer', "不明")
print(brand, type(brand))

car = dict(
    brand='Suzuki', model='ジムニー', year=2500
)
print(car, type(car))