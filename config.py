import os

class Config:
    '''
    General configuration parent class
    '''

    SECRET_KEY ='1234'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://hudson:1234@localhost/pitchh'
    UPLOADED_PHOTOS_DEST ='app/static/photos'

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("oliveenterprise2@gmail.com")
    MAIL_PASSWORD = os.environ.get("NOTEKCS158M")



class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://hudson:1234@localhost/pitchh'

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings

    '''

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://hudson:1234@localhost/pitchh'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig

}
