count = 0 # グローバル変数

def increment():
    # count = 2 # ローカル変数
    global count # グローバルのcountを指す
    count = count + 2
    print("関数内: ", count)
    print("関数内(id): ", id(count))

increment()
print("関数外: ", count)
print("関数外(id): ", id(count))