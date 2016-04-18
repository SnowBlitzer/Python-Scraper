import scrapy

class NewsSpider(scrapy.Spider):
    name = "news"
    start_urls = [
        #Guardian
        "http://www.theguardian.com/us-news",
        "http://www.theguardian.com/us-news/us-elections-2016",
        "http://www.theguardian.com/us/technology",
        "http://www.theguardian.com/world",
        #Independent
        "http://www.independent.co.uk/news/uk/politics",
        "http://www.independent.co.uk/news/business",
        "http://www.independent.co.uk/news/world",
        "http://www.independent.co.uk/news/world/americas",
        "http://www.independent.co.uk/life-style/gadgets-and-tech",
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


        if "bbc" in file2:
            self.bbc_work(response, file_name)
        if "foxbusiness" in file2:
            self.fox_work(response, file_name)
        if "independent" in file2:
            self.independent_work(response, file_name)
        if "guardian" in file2:
            self.guardian_work(response, file_name)
        else:
            self.make_files(response, file_name)



    def bbc_work(self,response, file_name):
        html_file, json_file = self.make_files(response,file_name)

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
        html_file, json_file = self.make_files(response,file_name)

        head = "<h3><a href="
        url = "http://www.foxbusiness.com"

        news = open(html_file,'r+')
        jfile = open(json_file,'wb')

        self.extactor(head,url,news,jfile)


    def independent_work(self, response, file_name):
        html_file, json_file = self.make_files(response,file_name)

        head = "<h1><a href=\""

        url = "http://www.independent.co.uk"

        news = open(html_file,'r+')
        jfile = open(json_file,'wb')

        self.extactor(head,url,news,jfile)


    def guardian_work(self, response, file_name):
        html_file, json_file = self.make_files(response,file_name)

        head = "<a href=\""
        url = "http://www.theguardian.com/"
        news = open(html_file,'r+')
        jfile = open(json_file,'wb')


        for href in news.readlines():
            if head in href:
                title = href.split("<")[-2]
                title = title.split(">")[-1]
                if title == "":
                    continue

                title = "{\"title\": \"" + title +"\",\n"

                link = href.split("href=\"")[1]
                link = link.split("\"")[0]
                if "http" not in link:
                    link = url +link
                if "theguardian" not in link:
                    continue
                link = "\"url\": \"" + link +"\",}\n"
                jfile.write(title+link)
                link = ""
                title = ""


    def make_files(self, response, file_name):
        html_file = file_name + ".html"
        json_file = file_name + ".json"

        with open(html_file, 'wb') as f:
            f.write(response.body)

        return html_file, json_file


    def extactor(self,head,url,news,jfile):
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
                link = ""
                title = ""
