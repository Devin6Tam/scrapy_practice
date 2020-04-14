#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/14 16:55
# @Author  : tanxw


import requests
from week04.yundama_profile import indetify
from fake_useragent import UserAgent

if __name__ == '__main__':
    ua = UserAgent()
    code_image_url = 'http://www.yundama.com/resources/sample/4.jpg'
    headers = {"User-Agent": ua.random}
    # 发送请求
    image_content = requests.get(code_image_url, headers=headers).content

    # 使用第三方平台 识别
    ret = indetify(image_content)
    print("验证的结果是：{}".format(ret))