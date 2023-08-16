# -*- coding:utf-8 -*-

import requests

import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

index_url = 'https://spa1.scrape.center/api/movie/?limit={limit}&offset={offset}'

def scrape_api(url):
    logging.info('Scraping %s.....' % url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            logging.info('Scraping %s Successful' % url)
            return response.json()
        logging.error('get invalid status code %s while scraping %s' % (response.status_code, url))
    except Exception as e:
        logging.error('error occured while scraping %s and error is %s' % (url, e))

def scrape_index(page):
    LIMIT = 10
    url = index_url.format(limit=LIMIT,offset=LIMIT * (page -1))
    return scrape_api(url)


def scrape_detail(id):
    detail_url = 'https://spa1.scrape.center/api/movie/{id}'.format(id=id)
    return  scrape_api(detail_url)

def main():
    Total_page = 10
    for page in range(1,Total_page + 1):
        page_info = scrape_index(page)
        for item in page_info.get('results'):
            id = item.get('id')
            detail_data = scrape_detail(id)
            logging.info('Detail Data: %s' % detail_data)


if __name__ == '__main__':
    main()
