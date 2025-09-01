from .database import Database
from .utils import log_message

def processs_data(app_config, user):
    with Database(
        app_config['database_url'], app_config['api_key']
    ) as connection:
        # DBにデータを登録
        result = {
            'processed': True,
            'user': user
        }
        log_message(f'データ処理完了: {result}')
        return result
