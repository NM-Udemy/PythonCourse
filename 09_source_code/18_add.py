from models2 import Customers, session

c1 = Customers(name='Taro', address='Tokyo', email='taro@mail.com')

# session.add(c1)
session.add_all([
    Customers(name='Jiro', address='Osaka', email='jiro@mail.com'),
    Customers(name='Hanako', address='Fukuoka', email='hanako@mail.com')
])
session.commit()
