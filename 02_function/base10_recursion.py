def factorial(n):
    if n <= 1:
        return 1
    result = 1
    for i in range(1, n+1):
        result *= i # result = result * i(1, 2, 3, 4, 5)
    return result
    # if n <= 1:
    #     return 1
    # else:
    #     return n * factorial(n - 1)

print(factorial(5))
print(factorial(4))

# 直前の2つの数を足した値が次の数
# 0: 0, 1: 1, 2: 1, 3: 2, 4: 3, 5: 5
def fibonacci(n):
    first = 0
    second = 1
    for _ in range(n): # n回繰り返す
        next_number = first + second # 次の数は前の二つの合計
        first = second # 2番目が次の1番目に
        second = next_number # 計算した値が次の2番目に
    return first
    
    # if n < 2:
    #     return n
    # return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5)) # 5
