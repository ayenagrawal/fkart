import logging
from flask import request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

from fkart.app import bcrypt
from fkart.controllers.base import BaseAPI
from fkart.models.customer import CustomerModel

LOGGER = logging.getLogger(__name__)

class Customer_Auth(BaseAPI):
    def post(self):
        try:
            data_dict = dict(request.get_json())
            email = data_dict['email']
            password = data_dict['password']
        except Exception as error:
            LOGGER.info("CUSTOMER: Exceptions occured while reeading data from JSON header")
            return jsonify({ "message": "A problem with Header occured!!!",
                             "error": str(error)}), 401
        user = CustomerModel.query.filter_by(email_address=email).first()
        if not user:
            LOGGER.info("CUSTOMER: Login failed")
            return jsonify({"message": "Invalid email"}), 401
        if not bcrypt.check_password_hash(user.password, password):
            LOGGER.info("CUSTOMER: Login failed")
            return jsonify({"message": "Invalid credentials"}), 401
        access_token = create_access_token(user.id)
        LOGGER.info("CUSTOMER: Login sucessful")
        return jsonify({"access_token": access_token}), 200

class Customer_Profile(BaseAPI):
    @jwt_required
    def get(self):
        try:
            userid = get_jwt_identity()
            user = CustomerModel.query.filter_by(id=userid).first()
            LOGGER.info("CUSTOMER: Getting logged-in user info for USER ID: %s", user.id)
            data_dict = user.basic_data()
            LOGGER.info("CUSTOMER: Profile data returned sucessfully")
            return jsonify({"payload": data_dict})
        except AttributeError as error:
            LOGGER.info("CUSTOMER: Exceptions occured while getting user profile")
            return jsonify({ "messsge": "Invalid JWT", "error": str(error)}), 401
