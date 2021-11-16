# 09_column_distinct.py
from models import students, engine


sql = students.select().where(students.c.id==3).with_only_columns(
    [students.c.id.label("student_id")]
)
sql = students.select().distinct(students.c.first_name, students.c.last_name).with_only_columns(
    [students.c.first_name, students.c.last_name]
)

with engine.connect() as conn:
    print(conn.execute(sql).fetchall())