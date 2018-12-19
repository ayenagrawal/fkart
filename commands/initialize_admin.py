from fkart.app import db, bcrypt
from fkart.models.administrator import AdminModel

def create():
    adminusernanme = 'admin'
    adminemail = 'admin@atmecs.com'
    adminpassword = 'atmecs@1234'

    adminobj = AdminModel(username=adminusernanme,
                          email_address=adminemail,
                          password=bcrypt.generate_password_hash(adminpassword).decode('utf-8'))
    db.session.add(adminobj)
    db.session.commit()