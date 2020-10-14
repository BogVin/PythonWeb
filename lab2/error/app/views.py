from flask import render_template
from app import app



@app.route('/')
def to_main():
	return render_template('layout.html')


@app.route('/home')
def to_home():
	return render_template('home.html')

@app.route('/about')
def to_about():
	return render_template('about.html')
