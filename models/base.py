import uuid
from fkart.app import db

def get_randomhex():
    return uuid.uuid4().hex

class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column("id", db.String(32), primary_key=True, default=get_randomhex)