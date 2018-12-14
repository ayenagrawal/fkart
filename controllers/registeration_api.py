from fkart.controllers.base import BaseAPI

class Customer_Registeration_API(BaseAPI):
    def get(self):
        return 'This is get method of customer registeration api'

    def post(self):
        return 'This is post method of customer registeration api'

class Seller_Registeration_API(BaseAPI):
    def get(self):
        return 'This is get method of seller registeration api'

    def post(self):
        return 'This is post method of seller registeration api'

class Admin_Registeration_API(BaseAPI):
    def get(self):
        return 'This is get method of admin registeration api'

    def post(self):
        return 'This is post method of admin registeration api'