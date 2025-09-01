var = False

if var: # この中の式がTrueの場合実行される
    print('varがTrueの場合、この中は実行されます')

age = 0
print(bool(age))
if age: # 0以外はTrue
    print(f'ageの値: {age}')

msg = 'Hello'
if msg: # msgが空白でない場合はTrueに変換
    print(f'msg: {msg}')

# 数値は0, 0.0, 文字列 空文字, リスト、辞書、タプル、セットは空の場合
# => False

fruits = ['apple', 'lemon']
if fruits:
    print(f'fruitsの中身は: {fruits}')

age = 20
print(age >= 20)

if age >= 20: # ageが20以上の場合、True
    print('成人です')

# < <=, >, >=
# ==, !=
x = 5
if x == 5:
    print('xは5です')

if x != 10:
    print('xは10ではありません')

msg = 'Hello'
if msg == 'Hello':
    print('msgはHelloです')

if msg != 'Hi':
    print('msgはHiではありません')
