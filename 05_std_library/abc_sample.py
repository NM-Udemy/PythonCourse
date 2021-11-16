# 抽象基底クラス
from abc import (
    abstractproperty, abstractmethod, abstractclassmethod,
    abstractstaticmethod, ABC, ABCMeta
)

class BaseAbstractClass(metaclass=ABCMeta):

    @abstractproperty
    def value(self):
        return 'Read Only property'

    @abstractmethod
    def print_value(self):
        pass

    @abstractclassmethod
    def write_value(cls, value):
        pass

    @abstractstaticmethod
    def print_static():
        pass

class MyClass(BaseAbstractClass):

    _value = 'Default Value'

    @property
    def value(self):
        return self._value

    def print_value(self):
        print('value = {}'.format(self.value))

    @classmethod
    def write_value(cls, value):
        with open('tmp.txt', mode='w', encoding='utf-8') as fh:
            fh.write(value)

    # @staticmethod
    # def print_static():
    #     print('staticメソッド')

    def print_a():
        print('A')


a = MyClass()
print(a.value)
a.print_value()
MyClass.write_value('抽象クラスの演習')
# a.print_static()