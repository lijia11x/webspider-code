# -*- coding:utf-8 -*-
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
browser = webdriver.Chrome()

# try:
#     browser.get('https://www.baidu.com/')
#     input = browser.find_element(By.ID,'kw')
#     input.send_keys('Python')
#     input.send_keys(Keys.ENTER)
#     wait = WebDriverWait(browser, 10)
#     wait.until(EC.presence_of_element_located((By.ID,'content_left')))
#     print(browser.current_url)
#     print(browser.get_cookies())
#     print(browser.page_source)
# finally:
#     browser.close()

# 2
# browser.get('https://www.taobao.com')
# input = browser.find_element(By.ID, 'q')
# input.send_keys('Iphone')
# time.sleep(1)
# input.clear()
# input.send_keys('Ipad')
# button = browser.find_element(By.CLASS_NAME, 'btn-search')
# button.click()

# 3
# url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# browser.get(url)
# browser.switch_to.frame('iframeResult')
# source = browser.find_element(By.CSS_SELECTOR, '#draggable')
# target = browser.find_element(By.CSS_SELECTOR, '#droppable')
# actions = ActionChains(browser)
# actions.drag_and_drop(source, target)
# actions.perform()

# 4
# browser.get('https://www.zhihu.com/explore')
# browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
# time.sleep(4)
# browser.execute_script('alert("To Bottom")')
# time.sleep(2)

# 5使用back或forward实现后退或前进

# browser.get('https://www.baidu.com')
# time.sleep(1)
# browser.get('https://www.taobao.com')
# time.sleep(1)
# browser.get('https://www.python.org')
# time.sleep(1)
# browser.back()
# time.sleep(1)
# browser.back()
# time.sleep(1)
# browser.forward()
# time.sleep(1)

# 6.使用selenium操作cookie
# browser.get('https://www.zhihu.com/explore')
# print(browser.get_cookies())
# browser.add_cookie({'name': 'jianxinli', 'domain': 'www.zhihu.com', 'value': 'Claus_li'})
# print(browser.get_cookies())
# browser.delete_all_cookies()
# print(browser.get_cookies())

# 7.选项卡管理
browser.get('https://www.baidu.com/')
time.sleep(1)
browser.execute_script('window.open()')
print(browser.window_handles)
browser.switch_to.window(browser.window_handles[1])
browser.get('https://www.taobao.com/')
time.sleep(1)
browser.switch_to.window(browser.window_handles[0])
browser.get('https://python.org')