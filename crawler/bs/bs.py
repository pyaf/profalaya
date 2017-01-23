# _*_ coding:utf-8 _*_
import requests
from bs4 import BeautifulSoup as bs
import os
import csv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

print(BASE_DIR)
profile_data = os.path.join(BASE_DIR, "data\profile_data.csv")
response = requests.get('http://www.iitbhu.ac.in/mec/index.php/people/faculty.html')

soup = bs(response.text, 'html.parser')
links = [a.attrs.get('href') for a in soup.select('a[href]')]
data  = soup.getText()
with open(profile_data, 'w', newline='') as csvfile:
    file = csv.writer(csvfile)
    for string in soup.stripped_strings:
        string = string.replace('  ','').replace('\n','').replace('\t','')
        if string[0] != '<' and repr(string) != "'Designation:'" and repr(string) != "'Qualification:'" and repr(string) != "'Phone No.:'" and repr(string) !='Area of Interest:' and repr(string) != "'Email:'" and repr(string) != "'View Profile'":
            file.writerow([string])
        # pass
        # print(repr(string).encode('utf-8')[1:-1])
# print(data.encode('utf-8'))
# print(data.replace("\t", "").replace("\r", "").replace("\n", "").replace("\xc2","").replace("\xa0","").encode('utf-8'))
# for i in data:
#     print(i.encode('utf-8'))
# print(data)

# import re

#
# print(re.sub(r'[\t\r\n]', '', str(data)))
