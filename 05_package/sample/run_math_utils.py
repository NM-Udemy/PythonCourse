from mypackage import add, multiply
# # print(mypackage.math_utils.add(1, 3))

# print(add(2, 3))
# print(multiply(10, 4))
# print(__name__) # __main__

def main():
    print('モジュール使用例')
    result1 = add(10, 20)
    result2 = multiply(50, 5)
    print(result1, result2)

if __name__ == '__main__':
    main()