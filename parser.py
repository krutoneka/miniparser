from typing import List, Dict, Any

import requests
from bs4 import BeautifulSoup

URL = 'https://cars.av.by/audi/a5'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
           'accept': '*/*'}
HOST = 'https://cars.av.by'

def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='listing-item__wrap')

    cars = []
    for item in items:
        cars.append({
            'title': item.find('h3', class_='listing-item__title').get_text(strip = False),
            'link': HOST + item.find('a', class_='listing-item__link').get('href'),
            'prices': item.find('div', class_='listing-item__prices').get_text(),
            'year': item.find('div', class_='listing-item__params').get_text(),
        })
    return cars


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        cars = get_content(html.text)
    else:
        print('ERROR')

parse()