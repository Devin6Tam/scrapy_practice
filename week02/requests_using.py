#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/15 0:52
# @Author  : tanxw
# @Desc    : requests 请求使用示例

import requests
from retrying import retry

url = "https://mip.tutumanhua.com/"
proxy = {
    'http': "125.108.108.165:9000"
}


# # SSLError 需要把验证屏蔽
# r = requests.get(url, verify=False)
#
# # 设置请求超时时间
# r = requests.get(url, timeout=60)

# # 代理
# r = requests.get(url, proxies=proxy)

# # 失败重试次数
# @retry(stop_max_attempt_number=3)
# def test():
#     r = requests.get(url, proxies=proxy)
#     return r

@retry(stop_max_attempt_number=3)
def test():
    r = requests.get(url, verify=False, timeout=60, proxies=proxy)
    return r


print(test())

