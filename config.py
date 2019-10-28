import os
class Config:
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://byrone:Albert254@localhost/blog'
    SQLALCHEMY_DATABASE_URI=os.environ.get("DATABASE_URL")
    SECRET_KEY = os.environ.get("SECRET_KEY")
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


class ProdConfig(Config):
    pass

class DevConfig(Config):
    pass

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}