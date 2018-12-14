from fkart.models.base import BaseModel
from fkart.app import db

class CustomerModel(BaseModel):
    __tablename__ = 'customer'
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    dob = db.Column(db.DateTime(timezone=True), nullable=False)
    address = db.Column(db.String(50), nullable=True)
    is_verified = db.Column(db.Boolean(), default=False)
