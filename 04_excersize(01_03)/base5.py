# base5.py

from abc import abstractmethod, ABCMeta

class Animals(metaclass=ABCMeta):

    @abstractmethod
    def speak(self):
        pass

class Dog(Animals):

    def speak(self):
        print('わん')

class Cat(Animals):
    
    def speak(self):
        print('にゃー')

class Sheep(Animals):

    def speak(self):
        print('めー')

class Other(Animals):

    def speak(self):
        print('そんな動物いない')

number = input('好きな動物は？ 1: 犬、2: 猫, 3:羊')

if number == '1':
    animal = Dog()
elif number == '2':
    animal = Cat()
elif number == '3':
    animal = Sheep()
else:
    animal = Other()

animal.speak() # speakの呼び出し（ポリモーフィズム）