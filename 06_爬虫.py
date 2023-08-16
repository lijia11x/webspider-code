# import urllib.parse
# import urllib.request

# data = bytes(urllib.parse.urlencode({'name': 'NiClaus'}), encoding='utf-8')
# response = urllib.request.urlopen('https://www.httpbin.org/post', data=data)
#
# print(response.read().decode('utf-8'))
import re

import requests
from requests.auth import HTTPBasicAuth
url = 'https://ssr3.scrape.center/'
#
response = requests.get(url,auth = HTTPBasicAuth('admin', 'admin'))
#
# pattern = re.compile('<h2.*?>(.*?)</h2>',re.S)
#
# res = pattern.findall(response.text)
#
# print(res)

print(response.text)
print(response.status_code)


a = 'abacadaeaf'.split()