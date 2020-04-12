#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/11 22:49
# @Author  : tanxw
# @Desc    : 爬取json数据格式的网站

import requests
import json
import jsonpath
# pip install jsonpath

json_url = "https://www.lagou.com/lbs/getAllCitySearchLabels.json"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"}

response = requests.get(json_url, headers=headers)

# 响应结果，需要通过json.loads方法
# data = response.content.decode("utf-8")
# data_dict = json.loads(data)
# print(data_dict)
# print(type(data_dict))


# json() 方法 必须返回的是json
data_dict = response.json()
print(data_dict)
print(type(data_dict))

# 解析 jsonpath 接收到dict/list 得到的是一个列表
result_list = jsonpath.jsonpath(data_dict, '$..name')
print(result_list)
#ensure_ascii 默认是 True ASCII False
json.dump(result_list, open("city.json", 'w', encoding="utf8"), ensure_ascii=False)