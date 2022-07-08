import os


class Config:
    FLASK_ENV = 'development'
    SECRET_KEY = os.urandom(20)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    FLASK_ADMIN_SWATCH = 'spacelab'
    BABEL_DEFAULT_LOCALE = 'ru'

    MAIL_SERVER = 'smtp.yandex.ru'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'dr0nx@yandex.ru'
    MAIL_PASSWORD = 'KwfJ8WeyXrdMGR'
