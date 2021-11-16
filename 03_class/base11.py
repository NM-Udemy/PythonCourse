# getter, setter その1

class Human:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    def get_name(self):
        print('getter name を呼び出しました')
        return self.__name
    
    def get_age(self):
        print('getter ageを呼び出しました')
        return self.__age
    
    def set_name(self, name):
        print('setter nameを呼び出しました')
        self.__name = name
    
    def set_age(self, age):
        print('setter ageを呼び出しました')
        self.__age = age
    
    name = property(get_name, set_name) # nameを指定するとget_name, set_nameが呼び出される, human.set_name()
    age = property(get_age, set_age)

    def print_msg(self):
        print(self.name, self.age)

human = Human('Taro', 15)
human.name = 'Jiro'
human.age = 18

name = human.name
age = human.age
print(name, age)
human.print_msg()