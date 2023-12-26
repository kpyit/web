from flask import Flask
# conda remove -n Flask  flask-bootstrap   - сломался пришлось заменить
# conda install -n Flask -c conda-forge flask-bootstrap
#       -  conda-forge/noarch::flask-bootstrap-3.3.7.1-py_0
from flask_bootstrap import Bootstrap 
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_pagedown import PageDown
from config import config
import os # перенесено из note.py для поиска конфига
from flask_migrate import Migrate, upgrade# перенесено из note.py для консоли

from flask_cors import CORS # для реакта разработки разрешение на крос запросы 

#с оф документации  https://flask-restx.readthedocs.io/en/latest/quickstart.html
from flask_restx import Api, Resource, fields 

#REST
rest_api = Api()

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()
migrate = Migrate()# # перенесено из note.py для консоли

pagedown = PageDown()

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
   

# def create_app(config_name):
def create_app():
    
    app = Flask(__name__)
    CORS(app) #обертка для кросс запросов сервера реакта
    # перенесено из note.py схема сработала
    # config_name = os.getenv('FLASKCONFIG') or 'default'
    #сервер помер используем локальную копию
    config_name = os.getenv('FLASKCONFIG') or 'testing'
    
    
    app.config.from_object(config[config_name])
    
    config[config_name].init_app(app) 

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    
    rest_api.init_app(app)
    
    migrate.init_app(app, db)# перенесено из старого проекта
    
    login_manager.init_app(app)
    pagedown.init_app(app)

    if app.config['SSL_REDIRECT']:
        from flask_sslify import SSLify
        sslify = SSLify(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')
    
    # шалоны к реакту пока не нужны 
    # from .react import B_react as react_blueprint
    # app.register_blueprint(react_blueprint, url_prefix='/react')
 
    return app

