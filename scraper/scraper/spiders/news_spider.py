import scrapy

class NewsSpider(scrapy.Spider):
    name = "news"
    start_urls = [
	#CNN pages
        "http://www.cnn.com/politics",
        "http://www.cnn.com/world",
        "http://www.cnn.com/health",
        "http://www.cnn.com/travel",
        "http://www.cnn.com/tech",
        "http://www.cnn.com/us",

	#BBC
	"http://www.bbc.com/travel",
	"http://www.bbc.com/news/world",
	"http://www.bbc.com/news/world/us_and_canada",	
	"http://www.bbc.com/news/technology",
	"http://www.bbc.com/news/health",
	]

    def parse(self, response):
        filename = response.url.split("/")[-1] + '.html'
	file2 = response.url.split(".")[-2]
	filename = file2+"_"+filename
        with open(filename, 'wb') as f:
            f.write(response.body)



