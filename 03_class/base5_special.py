class Vector:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f'x: {self.x}, y: {self.y}'
        
v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2 # v1.__add__(v2)
print(v3) # x: 4, y: 6 print(v3), str(v3)
v4 = str(v3) # x: 4, y: 6
print(v4)

print(Vector.__name__) # Vector
print(v3.__class__.__name__)

class Person:
    
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r})"# {self.name} -> str(self.name) -> 花子, {self.name!r} -> repr(self.name) -> '花子'
    
    def __str__(self):
        return f"{self.name}"
    
p = Person('花子')
print(p) # strをよぶ。ない場合はreprを呼ぶ
print(repr(p)) # Person(name='花子')
print(f'{p!r}') # Person(name='花子')
print(str(p)) # 花子

val = eval(repr(p)) # eval(Person(name='花子'))
print(val) # 花子

print('-'*100)
class Logger:
    
    def __init__(self, name):
        self.name = name
        self.logs = []
        
    def __call__(self, message): # 関数の呼び出し
        self.logs.append(message)
        print(f'{message}: を追加')
        return message    
    
    def __eq__(self, other): # ==の際に呼ばれる
        return self.name == other.name
    
    def __len__(self): # len関数で呼び出し
        return len(self.logs)
    
    def __bool__(self): # bool関数とifの条件で使用
        return len(self.logs) > 0
    
    def __hash__(self): # ハッシュ値に変換する際に利用
        print(self.name, hash(self.name))
        return hash(self.name)
    
app_log = Logger('アプリ')
error_log = Logger('エラー')

print(app_log == error_log) # app_log.__eq__(error_log)

app_log('アプリケーション開始')
app_log('ユーザーがログイン')
error_log('エラー発生')
print(len(app_log), len(error_log))
print(bool(app_log), bool(error_log))
if error_log:
    print('エラーがあります。')
    
loggers = {app_log: 'メインログ', error_log: 'エラーログ'}
print(loggers[app_log])
app_log('処理完了')