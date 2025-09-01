# ジェネレータ関数
def generator():
    yield 1
    yield 2
    yield 3
    
gen = generator() # ジェネレータオブジェクトを作成
print(type(gen)) # <class 'generator'>
# print(next(gen)) # 1
# print(next(gen)) # 2
# print(next(gen)) # 3
# print(next(gen)) # 1
for i in gen:
    print(i)

# ジェネレータ2
def print_num(max):
    print('ジェネレータ作成')
    for n in range(max):
        print(f'n: {n}')
        yield n

gen = print_num(10)
for i in gen:
    print(f'i: {i}')

# ジェネレータ3
import sys

N = 10**6

def get_list():
    for i in range(N):
        yield i
    # return [i for i in range(N)] # [0, 1,.. ~ 999999]

lst = get_list()
print(sys.getsizeof(lst), 'bytes')

# for i in lst:
#     # print(i)
print('-' * 100)

def number_generator():
    num = 0
    while True:
        try:
            value = yield num
            print(f"value: {value}")
            num += 1
        except ValueError as e:
            print(e)

gen = number_generator()
print(next(gen)) # 0
print(gen.send("Hello")) # 1
print(gen.send(10)) # 1
gen.throw(ValueError("Value Errorです"))
gen.close() # ジェネレータを終了

print(next(gen))
