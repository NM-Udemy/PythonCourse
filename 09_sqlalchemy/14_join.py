# 14_join.py
from models import addresses, students, engine

sql = students.join(addresses,
    students.c.id == addresses.c.student_id, isouter=True
).select().where(addresses.c.email_address.like('%yahoo.com'))

delete_sql = addresses.delete().where(addresses.c.student_id.between(5,20))
with engine.connect() as conn:
    conn.execute(delete_sql)
    result = conn.execute(sql)
    for row in result.fetchmany(10):
        print(row)