# クラス定義
class Car:
    country = 'Japan'
    year = 2030
    name = 'Prius'
    
    def __init__(self, name, year):
        self.name = name
        self.year = year
        
    # インスタンスメソッド
    def print_name(self):
        print('Print Name実行')
        print(self.name)
    
    def set_name(self, name):
        self.name = name

print(Car.country) # Japan
# print(Car.year) # 30 

# インスタンス作成
my_car = Car("Cienta", 2035) # 実体
print(my_car.year) # 2030
print(my_car.country) # Japan
# my_car.set_name('Lexus')
# my_car.name = 'Lexus
my_car.print_name() # Prius