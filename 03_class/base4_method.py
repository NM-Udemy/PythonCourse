class Car:
    total_cars = 0
    
    def __init__(self, model, year, price):
        if not self.is_valid_year(year):
            raise ValueError(f"不正な年式: {year}")
        if not self.is_valid_price(price):
            raise ValueError(f"不正な価格: {price}")
        self.model = model
        self.year = year
        self.price = price
        Car.total_cars += 1
    
    @staticmethod
    def is_valid_year(year):
        return 1900 <= year <= 2100
    
    @staticmethod
    def is_valid_price(price):
        return 0 < price <= 10000
        
    # インスタンスメソッド
    def drive(self, distance):
        print(f'{self.model}を{distance}km運転')
        
    # クラスメソッド
    @classmethod
    def get_total_info(cls):
        return f"総製造台数: {cls.total_cars}台"
    
    @classmethod
    def create_used_car(cls, model, year):
        age = 2030 - year # 10
        price = 300 - age * 10 # 200
        price = price if price >= 0 else 0
        return cls(model, year, price)

    
    # スタティックメソッド
    @staticmethod
    def calcurate_tax(price):
        return price * 0.1

car1 = Car('プリウス', 2026, 300)
car2 = Car('カローラ', 2030, 200)
car3 = Car.create_used_car('シエンタ', 2020)
car1.drive(200)
print(Car.get_total_info())
print(car1.calcurate_tax(car1.price))
print(Car.calcurate_tax(399))
car3.drive(100)
print(car3.year, car3.price)
