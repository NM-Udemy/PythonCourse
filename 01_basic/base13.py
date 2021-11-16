# セット

set_a = {'a', 'b', 'c', 'd', 'a', 12}

print(set_a)
print('e' not in set_a)

print(12 in set_a)
print(len(set_a))

# add, remove, discard, pop, clear
set_a.add('e')
print(set_a)

set_a.remove('e')
print(set_a)
# set_a.remove('E')
set_a.discard(12)
print(set_a)
set_a.discard(12)

print(set_a)
val = set_a.pop()
print(val)
print(set_a)
set_a.clear()
print(set_a)
