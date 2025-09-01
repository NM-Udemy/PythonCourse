# for, range
for i in range(10): # 0-9
    print(i)
    print('-' * 10)

for i in range(2, 20, 3): # 2-19 2つ飛ばし
    print(i)
    print('-' * 10)

list_a = list(range(2, 30))
print(list_a, type(list_a))

# 同じ処理を10回実行する。
# （_の場合は同じ処理を実行することを意味して、変数(_)は中で利用しない）
for _ in range(10): 
    print('A')
    # print(_)

samples = ['A', 'B', 'C', 'D']

for sample in samples: # samplesの中を取り出してsampleに格納
    print(sample)

human = {
    'name': 'taro', 'age': 20, 'gender': 'man'
}

for key in human: # Key一覧
    print(key, human[key])

for value in human.values(): # Value一覧
    print(value)

for key, value in human.items(): # => (key, value)
    print(key, value)