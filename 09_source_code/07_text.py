# 07_text.py
from models import students, engine
from sqlalchemy import text, bindparam


select_sql = text("SELECT id, first_name FROM students")
select_sql = text("SELECT * FROM students WHERE id BETWEEN :x AND :y")
select_sql = students.select().where(
    text('id=:x')
)
with engine.connect() as conn:
    # result = conn.execute(select_sql, x=1, y=2)
    result = conn.execute(select_sql, x=2)
    print(result.fetchall())