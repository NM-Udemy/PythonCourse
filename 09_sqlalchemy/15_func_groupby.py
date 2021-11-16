# 15_func_groupby.py
from models import students, engine
from sqlalchemy.sql import func, select


with engine.connect() as conn:
    print(conn.execute(select([func.now()])).fetchone()[0])
    print(conn.execute(students.select().with_only_columns(
        [func.max(students.c.id), func.min(students.c.id), func.avg(students.c.id)]
    )).fetchone())
    # group by
    sql = students.select().group_by(students.c.first_name, students.c.last_name).with_only_columns(
        [students.c.first_name, students.c.last_name, func.count(students).label('count'), func.max(students.c.id)]
    )
    print(conn.execute(sql).fetchall())
