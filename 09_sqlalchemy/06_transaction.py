# 06_transaction.py
from models import addresses, students, engine

select_sql = students.select()
insert_sql = students.insert().values(
    {'first_name': 'Taro', 'last_name': 'Kimura'}
)

with engine.connect() as conn:
    with conn.begin() as tran:
        try:
            result = conn.execute(insert_sql)
            address = addresses.insert().values(
                {
                    'studnt_id': result.inserted_primary_key[0],
                    'postal_address': 'aaaa',
                    'email_address': 'a@mail.com'
                }
            )
            conn.execute(address)
        except Exception as e:
            tran.rollback()
        # tran.commit() # ロールバック

    print(conn.execute(select_sql).fetchall())