import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    FLASK_ENV = 'development'
    SECRET_KEY = os.urandom(20)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'site.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_ADMIN_SWATCH = 'spacelab'
    BABEL_DEFAULT_LOCALE = 'ru'

    # VK
    # VK_APP_ID = os.environ.get('VK_APP_ID')
    # VK_APP_SECRET = os.environ.get('VK_APP_SECRET')
    VK_APP_ID = 'a6c0d012a6c0d012a6c0d01238a6bd4d5baa6c0a6c0d012c426b7143b5a856c469cc0fc'
    VK_APP_SECRET = 'NEGWtskA51u8yiBm6bdS'

    MAIL_SERVER = 'smtp.yandex.ru'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'dr0nx@yandex.ru'
    MAIL_PASSWORD = 'KwfJ8WeyXrdMGR'
