from models import addresses, engine
from sqlalchemy.sql import func
from sqlalchemy import union, union_all, except_, intersect


with engine.connect() as conn:
    sql = union(addresses.select().where(addresses.c.email_address.like("%@gmail.com")),
        addresses.select().where(addresses.c.id > 30)
    )
    sql = union_all(addresses.select().where(addresses.c.email_address.like("%@gmail.com")),
        addresses.select().where(addresses.c.id > 30)
    )
    sql = except_(addresses.select().where(addresses.c.email_address.like("%@gmail.com")),
        addresses.select().where(addresses.c.id > 30)
    )
    sql = intersect(addresses.select().where(addresses.c.email_address.like("%@gmail.com")),
        addresses.select().where(addresses.c.id > 30)
    )

    for row in conn.execute(sql):
        print(row)
