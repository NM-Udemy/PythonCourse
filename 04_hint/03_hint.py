from typing import Union


def get_user_data(user_id: int | str) -> dict[str, str] | None:
    mock_data = {
        1: {'name': '田中太郎', 'role': 'admin'},
        'user_002': {'name': '佐藤花子', 'role': 'user'}
    }
    return mock_data.get(user_id)

user = get_user_data('user_003')
print(user)