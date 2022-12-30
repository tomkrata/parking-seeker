from dto.user_dto import get_user, add_user


def user_exists(email):
    user = get_user(email)
    return user is not None

def fetch_user(email):
    user = get_user(email)
    return user

def insert_user(user):
    success = add_user(user)
    return success
