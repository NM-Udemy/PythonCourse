
# a = print

# a('Hello')
# print(id(a))
# print(id(print))

import time

def after(seconds, func):
    time.sleep(seconds)
    func()
    
def greeting(msg):
    def inner():
        print(msg)
    return inner

greet = greeting('Hello World')
# after(2, greet)

def process_number(number, even_callback, odd_callback):
    if number % 2 == 0:
        even_callback(number)
    else:
        odd_callback(number)

def handle_even(number):
    print(f"{number}は偶数です。")

def handle_odd(number):
    print(f"{number}は奇数です。")
    
process_number(4, handle_even, handle_odd)
process_number(7, handle_even, handle_odd)
