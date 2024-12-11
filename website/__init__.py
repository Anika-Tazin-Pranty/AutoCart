from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = 'database.sqlite3'

def create_database():
    db.create_all()
    print('Database created')

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hbnwdvbn ajnbsjn ahe' # encrypting session data by SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    db.init_app(app)

    login_manager = LoginManager() # for session management
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login' # tells login_manager about login view location

    @login_manager.user_loader
    def load_user(id): # loads user based on user id and retrieves the user obj for the current session
        return Customer.query.get(int(id))
    
    from .views import views
    from .auth import auth
    from .admin import admin
    from .models import Customer, Cart, Product, Order
    
    app.register_blueprint(views, url_prefix = '/') # localhost:5000/about-us
    app.register_blueprint(auth, url_prefix = '/') # localhost:5000/auth/change-password
    app.register_blueprint(admin, url_prefix = '/')

    #with app.app_context():
    #   create_database()

    return app