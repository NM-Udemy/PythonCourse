class DatabaseManager:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None
    
    def __enter__(self):
        print(f'データベース {self.db_name}に接続')
        self.connection = f'connection to {self.db_name}'
        return self.connection

    def __exit__(self, exc_type, exc_val, traceback):
        print(exc_type, exc_val, traceback)
        print(f'データベース {self.db_name}から切断')
        self.connection = None
        return True

with DatabaseManager('user_data.db') as db:
    print('データを挿入')
    print('処理完了')
    # raise ValueError('問題がありました')
