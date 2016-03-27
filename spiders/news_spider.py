import scrapy

class NewsSpider(scrapy.Spider):
    name = "news"
    start_urls = [
        "http://www.cnn.com/politics/",
        "http://www.cnn.com/world/",
        "http://www.cnn.com/health/",
        "http://www.cnn.com/travel/",
        "http://www.cnn.com/money/",
        "http://www.cnn.com/tech/",
        "http://www.cnn.com/us/"
        ]

    def parse(self, response):
        filename = response.url.split("/")[-2] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)



