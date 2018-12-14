db_user = 'fkart_admin'
db_pass = 'atmecs@1234'
db_host = 'localhost:5432'
db_name = 'fkart_db'
class Config:
    DEBUG = True
    SECRET_KEY = r'ad/dwdw2323waedcv3212131'
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://%s:%s@%s/%s"% (db_user, db_pass, db_host, db_name)
    SQLALCHEMY_TRACK_MODIFICATIONS = False