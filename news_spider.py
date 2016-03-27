from __future__ import print_function
import scrapy

class NewsSpider(scrapy.Spider):
	name = 'test'
	start_url = ['http://www.salon.com/']

	def parse(self, response):
		print(response)
		for href in response.css('.plain .gaTrackLinkEvent'):
			full_url = response.urljoin(href.extract())
			yield scrapy.Request(full_url, callback=self.parse_question)

	def parse_question(self, response):
		yield {
			'title': response.css('h1').extract(),
			'subtitle': response.css('h2').extract(),
			'date': response.css('.toLocalTime').extract(),
		}
