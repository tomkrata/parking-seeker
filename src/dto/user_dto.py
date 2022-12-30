from model.user import User
from . import db


def get_user(email):
    return db['users'].find_one({ "email": email })


def add_user(dicti):
    return db['users'].insert_one(dicti)
