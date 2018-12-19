from flask import request, jsonify
#from flask_jwt_extended import create_access_token
#from flask_jwt_extended import jwt_required, get_current_user, current_user
from fkart.app import bcrypt
from fkart.controllers.base import BaseAPI
from fkart.models.administrator import AdminModel


#class Admin_Auth(BaseAPI):
    #def post(self):
        #data_dict = dict(request.get_json())
        #user = AdminModel.query.filter_by(username=data_dict['username']).first()
        #if not user:
            #return jsonify({"message": "Invalid username"}), 401
        #if not bcrypt.check_password_hash(user.password, data_dict['password']):
            #return jsonify({"message": "Invalid credentials"}), 401
        #access_token = create_access_token(user.id)
        #return jsonify({"access_token": access_token, "userID": user.id, "username": user.username}), 200

#class AdminProfile(BaseAPI):
    #decorators = [jwt_required]
    #def get(self):
        #access = request.headers['Authorization']
        ##access_token = request.headers.get('JWT')
        ##return access_token
        ##identity = get_current_user()
        #user = jwt.current_user
        ##user = AdminModel.query.filter_by(id=identity).first()
        #return 'You are inside Admin profile username: %s' % str(type(user))
