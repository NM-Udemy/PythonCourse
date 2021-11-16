# クラスの継承

class Person: # 親クラス

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greeting(self):
        print('hello {}'.format(self.name))
    
    def say_age(self):
        print('{} years old'.format(self.age))

class Employee(Person): # Personの機能を継承

    def __init__(self, name, age, number):
        super().__init__(name, age)
        self.number = number
    
    def say_number(self):
        print('my number is = {}'.format(self.number))
    
    def greeting(self): # オーバライド
        super().greeting()
        print('I\'m employee phone_number = {}'.format(self.number))

    # def greeting(self, age): # オーバロード
    #     print('オーバーロード')
man = Employee('Tonegawa', 45, '08011111111')
man.greeting()
man.say_age()
man.say_number()