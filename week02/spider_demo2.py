#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/13 13:53
# @Author  : tanxw
# @Desc    : 爬虫示例2 - 内涵图

import re
import requests
from fake_useragent import UserAgent

class NeihanbaSpider(object):
    def __init__(self):
        ua = UserAgent()
        self.base_url = 'https://www.neihanba.com/mh/1120689.html'
        self.headers = {"User-Agent": ua.random}

        # 1.第一层 解析
        # python 字符串包裹 单包双 双包单
        # 正则 原始字符串 --
        self.first_pattern = re.compile('<a href="/mh/[0-9]+.html"> <img src="(.*?)" width="[0-9]+" />(.*?)</a>', re.S)
        # 我们添加re.S是为了给.的匹配模式扩展到整个字符串，包括\n换行符

    def send_request(self):
        response = requests.get(self.base_url, headers=self.headers)
        # 源码是gbk格式,  decode(gbk)
        data = response.content.decode('gbk')
        return data

    def parse_data(self, data):
        # 第一层数据
        result_list = self.first_pattern.findall(data)

        return result_list

    def download_image(self, data_list):
        for image in data_list:
            response = requests.get(image[0], headers=self.headers)
            # 图片是二进制流
            data = response.content
            save_path = "neihanba/"+image[1]+".jpg"
            with open(save_path, "wb") as f:
                f.write(data)


    def run(self):
        # 1.发请求
        data = self.send_request()
        # 2.解析数据
        data_list = self.parse_data(data)

        # 3.下载图片
        self.download_image(data_list)

# 内涵吧 爬虫单层解析
class Neihan8Spider(object):
    def __init__(self):
        ua = UserAgent()
        self.base_url = 'https://www.neihan8s.com/article/list_5_1.html'
        self.headers = {"User-Agent": ua.random}

        # 1.第一层 解析
        # python 字符串包裹 单包双 双包单
        # 正则 原始字符串 --
        self.first_pattern = re.compile('<div class="f18 mb20">(.*?)</div>', re.S)
        # 我们添加re.S是为了给.的匹配模式扩展到整个字符串，包括\n换行符

    def send_request(self):
        response = requests.get(self.base_url, headers=self.headers)
        # 源码是gbk格式,  decode(gbk)
        data = response.content.decode('gbk')
        return data

    def parse_data(self, data):
        # 第一层数据
        result_list = self.first_pattern.findall(data)

        return result_list

    def write_file(self, data_list):
        with open('neihan8.html', 'w', encoding='utf8') as f:
            for content in data_list:
                f.write(content)

    def run(self):
        # 1.发请求
        data = self.send_request()
        # 2.解析数据
        data_list = self.parse_data(data)

        # 3.保存
        self.write_file(data_list)

# 内涵吧 爬虫多层解析
class Neihan8Spider1(object):
    def __init__(self):
        ua = UserAgent()
        self.base_url = 'https://www.neihan8s.com/article/list_5_1.html'
        self.headers = {"User-Agent": ua.random}

        # 1.第一层 解析
        # python 字符串包裹 单包双 双包单
        # 正则 原始字符串 --
        self.first_pattern = re.compile('<div class="f18 mb20">(.*?)</div>', re.S)
        # 我们添加re.S是为了给.的匹配模式扩展到整个字符串，包括\n换行符

        # 2. 第二层解析
        # 标签        <(.*?)>
        # 字符实体    &(.*?);
        # 空白        \s
        self.second_pattern = re.compile('<(.*?)>|&(.*?);|\s')

    def send_request(self):
        response = requests.get(self.base_url, headers=self.headers)
        # 源码是gbk格式,  decode(gbk)
        data = response.content.decode('gbk')
        return data

    def parse_data(self, data):
        # 第一层数据
        result_list = self.first_pattern.findall(data)

        return result_list

    def write_file(self, data_list):
        with open('neihan8.txt', 'w', encoding='utf8') as f:
            for content in data_list:
                # 二次解析
                new_content = self.second_pattern.sub('', content) + '\n\n'
                f.write(new_content)

    def run(self):
        # 1.发请求
        data = self.send_request()
        # 2.解析数据
        data_list = self.parse_data(data)

        # 3.保存
        self.write_file(data_list)

# 内涵吧 爬虫多层解析，多页面
class Neihan8Spider2(object):
    def __init__(self):
        ua = UserAgent()
        self.base_url = 'https://www.neihan8s.com/article/list_5_{}.html'
        self.headers = {"User-Agent": ua.random}

        # 1.第一层 解析
        # python 字符串包裹 单包双 双包单
        # 正则 原始字符串 --
        self.first_pattern = re.compile('<div class="f18 mb20">(.*?)</div>', re.S)
        # 我们添加re.S是为了给.的匹配模式扩展到整个字符串，包括\n换行符

        # 2. 第二层解析
        # 标签        <(.*?)>
        # 字符实体    &(.*?);
        # 空白        \s
        self.second_pattern = re.compile('<(.*?)>|&(.*?);|\s')

    def send_request(self, url):
        response = requests.get(url, headers=self.headers)
        # 源码是gbk格式,  decode(gbk)
        data = response.content.decode('gbk')
        return data

    def parse_data(self, data):
        # 第一层数据
        result_list = self.first_pattern.findall(data)

        return result_list

    def write_file(self, data_list, page):
        page_number = '\n---------------------第' + str(page) + '页---------------------\n\n'
        print(page_number)
        with open('neihan8_{}.txt'.format(page), 'w', encoding='utf8') as f:
            for content in data_list:
                # 二次解析
                new_content = self.second_pattern.sub('', content) + '\n\n'
                f.write(new_content)

    def run(self):
        for page in range(1, 5):
            url = self.base_url.format(page)
            # 1.发请求
            data = self.send_request(url)
            # 2.解析数据
            data_list = self.parse_data(data)

            # 3.保存
            self.write_file(data_list, page)


if __name__ == '__main__':
    # NeihanbaSpider().run()
    Neihan8Spider2().run()


"""
re.sub的参数：有五个参数
re.sub(pattern, repl, string, count=0, flags=0)
其中三个必选参数：pattern, repl, string
两个可选参数：count, flags

pattern：表示正则表达式中的模式字符串；
repl：被替换的字符串（既可以是字符串，也可以是函数）；
string：要被处理的，要被替换的字符串；
count：匹配的次数, 默认是全部替换

第一个：pattern
pattern，表示正则中的模式字符串。
反斜杠加数字（\n），则对应着匹配的组（matched group）比如\6，表示匹配前面pattern中的第6个group 
第二个参数：repl
repl，就是replacement，被替换，的字符串的意思。
repl可以是字符串，也可以是函数。
repl是字符串
如果repl是字符串的话，其中的任何反斜杠转义字符，都会被处理的。
即：
\n：会被处理为对应的换行符； 
\r：会被处理为回车符； 
其他不能识别的转移字符，则只是被识别为普通的字符： 
比如\j，会被处理为j这个字母本身； 
反斜杠加g以及中括号内一个名字，即：\g，对应着命了名的组，named group
第三个参数：string
string，即表示要被处理，要被替换的那个string字符串。
没什么特殊要说明。
第四个参数：count
举例说明：
继续之前的例子，假如对于匹配到的内容，只处理其中一部分。
比如对于：
hello 123 world 456 nihao 789
只是像要处理前面两个数字：123,456，分别给他们加111，而不处理789，
那么就可以写成：
replacedStr = re.sub("(?P\d+)", _add111, inputStr, 2);
"""