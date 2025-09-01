def sub_gen():
    yield 'X'
    yield 'Y'
    return 'サブジェネレータの結果'

def main_gen():
    # s = sub_gen()
    # next(s)
    result = yield from sub_gen()
    # サブジェネレータから受け取った値: サブジェネレータの結果
    print(f"サブジェネレータから受け取った値: {result}")
    yield result
    
g = main_gen()
# print(next(g)) # X
# print(next(g)) # Y
# print(next(g)) # サブジェネレータの結果
# print(next(g)) # Error

