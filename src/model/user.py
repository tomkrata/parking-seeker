from mongoengine import Document, StringField


class User(Document):
    username = StringField(max_length=60, required=True, unique=False)
    password = StringField(max_length=60, required=True, unique=False)
    email = StringField(max_length=60, required=True, unique=True)
