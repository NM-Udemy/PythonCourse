# セット型
set_a = {'a', 'b', 'c', 'd', 'a', 12}

print(set_a, type(set_a))

# add, update, remove, discard, pop, clear
set_a.add('e') # 要素一つ追加
print(set_a) 
set_a.update(['f', 'g']) # 複数要素を追加
print(set_a)

set_a.remove('e') # eを削除、存在しない場合エラー
print(set_a)

set_a.discard('f') # fを削除、存在しない場合もエラーにならない
print(set_a)

# 要素を取り出す
val = set_a.pop()
print(val)
print(set_a)

set_a.clear()
print(set_a)

set_a = set([1,2,3,4])
print(1 in set_a) # set_aに1があるかどうか
print(2 not in set_a) # set_aに1がないかどうか
print(len(set_a)) # set_aの要素数
