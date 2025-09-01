class Database:
    
    def __init__(self, database_url, api_key):
        self.database_url = database_url
        self.api_key = api_key
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, traceback):
        pass
