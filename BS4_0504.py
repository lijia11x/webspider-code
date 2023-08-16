
from bs4 import BeautifulSoup




html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
# 构造soup的方法
# soup = BeautifulSoup(open("index.html"), 'lxml')
# soup = BeautifulSoup("<html>data</html>", 'lxml')

soup = BeautifulSoup(html_doc, 'lxml')

# 美化html文档
print(soup.prettify())

# <title>The Dormouse's story</title>
# print(soup.title)

# title
# print(soup.title.name)

# The Dormouse's story
# print(soup.title.string)

# <head><title>The Dormouse's story</title></head>
# print(soup.title.parent)

# head
# print(soup.title.parent.name)

# Elsie
# print(soup.a.string)

# <class 'bs4.element.Tag'>
# print(type(soup.title))

# <b>The Dormouse's story</b>
# print(soup.body.b)

# 通过点取属性的方式只能获得当前名字的第一个tag:
# soup.a
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
# 如果想要得到所有的\<a>标签,或是通过名字得到比一个tag更多的内容的时候,就需要用到 Searching the tree 中描述的方法,比如: find_all()
# print(soup.find_all('a'))

tag = soup.a
# ['sister']
print(tag['class'])
# link1
print(tag['id'])
# {'href': 'http://example.com/elsie', 'class': ['sister'], 'id': 'link1'}
print(tag.attrs)