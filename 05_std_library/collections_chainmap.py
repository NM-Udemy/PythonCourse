# ChainMap

from collections import ChainMap
c_map = ChainMap({'key1': 1, 'key2': 2}, {'key3': 3, 'key2': 4})

print(c_map['key1']) # 1
print(c_map['key2']) # 2
print(c_map['key3']) # 3

c_map['key4'] = 4
print(c_map)
c_map = c_map.new_child({'key5': 5, 'key1': 100})
print(c_map)
print(c_map['key5'])
print(c_map['key1'])
print(list(c_map.keys()))
print(list(c_map.values()))