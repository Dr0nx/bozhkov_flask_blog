import os

from flask import url_for
from flask_admin import expose, AdminIndexView
from flask_login import login_user, logout_user
from sqlalchemy import desc

from flask_blog import login_manager, admin
from flask_blog.models import Post, User

file_path = os.path.abspath(os.path.dirname(__name__))


# @admin.route('/login')
# def login():
#     user = User.query.get(1)
#     login_user(user)
#     return 'Вход'
#
#
# @admin.route('/logout')
# def logout():
#     logout_user()
#     return 'Выход'


class MyAdminMainView(AdminIndexView):

    @expose('/')
    def admin_main(self):
        posts = Post.query.order_by(desc(Post.date_posted)).all()
        image = url_for('static', filename='storage/post_img')
        return self.render('admin/index.html')
