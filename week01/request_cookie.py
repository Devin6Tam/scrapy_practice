#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/11 11:33
# @Author  : tanxw
# @Desc    : cookies,session使用

import requests

# cookies 使用
"""
url = "https://www.baidu.com"

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"}

# 爬虫请求
r = requests.get(url, headers=headers)
print(type(r.cookies))

# 解析响应的cookie信息
cookies = requests.utils.dict_from_cookiejar(r.cookies)
print(cookies)
"""

# session使用，保存登录会话信息
"""
post_url = "http://www.renren.com/PLogin.do"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
    "Cookie": "anonymid=k1huowmq-t0jfd8; _r01_=1; jebe_key=c0ef33d0-39de-418f-bf56-edbd19c4ea2c%7C8da1fa8db318da7873743d11a45be0f9%7C1570540182207%7C1%7C1570540186909; depovince=GW; JSESSIONID=abcDuGzGEbikK5Ls0Ft6w; ick_login=be65490c-88e1-47b1-9460-624f7d20b1c1; first_login_flag=1; ln_uact=917848283@qq.com; ln_hurl=http://hdn.xnimg.cn/photos/hdn221/20191119/1450/h_main_0HRL_13bc0010a62f1986.jpg; jebe_key=c0ef33d0-39de-418f-bf56-edbd19c4ea2c%7C9b4c6b6b73f0895bc8873fcb09d1ac5c%7C1574432786477%7C1%7C1574432799305; _de=C72FF6EE733E7601340E4CEC836F3769696BF75400CE19CC; jebecookies=ddbbb7bf-3976-47a0-a766-53a8268da2c6|||||; p=06367a3ff7e676f451716be2a09f02a41; t=fbdfec419e02bbe5f372eff6ba6d49f71; societyguester=fbdfec419e02bbe5f372eff6ba6d49f71; id=972902211; xnsid=6c750b84; loginfrom=syshome"
}
post_data = {
    "email": "XXXXX",
    "password": "XXXXX"
}
session = requests.session()
session.post(post_url, post_data, headers=headers)
cookies = session.cookies
print(cookies)

cookies_dict = requests.utils.dict_from_cookiejar(cookies)
print(cookies_dict)
"""

# session使用，访问个人主页（需要先登录）

get_url = "http://www.renren.com/972902211/profile"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
    "Cookie": "anonymid=k1huowmq-t0jfd8; _r01_=1; jebe_key=c0ef33d0-39de-418f-bf56-edbd19c4ea2c%7C8da1fa8db318da7873743d11a45be0f9%7C1570540182207%7C1%7C1570540186909; depovince=GW; JSESSIONID=abcDuGzGEbikK5Ls0Ft6w; ick_login=be65490c-88e1-47b1-9460-624f7d20b1c1; first_login_flag=1; ln_uact=917848283@qq.com; ln_hurl=http://hdn.xnimg.cn/photos/hdn221/20191119/1450/h_main_0HRL_13bc0010a62f1986.jpg; jebe_key=c0ef33d0-39de-418f-bf56-edbd19c4ea2c%7C9b4c6b6b73f0895bc8873fcb09d1ac5c%7C1574432786477%7C1%7C1574432799305; _de=C72FF6EE733E7601340E4CEC836F3769696BF75400CE19CC; jebecookies=ddbbb7bf-3976-47a0-a766-53a8268da2c6|||||; p=06367a3ff7e676f451716be2a09f02a41; t=fbdfec419e02bbe5f372eff6ba6d49f71; societyguester=fbdfec419e02bbe5f372eff6ba6d49f71; id=972902211; xnsid=6c750b84; loginfrom=syshome"
}

r = requests.get(get_url, headers=headers)
with open("user_profile.html", "w", encoding="utf8") as f:
    f.write(r.content.decode())