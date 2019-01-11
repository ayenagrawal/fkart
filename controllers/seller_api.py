import logging
from flask import request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

from fkart.app import bcrypt
from fkart.controllers.base import BaseAPI
from fkart.models.seller import SellerModel

LOGGER = logging.getLogger(__name__)

class Seller_Auth(BaseAPI):
    def post(self):
        try:
            data_dict = dict(request.get_json())
            email = data_dict['email']
            password = data_dict['password']
        except Exception as error:
            LOGGER.info("SELLER: Exceptions occured while reeading data from JSON header")
            return jsonify({ "message": "A problem with Header occured!!!",
                             "error": str(error)}), 401
        user = SellerModel.query.filter_by(email_address=email).first()
        if not user:
            LOGGER.info("SELLER: Login failed")
            return jsonify({"message": "Invalid email"}), 401
        if not bcrypt.check_password_hash(user.password, password):
            LOGGER.info("SELLER: Login failed")
            return jsonify({"message": "Invalid credentials"}), 401
        access_token = create_access_token(user.id)
        LOGGER.info("SELLER: Login sucessful")
        return jsonify({"access_token": access_token}), 200

class Seller_Profile(BaseAPI):
    @jwt_required
    def get(self):
        try:
            userid = get_jwt_identity()
            user = SellerModel.query.filter_by(id=userid).first()
            LOGGER.info("SELLER: Getting logged-in user info for USER ID: %s", user.id)
            data_dict = user.basic_data()
            LOGGER.info("SELLER: Profile data returned sucessfully")
            return jsonify({"payload": data_dict})
        except AttributeError as error:
            LOGGER.info("SELLER: Exceptions occured while getting user profile")
            return jsonify({ "messsge": "Invalid JWT", "error": str(error)}), 401
