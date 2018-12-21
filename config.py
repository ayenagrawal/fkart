import datetime
db_user = 'fkart_admin'
db_pass = 'atmecs@1234'
db_host = 'localhost:5432'
db_name = 'fkart_db'
class Config:
    DEBUG = True
    ENV = ""
    SECRET_KEY = 'e\xa9m2?\x1c\x83\xb3X7\xcf=\xa1s8\x12\xe2\xfe\xd7\xc1\xc4O\xbf\x0f'
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://%s:%s@%s/%s"% (db_user, db_pass, db_host, db_name)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'ba5378f05509592440efb0237b3651ac9e9c4406dea22c49e69b21a60d9a3c2b'
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(days=1)
    JWT_AUTH_USERNAME_KEY = 'email'