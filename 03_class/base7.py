# クラスの多重継承

class ClassA:

    def __init__(self, name):
        self.a_name = name
    
    def print_a(self):
        print('ClassAのメソッド実行')
        print('a = {}'.format(self.a_name))
    
    def print_hi(self):
        print('A hi')

class ClassB:

    def __init__(self, name):
        self.b_name = name
    
    def print_b(self):
        print('ClassBのメソッド実行')
        print('b = {}'.format(self.b_name))
    
    def print_hi(self):
        print('B hi')

class NewClass(ClassA, ClassB):

    def __init__(self, a_name, b_name, name):
        ClassA.__init__(self, a_name)
        ClassB.__init__(self, b_name)
        self.name = name
    
    def print_new_name(self):
        print('name = {}'.format(self.name))
    
    def print_hi(self):
        ClassA.print_hi(self)
        ClassB.print_hi(self)
        print('NewClass hi')

sample = NewClass('AName', 'BName', 'New Class Name')

sample.print_a()
sample.print_b()
sample.print_new_name()
sample.print_hi()