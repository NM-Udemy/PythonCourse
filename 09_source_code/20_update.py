from models2 import session, Customers

result = session.query(Customers).all()
for row in result:
    print(row.name)

session.query(Customers).filter(Customers.name=='Jiro').update({'name': 'Shiro'})
session.commit()

result = session.query(Customers).get(1)
result.address='America'
session.commit()
result = session.query(Customers).all()
for row in result:
    print(row.id, row.name, row.address)


result = session.query(Customers).all()
for row in result:
    row.address='Japan'
session.commit()

result = session.query(Customers).all()
for row in result:
    print(row.address, row.name)