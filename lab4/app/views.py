from flask import render_template, flash , redirect, url_for
from app import app, bcrypt, db
from app.forms import LoginForm, RegistrationForm
from .models import User, Post


@app.route('/')
def to_main():
	return render_template('layout.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = User.query.filter_by(email=email).first()

        if user and bcrypt.check_password_hash(user.password_hash, password):
            flash("Sing in successfully")
            return redirect(url_for('to_main'))
        else:
            flash('Login or password is incorrect', 'warning')
    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        print(email)
        hashed = bcrypt.generate_password_hash(password).decode('utf-8')
        print(hashed)
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
