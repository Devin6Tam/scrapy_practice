#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/12 17:11
# @Author  : tanxw

import requests

# 访问人人网获取cookie
access_url = "http://www.renren.com/"

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"}

r = requests.get(access_url, headers=headers)
cookies = r.cookies

# 使用当前cookies，保存登录话信息
post_url = "http://www.renren.com/PLogin.do"

post_data = {
    "email": "XXXXX",
    "password": "XXXXX"
}
session = requests.session()
session.post(post_url, post_data, headers=headers, cookies=cookies)

# 在当前会话有效期内，访问个人主页
get_url = "http://www.renren.com/972902211/profile"

r = session.get(get_url, headers=headers)
with open("user_profile2.html", "w", encoding="utf8") as f:
    f.write(r.content.decode())