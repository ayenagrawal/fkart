import logging.config
import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from flask_jwt import JWT
from flask_jwt_extended import JWTManager

app = Flask(__name__)

print("Project is running!!!")

# Loading configuration settings for logger

with open("fkart/logging_config.json", "r") as fileptr:
    config_dict_data = json.loads(fileptr.read())
logging.config.dictConfig(config_dict_data)
LOGGER = logging.getLogger(__name__)
LOGGER.info("LOGGER CONFIGURED")

from fkart.config import Config

app.config.from_object(Config)
db = SQLAlchemy(app)
LOGGER.info("Initialized ORM")

from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)
LOGGER.info("Initialzed Bcrypt")


jwt = JWTManager(app)
LOGGER.info("Initialzed JSON web token")


from fkart.controllers import export_api_list, PKG_DIR

#for c_name in export_api_list:
#    print(c_name.__name__)

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
    #print("API URL:"+api_url)
    #print('API NAME:'+api_name)
    # for removing '/' from beginning if present
    # if api_url[0] == "/":
        # api_url = api_url[1:]
    view = api.as_view("%s" % api_name)
    app.add_url_rule("/"+(api_url), view_func=view)
LOGGER.info("Added APIs to be used")
