# 02_insert.py
from models import addresses, students, engine


insert_sql = students.insert()
print(insert_sql)
insert_sql = insert_sql.values(
    {'first_name': 'Satoko', 'last_name': 'Yamada'}
)
print(insert_sql)
print(insert_sql.compile().params)

conn = engine.connect()
# conn.execute(insert_sql)

insert_sql2 = students.insert().values(
    [
        {'first_name': 'Jiro', 'last_name': 'Sato'},
        {'first_name': 'Hanako', 'last_name': 'Kimura'},
        {'first_name': 'Saburo', 'last_name': 'Suzuki'}
    ]
)

result = conn.execute(insert_sql)
print(result)
print(result.is_insert)
print(result.inserted_primary_key)
