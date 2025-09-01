# 1~100
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(f'{i}は15の倍数')
    elif i % 3 == 0:
        print(f'{i}は3の倍数')
    elif i % 5 == 0:
        print(f'{i}は5の倍数')
    else:
        print(i)
