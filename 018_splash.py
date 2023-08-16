# -*- coding:utf-8 -*-
import requests


response = requests.get('http://120.26.103.203:8050/render.html?url=https://www.baidu.com')
print(response.text)
