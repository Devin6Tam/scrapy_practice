#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/13 0:12
# @Author  : tanxw
# @Desc    : 代理池

import requests
from fake_useragent import UserAgent
from retrying import retry
# pip install retrying

def proxy_use(ua):
    url = "http://www.baidu.com"

    headers = {"user-agent": ua.random}

    # 代理池
    proxy_list =[
        {"http": "39.96.210.247:80"},
        {"http": "39.137.69.10:80"},
        {"https": "150.138.106.174:82"},
        {"https": "58.220.95.86:9401"},
        {"https": "183.166.125.51:9999"},
        {"https": "49.235.246.24:8118"},
        {"http": "120.78.68.241:80"}
    ]
    # 过滤
    use_proxy = []
    for proxy in proxy_list:
        try:
            response = requests.get(url, headers=headers, proxies=proxy, timeout=3)
            if response.status_code == 200:
                use_proxy.append(proxy)
        except Exception as e:
            print(e)

    print(use_proxy)

def proxy_use2(ua):
    url = "http://2000019.ip138.com/"
    headers = {
        "user-agent": ua.random
    }
    # 高匿代理
    proxy = {"http": "39.137.69.10:80"}

    r = requests.get(url, headers=headers, proxies=proxy, timeout=3)

    print(r.content.decode())

# 使用装饰器来执行超时重试
@retry(stop_max_attempt_number=3)
def proxy_use3(ua):
    url = "http://www.baidu.com/"
    headers = {
        "user-agent": ua.random
    }
    # 高匿代理
    proxy = {"http": "39.137.69.10:80"}

    r = requests.get(url, headers=headers, proxies=proxy, timeout=3)

    print(r.content.decode())


if __name__ == '__main__':
    ua = UserAgent()
    # proxy_use(ua)
    proxy_use3(ua)