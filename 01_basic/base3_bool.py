# True, False
x = True
y = False
print(x, y)
print(type(x)) # type <class 'bool'>

# if　での使用
is_admin = True
if is_admin: # is_adminがTrueのとき実行
    print('管理者画面にアクセスできます')
else:
    print('アクセス権がありません')

name = input('名前: ')
if name == "admin":
    print('管理者画面にアクセスできます')
print(name == "admin") # name == "admin" → True or False

# bool関数
print(bool(0)) # False: 0はFalse
print(bool(1)) # True: 0以外はTrue
print(bool("")) # False: 空文字False
print(bool("Hello")) # True: 空文字以外はTrue

age = 25
income = 50000
if age >= 18 and income >= 30000: # 両方を満たす
    print("ローン承認")

# OR
weather = "雨"
temperature = 35
if weather == "雨" or temperature > 30: # どちらかを満たす
    print("外出しない")
