from flask import url_for, redirect
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from wtforms import validators

from flask_blog.models import Post, User


class UserView(ModelView):
    column_display_pk = True
    column_labels = {
        'id': 'ID',
        'username': 'Имя пользователя',
        'last_seen': 'Последний вход',
        'image_file': 'Аватар',
        'posts': 'Посты',
        'email': 'Почта',
        'password': 'Пароль',
        'role': 'Роль',
        'file': 'Выберите изображение'
    }
    column_list = ['id', 'role', 'username', 'email', 'password', 'last_seen', 'image_file']
    column_default_sort = ('username', True)
    column_sortable_list = ('id', 'role', 'username', 'email')
    can_create = True
    can_edit = True
    can_delete = False
    can_export = True
    export_max_rows = 100
    export_types = ['json']
    form_args = {
        'username': dict(label='Пользователь', validators=[validators.DataRequired()]),
        'email': dict(label='Почта', validators=[validators.Email()]),
        'password': dict(label='Пароль', validators=[validators.DataRequired()])
    }
    AVAILABLE_USER_TYPES = [
        (u'Админ', u'Админ'),
        (u'Автор', u'Автор'),
        (u'Редактор', u'Редактор'),
        (u'Пользователь', u'Пользователь')
    ]
    form_choices = {
        'role': AVAILABLE_USER_TYPES,
    }
    column_descriptions = dict(username='Имя и, возможно, фамилия')
    column_exclude_list = ['password']
    column_searchable_list = ['email', 'username']
    column_filters = ['email', 'username']
    column_editable_list = ['role', 'username', 'email']
    create_modal = True
    edit_modal = True
    form_excluded_columns = ['id']


def name_gen_image(model, file_data):
    hash_name = f'{model.author}/post_id-{model.id}/{file_data.filename}'
    return hash_name


class PostView(ModelView):
    column_labels = {
        'id': 'ID',
        'author': 'Автор',
        'tag_post': 'Тег поста',
        'title': 'Заголовок',
        'image_post': 'Изображение поста',
        'category': 'Категория',
        'slug': 'Слаг',
        'text': 'Текст',
        'date': 'Дата',
        'user': 'Пользователь',
        'username': 'Имя',
        'tag': 'Тег',
        'tags': 'Теги',
        'name': 'Имя',
    }

    can_create = True
    can_edit = True
    can_delete = True

    column_list = ['id', 'author', Post.title, 'image_post', 'tags']
    column_default_sort = ('title', True)
    column_sortable_list = ('id', 'author', 'title', 'tags')
    column_exclude_list = []
    column_searchable_list = ['title']
    column_filters = ['title', User.username, 'tags']
    column_editable_list = ['title']

    create_modal = True
    edit_modal = True

    form_widget_args = {
        'text': {
            'rows': 5,
            'class': 'w-100 border border-info text-success'
        },

        'image_post': {
            'class': 'btn btn-success btn-lg'
        }
    }


class CommentView(ModelView):
    column_labels = {
        'name': 'Имя комментария'
    }
    can_delete = True
    can_create = True
    can_edit = True


class TagView(ModelView):
    column_labels = {
        'name': 'Имя тега',
        'tag_post': 'Посты тега',
    }
    can_delete = True
    can_create = True
    can_edit = True


class MyAdminModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('main.home'))
