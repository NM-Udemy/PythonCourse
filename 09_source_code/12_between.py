# 12_between.py
from models import students, engine
from sqlalchemy import not_

# BETWEEN
sql = students.select().where(students.c.id.between(10, 20))
sql = students.select().where(not_(students.c.id.between(10, 20)))

# LIKE
sql = students.select().where(students.c.first_name.like('直%'))
sql = students.select().where(students.c.first_name.like('%一'))
sql = students.select().where(students.c.first_name.like('%一%')) # 中間一致

sql = students.select().where(students.c.first_name.notlike('直%'))
sql = students.select().where(not_(students.c.first_name.like('直%')))

#IN
sql = students.select().where(students.c.id.in_([1,3,5]))
sql = students.select().where(students.c.first_name.in_(['洋介', '直人']))
sql = students.select().where(students.c.id.notin_([1,3,5]))

# LIMIT OFFSET
sql = students.select().offset(10)
sql = students.select().limit(3)
sql = students.select().offset(3).limit(3)


with engine.connect() as conn:
    for row in conn.execute(sql):
        print(row)