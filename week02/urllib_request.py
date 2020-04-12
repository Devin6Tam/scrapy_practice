#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/11 22:30
# @Author  : tanxw
# @Desc    : 使用urllib自带request

import urllib.request

url = "https://www.baidu.com"

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"}

# 请求对象
request = urllib.request.Request(url, headers=headers)

# urlopen 页面响应
response = urllib.request.urlopen(request)
print(response)

# 取请求头里面的字段 首个字母大写其余都是小写
print(request.get_header('User-agent'))

html_bytes = response.read()
html_str = html_bytes.decode('utf8')
print(html_str)
