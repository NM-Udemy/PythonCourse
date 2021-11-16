# Counter
from collections import Counter
from random import randint, seed

seed(1)
list_a = [randint(0,10) for _ in range(100)]

cnt = Counter(list_a)
# print(sorted(list_a))
# print(cnt)

print(cnt[0]) #0の数
print(list(cnt.elements())) # リスト
print(cnt.most_common()) # リスト+タプル
cnt.subtract({7:20, 6:-5}) # 値を引く
print(cnt.most_common())
