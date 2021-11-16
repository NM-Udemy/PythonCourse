# 13_join.py
from models import addresses, students, engine
from sqlalchemy.sql import select


with engine.connect() as conn:
    sql = select([addresses, students]).where(
        students.c.id == addresses.c.student_id
    ).with_only_columns(
        [students.c.id.label('student_id'), students.c.first_name,
        addresses.c.id.label('address_id'), addresses.c.email_address]
    )
    result = conn.execute(sql)
    for row in result.fetchmany(10):
        print(row.first_name)
