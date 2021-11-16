# Map関数

list_a = [1,2,3,4,5]
map_a = map(lambda x: x * 2, list_a)

for x in map_a:
    print(x)

man = {
    'name': 'Ichiro',
    'age': '18',
    'country': 'Japan'
}
map_man = map(lambda x: x + ',' + man.get(x), man)
for x in map_man:
    print(x)

def calcurate(x, y, z):
    if z == 'plus':
        return x + y
    elif z == 'minus':
        return x - y

map_sample = map(calcurate, range(5), [3,3,3,3,3], ['plus', 'minus', 'plus', 'minus', 'plus'])
for x in map_sample:
    print(x)