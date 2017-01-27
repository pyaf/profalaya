'''
apc
'''
import scrapy
import csv
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
apc_profile_links = os.path.join(BASE_DIR, "data/apc_profile_links.csv")
apc_profile_data = os.path.join(BASE_DIR, "data/apc_profile_data.csv")


class BlogSpider(scrapy.Spider):
    name = '1'
    # with open(apc_profile_links, 'r', newline='') as apc_profile_links:
    #     apc_profile_links = csv.reader(apc_profile_links)
        # start_urls = [x[0] for x in apc_profile_links]
    start_urls = ['http://www.iitbhu.ac.in/apc/faculty.html']
    def parse(self, response):

        names = response.css('a::text').extract()

        links = response.css('a::attr(href)').extract()
        images = response.css('img::attr(src)').extract()
        p = response.css('p::text').extract()
        div = response.css('div::text').extract()
        with open(apc_profile_data, 'w', newline='') as csvfile:
            file = csv.writer(csvfile)
            # for name, link,image in zip(names, links, images):
            #     file.writerow([name, response.urljoin(link), response.urljoin(image)])
            for name in set(names):
                file.writerow([name])
            for link in set(links):
                file.writerow([response.urljoin(link)])
            for image in set(images):
                file.writerow([response.urljoin(image)])
            x=0
            while True:
                try:
                    print(p[x+2],p[x],p[x+1])
                    email = p[x+2].split(' ')[-1]
                    print(email)
                    phone = p[x]
                    print(phone)
                    desig = p[x+1]
                    print(email,phone, desig)
                    file.writerow([email+";"+desig+";"+phone+";"])
                    x+=3
                except Exception as e:
                    print(e)
                    break
            for x in div:
                if not x.isspace():
                    file.writerow([x])
'''
cse
'''
import scrapy
import csv
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
profile_data = os.path.join(BASE_DIR, "data/profile_data.csv")


class BlogSpider(scrapy.Spider):
    name = 'profile'
    start_urls = ['http://www.iitbhu.ac.in/cse/index.php/people/faculty.html']
    def parse(self, response):

        # a = response.css('a::attr(href)').extract()
        # names = response.css('span::text').extract()
        a = response.css('img::attr(src)').extract()
        with open(profile_data, 'a', newline='') as csvfile:
            file = csv.writer(csvfile)
            # for name in names:
            #     if not name.isspace():
            #         name = name.replace("\n","")
            #         name = name.replace("  ","")
            #         file.writerow([name])
            for x in a:
                print(x, response.urljoin(x))
                file.writerow([response.urljoin(x)])
'''
eee
'''

import scrapy
import csv
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
profile_data = os.path.join(BASE_DIR, "data/profile_data.csv")


class BlogSpider(scrapy.Spider):
    name = 'profile'
    start_urls = ['http://www.iitbhu.ac.in/eee/index.php/peo/faculty.html']
    def parse(self, response):

        a = response.css('a::attr(href)').extract()
        names = response.css('p::text').extract()
        images = response.css('img::attr(src)').extract()
        with open(profile_data, 'w', newline='') as csvfile:
            file = csv.writer(csvfile)
            for name in names:
                if not name.isspace():
                    # name = name.replace("\n","")
                    # name = name.replace("  ","")
                    file.writerow([name])
            for x in a:
                # print(x, response.urljoin(x))
                file.writerow([response.urljoin(x)])
            for y in images:
                file.writerow([response.urljoin(y)])
'''
ece
'''
import scrapy
import csv
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
profile_data = os.path.join(BASE_DIR, "data/profile_data.csv")


class BlogSpider(scrapy.Spider):
    name = 'profile'
    start_urls = ['http://www.iitbhu.ac.in/ece/index.php/people/faculty-members.html']
    def parse(self, response):

        a = response.css('a::attr(href)').extract()
        names = response.css('font::text').extract()
        images = response.css('img::attr(src)').extract()
        with open(profile_data, 'w', newline='') as csvfile:
            file = csv.writer(csvfile)
            for name in names:
                if not name.isspace():
                    name = name.replace('\n',' ')
                    name = name.replace('  ','')
                    if name != "Qualification:" and name !="Designation:" and name != "AreaofInterest:" and name !="MobileNo.:" and name!="PhoneNo.:" and name != "Email:":
                        file.writerow([name])
            for x in a:
                # print(x, response.urljoin(x))
                file.writerow([response.urljoin(x)])
            for y in images:
                file.writerow([response.urljoin(y)])
