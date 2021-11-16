# private変数

class Human:

    __class_val = 'Human'

    def __init__(self, name, age):
        self.__name = name # private変数
        self.__age = age

    def print_msg(self):
        print('name = {}, age = {}'.format(self.__name, self.__age))


human = Human('Taro', 15)
human.print_msg()