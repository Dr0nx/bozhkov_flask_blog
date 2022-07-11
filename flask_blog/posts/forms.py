from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, InputRequired


class PostForm(FlaskForm):
    title = StringField('Заголовок', validators=[DataRequired()])
    content = TextAreaField('Текст', validators=[DataRequired()])
    submit = SubmitField('Сохранить')


class CommentForm(FlaskForm):
    body = StringField('Ваш комментарий', validators=[InputRequired()])
    submit = SubmitField('Опубликовать')


class CommentUpdateForm(FlaskForm):
    body = StringField('Заголовок', validators=[DataRequired()])
    submit = SubmitField('Опубликовать')
