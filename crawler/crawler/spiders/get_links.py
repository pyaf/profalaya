import scrapy
from scrapy.http import Response, Request,HtmlResponse
import csv
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
prof_data = os.path.join(BASE_DIR, "data/test.csv")

print(prof_data)

class BlogSpider(scrapy.Spider):
    name = 'get_links'
    start_urls = ['http://www.iitbhu.ac.in/apc/faculty.html']

    def parse_title(self, response):
        print(response,response.css('title::text'))

    def parse(self, response):
        links = response.css('a ::attr(href)')
        with open(prof_data, 'a', newline='') as csvfile:
            file = csv.writer(csvfile)
            for x in links.extract():
                u = response.urljoin(x)
                Request(u, callback=self.parse_title)
                # print(re.css('title::text').extract_first())
                # file.writerow([url])
        # if links:
        #         yield scrapy.Request(response.urljoin(links), callback=self.parse)
#http://www.iitbhu.ac.in/apc/faculty.html
