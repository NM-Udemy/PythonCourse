class Human:
    
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    def get_info(self):
        return {
            'name': self._name,
            'age': self._age
        }
    
human = Human('Taro', 32)

# print(human._Human__name) 
# human._name = 'Jiro' # 推奨されない
# print(human._name)
# print(human.get_info())