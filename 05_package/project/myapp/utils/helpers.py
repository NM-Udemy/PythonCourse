from datetime import datetime

def log_message(message):
    print(f'[{datetime.now()}] {message}')
    