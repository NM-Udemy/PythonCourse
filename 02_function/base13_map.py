list_a = [1, 2, 3, 4, 5]
map_a = map(lambda x: x * 2, list_a)
map_a = (x * 2 for x in list_a)

print(type(map_a))
print(list(map_a))

man = {
    'name': 'Ichiro',
    'age': '18',
    'country': 'Japan'
}
# map_man = map(lambda x: x + ',' + man.get(x), man)
map_man = (x + ',' + man.get(x, '') for x in man)
print(list(map_man))

def calcurate(x, y, z):
    if z == 'plus':
        return x + y
    elif z == 'minus':
        return x - y

# print(calcurate(2,3,'plus'))
map_sample = map(
    calcurate, range(5), [3,3,3,3,3],
    ['plus', 'minus', 'plus', 'minus', 'plus']
)
map_sample = (
    calcurate(x, y, z)
    for x, y, z in zip(
        range(5), [3,3,3,3,3],
    ['plus', 'minus', 'plus', 'minus', 'plus']
    )
)
print(list(map_sample))