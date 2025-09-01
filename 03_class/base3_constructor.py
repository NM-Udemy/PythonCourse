class Registry:
    registries = []
    
    def __init__(self, name='ABC'):
        print('コンストラクタ呼びだし')
        self.name = name
        Registry.registries.append(self.name)
    
    def __del__(self):
        print(f"{self.name}を削除")
        Registry.registries.remove(self.name)
    
    def print_name(self):
        print(self.name)
        
a = Registry('A') # a.name = 'A'
b = Registry('B')
c = Registry()
a.print_name() # A
b.print_name() # B
c.print_name() # ABC
print(Registry.registries) # ['A', 'B', 'ABC']
del a
print(Registry.registries) # ['B', 'ABC']
print('プログラムが終了しました。')
