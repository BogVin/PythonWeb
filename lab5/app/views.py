from flask import render_template, flash , redirect, url_for
from app import app, bcrypt, db
from app.forms import LoginForm, RegistrationForm
from .models import User, Post
from flask_login import current_user, login_user, logout_user, login_required


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

@app.route('/account')
@login_required
def account():
    return render_template('account.html')
