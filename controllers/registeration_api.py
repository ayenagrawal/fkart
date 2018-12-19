import sys
from datetime import datetime
import hashlib
from flask import request
from sqlalchemy.exc import IntegrityError
from fkart.controllers.base import BaseAPI
from fkart.app import bcrypt, db
from fkart.models.customer import CustomerModel
from fkart.models.seller import SellerModel

class Customer_Registeration_API(BaseAPI):
    def get(self):
        return 'This is get method of customer registeration api'
    # data in json format like {"first_name", "last_name", "dob", "address", "email_address", "password"}
    def post(self):
        try:
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
        except IntegrityError as error:
            return ("Same data already exists!!! Enter valid data")
        except:
            print(sys.exc_info()[0])
            db.session.rollback()
            db.session.commit()
            return 'Some error occured!!!'
        return 'Data entered intontable sucessfully!!!'

class Seller_Registeration_API(BaseAPI):
    def get(self):
        return 'This is get method of seller registeration api'

    def post(self):
        try:
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
        except IntegrityError as error:
            return ("Same data already exists!!! Enter valid data")
        except:
            print(sys.exc_info()[0])
            db.session.rollback()
            db.session.commit()
            return 'Some error occured!!!'
        return 'Data entered intontable sucessfully!!!'

class Admin_Registeration_API(BaseAPI):
    def get(self):
        return 'This is get method of admin registeration api'

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
            return ("Same data already exists!!! Enter valid data")
        except:
            print(sys.exc_info()[0])
            db.session.rollback()
            db.session.commit()
            return 'Some error occured!!!'
        return 'Data entered intontable sucessfully!!!'