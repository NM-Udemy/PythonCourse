# インスタンス変数、クラス変数

class SampleA():
    class_val = 'class val' # クラス変数

    def set_val(self):
        self.instance_val = 'instance val' # インスタンス変数
    
    def print_val(self):
        print('クラス変数 = {}'.format(self.class_val))
        print('インスタンス変数 = {}'.format(self.instance_val))

instance_a = SampleA() # インスタンス化
instance_a.set_val()
print(instance_a.instance_val)
instance_a.print_val()
print(SampleA.class_val)
print(instance_a.__class__.class_val) # クラス変数
instance_b = SampleA() #インスタンス化
instance_b.set_val()
instance_b.print_val()
instance_a.__class__.class_val = 'class val 2'
instance_b.print_val()

print('*'*100)
print(id(instance_a.__class__.class_val))
print(id(instance_b.__class__.class_val))
