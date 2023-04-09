# -*- coding: utf-8 -*-
"""
@author: luhx
@file: e1.py
@time: 2023/4/5 11:31
@desc:  测试代码
"""
import time
from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(int(datetime.datetime.now().timestamp()))


def getLinks(articleUrl):
    url = 'http://en.wikipedia.org{}'.format(articleUrl)
    print(f"url: {url}")
    html = urlopen(url)
    bs = BeautifulSoup(html, 'html.parser')
    bs_div_body_content = bs.find('div', {'id': 'bodyContent'})
    wiki = bs_div_body_content.find_all('a', href=re.compile('^(/wiki/)((?!:).)*$'))
    return wiki


links = getLinks('/wiki/Kevin_Bacon')
while len(links) > 0:
    newArticle = links[random.randint(0, len(links) - 1)].attrs['href']
    print(newArticle)
    links = getLinks(newArticle)
    time.sleep(1)
