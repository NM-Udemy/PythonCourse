from models2 import session, Customers
from sqlalchemy import or_, not_


# result = session.query(Customers).filter(Customers.name.like('%A%')).all()
# result = session.query(Customers).filter(Customers.id.in_([1,5,6]))
# result = session.query(Customers).filter(Customers.id < 10, Customers.name.like('B%'))
# result = session.query(Customers).filter(or_(Customers.id<5, Customers.id>95))
result = session.query(Customers).filter(not_(Customers.id>10))
for row in result:
    print(row.id, row.name, row.address)



