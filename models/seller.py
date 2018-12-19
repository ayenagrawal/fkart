from datetime import datetime
from fkart.models.base import BaseModel, db

class SellerModel(BaseModel):
    __tablename__ = 'seller'
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    dob = db.Column(db.DateTime(timezone=True), default=datetime.utcnow)
    shop_name = db.Column(db.String(60), nullable=False)
    shop_description = db.Column(db.String(100), nullable=True)
    shop_address = db.Column(db.String(50), nullable=True)
    email_address = db.Column(db.String(32), unique=True, nullable=False)
    password = db.Column(db.String(64), nullable=False)
    is_verified = db.Column(db.Boolean(), default=False)
