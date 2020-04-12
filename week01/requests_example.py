#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/11 0:59
# @Author  : tanxw
# @Desc    : 第一个爬虫

import requests
# 目标地址
url = 'http://www.baidu.com'
# 发送请求，获取响应对象
response = requests.get(url)
print(response)
data = response.content.decode()
print(data)

# 入库或者保存
with open('baidu.html', 'w', encoding='utf8') as f:
    f.write(data)
