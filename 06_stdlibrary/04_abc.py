from abc import ABC, abstractmethod

class DataProcessor(ABC):
    
    def process_data(self, data):
        print(f'=== {self.get_type()} 処理開始 ===')
        validated_data = self.validate(data)
        processed_data = self.transform(validated_data)
        result = self.save(processed_data)
        print(f'税額: {self.calc_fee(len(data))}円')
        print('処理完了')
        return result
    
    @abstractmethod
    def validate(self, data):
        pass
    
    @abstractmethod
    def transform(self, data):
        pass
    
    @abstractmethod
    def save(self, data):
        pass
    
    @classmethod
    @abstractmethod
    def get_type(cls):
        pass
    
    @staticmethod
    @abstractmethod
    def calc_fee(count):
        pass
    
class CSVProcessor(DataProcessor):
    
    def validate(self, data):
        print('csv形式のチェック')
        return data
    
    def transform(self, data):
        print('CSV形式に変換')
        return data
    
    def save(self, data):
        print(f'csvファイルに保存: {data}')
        return data
    
    @classmethod
    def get_type(cls):
        return 'csv処理'
    
    @staticmethod
    def calc_fee(count):
        return count * 100

class ExcelProcessor(DataProcessor):
    pass

csv_processor = CSVProcessor()
csv_processor.process_data('サンプルデータ')
