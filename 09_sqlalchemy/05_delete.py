# 05_delete.py

from models import students, engine


select_sql = students.select()

with engine.connect() as conn:
    delete_sql = students.delete()
    print(delete_sql)

    # delete_sql = delete_sql.where(students.c.id > 3)
    delete_sql = delete_sql.where(students.c.first_name != 'taro')
    conn.execute(delete_sql)

    delete_sql = students.delete()
    conn.execute(delete_sql)