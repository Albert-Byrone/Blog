from flask import Flask 
from config import config_options
from flask_bootstrap import Bootstrap

bootstap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_options[config_name])
    from .auth import auth as authentication_blueprint
    from .main import main as main_blueprint
    bootstap.init_app(app)

    app.register_blueprint(authentication_blueprint)
    app.register_blueprint(main_blueprint)


    return app