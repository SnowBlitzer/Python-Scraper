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
    	"http://www.bbc.com/news/world",
    	"http://www.bbc.com/news/world/us_and_canada",	
    	"http://www.bbc.com/news/technology",
    	"http://www.bbc.com/news/health",
	]

    def parse(self, response):
        file1 = response.url.split("/")[-1]
        file2 = response.url.split(".")[-2]
        html_file = file2+"_"+file1  + '.html'
        json_file = file2+"_"+file1  + '.json'
        with open(html_file, 'wb') as f:
            f.write(response.body)
        
        news = open(html_file,'r+')
        head = "title-link__title-text"
        jfile = open(json_file,'wb')

        for href in news.readlines():
            if head in href:
                title = href.split("<")[-2]
                title = title.split(">")[-1]
                title = '{\"title\": \"' + title +"\"}\n"
                jfile.write(title)


