import scrapy

class NewsSpider(scrapy.Spider):
    name = "news"
    start_urls = [

        "http://www.abcnews.go.com/US",

        #FOX
        "http://www.foxbusiness.com/politics.html",
        "http://www.foxbusiness.com/markets.html",
        "http://www.foxbusiness.com/category/technology.html",
    	#BBC
    	"http://www.bbc.com/news/world",
    	"http://www.bbc.com/news/world/us_and_canada",
    	"http://www.bbc.com/news/technology",
    	"http://www.bbc.com/news/health",
	]

    def parse(self, response):
        file1 = response.url.split("/")[-1]
        file2 = response.url.split(".")[-1]

        if "html" in file2:
            file2 = response.url.split(".")[-3]
            file1 = file1.split(".")[0]
        else:
            file2 = response.url.split(".")[1]
        file_name= file2+"_"+file1


        if file2 == "bbc":
            self.bbc_work(response, file_name)
        if file2 == "foxbusiness":
            self.fox_work(response, file_name)
        #if file2 == "go":
        #    print("Yes maybe?")
        #    head = "<a href"



    def bbc_work(self,response, file_name):
        html_file = file_name + ".html"
        json_file = file_name + ".json"

        with open(html_file, 'wb') as f:
            f.write(response.body)

        head = "title-link__title-text"
        url_head = "class=\"title-link\""

        url = "http://www.bbc.com"

        news = open(html_file,'r+')
        jfile = open(json_file,'wb')

        link = ""
        title = ""
        for href in news.readlines():
            if url_head in href:
                link = href.split("href=\"")[1]
                link = link.split("\"")[0]
                if "http" not in link:
                    link = url +link
                link = "\"url\": \"" + link +"\",}\n"

            if head in href:
                title = href.split("<")[-2]
                title = title.split(">")[-1]
                title = '{\"title\": \"' + title +"\",\n"

            if link is not "" and title is not "":
                jfile.write(title+link)
                title = ""
                link = ""




    def fox_work(self,response, file_name):
        html_file = file_name + ".html"
        json_file = file_name + ".json"

        with open(html_file, 'wb') as f:
            f.write(response.body)

        head = "<h3><a href="
        url = "http://www.foxbusiness.com"

        news = open(html_file,'r+')
        jfile = open(json_file,'wb')

        for href in news.readlines():
            if head in href:
                title = href.split("<")[-3]
                title = title.split(">")[-1]
                title = "{\"title\": \"" + title +"\",\n"

                link = href.split("href=\"")[1]
                link = link.split("\"")[0]
                if "http" not in link:
                    link = url +link
                link = "\"url\": \"" + link +"\",}\n"
                jfile.write(title+link)

    def abc_work(self, response):
        pass

    def make_files(self, response, file_name):
        pass
