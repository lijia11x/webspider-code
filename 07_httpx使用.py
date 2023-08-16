# -*- coding:utf-8 -*-

# import httpx
# from bs4 import BeautifulSoup
# url = 'https://spa16.scrape.center/'
# client = httpx.Client(http2=True)
# response = client.get(url)
# soup = BeautifulSoup(response.text,'lxml')
# print(soup.prettify())
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
url = 'https://ssr1.scrape.center/'

response = requests.get(url)

# print(response.text)

soup = BeautifulSoup(response.text,'lxml')
movies = []
for href in soup.find('ul',class_='el-pager').find_all('a'):
    print(href.attrs['href'])
    page_url = urljoin(url,href.attrs['href'])
    page_response = requests.get(page_url)
    page_soup = BeautifulSoup(page_response.text,'lxml')


# print(soup.prettify())

    for i in page_soup.find_all('div', class_= 'el-card__body'):
        # print('----------------------------------------------')
        # print(i)
        single_movie = {}
        print('==================================================')
        name = i.h2.string
        pic_url = i.img.attrs['src']
        detail_url = urljoin(url,i.a.attrs['href'])
        print(detail_url)
        res1 = requests.get(detail_url)
        res1.encoding ='utf-8'
        soup1 = BeautifulSoup(res1.text,'lxml')
        # print(soup1.prettify())
        print('->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->')

        tag = list(soup1.find('div', class_='categories').stripped_strings)

        introduction = list(soup1.find('div', class_='drama').stripped_strings)
        score = list(soup1.find('p', class_='score m-t-md m-b-n-sm').stripped_strings)
        single_movie['name'] = name
        single_movie['tag'] = tag
        single_movie['introduction'] = introduction[1]
        single_movie['score'] = score[0]
        mvsm_info = []
        for j in list(soup1.find_all('div', class_='m-v-sm info')):
            # print(j)
            # print(list(e for e in j.strings if e != '\n'))
            mvsm_info += list(e for e in j.strings if e != '\n' and e != ' / ')
        single_movie['mvsm_info'] = mvsm_info
        print(single_movie)
        movies.append(single_movie)
print(movies)

