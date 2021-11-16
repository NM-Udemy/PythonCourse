from models import addresses, students, engine
from faker import Faker

faker = Faker('ja_JP')

print(faker.first_name())
print(faker.last_name())
print(faker.email())
print(faker.address())

with engine.connect() as conn:
    for i in range(5, 21):
        
        address = addresses.insert().values(
            id = i,
            student_id=i,
            postal_address=faker.address(),
            email_address=faker.email()
        )
        conn.execute(address)