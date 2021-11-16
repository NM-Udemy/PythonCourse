# セイウチ演算子

if (n := 10) > 5:
    print('5より大きい: {}'.format(n))

n = 0
while (n := n + 1) < 10:
    print(n)