# 04_update.py
from models import students, engine


select_sql = students.select()

with engine.connect() as conn:
    update_sql = students.update()
    print(update_sql)
    update_sql = update_sql.where(students.c.id==2).values(first_name='Shiro')
    conn.execute(update_sql)
    rows = conn.execute(select_sql)
    for row in rows:
        update_sql = students.update().where(
            students.c.id == row.id
        ).values(
            first_name = row.first_name.lower(),
            last_name = row.last_name.lower()
        )
        conn.execute(update_sql)