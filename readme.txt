# Python3.7 interpretor required
# create a virtual environment using:   virtualenv <envname>    (Windows specific)
                                        pip install virtualenv
                                        virtualenv virtualenv_name  (Linux Specific)
# To install dependencies:  pip install -r requirements.txt

# To run project:   python -m fkart

# To create database:   python -m fkart shell
                        from fkart.models import *
                        from fkart.models.base import db
                        db.create_all()
                        db.session.commit()

# To create Admin:      python -m fkart shell
                        from fkart.models.base import db
                        from fkart.commands.initialize_admin import *
                        create()