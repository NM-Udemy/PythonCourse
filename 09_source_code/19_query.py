from models2 import Customers, session

result = session.query(Customers).all()
for row in result:
    print(row.name)

result = session.query(Customers).count()
print(result)

result = session.query(Customers).first()
print(result.name)

result = session.query(Customers).filter(Customers.id==2).all()
for row in result:
    print(row.name)

# nameで昇順
result = session.query(Customers).order_by(Customers.name).all()
for row in result:
    print(row.name)


from sqlalchemy import desc
result = session.query(Customers).order_by(desc(Customers.id)).all()
for row in result:
    print(row.name)

result = session.query(Customers).add_columns(Customers.id, Customers.name).all()
for row in result:
    print(row.id, row.name, row.address)