#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/14 0:02
# @Author  : tanxw
# @Desc    : beatifulsoup 爬虫示例

import requests,json
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

ua = UserAgent()
start_url = "https://tieba.baidu.com/mo/q/m?kw=%E7%BE%8E%E9%A3%9F&pn=0&lp=5024&forum_recommend=1&lm=0&cid=0&has_url_param=90&pn=0&is_ajax=1"
headers = {"User-Agent": ua.random}
r = requests.get(start_url, headers=headers)
html = r.content.decode()

html_dict = json.loads(html)["data"]["content"]

soup = BeautifulSoup(html_dict, "lxml")
l = soup.select('a[data-thread-type="0"]')
print(len(l))
for x in l:
    print(x.get('href'))