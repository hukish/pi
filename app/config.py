import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://hudson:12345@localhost/PITCHES'
    UPLOADED_PHOTOS_DEST ='app/static/photos'


     #email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    def init_app(app):
        pass
