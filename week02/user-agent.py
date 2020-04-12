#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/12 23:41
# @Author  : tanxw
# @Desc    : 随机User—Agent,及使用示例

# Python3中通过fake_useragent生成随机UserAgent
# pip install fake_useragent
import requests
import re
from fake_useragent import UserAgent

ua = UserAgent()
# # 随机打印ie浏览器任意版本
# print(ua.ie)
# # 随机打印firefox浏览器任意版本
# print(ua.firefox)
# # 随机打印chrome浏览器任意版本
# print(ua.chrome)
# # 随机打印任意厂家的浏览器
# print(ua.random)


# 示例
url = "https://www.mzitu.com"
# 反爬 加上referer
headers = {
    "Referer": "https://www.mzitu.com/",
    "User-Agent": ua.random
}
response = requests.get(url, headers=headers)
html = response.content.decode()
print(html)

# 使用正则表达式获取地址的列表
ret_json = re.findall("<img class='lazy' src='https://www.mzitu.com/static/pc/img/lazy.png' data-original='(.*?)' alt",html)
print(ret_json)

for pic_url in ret_json:
    # 发起请求获取这个图片对象
    r = requests.get(pic_url, headers=headers)
    name = pic_url.split('/')[-1]
    # 保存图片
    with open("meizitu/%s" % name, "wb") as f:
        f.write(r.content)
