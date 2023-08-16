# -*- coding:utf-8 -*-
from pyppeteer import launch
from pyquery import PyQuery as pq
import asyncio

# 1
# async def main():
#     browser = await launch()
#     page = await browser.newPage()
#     await page.goto('https://spa2.scrape.center/')
#     await  page.waitForSelector('.item .name')
#     doc = pq(await page.content())
#     names = [item.text() for item in doc('.item .name').items()]
#     print('Names:', names)
#     await browser.close()
#
#
# asyncio.get_event_loop().run_until_complete(main())


# 2
# width, height = 1366, 768
#
#
# async def main():
#     browser = await launch()
#     page = await browser.newPage()
#     await page.setViewport({'width': width, 'height': height})
#     await page.goto('https://spa2.scrape.center/')
#     await page.waitForSelector('.item .name')
#     await asyncio.sleep(2)
#     await page.screenshot(path='example.png')
#     dimensions = await page.evaluate('''() => {
#     return {
#     width: document.documentElement.clientWidth,
#     height: document.documentElement.clientHeight,
#     deviceScaleFactor: window.devicePixelRatio,
#     }
#     }''')
#
#     print(dimensions)
#     await browser.close()
#
# asyncio.get_event_loop().run_until_complete(main())

# 3
# async def main():
#     browser = await launch(headless=False)
#     await asyncio.sleep(30)
#
# asyncio.get_event_loop().run_until_complete(main())

# 4
# async def main():
#     browser = await launch(devtools=True, userDataDir='./userdata', args=['--disable-infobars'])
#     page = await browser.newPage()
#     await page.goto('https://www.taobao.com')
#     await asyncio.sleep(60)
#
# asyncio.get_event_loop().run_until_complete(main())

# 5
async def main():
    browser = await launch(headless=False)
    page = await browser.newPage()
    await page.goto('https://spa2.scrape.center/')
    await page.waitForSelector('.item .name')
    await page.click('.name', options={
        'button': 'right',
        'clickCount': 2,
        'delay': 3000,
    })
    await asyncio.sleep(20)
    await browser.close()


if __name__ == '__main__':

    asyncio.get_event_loop().run_until_complete(main())