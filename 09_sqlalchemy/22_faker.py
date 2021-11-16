from models2 import session, Customers
from faker import Faker

faker = Faker()
customers = []
for _ in range(100):
    customer = Customers(name=faker.name(), address=faker.address(), email=faker.email())
    customers.append(customer)
session.add_all(customers)
session.commit()
