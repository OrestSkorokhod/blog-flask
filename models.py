from app import db
from datetime import datetime
import re

from flask_security import UserMixin, RoleMixin
 
	
def slugify(s):
	pattern = r'[^\w+]'
	return re.sub(pattern, '-', s)


roles_users = db.Table('roles_users',
	db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
	db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
	)

class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(140))
	password = db.Column(db.String(255))
	active = db.Column(db.Boolean())
	email = db.Column(db.String(100))
	roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))

	posts = db.relationship('Post', backref='user', lazy='dynamic')

	def __repr__(self):
		return '{}'.format(self.name)


class Role(db.Model, RoleMixin):
	id = db.Column(db.Integer(), primary_key=True)
	name = db.Column(db.String(100), unique=True)
	description = db.Column(db.String(255))

class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(140))
	subtitle = db.Column(db.String(140))
	slug = db.Column(db.String(140), unique=True)
	body = db.Column(db.Text)
	created = db.Column(db.DateTime, default=datetime.now())

	def __init__(self, *args, **kwargs):
		super(Post, self).__init__(*args, **kwargs)
		self.generate_slug()

	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	def generate_slug(self):
		if self.title:
			self.slug = slugify(self.title)

	def __repr__(self):
		return '<Post id: {}, title: {} >'.format(self.id, self.title)




