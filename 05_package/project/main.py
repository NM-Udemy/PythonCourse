from config import get_config
from myapp.database import User
from myapp.utils import validate_user
from myapp import processs_data

def main():
    app_config = get_config()
    print(f'デバッグモード: {app_config["debug"]}')
    test_data = User(name='Taro', email='taro@mail.com')
    if validate_user(test_data): # チェック完了
        result = processs_data(app_config, test_data)
        print(f'処理成功: {result}')

    
if __name__ == '__main__':
    main()
