# OrderedDict
from collections import OrderedDict

o_dict = OrderedDict([('A', 100), ('B', 200)])
print(o_dict['A']) # 普通の辞書型は3.7以降、順番を保持する
o_dict.move_to_end('B', False)
print(o_dict)

print({'A': 100, 'B': 200} == {'B': 200, 'A': 100})
print(OrderedDict([('A', 100), ('B', 200)]) == OrderedDict([('B', 200), ('A', 100)]))
