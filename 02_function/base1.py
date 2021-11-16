# 関数

def print_hello():
    print('Hello World')

print_hello()

def num_max(a: int, b: int):
    print('a = {}, b = {}'.format(a, b))
    if a > b:
        return a
    else:
        return b
print(num_max(b=100,a=20))
print(num_max())