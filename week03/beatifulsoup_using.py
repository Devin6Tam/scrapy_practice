#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/13 23:44
# @Author  : tanxw
# @Desc    : beatifulsoup 使用

# pip install beautifulsoup4
from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>WEIZI The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

# 创建一个BS对象
soup = BeautifulSoup(html, "lxml")
# print(soup)
# 格式化输出
print(soup.prettify())

#标签 #样式表（行内）# ID （行位）

#一、搜索文档树
# find_all() # 满足条件的所有，列表
# find() # 第一个符合匹配结果的字符

# 传字符串 标签
# print(soup.find(name="p"))

# l = soup.find_all("p")
# 传正则表达式
# import re
#
# for l in soup.find_all(re.compile("^a")):
#     print(l)
# 传列表
# l = soup.find_all(['a','b'])

# 关键字参数
# l = soup.find_all(class ="sister")  4.8版本是否去除了这个方法？？？？
# l = soup.find_all(id="link1")

# text参数
# l = soup.find_all(text=["Tillie","Lacie"])
# css选择器
#标签 find_all select
# l = soup.select("title")
#样式
# l = soup.select(".sister")

# l = soup.find("p")

# l = soup.select("#link2")
#属性选择器查找
l = soup.select('a[href="http://example.com/lacie"]')[0].get_text()

#获取文本内容 get_text()
# l = soup.select("a")[2].get_text()
# .get("href") 获取属性
print(l)