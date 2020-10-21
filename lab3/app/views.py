from flask import render_template, flash , redirect
from app import app
from app.forms import LoginForm

@app.route('/')
def to_main():
	return render_template('layout.html')


@app.route('/login', methods=['GET', 'POST'])
def to_login():
	form = LoginForm()

	if form.validate_on_submit():
		flash('Login requested for user {}, password={}'.format(
			form.username.data, form.password.data))
		return redirect('/login')
	return render_template('login.html', form=form)
