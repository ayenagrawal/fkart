import logging
from flask import request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

from fkart.app import bcrypt, db
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
            LOGGER.error("SELLER: Exceptions occured while reeading data from JSON header")
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
            data_dict1 = dict(request.get_json())
            user = SellerModel.query.filter_by(id=userid).first()
            LOGGER.info("SELLER: Getting logged-in user info for USER ID: %s", user.id)
            data_dict = user.basic_data()
            LOGGER.info("SELLER: Profile data returned sucessfully")
            return jsonify({"payload": data_dict, "payload2": data_dict1})
        except AttributeError as error:
            LOGGER.error("SELLER: Exceptions occured while getting user profile")
            return jsonify({ "messsge": "Invalid JWT", "error": str(error)}), 401

    @jwt_required
    def put(self):
        try:
            userid = get_jwt_identity()
            data_dict = dict(request.get_json())
            user = SellerModel.query.filter_by(id=userid).first()
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
            if "shop_name" in data_dict:
                user.shop_name = data_dict["shop_name"]
            if "shop_description" in data_dict:
                user.shop_description = data_dict["shop_description"]
            if "shop_address" in data_dict:
                user.shop_address = data_dict["shop_address"]
            db.session.add(user)
            db.session.commit()
            db.session.refresh(user)
            LOGGER.info("SELLER: Profile data updated sucessfully")
            return jsonify({"message": "User profile updated sucessfully with data: "+str(user.basic_data())}), 200
        except Exception as error:
            LOGGER.error("SELLER: Profile updation failed")
            return jsonify({"message": "Updated failed for profile", "error": str(error)})

    @jwt_required
    def delete(self):
        try:
            userid = get_jwt_identity()
            user = SellerModel.query.filter_by(id=userid).first()
            db.session.delete(user)
            db.session.commit()
            return jsonify({"message": "Profile delete sucessfully"})
        except:
            return jsonify({"message": "Delete profile failed for user"})
