from models2 import session, Presidents, Companies, Employees
from faker import Faker


faker = Faker('ja_JP')
for _ in range(10):
    president = Presidents(name=faker.name())
    session.add(president)
    session.commit()
    company = Companies(name=faker.company(), email=faker.company_email(), president_id=president.id)
    session.add(company)
    session.commit()
    for _ in range(10):
        employee = Employees(name=faker.name(), company_id=company.id)
        session.add(employee)
    session.commit()
