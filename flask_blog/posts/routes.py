from flask import render_template, url_for, flash, redirect, request, abort, Blueprint
from flask_login import current_user, login_required

from flask_blog import db
from flask_blog.models import Post, Comment
from flask_blog.posts.forms import PostForm, CommentForm, CommentUpdateForm
from flask_blog.posts.utils import save_picture_post

posts = Blueprint('posts', __name__)


@posts.route('/')
@posts.route('/allpost')
# @login_required
def allpost():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('allpost.html', posts=posts, legend='Посты')


@posts.route('/post/new', methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        if form.picture.data.filename:
            post = Post(title=form.title.data, content=form.content.data,
                        image_post=form.picture.data, author=current_user)

            picture_file = save_picture_post(form.picture.data)
            post.image_post = picture_file

        else:
            post = Post(title=form.title.data, content=form.content.data,
                        author=current_user)

        db.session.add(post)
        db.session.commit()
        flash('Ваш пост создан!', 'success')
        return redirect(url_for('posts.allpost'))

    image_file = url_for('static', filename=f'images/' + current_user.username + current_user.image_file)

    return render_template('create_post.html',
                           title='Новый пост',
                           form=form,
                           legend='Новый пост',
                           image_file=image_file)


@posts.route('/post/<int:post_id>', methods=['GET', 'POST'])
@login_required
def post(post_id):
    post = Post.query.get_or_404(post_id)
    comment = Comment.query.filter_by(post_id=post.id).order_by(db.desc(Comment.date_posted)).all()
    db.session.commit()
    form = CommentForm()
    if request.method == 'POST' and form.validate_on_submit():
        username = current_user.username
        comment = Comment(username=username, body=form.body.data, post_id=post_id)
        db.session.add(comment)
        db.session.commit()
        flash('Комментарий к посту был добавлен', 'success')
        return redirect(url_for('posts.post', post_id=post.id))

    return render_template('post.html', title=post.title, post=post, post_id=post_id, form=form, comment=comment)


@posts.route('/post/<int:post_id>/update', methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)

    if post.author != current_user:
        abort(403)
    form = PostForm()

    if form.validate_on_submit():
        if form.picture.data.filename:
            picture_file = save_picture_post(form.picture.data)
            post.image_post = picture_file
        else:
            post = Post(title=form.title.data, content=form.content.data, author=current_user)

        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Ваш пост обновлен!', 'success')
        return redirect(url_for('posts.post', post_id=post.id))

    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content

    return render_template('create_post.html', title='Обновление поста', form=form, legend='Обновление поста')


@posts.route('/post/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    # !!! ?
    db.session.delete(post)
    db.session.commit()
    flash('Ваш пост был удален!', 'success')
    return redirect(url_for('posts.allpost'))


@posts.route('/comment/<int:comment_id>/update/', methods=['GET', 'POST'])
@login_required
def update_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    form = CommentUpdateForm()
    if current_user.is_admin or comment.username == current_user.username:
        if request.method == 'GET':
            form.body.data = comment.body
        if request.method == 'POST' and form.validate_on_submit():
            comment.body = form.body.data
            db.session.commit()
            return redirect(url_for('posts.post', post_id=comment.post_id))
    else:
        abort(403)
    return render_template('update_comment.html', form=form, title="Обновление комментария")


@posts.route('/comment/<int:comment_id>/delete/', methods=['GET', 'POST'])
@login_required
def delete_comment(comment_id):
    single_comment = Comment.query.get_or_404(comment_id)
    db.session.delete(single_comment)
    db.session.commit()
    flash('Ваш комментарий был удален!', 'success')
    return redirect(url_for('posts.post', post_id=single_comment.post_id))
