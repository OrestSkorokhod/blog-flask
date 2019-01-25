class Configuration(object):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:1@localhost/blog_flask'
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SECRET_KEY = '123'

	SECURITY_PASSWORD_SALT = 'salt'
	SECURITY_PASSWORD_HASH = 'sha512_crypt'
		