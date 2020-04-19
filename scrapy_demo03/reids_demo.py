#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/20 0:06
# @Author  : tanxw
# @Desc    : redis 使用示例
from redis import *

if __name__ == '__main__':

    try:
        # 创建StrictRedis连接对象sr = StrictRedis() 默认连接本地 0号数据库
        sr = StrictRedis(host='localhost', port=6379, db=10)
        # 获取key
        # name = sr.get("name")
        # age = sr.get("age")
        # mobile = sr.get("mobile")
        # print(name, age, mobile)
        # 设置key
        result = sr.set('name', 'devin tam')
        print(result)
    except Exception as e:
        print(e)


