DATABASE_URL = 'sqlite:///app.db'
API_KEY = 'your-secret'
DEBUG = True

def get_config():
    return {
        'database_url': DATABASE_URL,
        'api_key': API_KEY,
        'debug': DEBUG
    }
