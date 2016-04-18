from flask import render_template
import app
from app.forms import ArticleSearch
#import bbc_technology.json #impost w.e function makes json file instead
import json

#For spider
from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy.settings import Settings
from scrapy import signals
import scrapy

from news_spider import NewsSpider


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
		crawls()

		article_name = form.article_name.data
		news_site = form.news_site.data
		#posts = get_posts(article_names, news_site)
		#posts = bbc_technology.json
		#print posts
		f = open("bbc_technology.json", 'rb')
	return render_template('search.html', title='Search for an Article', form=form)

def crawls():
	spider = NewsSpider()
	crawler = Crawler(spider, Settings())
	crawler.signals.connect(reactor.stop, signal=signals.spider_closed)
	crawler.crawl()
	reactor.run(installSignalHandlers=False)
	#reactor.run(installSignalHandlers=False) # the script will block here
