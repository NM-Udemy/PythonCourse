from typing import Final, Self, Callable, TypeVar

API_VERSION: Final[str] = 'v2.1'
# API_VERSION = 'v2.2'

class QueryBuilder:
    
    def __init__(self) -> None:
        self._table = ''
        self._conditions = []
    
    def from_table(self, table_name: str) -> Self:
        self._table = table_name
        return self
    
    def where(self, condition: str) -> Self:
        self._conditions.append(condition)
        return self
    
    def build(self) -> str:
        query = f'SELECT * FROM {self._table}'
        if self._conditions:
            query += f" WHERE { ' AND '.join(self._conditions)}"
        return query
    
query = QueryBuilder().from_table(
    'user'
).where('age > 20').where('active = true').build()
print(query) # SELECT * FROM user WHERE age > 20 AND active = true

T = TypeVar('T')

def process_items(
    items: list[T],
    processor: Callable[[T], str]
) -> list[str]:
    return [processor(item) for item in items]

def format_user(user: dict[str, str]) -> str:
    return f"{user['name']} ({user['email']})"

def format_number(num: int) -> str:
    return f"#{num}"

user_list = [
    {'name': '田中太郎', 'email': 'tanaka@mail.com'},
    {'name': '佐藤花子', 'email': 'sato@mail.com'},
]
# user_list = list[dict[str, str]] 
# formst_user = [dict[str, str], str]
# process_items = list[T], Callable[[T], str] -> str
# T = dict[str, str], 
print(process_items(user_list, format_user))
numbers = [1, 15, 123]
print(process_items(numbers, format_number))