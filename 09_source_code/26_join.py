# 26_join.py
from models2 import session, Presidents, Companies, Employees


result = session.query(Presidents).filter(Presidents.id.in_([2, 3]))
for row in result:
    print(row.name)
    print(row.companies.name)


result = session.query(Companies).filter(Companies.id == 2)
for row in result:
    print(row.president.name)
    for r in row.employees:
        print(r.name)

result = session.query(Employees).filter(Employees.id==1)
for row in result:
    print(row.company.name)
