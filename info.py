import requests
from bs4 import BeautifulSoup
import csv

f = open('./href.csv', 'r')
wr = csv.reader(f)
url_list = []
for line in wr:
    url = 'https://serieson.naver.com/' + line[0]
    url_list.append(url)

temp = url_list[:3]
for url in temp:
    response = requests.get(url)
    print(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup)
    title = soup.select_one('#content > div.end_head.NE\=a\:mvi > h2').text
    print(title)
f.close()