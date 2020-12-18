from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from project.config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'account.login'

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from project.main.routes import main
    app.register_blueprint(main)
    
    from project.account.routes import account
    app.register_blueprint(account)

    from project.orders.routes import orders
    app.register_blueprint(orders)

    return app