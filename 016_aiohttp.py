# -*- coding:utf-8 -*-

import asyncio
import aiohttp
import logging
import json
logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')

Page = 503
CONCURRENCY = 5
semaphore = asyncio.Semaphore(CONCURRENCY)
session = None

offset = 18

async def get(url):
    async with semaphore:
        try:
            logging.info('scraping url: %s' % url)
            async with session.get(url) as response:
                logging.info('single result: %s' % await response.json())
                return await response.json()
        except aiohttp.ClientError:
            logging.error('error occured while scraping %s' % url)


async def scrape(page):

    url = 'https://spa5.scrape.center/api/book?limit=18&offset={}'.format((page-1)*18)
    data = await get(url)
    return data

async def main():
    global session
    session = aiohttp.ClientSession()
    tasks = [asyncio.ensure_future(scrape(i)) for i in range(1, 504)]
    results = await asyncio.gather(*tasks)
    # logging.info('results: %s' % json.dumps(results, ensure_ascii=False, indent=2))


if __name__ == '__main__':

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
