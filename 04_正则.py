import re
from bs4 import BeautifulSoup
# with open(r'C:\Lesson\爬虫从入门到应用\2022_06_08直播数据解析_正则\素材\豆瓣.html','r',encoding='utf-8') as f:
# con = f.read()
# print(con)
# <a href="https://book.douban.com/subject/27132313/">未尽之路：世界电影地图亚洲和大洋洲卷</a>
# book_compile = re.compile(r'<a href="https://book.douban.com/subject/\d+/">(.*?)</a>')
# book_list = book_compile.findall(con)
# print(book_list)
# <img src="https://img3.doubanio.com/mpic/s29507081.jpg"/>
# image_compile = re.compile(r'<img src="https://img3.doubanio.com/mpic/\w+\.jpg"/>')
# image_list = image_compile.findall(con)
# print(image_list)
# with open('img.html','w+') as f1:
#     for i in image_list:
#         f1.write(i)
'''
     <p>
                        “暗黑美学大师”涩泽龙彦对挚友三岛由纪夫的追忆之作，展现了两人倾心相交十余年的点滴，从几个不同角度解读了三岛时代。        
                    </p>
'''
# snapshot_compile = re.compile(r'<p class="detail">(.*?)</p>',re.S)
# snapshot_compile = re.compile('<p class="color-gray">(.*?)</p>',re.DOTALL)
# snapshot_compile = re.compile('<div class="detail-frame">(.*?)</div>',re.DOTALL)
# snapshot_compile = re.compile('(?:<p class="color-gray">.*?</p>)|(?:<p class="detail">.*?</p>)',re.DOTALL)
# snapshot_list = snapshot_compile.findall(con)
# print(snapshot_list)


# with open(r'C:\Lesson\爬虫从入门到应用\2022_06_08直播数据解析_正则\素材\股票.html', 'r',encoding='utf-8') as f:
#     con = f.read()
#     tr_compile = re.compile(r'<tr>.*?</tr>', re.DOTALL)
#     tr_list = tr_compile.findall(con)
#     # print(tr_list)
#     shares_list = []
#     for tr in tr_list:
#         shares_code_compile = re.compile(r'<a href="//stock\.quote\.stockstar\.com/\d+\.shtml">(\d+)</a>')
#         shares_name_compile = re.compile(r'<a href="//stock\.quote\.stockstar\.com/\d+\.shtml">(.[^0-9]*?)</a>',re.DOTALL)
#         shares_num_compile = re.compile(r'<td class="align_right ">(\d+\.\d+)</td>')
#
#
#         # print(tr)
#         if shares_code_compile.search(tr):
#             shares_code = shares_code_compile.search(tr).group(1)
#             shares_name = shares_name_compile.search(tr).group(1)
#             shares_num = shares_num_compile.findall(tr)
#             print(shares_code)
#             print(shares_name)
#             print(shares_num)
#             # a = [x for x in shares_num]
#             shares_list.append([shares_code, shares_name] + shares_num)
#             print(shares_list)
#
#
#         else:
#             print('匹配失败')
# print(shares_list)

# with open(r'C:\Lesson\爬虫从入门到应用\2022_06_08直播数据解析_正则\素材\大学排名.html', 'r',encoding='utf-8') as f:
#     con = f.read()
#     soup = BeautifulSoup(con, 'lxml')
#     print(soup.prettify())
#     # print(con)
#     total_rank = []
#     pattern = re.compile('<tbody>.*?</tbody>',re.S)
#     res = pattern.search(con).group()
#     tr_list = re.findall(r'<tr class="\w+">.*?</tr>', res, re.S)
#     for tr in tr_list:
#         rank = re.findall('<center>(\d+)</center>',tr)[1]
#         # print(tr)
#         print(rank)
#         univercity_name = re.search(r'<a href=".*?" target="_blank">(.*?)</a>', tr, re.S).group(1)
#         print(univercity_name)
#         total_rank.append([univercity_name,rank])
#     print(total_rank)


# with open(r'C:\Lesson\爬虫从入门到应用\2022_06_08直播数据解析_正则\素材\大学排名.html', 'r',encoding='utf-8') as f:
#     con = f.read()
#     soup = BeautifulSoup(con, 'lxml')
    # print(soup.prettify())
    # print(soup.title)
    # print(soup.title.name)
    # print(soup.title.string)
    # print(soup.a['class'])
    # print(soup.find_all('tr'))
    # print(soup.find_all(href=re.compile("https://www.*?/")))
    # print(soup.a.get('href'))
    # print(soup.get_text())
    # for i in soup.tbody.contents:
    #     print(i)
    # print(soup.tbody.contents[1])

# soup = BeautifulSoup(open(r'C:\Lesson\爬虫从入门到应用\2022_06_08直播数据解析_正则\素材\大学排名.html', 'r',encoding='utf-8'), 'lxml')
#
# univercity_rank = []
# for i in soup.tbody.find_all('tr'):
#     name = i.a.text
#     print(name)
#     print(type(name))
#     rank = i.find_all(text=re.compile('\d+'), limit=2)
#     print(type(rank))
#     rank.append(name)
#     print(rank)
#     univercity_rank.append(rank)
# print(univercity_rank)

#
# soup = BeautifulSoup(open(r'C:\Lesson\爬虫从入门到应用\2022_06_08直播数据解析_正则\素材\豆瓣.html', 'r',encoding='utf-8'), 'lxml')
#
# # print(soup.prettify())
# for i in soup.find_all('div',class_='detail-frame'):
#     name = i.a.string
#     print(i.select('p'))
    # print(i.select("h.color-gray"))

# soup = BeautifulSoup(open(r'C:\Lesson\爬虫从入门到应用\2022_06_08直播数据解析_正则\素材\股票.html', 'r',encoding='utf-8'), 'lxml')
# # print(soup.prettify())
# for i in soup.tbody.find_all('tr'):
#     print(i)
#     print(list(i.strings))
#     # for j in i.find_all('a'):
#     #     print(j.text)

# C:\Lesson\爬虫从入门到应用\2022_06_10_直播数据解析_bs4\素材
# soup = BeautifulSoup(open(r'C:\Lesson\爬虫从入门到应用\2022_06_10_直播数据解析_bs4\素材\三国演义.html', 'r',encoding='utf-8'), 'lxml')

# print(soup.prettify())
# print(soup.find_all('div', class_= 'book-mulu'))
# for i in soup.find_all('div', class_= 'book-mulu'):
#     print(list(i.stripped_strings))
# print(list(soup.find('div', class_='book-mulu').stripped_strings))



# soup = BeautifulSoup(open(r'C:\Lesson\爬虫从入门到应用\2022_06_10_直播数据解析_bs4\素材\匹配天气.html', 'r',encoding='utf-8'), 'lxml')
# # print(soup.prettify())
# # print(soup.find_all('td', attrs={'height':'23','width':'83'}))
# b = []
# for i in soup.find_all('tr'):
#     if i.find('td', attrs={'width': '83', 'height': '23'}):
#         a = {}
#         city = i.find('td', attrs={'width': '83', 'height': '23'}).text.lstrip('\n')
#         high_temp = i.find('td', width='92').text
#         a['city'] = city
#         a['temp'] = high_temp
#         b.append(a)
# print(b)



soup = BeautifulSoup(open(r'C:\Lesson\爬虫从入门到应用\2022_06_10_直播数据解析_bs4\素材\广州二手房.html', 'r',encoding='utf-8'), 'lxml')


# for i in soup.find_all('h4', class_='house-title'):
#     print(i.a.string)

# for j in soup.find_all('div', class_='item-info fl'):
#     print(list(j.stripped_strings))
for i in soup.find_all('div',class_='house-item house-itemB clearfix'):
    print('---------------------------------------------------------------------------------')
    print(i)
    print(i.select('.cBlueB')[0].text)
    print(i.select('.house-name')[0].text.replace('|', ''))
    print(i.select('.house-txt')[0].text)
    print(i.select('.house-txt')[1].text)
    print('--------------------')
    print(list(i.find('div',class_='item-pricearea fr').stripped_strings))
    # print(i.select('.item-pricearea fr')[0].text)

