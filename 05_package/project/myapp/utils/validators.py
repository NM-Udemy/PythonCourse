from myapp.database.models import User
from . import log_message

def validate_user(user):
    if not isinstance(user, User):
        log_message('ユーザーではありません')
        return False
    if user.name and user.email:
        if '@' in user.email and '.' in user.email:
            return True
    log_message('問題が発生しました')
    return False
