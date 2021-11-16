#　クラスの定義

class Car:
    """車クラス"""
    country = 'Japan'
    year = 2019
    name = 'Prius' #プロパティ
    def print_name(self):
        print('print_name実行')
        print(self.name)

my_car = Car() #インスタンス化
print(my_car.year)
my_car.print_name()
list_a = ['apple', 'banana', Car()]
# second_car = list_a[2]()
# second_car.print_name()
list_a[2].print_name()
help(Car)