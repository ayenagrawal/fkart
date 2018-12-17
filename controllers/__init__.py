import os, sys
import pkgutil, importlib
import types
from flask.views import MethodViewType
from fkart.controllers.base import BaseAPI

export_api_list = []
#ALL_MY_BASE_CLASSES = {BaseAPI}

# getting package/directory name
PKG_DIR = os.path.dirname(__file__)

# getting filenames and other details from a oackage
for (module_loader, name, ispkg) in pkgutil.iter_modules([PKG_DIR]):
    # print(name)
    # importing all modules/files
    importlib.import_module('.' + name, __package__)
    # creating python specific module path
    pkg_name = __name__ + '.' + name
    # chainging all modules as module type
    obj = sys.modules[pkg_name]
    # getting all classnames from module one by one using dir()
    for dir_name in dir(obj):
        # filtering predefinded dunder modules
        if dir_name.startswith('_'):
            continue
        # getting class object from selected classnames with help of module type
        dir_obj = getattr(obj, dir_name)
        # print(dir_obj)
        # getiing objects whose base class is MethodView
        if isinstance(dir_obj, MethodViewType) and hasattr(dir_obj, "__bases__"):
            #and set(ALL_MY_BASE_CLASSES) > set(dir_obj.__bases__):
            if dir_obj.__name__ not in {'BaseAPI', 'MethodView'}:
                export_api_list.append(dir_obj)