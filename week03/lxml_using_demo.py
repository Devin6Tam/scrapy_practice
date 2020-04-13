#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/13 16:56
# @Author  : tanxw

# https://tieba.baidu.com/f?ie=utf-8&kw=美食吧&fr=search&pn=0&
import requests, json
from fake_useragent import UserAgent
from lxml import etree

ua = UserAgent()
start_url = "https://tieba.baidu.com/mo/q/m?kw=%E7%BE%8E%E9%A3%9F&pn=0&lp=5024&forum_recommend=1&lm=0&cid=0&has_url_param=90&pn=0&is_ajax=1"
headers = {"User-Agent": ua.random}
r = requests.get(start_url, headers=headers)
html = r.content.decode()
# print(html)
html_dict = json.loads(html)["data"]["content"]
# print(html_dict)
t = etree.HTML(html_dict)
href_list = t.xpath('//li[@class="tl_shadow tl_shadow_new "]/a/@href')
print(href_list)
#https://tieba.baidu.com/p/6355219109?lp=5028&mo_device=1&is_jingpost=0
