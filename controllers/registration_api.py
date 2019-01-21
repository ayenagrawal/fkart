import sys
import logging
#from datetime import datetime
#import hashlib
from flask import request, jsonify
from sqlalchemy.exc import IntegrityError
from fkart.controllers.base import BaseAPI
from fkart.app import bcrypt, db
from fkart.models.customer import CustomerModel
from fkart.models.seller import SellerModel

LOGGER = logging.getLogger(__name__)

class Customer_Registration_API(BaseAPI):
    # data in json format like {"first_name", "last_name", "dob", "address", "email_address", "password"}
    def post(self):
        try:
            LOGGER.info("Registration started for Customer")
            data_dict = dict(request.get_json())
            print(data_dict)
            cus = CustomerModel(first_name=data_dict['first_name'],
                                last_name=data_dict['last_name'],
                                dob=data_dict['dob'],
                                address=data_dict['address'],
                                email_address=data_dict['email_address'],
                                #password=hashlib.sha256(data_dict['password'].encode('utf-8')).hexdigest())
                                password=bcrypt.generate_password_hash(data_dict['password']).decode('utf-8'))
            db.session.add(cus)
            db.session.commit()
            LOGGER.info("Customer registration sucessful with email: %s", data_dict['email_address'])
        except IntegrityError as error:
            LOGGER.info("Exceptions occured while registering Customer")
            return jsonify({"message": "Same data already exists!!! Enter valid data", "error": str(error)}), 401
        except:
            LOGGER.info("Exceptions occured while registering Customer")
            print(sys.exc_info()[0])
            db.session.rollback()
            db.session.commit()
            return jsonify({"message": "Some error occured!!!"}), 500
        return jsonify({"message": "Data entered into table sucessfully!!!"}), 200

class Seller_Registration_API(BaseAPI):
    def post(self):
        try:
            LOGGER.info("Registration started for Seller")
            data_dict = dict(request.get_json())
            print(data_dict)
            sel = SellerModel(first_name=data_dict['first_name'],
                              last_name=data_dict['last_name'],
                              dob=data_dict['dob'],
                              shop_name=data_dict['shop_name'],
                              shop_description=data_dict['shop_description'],
                              shop_address=data_dict['shop_address'],
                              email_address=data_dict['email_address'],
                              #password=hashlib.sha256(data_dict['password'].encode('utf-8')).hexdigest())
                              password=bcrypt.generate_password_hash(data_dict['password']).decode('utf-8'))
            db.session.add(sel)
            db.session.commit()
            LOGGER.info("Seller registration sucessful with email: %s", data_dict['email_address'])
        except IntegrityError as error:
            LOGGER.info("Exceptions occured while registering Seller")
            return jsonify({"message": "Same data already exists!!! Enter valid data", "error": str(error)}), 401
        except:
            LOGGER.info("Exceptions occured while registering Seller")
            print(sys.exc_info()[0])
            db.session.rollback()
            db.session.commit()
            return jsonify({"message": "Some error occured!!!"}), 500
        return jsonify({"message": "Data entered into table sucessfully!!!"}), 200

class Admin_Registration_API(BaseAPI):
    def post(self):
        try:
            data_dict = dict(request.get_json())
            print(data_dict)
            sel = SellerModel(first_name=data_dict['first_name'],
                              last_name=data_dict['last_name'],
                              email_address=data_dict['email_address'],
                              password=bcrypt.generate_password_hash(data_dict['password']).decode('utf-8'))
            db.session.add(sel)
            db.session.commit()
        except IntegrityError as error:
            return jsonify({"message": "Same data already exists!!! Enter valid data", "error": str(error)}), 401
        except:
            print(sys.exc_info()[0])
            db.session.rollback()
            db.session.commit()
            return jsonify({"message": "Some error occured!!!"}), 500
        return jsonify({"message": "Data entered intontable sucessfully!!!"}), 200
