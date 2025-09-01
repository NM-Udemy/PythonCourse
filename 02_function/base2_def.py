# デフォルト、可変長引数、複数の戻り値
def sample(arg1=300, arg2=100):
    print(arg1, arg2)

sample(100, 200)
sample(50)

def sample_2(arg1, *arg2): # arg2にはタプル
    print(f'arg1: {arg1}, arg2: {arg2}')
    print(arg2[1])
    print(type(arg2))

sample_2(1, 2, 3, 4, 5)
list_a = [2,3,4,5]

def sample_3(arg1, **arg2):
    print(f'arg1: {arg1}, arg2: {arg2}')
    print(type(arg2))

sample_3(3, name='Taro', age=20)

man = {'name': 'Jiro', 'age': 30}
sample_3(3, **man)

def sample_4(arg1, *arg2, **arg3):
    print(arg1, arg2, arg3)

sample_4(1, 2, 3, 4, 5, name='Taro', age=20)

def get_person():
    name = '田中'
    age = 30
    city = '東京'
    return name, age, city
    
result = get_person()
print(f'result: {result}, {type(result)}')
name, age, city = get_person()

print(name, age, city) # 田中 30 東京

# 部分的なあんパック
def get_results():
    return 90, 85, 78, 92, 88

first, *others, last = get_results()
print(first, others, last)
print(type(first), type(others), type(last))
