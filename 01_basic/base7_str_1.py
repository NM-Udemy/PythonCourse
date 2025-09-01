# 文字列

fruit = 'Apple' # ""
print(fruit, type(fruit))
# print(dir(fruit))
print(fruit.lower()) # 小文字

print(fruit * 10) # 10回表示

number = '10'
print(number * 5)

new_fruit = fruit + ' banana'
print(new_fruit)

# """ '''
fruits = """apple
banana
grape"""
print(fruits)
fruits = "apple\nbanana\ngrape"
print(fruits)

fruit = 'banana'
print(fruit[-1]) # a

print("=" * 30)
# encode, decode (bytesへの変換)
message = 'こんにちは'
message_encoded = message.encode('shift-jis')
print(message_encoded.decode('shift-jis'))
print(type(message_encoded))
s = "Python programming"

print("=" * 50)
msg = "ABCDAEABC"
result = msg.count('ABCDEF')
print(result)

# startswith, endswith
print(msg.startswith('ABC'))
print(msg.endswith('ABC'))

# strip, rstrip lstrip
print(msg.strip('ACB')) # 両側から削る
print(msg.lstrip('ACB')) # 左側から削る
print(msg.rstrip('ACB')) # 右側から削る

print("   Hello   ".strip())
print("   Hello   ")

# upper, lower, swapcase, replace, capitalize
msg = 'abcABC'
msg_u = msg.upper()
msg_l = msg.lower()
msg_s = msg.swapcase()

print(msg_u, type(msg_u)) # ABCABC <class 'str'>
print(msg_l, type(msg_l)) # abcabc <class 'str'>
print(msg_s, type(msg_s)) # ABCabc <class 'str'>

msg = 'ABCDEABC'
msg_r = msg.replace('ABC', 'abc') # 文字列の変換
print(msg_r)

msg = 'hEllO World'
print(msg.capitalize()) # 一番頭だけ大文字に変換

# 文字列のチェック(isupper, islower, isdigit, isalpha)
name = 'TARO. マツダ'
age = '20'
print(name.islower()) # 全て小文字か
print(name.isupper()) # 全て大文字か
print(age.isdigit()) # 全て数値か
print(name.isalpha()) # 全てアルファベットか

# 検索
msg = 'ABCDEABC'
# 最初のインデックス見つからなければ-1
print(msg.find('DFE'))
print(msg.rfind('ABC'))

# 最初のインデックス見つからなければエラー
print(msg.index('DE'))
print(msg.rindex('ABC'))

# エラーなら、この後は実行されない
print('処理終了')

# 文字列スライシング
msg = '0123456789'
print(msg[0:6]) # 012345
print(msg[2:6]) # 2345
print(msg[0:6:2]) # 024
print(msg[3:]) # 3456789
print(msg[:5]) # 01234
print(msg[-5:]) # 56789
print(msg[:-5]) # 01234
print(msg[:-5:2]) # 024

sliced_msg = msg[0:8]
stepped_msg = sliced_msg[::3]
print(sliced_msg, stepped_msg)
