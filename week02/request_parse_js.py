#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/12 23:19
# @Author  : tanxw
# @Desc    :  加载并解析javascript数据

import re
import requests
import json

url = "https://36kr.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
}

r = requests.get(url, headers=headers)
html_str = r.content.decode("utf-8")
print(html_str)

ret_list = re.findall("<script>window.initialState=(.*?)</script>", html_str)
# print(ret_list)
ret_dict = json.loads(ret_list[0], encoding="utf8")
# print(ret_dict)

a_dict = ret_dict["homeData"]["data"]["hotlist"]["data"]

for new in a_dict:
    print(new["templateMaterial"]["widgetImage"], new["templateMaterial"]["widgetTitle"])