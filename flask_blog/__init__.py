import locale

from flask import Flask
from flask_admin import Admin
from flask_babel import Babel
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_oauthlib.client import OAuth
from flask_sqlalchemy import SQLAlchemy

from flask_blog.config import Config
from flask_blog.errors.handlers import errors

db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()
mail = Mail()
babel = Babel()
oauth = OAuth()


def create_app(config_class=Config):
    locale.resetlocale()
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    mail.init_app(app)
    babel.init_app(app)
    oauth.init_app(app)

    from flask_blog.main.routes import main
    from flask_blog.users.routes import users
    from flask_blog.posts.routes import posts
    from flask_blog.admin.routes import MyAdminMainView
    from flask_blog.admin.views import UserView, PostView, CommentView, TagView, MyAdminModelView
    from flask_blog.models import User, Post, Comment, Tag

    app.register_blueprint(main)
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(errors)

    admin = Admin(app, 'Блог', index_view=MyAdminMainView(), template_mode='bootstrap4', url='/')
    admin.add_view(UserView(User, db.session, name='Пользователь'))
    admin.add_view(PostView(Post, db.session, name='Статьи'))
    admin.add_view(CommentView(Comment, db.session, name='Комментарии'))
    admin.add_view(TagView(Tag, db.session, name='Теги'))


    return app
