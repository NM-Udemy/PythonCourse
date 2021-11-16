from models2 import session, Customers

result = session.query(Customers).all()
for row in result:
    print(row.name)

# id1だけdelete
session.query(Customers).filter(Customers.id==1).delete()

# 全員delete
session.query(Customers).delete()

session.commit()

result = session.query(Customers).all()
for row in result:
    print(row.name)
