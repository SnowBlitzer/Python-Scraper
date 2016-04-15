from flask import render_template 
from app import my_app
from app.forms import ArticleSearch
#import bbc_technology.json #impost w.e function makes json file instead
import json
@my_app.route('/')
@my_app.route('/index')
def index():
	return render_template('index.html')
	#return "HI there"

@my_app.route('/search', methods=['GET', 'POST']) 
def search(): 
    form = ArticleSearch() 
    f = open("bbc_technology.json", 'rb')
    posts = []
    for line in f:
	temp = line[11:]
	posts.append(temp.rsplit('"')[0])	
    print posts	
    if form.validate_on_submit(): #when user hits submit, make posts
	article_name = form.article_name.data
	news_site = form.news_site.data
	#posts = get_posts(article_names, news_site)
	#posts = bbc_technology.json
	#print posts
	f = open("bbc_technology.json", 'rb')
    return render_template('search.html', title='Search for an Article', form=form) 
