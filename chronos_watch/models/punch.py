from peewee import *

db = SqliteDatabase('punches.db')

class Punch(Model):
    timestamp = DateTimeField()
    punch_type = CharField()

    class Meta:
        database = db
