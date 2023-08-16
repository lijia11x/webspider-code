# -*- coding:utf-8 -*-


from pyquery import PyQuery as pq

# doc = pq(url='https://cuiqingcai.com')

# print(doc('title'))  # <title>静觅丨崔庆才的个人站点 - Python爬虫教程</title>

html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''
doc = pq(html)

print(doc('#container .list li'))

for item in doc('#container .list li').items():
    print(item)
    print(item.text())


a = doc('.item-0.active a')

print('a:%s' % a)

print(a('span').attr('class'))



