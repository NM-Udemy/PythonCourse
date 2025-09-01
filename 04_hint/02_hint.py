from typing import Optional
# Optional[]: Noneか中身

def find_user_by_id(users: list[dict[str, str]], user_id: str) -> dict[str, str] | None:
    for user in users:
        if user.get('id') == user_id:
            return user
    return None

users = [
    {'id': '001', 'name': '田中'},
    {'id': '002', 'name': '佐藤'},
]
user = find_user_by_id(users, '001')
if user is not None:
    print(user['name'])

class Product:
    def __init__(self, name, category):
        self.name = name
        self.category = category

items = [
    Product(name='ノートPC', category='電子機器'),
    Product(name='マウス', category='電子機器'),
    Product(name='コーヒー', category='飲料'),
]

def group_items_by_category(
    items: list[Product]
) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    for item in items:
        category = item.category
        name = item.name
        if category not in result:
            result[category] = []
        result[category].append(name)
    return result

items_group = group_items_by_category(items)
print(items_group)