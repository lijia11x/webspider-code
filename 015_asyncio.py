# -*- coding:utf-8 -*-
import asyncio

import aiohttp
import requests

import time
# async def get_baidu():
#     url = 'https://www.baidu.com/'
#     response = requests.get(url)
#     # print(response.status_code)
#     return response.status_code
#
# tasks = [asyncio.ensure_future(get_baidu()) for i in range(5)]
# print('Tasks: ', tasks)
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait(tasks))
#
#
# for task in tasks:
#     print(task.result())



# def test(number):
#     start_time = time.time()
#
#     async def get(url):
#         session = aiohttp.ClientSession()
#         response = await session.get(url)
#         await response.text()
#         await session.close()
#         return response
#
#     async def request():
#         url = 'https://www.baidu.com/'
#         await get(url)
#
#     tasks = [asyncio.ensure_future(request()) for i in range(number)]
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(asyncio.wait(tasks))
#
#     end = time.time()
#     print('Number:', number, 'Cost time:', end-start_time)
#
# for num in [1, 3, 5, 10, 15, 30, 50, 75, 100, 200, 500]:
#     test(num)


async def get(url,session):
    async with session.get(url) as response:
        return await response.text(), response.status

async def main():
    async with aiohttp.ClientSession() as session:
        url = 'https://cuiqingcai.com'
        text,status = await get(url,session)
        print(text)
        print(status)

if __name__ == '__main__':
    asyncio.run(main())