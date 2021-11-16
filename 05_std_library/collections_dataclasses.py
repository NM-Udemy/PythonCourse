# dataclasses(3.7以降)
from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int
    grade: int

taro = Student('Taro', 12, 3)
print(taro.name)
print(taro.age)
taro.grade = 4
print(taro)
jiro = Student('Taro', 12, 4)
print(taro==jiro)