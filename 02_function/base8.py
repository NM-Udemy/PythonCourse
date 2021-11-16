# 高階関数

# def print_hello():
#     print('hello')

# def print_goodbye():
#     print('goodbye')

# var = ['AA', 'BB', print_hello, print_goodbye]
# var[2]()
# var[3]()

def print_world(msg):
    print('{} world'.format(msg))

def print_konnichiwa():
    print('こんにちは')

def print_hello(func):
    func('hello')
    return print_konnichiwa

var = print_hello(print_world)
var()