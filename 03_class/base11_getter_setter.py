class Person:
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
        
    @property
    def full_name(self):
        return f'{self._first_name} {self._last_name}'
    
    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, value):
        print('setter呼び出し')
        if not value:
            raise ValueError('名前を空白にしないで')
        self._first_name = value
        
person = Person('太郎', '田中')
print(person.first_name)
person.first_name = '次郎' # @first_name.setter呼び出し
print(person.first_name)
print(person.full_name)
