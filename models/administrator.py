from fkart.models.base import BaseModel, db

class AdminModel(BaseModel):
    __tablename__ = 'administrator'
    user_name = db.Column(db.String(20), nullable=False)
    email_address = db.Column(db.String(32), unique=True, nullable=False)
    password = db.Column(db.String(64), nullable=False)
