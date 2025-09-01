# int,float → str変換
int_num = 12
str_num = str(int_num) # 数値→文字列
print(str_num, type(str_num))

float_num = -20.5
str_float = str(float_num)
print(str_float, type(str_float))

# str → int, float
msg = '12'
int_msg = int(msg)
float_msg = float(msg)

print(int_msg, type(int_msg))
print(float_msg, type(float_msg))

age = input('年齢を入力して: ')
age = int(age) # str → int
print('あなたの年齢 x 2 は: ', age * 2)