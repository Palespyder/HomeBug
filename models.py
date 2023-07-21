
from flask_mongoengine import MongoEngine

db = MongoEngine()

class Bug(db.Document):
    title = db.StringField(required=True, max_length=200)
    description = db.StringField(required=True)
    status = db.StringField(default='Open', choices=('Open', 'In Progress', 'Closed'))
    priority = db.IntField(default=1)

    meta = {'collection': 'bugs'}