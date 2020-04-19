#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/14 22:59
# @Author  : tanxw
# @Desc    : 猫眼点评，仅供个人学习
import requests
from lxml import etree
from fake_useragent import UserAgent

url = "https://maoyan.com/films/247300"
ua = UserAgent()
headers = {"Referer": "https://maoyan.com/", "User-Agent": ua.random}
r = requests.get(url, headers=headers)
data = r.content.decode()
# print(data)
e = etree.HTML(data)
print(e)
d = e.xpath('/html/body/div[3]/div/div[2]/div[3]/div[1]/div/span/span/text()')
print(d)