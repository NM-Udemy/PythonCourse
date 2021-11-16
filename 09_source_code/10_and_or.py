# 10_and_or.py
from sqlalchemy import and_, or_
from models import students, engine


sql = students.select().where(
    and_(
        students.c.id>20,
        students.c.first_name=='陽子',
        students.c.last_name=='山田'
    )
)

sql = students.select().where(
    or_(
        students.c.id>20,
        students.c.id<5,
        students.c.first_name=='山田'
    )
)

with engine.connect() as conn:
    print(conn.execute(sql).fetchall())