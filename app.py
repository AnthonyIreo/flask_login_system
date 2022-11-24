from flask import Flask,render_template, url_for, redirect
from views import views
from flask_sqlalchemy import SQLAlchemy
# UserMixin provides the implementation of the properties required by flask_login
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user

# used to web form
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError

# for password
from flask_bcrypt import Bcrypt

# create the app
app = Flask(__name__)
# database setting
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'thisisasecretkey'

# blueprint setting
# app.register_blueprint(views, url_prefix="/views")

# create the extension
db = SQLAlchemy(app)
# password encryption
bcrypt = Bcrypt(app)

# initialize the app with the extension
db.init_app(app)

# login and return the user information
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# create a table
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)

# create db in app_context
with app.app_context():
    db.drop_all()
    db.create_all()

# register requirement
class RegisterForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "username"})
    password = PasswordField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder":"password"})
    submit = SubmitField("Register")

    def validate_username(self, username):
        existing_user_username = User.query.filter_by(
            username=username.data).first()
        if existing_user_username:
            raise ValidationError("That username already exists, please choose another one.")

# login requirement
class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "username"})
    password = PasswordField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder":"password"})
    submit = SubmitField("Login")


# from flask_mail import Mail, Message
# mail_settings = {
#     "MAIL_SERVER": 'smtp.live.com',
#     "MAIL_PORT": 25,
#     "MAIL_USE_TLS": False,
#     "MAIL_USE_SSL": True,
#     "MAIL_USERNAME": 'ubmdfl_deepfake@hotmail.com',
#     "MAIL_PASSWORD": 'lab2022#ub.',
#     "MAIL_DEBUG" : True
#     }
# app.config.update(mail_settings)
# mail = Mail(app)

# @app.route("/email")
# def send_email():
#     msg = Message(subject="Hello", sender=app.config.get("MAIL_USERNAME"), recipients=["ubmdfl.deepfake@gmail.com"])
#     msg.body="This is a test email I sent with Gmail and Python!"
#     mail.send(msg)
#     return "sent"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            # check the password
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('dashboard'))
    return render_template('login.html', form = form)

@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('register.html', form = form)



if __name__ == '__main__':
    app.run(debug = "True")
