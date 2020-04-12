#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/11 22:40
# @Author  : tanxw
# @Desc    : json 使用

import json
user = {
    "name": "江涛",
    "age": 18
}

user_str = json.dumps(user)
print(type(user_str))
print(user_str)

json_dict = json.loads(user_str)
print("-------------------------------------")
print(type(json_dict))
print(json_dict)

with open('user.json', 'w', encoding='utf8') as fp:
    json.dump(user, fp)
    fp.close()

with open('user.json', 'r') as fp:
    fp_dict = json.load(open('user.json', 'r', encoding='utf8'))
    print("-------------------------------------")
    print(type(fp_dict))
    print(fp_dict)
