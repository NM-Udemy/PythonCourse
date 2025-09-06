from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    email: str = 'noreply@mail.com'
    
person1 = Person('田中太郎', 25, 'tanaka@email.com')
person2 = Person('田中太郎', 24, 'tanaka@email.com')

# Person(name='田中太郎', age=25, email='tanaka@email.com')
# dataclassで自動定義された__repr__
print(person1)
print(person1 == person2) # True, __eq__

person3 = Person('佐藤よしお', 30)
print(person3)
# Person(name='佐藤よしお', age=30, email='noreply@mail.com')