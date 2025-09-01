# タプル
fruits = ('apple', 'banana', 'lemon')

print(fruits, type(fruits), fruits[0])

# 要素の追加
fruits = fruits + ('grape',)
print(fruits)

list_fruits = list(fruits)
print(list_fruits, type(list_fruits))

tuple_fruits = tuple(list_fruits)
print(tuple_fruits, type(tuple_fruits))

# タプルのメソッド
print(fruits.count('apple')) # appleの数
print(fruits.index('banana')) # bananaの最初のインデックス

cordinates = (135, 35)
# longtitude = cordinates[0] # 経度
# latitude = cordinates[1] # 緯度

# アンパック
longtitude, latitude = cordinates
print(longtitude, type(longtitude))
print(latitude, type(latitude))

# 辞書のキー
countries = {cordinates: 'Japan'}
print(countries.get((135,35)))