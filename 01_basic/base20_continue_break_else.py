# continue, break, else
for i in range(10):
    if i == 7:
        break
    if i % 3 == 0:
        continue
    print(i)
else: # 正常終了の場合だけ実行
    print('ループ終了')

print('-'*10)
num = 0
while num < 10:
    num += 1
    if num > 5:
        break
    if num % 2 == 0:
        continue
    print(num)
else:
    print('while終了')    
