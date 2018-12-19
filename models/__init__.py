import os, sys
import pkgutil, importlib
from fkart.models.base import BaseModel

export_models_list = []
PKG_DIR = os.path.dirname(__file__)

for (module_loader, name, ispkg) in pkgutil.iter_modules([PKG_DIR]):
    importlib.import_module('.' + name, __package__)
    pkg_name = __name__ + '.' + name
    obj = sys.modules[pkg_name]
    for dir_name in dir(obj):
        if dir_name.startswith('_'):
            continue
        dir_obj = getattr(obj, dir_name)
        if hasattr(dir_obj, "__bases__") and hasattr(dir_obj, '__tablename__') and BaseModel in dir_obj.__bases__:
            export_models_list.append(dir_obj)