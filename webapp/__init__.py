from flask import Flask 
#from testproj import config

my_app = Flask(__name__)
my_app.config.from_object("config")
#WTF_CSRF_ENABLED = True
#SECRET_KEY = 'somesuperdupersecretkey'


from app import views
