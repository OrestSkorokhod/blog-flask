from flask import Blueprint
from flask import render_template
from flask import request

from models import Post, User

from flask_security import login_required

posts = Blueprint('posts', __name__, template_folder='templates')

@posts.route('/')
def index():
	

	page = request.args.get('page')

	if page and page.isdigit():
		page = int(page)
	else:
		page = 1


	posts = Post.query.order_by(Post.created.desc())
	users = User.query.all()

	pages = posts.paginate(page=page, per_page=5)

	return render_template('posts/index.html', posts=posts, users=users, pages=pages)

@posts.route('/<slug>')
def post_detail(slug):
	post = Post.query.filter(Post.slug==slug).first_or_404()
	user = User.query.filter(User.id==post.user_id).first_or_404()
	return render_template('posts/post_detail.html', post=post, user=user)