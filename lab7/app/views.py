from flask import render_template, flash , redirect, url_for, request
from app import app, bcrypt, db
from app.forms import LoginForm, RegistrationForm, UpdateAccountForm, PostForm, UpdatePostForm
from .models import User, Post
from flask_login import current_user, login_user, logout_user, login_required
import secrets
from datetime import datetime
import os
from PIL import Image
from datetime import datetime as dt

@app.route('/')
def to_main():
	return render_template('layout.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('to_main'))

    login_form = LoginForm()
    if login_form.validate_on_submit():
        email = login_form.email.data
        password = login_form.password.data

        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            flash(f'Welcome back {user.username}', 'info')
            login_user(user)
            
            return redirect(url_for('account'))
        else:
            flash(f'Incorrect email or password', 'warning')
        
    return render_template('login.html', form=login_form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('to_main'))
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        hashed = bcrypt.generate_password_hash(password).decode('utf-8')

        user = User(username=username, email=email, password_hash=hashed)
        db.session.add(user)
        db.session.commit()
        flash("Sing up successfully")
        return redirect(url_for('to_main'))
    return render_template('register.html', form=form)

@app.route('/posts')
def posts():
    posts = Post.query.all()
    return render_template('posts.html', posts=posts)


@app.route('/logout')
def logout():
    logout_user()
    flash('Logged out')
    return redirect(url_for('to_main'))


@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.about_me = form.about_me.data
        if form.old_password.data:
            current_user.password_hash = bcrypt.generate_password_hash(form.new_password.data).decode('utf-8')
        db.session.commit()
        flash('Your account has been updated!', 'success')
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.about_me.data = current_user.about_me
    image_file = url_for('static', filename='images/thumbnails/' + current_user.image_file)
    return render_template('account.html', title='Account', image_file=image_file, form=form, user=current_user)


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    f_name, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = f_name + random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/images/thumbnails/', picture_fn)
    # form_picture.save(picture_path)

    output_size = (128, 128)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()


@app.route('/post/new', methods=['GET', 'POST'])
@login_required
def add_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, body=form.body.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash("Post was created", category="info")
        return redirect(url_for('posts'))

    return render_template('create_post.html', form=form)

@app.route('/post/<int:post_id>', methods=['GET', 'POST'])
@login_required
def post(post_id):
    post = Post.query.filter_by(id=post_id).first()
    form = UpdatePostForm()

    if current_user.username != post.author.username:
        flash("Its not your post", category="eror")
        return redirect(url_for('posts'))

    elif form.validate_on_submit():
        post.title = form.title.data
        post.body = form.body.data
        post.updatetime = datetime.utcnow()
        db.session.commit()
        flash("Post was updated", category="info")
        return redirect(url_for('post', post_id=post.id))

    elif "delete" in request.form:
        db.session.delete(post)
        db.session.commit()
        flash("Post deleted", category="eror")
        return redirect(url_for('posts'))

    return render_template('post.html', post=post, form=form)