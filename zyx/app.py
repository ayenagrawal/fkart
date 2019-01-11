from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt import JWT
#from flask_jwt_extended import JWTManager

app = Flask(__name__)

from fkart.config import Config

app.config.from_object(Config)
db = SQLAlchemy(app)


from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

print("Project is running!!!")

from fkart.models.administrator import AdminModel
#from fkart.models.customer import CustomerModel
#from fkart.models.seller import SellerModel

def authenticate(email, password):
    #logintype = categorynemail.split('-')[1]
    #email = categorynemail.split('-')[0]
    #if logintype == 'admin':
        #tbl = AdminModel
    #elif logintype == 'customer':
        #tbl = CustomerModel
    #elif logintype == 'seller':
        #tbl = SellerModel

    user = AdminModel.query.filter_by(email_address=email).first()
    if user:
        if bcrypt.check_password_hash(user.password, password):
            return user

def identity(payload):
    user_id = payload['identity']
    user = AdminModel.query.filter_by(id=user_id).first()
    return user

jwt = JWT(app, authenticate, identity)

#jwt = JWTManager(app)


from fkart.controllers import export_api_list, PKG_DIR

for c_name in export_api_list:
    print(c_name.__name__)

# Initialzing apis from controllers
for api in export_api_list:
    # in-case export list contains direct urls
    # if hasattr(api, "url"):
        # api_url = getattr(api, "url")
    #else:
    api_url = api.__name__.lower().split("api")[0]
    api_name = api.__name__.lower()
    api_url_temp = ""
    for i in api_url.split('_'):
        api_url_temp += i
    api_url = api_url_temp
    del(api_url_temp)
    print("API URL:"+api_url)
    #print('API NAME:'+api_name)
    # for removing '/' from beginning if present
    # if api_url[0] == "/":
        # api_url = api_url[1:]
    view = api.as_view("%s" % api_name)
    app.add_url_rule("/"+(api_url), view_func=view)
