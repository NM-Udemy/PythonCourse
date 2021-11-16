from models import addresses, students, engine
from faker import Faker

faker = Faker('ja_JP')

print(faker.first_name())
print(faker.last_name())
print(faker.email())
print(faker.address())

with engine.connect() as conn:
    for _ in range(50):
        student = students.insert().values(
            first_name=faker.first_name(),
            last_name=faker.last_name()
        )
        result = conn.execute(student)
        student_id = result.inserted_primary_key[0]
        address = addresses.insert().values(
            student_id=student_id,
            postal_address=faker.address(),
            email_address=faker.email()
        )
        conn.execute(address)