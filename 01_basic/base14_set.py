# セットの集合演算

s = {'a', 'b', 'c', 'd'}
t = {'c', 'd', 'e', 'f'}

#　和集合
u = s.union(t) # u = s | t
print(u, type(u))

# 積集合
inter = s.intersection(t) # inter = s & t
print(inter, type(inter))

# 差集合
diff = s.difference(t) # diff = s - t
print(diff, type(diff))

# 対象差
sym_diff = s.symmetric_difference(t) # sym_diff = s ^ t
print(sym_diff, type(sym_diff))

# subset, superset
s = {'apple', 'banana'}
t = {'apple', 'banana', 'lemon'}

print(s.issubset(t))
print(s.issuperset(t))
print(t.issubset(s))
print(t.issuperset(s))

print(s <= t) # sがtのサブセットか
print(t >= s) # tがsのスーパーセットか

# 重複削除
numbers = [1,2,2,2,3,4,5,2,6,6]
numbers = list(set(numbers))
print(numbers)

# 高速処理
large_list = set(range(10000000)) # 0-9999999までのリスト
test_number = 999999

import time
start = time.time()

# この処理に何秒かかったか計算
result = test_number in large_list
print(result)

end = time.time()
print('検索時間: ', end - start)
# 0.0000369