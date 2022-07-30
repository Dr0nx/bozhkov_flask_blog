import os
from secrets import token_hex

from PIL import Image
from flask import current_app, url_for
from flask_mail import Message

from flask_blog import mail


def save_picture(form_picture):
    random_hex = token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static', 'profile_pics', picture_fn)

    im = Image.open(form_picture)
    old_size = im.size  # old_size[0] is in (width, height) format

    desired_size = 150
    ratio = float(desired_size) / max(old_size)
    new_size = tuple([int(x * ratio) for x in old_size])

    # use thumbnail() or resize() method to resize the input image
    # thumbnail is a in-place operation
    # im.thumbnail(new_size, Image.ANTIALIAS)
    im = im.resize(new_size, Image.ANTIALIAS)

    # create a new image and paste the resized on it
    new_im = Image.new("RGB", (desired_size, desired_size))
    new_im.paste(im, ((desired_size - new_size[0]) // 2,
                      (desired_size - new_size[1]) // 2))

    new_im.save(picture_path)

    return picture_fn


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Запрос на сброс пароля', sender='dr0nx@yandex.ru', recipients=[user.email])
    msg.body = f'''
Здравствуйте!

Чтобы сбросить пароль, перейдите по следующей ссылке: \n
{url_for('users.reset_token', token=token, _external=True)}. \n
Если вы не делали этот запрос, просто проигнорируйте это письмо.'''
    mail.send(msg)
