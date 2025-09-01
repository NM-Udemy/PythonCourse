from typing import Literal, Final, NotRequired, TypedDict, TypeVar, Generic

class UserProfile(TypedDict):
    id: int
    name: str
    role: Literal['admin', 'user', 'guest']
    last_login: NotRequired[str]
    
def create_user_profile(
    user_id: int,
    name: str,
    role: Literal['admin', 'user', 'guest']
) -> UserProfile:
    return {'id': user_id, 'name': name, 'role': role}

def get_user_permission_level(
    role: Literal['admin', 'user', 'guest']
) -> int:
    permissions_map: Final[dict[str, int]] = {
        'admin': 10, 'user': 5, 'guest': 1
    }
    return permissions_map[role]

user = create_user_profile(1, '田中太郎', 'admin')
print(user)
print(get_user_permission_level(user['role']))

T = TypeVar('T')

class Cache(Generic[T]):
    
    def __init__(self):
        self._data: dict[str, T] = {}
        
    def set(self, key: str, value: T):
        self._data[key] = value
    
    def get(self, key:str) -> T | None:
        return self._data.get(key)
    
    def get_all(self) -> list[T]:
        return list(self._data.values())

string_cache: Cache[str] = Cache()
string_cache.set('greeting', 'こんにちは')
print(string_cache.get('greeting'))
print(string_cache.get_all())

dict_cache: Cache[dict[str, int]] = Cache()
dict_cache.set('scores', {'math': 90, 'english': 80})
print(dict_cache.get_all())