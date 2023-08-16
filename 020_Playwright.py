# -*- coding:utf-8 -*-
from playwright.sync_api import sync_playwright
import time
# 1.同步
# with sync_playwright() as p:
#     for browser_type in [p.chromium, p.firefox, p.webkit]:
#         browser = browser_type.launch(headless=False)
#         page = browser.new_page()
#         page.goto('https://www.baidu.com')
#         page.screenshot(path=f'screenshot-{browser_type.name}.png')
#         print(page.title())
#         browser.close()


# 2.异步
# from playwright.async_api import async_playwright
# import asyncio
#
# async def main():
#     async with async_playwright() as p:
#         browser_type = p.chromium
#         browser = await browser_type.launch(headless=False)
#         page = await browser.new_page()
#         await page.goto('https://www.baidu.com')
#         await page.screenshot(path=f'screenshot-{browser_type.name}.png')
#         print(await page.title())
#         await asyncio.sleep(10)
#         await browser.close()
#
# asyncio.run(main())


# 3.模拟Iphone 12 pro max safari
# with sync_playwright() as p:
#     device = p.devices['iPhone 12 Pro Max']
#     browser = p.chromium.launch(headless=False)
#     context = browser.new_context(**device, locale='zh-CN')
#     page = context.new_page()
#     page.goto('https://www.whatismybrowser.com/')
#     page.wait_for_load_state(state='networkidle')
#     page.screenshot(path='iphone.png')
#     time.sleep(10)
#     browser.close()

# 4.on方法监听事件 close console load request response
# def on_response(response):
#     print(f'Statue {response.status}: {response.url}')
#
# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     page = browser.new_page()
#     page.on('response',on_response)
#     page.goto('https://spa6.scrape.center/')
#     page.wait_for_load_state('networkidle')
#     time.sleep(10)
#     browser.close()

# def on_response(response):
#     if '/api/movie' in response.url and response.status==200:
#
#         print(response.json())
#
# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     page = browser.new_page()
#     page.on('response',on_response)
#     page.goto('https://spa6.scrape.center/')
#     page.wait_for_load_state('networkidle')
#     page.goto('https://spa6.scrape.center/page/2')
#     page.wait_for_load_state('networkidle')
#     time.sleep(30)
#     browser.close()

# 5.获取页面源代码

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://www.baidu.com/')
    page.wait_for_load_state('networkidle')
    print(page.content())
    time.sleep(10)
    browser.close()