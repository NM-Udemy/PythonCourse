# elif, else, and, or, not

color = 'blue'

if color == 'blue':
    print('進め')
elif color == 'red':
    print('止まれ')
elif color == 'yellow':
    print('気をつけろ')
else:
    print('それ以外')

age = 60
if age < 20:
    print('20未満')
elif age <= 40:
    print('20以上で40以下')
elif age >= 60:
    print('60以上')
else:
    print('40より大きく、60より小さい')

gender = 'woman'
age = 40

if gender == 'man' or age <= 20:
    print('男性もしくは20未満')

if gender == 'woman' and age > 20:
    print('女性で20より大きい')

# if gender != 'man':
if not gender == 'man':
    print('男性ではない')

# is, is not(同じオブジェクトか→同じメモリ上にあるもの)
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(id(a))
print(id(b))
print(id(c))

print(a == b) # True
print(a == c) # True

print(a is b) # False
print(a is c) # True

print(a is not b) # True
print(a is not c) # False

if a is b:
    print('aとbは同じオブジェクトです。')
    
a = None # NoneTypeクラスのオブジェクト。Noneという値しかない

# a == Noneという書き方もできるが、慣習的で効率的な書き方
if a is None:
    print('aはNoneです。')
    
# isinstance
age = 25
name = "田中"
score = [80, 90]
print(isinstance(age, int))
print(isinstance(name, str))
print(isinstance(score, list))

if isinstance(age, int) and age > 20:
    pass

if 0 <= age <= 60:
    print('ageは0以上、60以下')
    
# 3項演算子
status = '成人' if age >= 20 else '未成年'

print(status)

# in, not int
fruits = ['りんご', 'バナナ', 'オレンジ']
print('りんご' in fruits)
print('ぶどう' not in fruits)

car = {'brand': 'トヨタ', 'model': 'Prius'}

if 'brand' in car:
    print(car['brand'])
