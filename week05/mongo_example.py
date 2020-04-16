#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/15 10:22
# @Author  : tanxw

#pip install pymongo
import pymongo
import json

# 1.链接数据库
client = pymongo.MongoClient(host="127.0.0.1", port=27017)

# 2. 建库
db = client['pystu']

# 3. 建表
collection = db['python']

# collection = client['pystu']['python']
# collection = client.pystu.python

# 4.把json文件的数据 插入到数据库 insert()
data_list = json.load(open('test.json', 'r'))
collection.insert_many(data_list)

# 5. 关闭
client.close()
