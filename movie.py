import requests
from bs4 import BeautifulSoup
import csv

f = open('./href.csv', 'w', newline='')
wr = csv.writer(f)
# wr.writerow(['href'])

href = []
 # 페이지 전환
for i in range(1, 41):
    url = 'https://serieson.naver.com/movie/categoryList.nhn?categoryCode=ALL&orderType=sale&sortingType=&mobileYn=&drmFreeYn=&freeYn=&discountYn=&tagCode=&page={i}'
    # number = '1'

    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup)

    div = soup.select('#content > div > ul')

    for ul in div:
        a_list = ul.select('a')
        for a in a_list : 
            wr.writerow([a['href']])
            href.append(a['href'])

f.close()