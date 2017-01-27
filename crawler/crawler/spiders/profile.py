import scrapy
import csv
import os
from bs4 import BeautifulSoup as bs
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
profile_data = os.path.join(BASE_DIR, "data/profile_data.csv")


class BlogSpider(scrapy.Spider):
    name = 'profile'
    start_urls = ['http://www.iitbhu.ac.in/ece/index.php/people/faculty-members.html']
    def parse(self, response):


        # a = response.css('a::attr(href)').extract()
        # names = response.css('p::text').extract()
        # images = response.css('img::attr(src)').extract()
        # with open(profile_data, 'w', newline='') as csvfile:
        #     file = csv.writer(csvfile)
        #     for name in names:
        #         if not name.isspace():
        #             name = name.replace('\n',' ')
        #             name = name.replace('  ','')
        #             if name != "Qualification:" and name !="Designation:" and name != "AreaofInterest:" and name !="MobileNo.:" and name!="PhoneNo.:" and name != "Email:":
        #                 file.writerow([name])
        #     for x in a:
        #         # print(x, response.urljoin(x))
        #         file.writerow([response.urljoin(x)])
        #     for y in images:
        #         file.writerow([response.urljoin(y)])
