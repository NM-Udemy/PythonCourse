# リスト
list_a = [1, 2, 3, 4]
list_b = [] # 空リスト

print(list_a, type(list_a))
print(list_a[2], type(list_a[2]))
print(list_a[-1], type(list_a[-1]))

list_a = [1, [1, 2, 'apple'], 3, 'banana']
print(list_a[1][2])
fruit = list_a[1][2]
print(fruit, type(fruit))

list_a[1][2] = 'lemon'
print(list_a)


list_a: list = [1, 2, 3, 4, 5]
list_b = list_a[:3]
print(list_b, type(list_b))
print(list_a[0:5:2])
list_b = list_a[2:]
print(list_b[::-1])

# append, insert, extend
list_a.append('apple')
print(list_a, type(list_a))

list_a.extend(['banana', 'lemon'])
print(list_a, type(list_a))

list_a.insert(1, 'grape')
print(list_a, type(list_a))

names = 'Taro Shiro Hanako'
# スペース区切りでリストに変換
name_list = names.split()
print(name_list, type(name_list))

names = 'Taro,Shiro,Hanako'
# カンマ区切りでリストに変換
name_list = names.split(',')
print(name_list, type(name_list))

# リストを文字列にする
fruits = ['apple', 'banana', 'lemon']
fruit_str = '-'.join(fruits)
print(fruit_str, type(fruit_str))

# remove, pop, count, index
list_a = [1, 2, 3, 4, 3]
list_a.remove(3) # 一番最初を削除
print(list_a, type(list_a))

list_a.pop(0) # インデックス0を削除
element = list_a.pop() # 最後の要素を削除
print(list_a)
print(element) # 3

fruits = ['apple', 'banana', 'lemon',]

print(fruits.count('banana')) # 数を数える1
print(fruits.index('lemon')) # 2

# sort reverse
list_a = ['banana', 'lemon', 'apple', 'grape']
# list_a.sort(reverse=True)
list_a = sorted(list_a)
print(list_a)


list_a.reverse() # 逆順にする
print(list_a)

my_list = [3, 6, 1, 2, 5, 4]
my_list.reverse()
print(my_list)

# 中身を完全削除
my_list.clear()
print(my_list)

import copy
# copy, deepcopy
list_a = [0, 1, [2,3], 3]
num_a = 12
# 片方を変更したら、もう片方も変更される
# list_b = list_a
# 片方を変更しても、ネストしてなければもう片方は変更されない
# list_b = list_a.copy()
# 片方を変更しても、もう片方は変更されない
list_b = copy.deepcopy(list_a)

num_b = num_a
list_b[2][0] = 100
print(list_a, list_b)
num_b = 24
print(num_a, num_b)
# リストの場合は=で片方を変更したら、もう片方も変更される
# 数値や文字列は=で片方を変更したら、もう片方は変更されない
