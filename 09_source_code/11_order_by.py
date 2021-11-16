# 11_order_by.py

from models import students, engine
from sqlalchemy import asc, desc

sql = students.select().order_by(students.c.first_name, students.c.last_name)
sql = students.select().order_by(desc(students.c.id), asc(students.c.first_name))

with engine.connect() as conn:
    for row in conn.execute(sql):
        print(row)