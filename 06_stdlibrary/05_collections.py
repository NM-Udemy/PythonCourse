from collections import Counter, defaultdict, namedtuple


# Counterの使用
text = 'hello world'
char_count = Counter(text)
print(char_count)
print(char_count.most_common(2))

fruits = [
    'apple', 'banana', 'apple',
    'cherry', 'banana', 'apple'
]
fruit_count = Counter(fruits)
print(fruit_count)
print(fruit_count['apple'])


# defaultdict

dd_int = defaultdict(int) # int: 0
print(dd_int)
dd_int['new_key'] += 1
print(dd_int)
print(dd_int['new_key_2'])
print(dd_int)

fruit_count = defaultdict(int)
for fruit in fruits:
    fruit_count[fruit] += 1
print(fruit_count)

students = [
    ('田中', '数学'),
    ('佐藤', '英語'),
    ('山田', '数学'),
    ('鈴木', '英語'),
    ('高橋', '数学'),
]

subject_groups = defaultdict(list) # デフォルト: []
for student, subject in students:
    subject_groups[subject].append(student)
    # if subject in subject_groups:
    #     subject_groups[subject].append(student)
    # else:
    #     subject_groups[subject] = [student,]

print(subject_groups)
# {'数学': ['田中', '山田', '高橋'], '英語': ['佐藤', '鈴木']}

Point = namedtuple('Point', ['x', 'y'])
p1 = Point(3, 4)
p2 = Point(0, 0)

print(p1, type(p1)) # Point(x=3, y=4) <class '__main__.Point'>
print(p1.x, p2.y)

def distance(point1: Point, point2: Point):
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5

print(distance(p1, p2)) # 5.0

Product = namedtuple('Product', ['name', 'price', 'category'])
products = [
    Product('ノートPC', 120000, '電子機器'),
    Product('マウス', 3000, '電子機器'),
    Product('コーヒー', 500, '飲料'),
    Product('紅茶', 400, '飲料'),
]

category_prices = defaultdict(list)
for product in products:
    category_prices[product.category].append(
        (product.name, product.price)
    )
print(category_prices)