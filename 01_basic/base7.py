# 文字列型

# fruit = 'apple' # ""
# print(fruit)
# print(type(fruit))

# print(fruit * 10)

# new_fruit = fruit + ' banana'
# print(new_fruit)

# # """
# fruits = """apple
# banana
# grape
# """
# print(fruits)

# fruit = 'banana'
# print(fruit[2])

# # encode, decode(bytes[]型の関数) => bytes[]
# byte_fruit = fruit.encode('utf-8')

# print(byte_fruit)
# print(type(byte_fruit))
# str_fruit = byte_fruit.decode('shift-jis')
# print(str_fruit)
# print(type(str_fruit))

# count関数

# msg = 'ABCDEABC'

# print(msg.count('ABCDEF'))

# # startswith endswith

# print(msg.startswith('ABCD'))
# print(msg.endswith('FABC'))

# #　strip, rstrip, lstrip

# print(msg.strip('ACB'))
# print(msg.rstrip('ACB'))
# print(msg.lstrip('ACB'))

# # upper, lower, swapcase, replace, capitalize

# msg = 'abcABC'
# msg_u = msg.upper()
# msg_l = msg.lower()
# msg_s = msg.swapcase()

# print(msg_u)
# print(msg_l)
# print(msg_s)

# msg = 'ABCDEABC'
# msg_r = msg.replace('ABC', 'abc', -1)

# msg = 'hELLO world'
# print(msg.capitalize())

# 文字列の一部取り出し、format関数、文字列から数値への変換、islower, isupper
msg = 'h '
print(msg.isupper())

msg = 'hello, my name is taro'

print(msg[0:10:2])
name = 'Hanako'
msg = f'my name is {name}' # 3.6
msg = f'my name is {name=}' # 3.8

print(msg)

msg = '12.21'
int_msg = float(msg)
print(int_msg)
print(type(int_msg))
# find, index, rfind, rindex

msg = 'ABCDEABC'
print(msg.rfind('ABDC'))
