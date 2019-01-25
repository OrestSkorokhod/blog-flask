from app import app
from flask import render_template
from flask import url_for, redirect


@app.route('/')
def index():
	title = 'main title'
	return redirect(url_for('posts.index'))
	# return render_template('index.html', title=title)

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404