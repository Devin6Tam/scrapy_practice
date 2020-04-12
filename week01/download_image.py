#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/11 1:27
# @Author  : tanxw
# @Desc    ：爬取图片

import requests

image_url = "https://www.baidu.com/img/bd_logo1.png"

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"}

response = requests.get(image_url, headers=headers)

# 图片是二进制流
data = response.content

with open("baidu_logo.png", "wb") as f:
    f.write(data)
