# -*- coding:utf-8 -*-

# from lxml import etree

# html = etree.parse('./test.html', etree.HTMLParser())

# res = html.xpath('//li[contains(@class, li) and @name="item"]/a/text()')

# print(res)

from bs4 import BeautifulSoup

soup = BeautifulSoup(open('./test.html'), 'lxml')

print(dir(soup))