from typing import TypedDict, Generic, TypeVar, Callable

class UserData(TypedDict):
    name: str
    age: int
    email: str
    
class ProductData(TypedDict):
    name: str
    price: int
    stock: int

K = TypeVar('K')
V = TypeVar('V')

class Database(Generic[K, V]):
    def __init__(self):
        self.items: dict[K, V] = {}
    
    def add(self, item_id: K, item: V) -> None:
        self.items[item_id] = item
    
    def get(self, item_id: K) -> V | None:
        return self.items.get(item_id)
    
    def delete(self, item_id: K) -> V | None:
        return self.items.pop(item_id, None)
    
    def get_all(self) -> list[V]:
        return list(self.items.values())
    
    def find_by_condition(self, condition_func: Callable[[V], bool]) -> list[V]:
        return [item for item in self.items.values() if condition_func(item)]

# テストデータ
user_db: Database[int, UserData] = Database()
user_db.add(1, {"name": "田中太郎", "age": 25, "email": "tanaka@example.com"})
user_db.add(2, {"name": "佐藤花子", "age": 30, "email": "sato@example.com"})

product_db: Database[str, ProductData] = Database()
product_db.add("P001", {"name": "ノートPC", "price": 80000, "stock": 5})
product_db.add("P002", {"name": "マウス", "price": 2000, "stock": 20})

# 使用例
user = user_db.get(1)
if user:
    print(user['name'], user['age'])

young_users: list[UserData] = user_db.find_by_condition(
    lambda u: u['age'] < 30
)
print(young_users)
expensive_products: list[ProductData] = product_db.find_by_condition(
    lambda p: p['price'] > 50000
)
print(expensive_products)