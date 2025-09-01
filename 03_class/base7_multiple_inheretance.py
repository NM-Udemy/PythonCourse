class Animal:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        pass
    
class Swimmer:
    def swim(self):
        return f'{self.name} is swimming' # type: ignore

    def fly(self):
        return f'{self.name} dont fly' # type: ignore

class Flyer:
    def fly(self):
        return f'{self.name} is flying' # type: ignore
    
    def speak(self):
        return 'speaking'

class Duck(Animal, Swimmer, Flyer):
    
    def speak(self):
        return f"{self.name} says quack!"

duck = Duck('Donald')
print(duck.speak()) # Donald says quack!
print(duck.swim()) # Donald is swimming
print(duck.fly()) # Donald is flying

print(Duck.__mro__)
# (<class '__main__.Duck'>, <class '__main__.Animal'>, <class '__main__.Swimmer'>, <class '__main__.Flyer'>, <class 'object'>)

class A:
    def method(self):
        return 'A'
    
class B(A):
    def method_b(self):
        return 'B'

class C(A):
    def method(self):
        return 'C'
    
class D(B, C):
    pass

print(D.__mro__)
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)

d = D()
print(d.method()) # B


class ClassA:
    
    def __init__(self, name):
        self.a_name = name
    
    def print_a(self):
        print('ClassAのメソッド実行')
        print(f'a: {self.a_name}')
    
    def print_hi(self):
        print('A hi')
        
class ClassB:
    
    def __init__(self, name):
        self.b_name = name
        
    def print_b(self):
        print('ClassBのメソッド実行')
        print(f'b: {self.b_name}')
    
    def print_hi(self):
        print('B hi')
        
class NewClass(ClassA, ClassB):
    def __init__(self, a_name, b_name, name):
        ClassA.__init__(self, a_name)
        ClassB.__init__(self, b_name)
        self.name = name
    
    def print_hi(self):
        ClassA.print_hi(self) # A hi
        ClassB.print_hi(self) # B hi
        print('NewClass hi')
        
    def print_new_name(self):
        print(f'name: {self.name}')

sample = NewClass('AName', 'BName', 'New Class Name')
sample.print_a()
sample.print_b()
sample.print_new_name()
sample.print_hi()

