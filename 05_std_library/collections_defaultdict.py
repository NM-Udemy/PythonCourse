from collections import defaultdict

d_dict = defaultdict(lambda: 1)
print(d_dict['A'])
print(type(d_dict['A']))
d_dict['A'] = 100
print(d_dict['A'])
d_dict['B'] += 1
print(d_dict)
print(d_dict.keys(), d_dict.values())