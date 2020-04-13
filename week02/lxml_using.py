#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/13 15:28
# @Author  : tanxw
# @Desc    : lxml 使用
# 安装 lxml pip install lxml

import requests, json, re
from fake_useragent import UserAgent
from lxml import etree
"""
（1）选取节点
------------------------------------
表达式           描述
nodename        选取此节点的所有子节点
/	            从根节点选取
//	            从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置
.	            选取当前节点
..	            选取当前节点的父节点
@	            选取属性
------------------------------------
"""
class Neihan8Spider(object):
    def __init__(self):
        ua = UserAgent()
        self.base_url = 'https://www.neihan8.com/wenzi/index.html'
        self.new_url = 'https://www.neihan8.com/wenzi/index_{}.html'
        self.headers = {"User-Agent": ua.random}
        self.data_list = []

    def send_request(self, url):
        response = requests.get(url, headers=self.headers)
        data = response.content.decode('utf-8')
        return data

    def parse_data(self, data):
        # 1.转换解析类型
        html_data = etree.HTML(data)
        # 2. 调用xpath方法
        # 2.1取出 所有行数  tr_list
        result_list = html_data.xpath('//div[@class="text-column-item box box-790"]')
        print(result_list)

        for tr in result_list:
            data_dict = {}
            # 标题
            data_dict['title'] = tr.xpath('.//h3/a/text()')[0]
            # 段子
            data_dict['desc'] = tr.xpath('.//div[@class="desc"]/text()')[0].replace("\u3000", "")
            # # 赞
            data_dict['good'] = tr.xpath('./div[@class="bottom"]/div[@class="good"]/text()')[0]
            # # 踩
            data_dict['bad'] = tr.xpath('./div[@class="bottom"]/div[@class="bad"]/text()')[0]
            # # 阅读量
            data_dict['view'] = tr.xpath('./div[@class="bottom"]/div[@class="view"]/text()')[0]
            print(data_dict)
            # 存入 list
            self.data_list.append(data_dict)

        return self.data_list

    def write_file(self, data_list, page):
        page_number = '\n---------------------第' + str(page) + '页---------------------\n\n'
        print(page_number)
        with open('neihan8_lxml.txt', 'a', encoding='utf8') as f:
            neihan_str = json.dumps(data_list, ensure_ascii=False)
            f.write(neihan_str)
            f.write("\n==============\n")

    def run(self):
        # 开循环发送请求
        for page in range(2, 7):
            # 拼接url
            url = self.new_url.format(page)
            # 1.发请求
            data = self.send_request(url)
            # 2.解析数据
            data_list = self.parse_data(data)
            print(data_list)
            # 3.保存
            self.write_file(data_list, page)

if __name__ == '__main__':
    Neihan8Spider().run()


if __name__ == '__main1__':
    html_str = """
           <div> 
               <ul> 
                   <li class="item-1"><a href="link1.html">111</a></li> 
                   <li class="item-1"><a href="link2.html">222</a></li> 
                   <li class="item-inactive"><a href="link3.html">333</a></li> 
                   <li class="item-1"><a href="link4.html">444</a></li> 
                   <li class="item-0"><a href="link5.html">555</a> 
               </ul>
           </div>
       """

    # 1. 转换类型
    data = etree.HTML(html_str)
    # 利用etree.HTML，将字符串转化为Element对象, Element对象具有xpath的方法, 返回结果的列表，能够接受bytes类型的数据和str类型的数据

    # 2. 调用xpath的语法解析---list
    # result_list = data.xpath('//li')
    # result_list = data.xpath('//li[3]')
    # 注意点: 在xpath中，第一个元素的位置是1，最后一个元素的位置是last(),倒数第二个是last()-1
    # result_list = data.xpath('//li')[2]
    # result_list = data.xpath('//a[@href="link4.html"]')
    # 标签包裹的内容
    # result_list = data.xpath('//a[@href="link4.html"]/text()')
    # 标签的属性
    # result_list = data.xpath('//li[3]/@class')
    # 了解 模糊查询
    # result_list = data.xpath('//li[contains(@class,"i")]') #contains 包含
    # 格式化
    # result_list = etree.tostring(data).decode()
    # 把转化后的element对象转化为字符串，返回bytes类型结果 etree.tostring(element)
    # print(result_list)

    href_list = data.xpath("//li[@class='item-1']/a/@href")
    title_list = data.xpath("//li[@class='item-1']/a/text()")

    # 组装成字典
    for href in href_list:
        item = {}
        item["href"] = href
        item["title"] = title_list[href_list.index(href)]
        print(item)