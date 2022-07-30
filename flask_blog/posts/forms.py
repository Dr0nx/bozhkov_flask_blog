from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, SubmitField, TextAreaField, FileField
from wtforms.validators import DataRequired, InputRequired


class PostForm(FlaskForm):
    title = StringField('Заголовок', validators=[DataRequired()])
    content = TextAreaField('Статья', validators=[DataRequired()])
    picture = FileField('Изображение (png, jpg)', validators=[FileAllowed(['png', 'jpg'])])
    submit = SubmitField('Опубликовать')


class PostUpdateForm(FlaskForm):
    title = StringField('Заголовок', validators=[DataRequired()])
    content = TextAreaField('Статья', validators=[DataRequired()])
    picture = FileField('Изображение (png, jpg)', validators=[FileAllowed(['png', 'jpg'])])
    submit = SubmitField('Опубликовать')


class CommentForm(FlaskForm):
    body = StringField('Ваш комментарий', validators=[InputRequired()])
    submit = SubmitField('Опубликовать')


class CommentUpdateForm(FlaskForm):
    body = StringField('Заголовок', validators=[DataRequired()])
    submit = SubmitField('Опубликовать')
