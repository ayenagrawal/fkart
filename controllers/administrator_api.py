import logging
from flask import request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

from fkart.app import bcrypt
from fkart.controllers.base import BaseAPI
from fkart.models.administrator import AdminModel

LOGGER = logging.getLogger(__name__)

class Admin_Auth(BaseAPI):
    def post(self):
        data_dict = dict(request.get_json())
        username = data_dict['username']
        password = data_dict['password']

        user = AdminModel.query.filter_by(user_name=username).first()
        if not user:
            LOGGER.info("ADMINISTRATOR: Login failed")
            return jsonify({"message": "Invalid username"}), 401
        if not bcrypt.check_password_hash(user.password, password):
            LOGGER.info("ADMINISTRATOR: Login failed")
            return jsonify({"message": "Invalid credentials"}), 401
        access_token = create_access_token(user.id)
        LOGGER.info("ADMINISTRATOR: Login sucessful")
        return jsonify({"access_token": access_token}), 200

class Admin_Profile(BaseAPI):
    @jwt_required
    def get(self):
        try:
            userid = get_jwt_identity()
            user = AdminModel.query.filter_by(id=userid).first()
            LOGGER.info("ADMINISTRATOR: Into the Admin profile")
            return 'You are into admin profile!!! username: %s' % user.user_name
        except AttributeError as error:
            LOGGER.info("ADMINISTRATOR: Exceptions occured while getting Admin profile")
            return jsonify({ "messsge": "Invalid JWT", "error": str(error)}), 401
