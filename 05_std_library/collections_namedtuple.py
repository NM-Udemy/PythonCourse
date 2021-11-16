from collections import namedtuple

S = namedtuple('Student', ['name', 'age', 'grade'])
taro = S('Taro', 12, 3)
print(taro.name)
print(taro[0])
taro = taro._replace(name='Jiro')
print(taro.name)
print(taro._asdict()) # 辞書
print(taro._fields) # キー一覧
dict_b = {'name': 'John', 'age': 20, 'grade': 2}
john = S(**dict_b)
print(john)

paul = S._make(['Paul', 15, 2])
print(paul)