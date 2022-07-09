from flask import url_for, redirect, request
from flask_admin import expose, AdminIndexView
from flask_login import current_user


class MyAdminMainView(AdminIndexView):

    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('users.login', next=request.url))

    @expose('/')
    def index(self):
        if not current_user.is_authenticated and current_user.is_admin:
            return redirect(url_for('users.login'))
        return super(MyAdminMainView, self).index()
