#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/11 1:17
# @Author  : tanxw
# @Desc    ：完整的爬虫请求

import requests
import random

url = 'http://www.baidu.com'

# 多个user_agent池
USER_AGENT_LIST = [
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
]

random_user = random.choice(USER_AGENT_LIST)
print(random_user)
print("------------------------------")
headers = {
    'User-Agent': random_user
}
baidu_params = {
    "wd":"美女",
    "ie":"utf-8"
}

r = requests.get(url, headers=headers, params=baidu_params)
data = r.content.decode(encoding='utf8')
print(r.status_code)
request_header = r.request.headers
print(request_header)

response_cookie = r.cookies
print(response_cookie)
# print(r.request.__cookie)

