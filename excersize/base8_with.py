from pathlib import Path

class SalesData:
    
    def __init__(self):
        self.total_sales = 0
        self.item_count = 0
        self.product_data = {} # 商品ごとのデータ

    def load_csv(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines() # 全行リスト
            lines = lines[1:]
            for line in lines:
                line = line.strip() # 改行、無駄な空白を左右から削除
                if line:
                    parts = line.split(',')
                    product_name = parts[0]
                    price = int(parts[1])
                    quantity = int(parts[2])
                    product_sales = price * quantity
                    self.total_sales += product_sales
                    self.item_count += 1
                    if product_name not in self.product_data:
                        self.product_data[product_name] = {
                            'total_sales': 0,
                            'count': 0
                        }
                    self.product_data[product_name]['total_sales'] += product_sales
                    self.product_data[product_name]['count'] += 1
    
    def analyze(self):
        self.average_sales = self.total_sales // self.item_count if self.item_count > 0 else 0
        self.product_average = {}
        for product_name, data in self.product_data.items():
            self.product_average[product_name] = data['total_sales'] // data['count']

    def save_result(self, file_path):
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write('=== 売上分析結果 === \n')
            f.write(f'総売上: {self.total_sales}円\n')
            f.write(f'取引数: {self.item_count}件\n')
            f.write(f'平均売上: {self.average_sales}円\n\n')
            
            f.write('=== 商品別平均売上 ===\n')
            for product_name, avg in self.product_average.items():
                f.write(f'{product_name}: {avg}円\n')

script_dir = Path(__file__).parent
load_file = script_dir / 'data' / 'sales.csv'
output_file = script_dir / 'data' / 'result.txt'

sales = SalesData()
sales.load_csv(load_file)
sales.analyze()
sales.save_result(output_file)