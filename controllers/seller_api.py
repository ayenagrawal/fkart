from flask import request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

from fkart.app import bcrypt
from fkart.controllers.base import BaseAPI
from fkart.models.seller import SellerModel

class Seller_Auth(BaseAPI):
    def post(self):
        data_dict = dict(request.get_json())
        email = data_dict['email']
        password = data_dict['password']

        user = SellerModel.query.filter_by(email_address=email).first()
        if not user:
            return jsonify({"message": "Invalid email"}), 401
        if not bcrypt.check_password_hash(user.password, password):
            return jsonify({"message": "Invalid credentials"}), 401
        access_token = create_access_token(user.id)
        return jsonify({"access_token": access_token}), 200

class Seller_Profile(BaseAPI):
    @jwt_required
    def get(self):
        userid = get_jwt_identity()
        user = SellerModel.query.filter_by(id=userid).first()
        return 'You are into Customer profile!!! username: %s %s shopname: %s' % (user.first_name, user.last_name, user.shop_name)
