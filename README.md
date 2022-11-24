# flask_login_system

1,  install libraries
pip3 install flask flask_sqlalchemy flask_login flask_bcrypt flask_wtf wtforms email_validator

2,  create database(if needed)(the database will be created in 'instance/', use step3 to check)
Flask-SQLAlchemy 3.0:
with the code in app.py :(with app.app_context():
                            db.create_all() )
run: 
$ flask shell
>>> db.create_all()

or 
$ python
>>> from project import app, db
>>> app.app_context().push()
>>> db.create_all()

old version of SQLAlchemy:
python3 
from app import db
db.create_all()
exit()

3,  check database
cd instance/
sqlite3 database.db
.tables
.show
.schema
.exit


Tips:
1, the config of app: (
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SECRET_KEY'] = 'thisisasecretkey')
must be set before the ( db = SQLAlchemy(app) ), or the error happens:( RuntimeError: Either 'SQLALCHEMY_DATABASE_URI' or 'SQLALCHEMY_BINDS' must be set. )