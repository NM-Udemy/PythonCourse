import time

def decorator_func(func):
    def wrap():
        # print('こんにちは')
        start_time = time.time()
        func()
        func()
        func()
        # print('さようなら')
        end_time = time.time()
        print(end_time - start_time)
    return wrap

# a = decorator_func(print) # wrap
# a()
@decorator_func
def introduce():
    print('私は田中です。')
# introduce = decorator_func(intruduce)
# introduce()

def log_calls(func):
    def wrapper(*args, **kwargs):
        print(args, kwargs) # (2, 3) {}
        result = func(*args, **kwargs)
        print(f"完了: {result}")
        return result
    return wrapper

@log_calls
def add(a, b):
    return a + b

# print(add(2, 3)) # 5

def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(args, kwargs)
            for i in range(times):
                print(f"{i+1}回目:")
                func(*args, **kwargs) # say_hello("太郎") = say_hello(name="太郎")
        return wrapper
    return decorator

@repeat(5) # say_hello = repeat(3)(say_hello)
def say_hello(name):
    print(f"こんにちは、{name}さん！")

# say_hello(name="太郎")
