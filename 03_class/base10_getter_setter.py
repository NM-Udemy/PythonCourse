class Person:
    
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    def get_name(self):
        print('get_nameが呼ばれました。')
        return self._name
    
    def set_name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise ValueError('名前に問題があります')
    
    def get_age(self):
        return self._age
    
    def set_age(self, age):
        if isinstance(age, int) and 0 <= age <= 120:
            self._age = age
        else:
            raise ValueError('年齢は0から120で')

person = Person('田中', 30)
# person._name
print(person.get_name()) # 田中
# person._name = '佐藤'
person.set_name('佐藤')
print(person.get_name())
person.set_age(10)
print(person.get_age())