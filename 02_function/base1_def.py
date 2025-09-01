# 関数
def print_hello(): # <class 'function'>
    print('Hello World')
    
print(type(print_hello))
print(id(print_hello))

abc = print_hello
print(id(abc))
abc()

def max_num(a, b):
    print(f'a = {a}, b = {b}')
    if a > b:
        return a # 呼び出し元に戻す値
    else:
        return b

c = max_num(10, 200)
d = max_num(30, 20)
print(c)
print(f'd: {d}')

e = max_num(b=19, a=21)
print(e)

num = {
    'a': 20,
    'b': 30
}

print(max_num(**num)) # a=20, b=30
