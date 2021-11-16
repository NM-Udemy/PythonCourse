#if and or not

# msg = 'yellow'
# if msg == 'blue':
#     print('すすめ')
# elif msg == 'red':
#     print('止まれ')
# else:
#     print('それ以外の処理')

age = 60
if age < 20:
    print('20未満')
elif age <= 40: # 20以上で実行される
    print('20以上、40以下です')
elif age >= 60:
    print('60以上です')
else:
    print('それ以外の年齢')

#  and or not

gender = 'woman'
age = 40
if gender == 'man' or age < 20:
    print('男性もしくは20未満です')

if gender != 'man':
    print('男ではない')