class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def greeting(self):
        print(f'Hello, Im {self.name}')
    
    def say_age(self):
        print(f'{self.age} years old')


class Employee(Person): # Personを継承
    
    def __init__(self, name, age, phone_number):
        super().__init__(name, age) # self.name=name, self.age=age
        self.phone_number = phone_number
    
    def greeting(self):
        super().greeting() # 親クラスを呼び出す
        print(
            f"I'm employee {self.name} phone_number: {self.phone_number}")
    
    def say_phone_number(self):
        print(self.phone_number)

man = Employee('Tanaka', 45, '08011112222')
man.greeting()
man.say_age()
man.say_phone_number() # 08011112222