import logging
from flask import request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

from fkart.app import bcrypt, db
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

    @jwt_required
    def put(self):
        try:
            userid = get_jwt_identity()
            data_dict = dict(request.get_json())
            user = CustomerModel.query.filter_by(id=userid).first()
            if "email_address" in data_dict:
                raise Exception("You can not update Email ID")
            if "password" in data_dict:
                user.password = bcrypt.generate_password_hash(data_dict["password"]).decode('utf-8')
            if "first_name" in data_dict:
                user.first_name = data_dict["first_name"]
            if "last_name" in data_dict:
                user.last_name = data_dict["last_name"]
            if "dob" in data_dict:
                user.dob = data_dict["dob"]
            if "address" in data_dict:
                user.address = data_dict["address"]
            db.session.add(user)
            db.session.commit()
            db.session.refresh(user)
            LOGGER.info("CUSTOMER: Profile data updated sucessfully")
            return jsonify({"message": "User profile updated sucessfully with data: "+str(user.basic_data())}), 200
        except Exception as error:
            LOGGER.error("CUSTOMER: Profile updation failed")
            return jsonify({"message": "Updated failed for profile", "error": str(error)}), 400

    @jwt_required
    def delete(self):
        try:
            userid = get_jwt_identity()
            user = CustomerModel.query.filter_by(id=userid).first()
            db.session.delete(user)
            db.session.commit()
            return jsonify({"message": "Profile delete sucessfully"}), 200
        except:
            return jsonify({"message": "Delete profile failed for user"}), 400
