# enumerate, zip, while

fruits = ['grape', 'Pine', 'Apple']

for index, value in enumerate(fruits):
    print('index = {}'.format(index))
    print('value = {}'.format(value))

classA = ['Taro', 'Hanako', 'Jiro']
classB = ['Katsuo', 'Wakame', 'Taro']

for A, B in zip(classA, classB):
    print('classA student: {}'.format(A))
    print('classB student: {}'.format(B))

count = 0
while count < 10: # countが10より小さい場合は中の処理を実行
    print(count)
    count += 1

