
from database import User


def get_user(username):
    user = User.query.filter_by(username=username).first()
    return f'{user}'
