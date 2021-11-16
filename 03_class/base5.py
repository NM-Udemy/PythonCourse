# 特殊関数

class Human:

    def __init__(self, name, age, phone_number):
        self.name = name
        self.age = age
        self.phone_number = phone_number

    def __str__(self):
        return 'name = {}, age = {}, phone_number: {}'.format(self.name, self.age, self.phone_number)

    def __hash__(self):
        print('hash関数が呼ばれました')
        return hash(self.name + self.phone_number)

    def __bool__(self):
        if self.age > 20:
            return True
        else:
            return False

    def __len__(self):
        print('lenが呼ばれました')
        return 2

woman = Human('Elsa', 20, '08011111111')
# w = str(woman)
woman2 = Human('Elsa', 22, '08022222222')
print(hash(woman))
print(hash(woman2))
# set, 辞書のキー
dict_a = {
    woman: 'AAA'
}
print(dict_a)
if woman:
    print('WomanはTrue')
if woman2:
    print('Woman2はTrue')

print(len(woman))
print(Human.__name__)