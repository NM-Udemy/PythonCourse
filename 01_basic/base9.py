# リスト
# list_a = [1,2,3,4]
# list_b = []

# print(list_a)
# print(list_a[-2])

# list_a = [1, [1,2,'apple'],3,'banana']

# print(list_a[1][2])
# print(list_a)
# list_a[1][2] = 'lemon'
# print(list_a)
# list_a.reverse()
# print(list_a)

# リスト関数

list_a = [1,2,3,4,5]
list_b = list_a[:3]
print(list_b)
print(list_a[0:5:2])

# append, extend, insert, clear
list_a.append('apple')
print(list_a)
list_a.extend(['banana', 'lemon'])
print(list_a)
list_a.insert(1, 'grape')
print(list_a)
# list_a.clear()
# print(list_a)

# remove, pop, count
list_a.remove(3)
print(list_a)
value = list_a.pop(1)
print(list_a)
print(value)
print(list_a.count('banana'))
print(list_a.index('apple'))

#copy
list_b = list_a.copy()
print(list_a)
list_b[0]='AAAAA'
print(list_a)

# sort reverse
list_a = ['banana', 'lemon', 'apple', 'grape']
print(list_a)
list_a = sorted(list_a)
list_a.reverse()
print(list_a)

