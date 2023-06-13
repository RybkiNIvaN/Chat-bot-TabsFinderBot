import peewee
from peewee import *


# Set database
db = SqliteDatabase('Tabs.db')
db.connect()


class Tab(Model):
    id = PrimaryKeyField(unique=True)
    groups = TextField()
    song = TextField()
    path = TextField()

    class Meta:
        database = db
        db_table = 'tabs'


class Collection(Model):
    tab_id = IntegerField()
    user_id = TextField()
    song = TextField()
    sent = IntegerField()

    class Meta:
        database = db
        db_table = 'collection'


class User(Model):
    name = TextField()
    user_id = TextField()

    class Meta:
        database = db
        db_table = 'users'