#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/14 11:35
# @Author  : tanxw
# @Desc    : 爬虫示例3 - 妹子图 仅学习使用

import time

import requests
from lxml import etree
from fake_useragent import UserAgent
ua = UserAgent()
headers = {"Referer": "https://www.mzitu.com/", "User-Agent": ua.random}
class MeiziTuScrapy(object):
    def __init__(self):
        self.url = "https://www.mzitu.com/xinggan/"
        self.headers = headers

    # 性感页面所有链接资源
    def first_scarpy(self):
        r = requests.get(self.url, headers=self.headers)
        html = r.content.decode()
        data = etree.HTML(html)
        ret_list = data.xpath('//*[@id="pins"]/li/a/@href')
        return ret_list
        print("=================================================\n")

    # 访问图片列表，返回图片总页数
    def second_scarpy(self, ret_list):
        for ret in ret_list:
            print(ret)
            r2 = requests.get(ret, headers=self.headers)
            html2 = r2.content.decode()
            print(html2)

            print("=================================================\n")
            data2 = etree.HTML(html2)
            ret2 = int(data2.xpath('//div[@class="pagenavi"]/a[last()-1]/span/text()')[0])

            self.third_scary(ret, ret2)

    # 访问图片页面，并下载图片
    def third_scary(self, ret, ret2):
        page_list = [ret, ]
        for i in range(2, ret2 + 1):
            url2 = ret + "/" + str(i)
            page_list.append(url2)
        print("=================================================\n")
        print(page_list)

        for x in page_list:
            time.sleep(2)
            r3 = requests.get(x, headers=self.headers)
            html3 = r3.content.decode()

            data3 = etree.HTML(html3)
            title = data3.xpath('/html/body/div[2]/div[1]/h2/text()')[0]
            pic = data3.xpath('//div[@class="content"]/div[@class="main-image"]/p/a/img/@src[1]')[0]
            print(title, pic)
            self.dowload_image(title, pic)

    def dowload_image(self, file_name, image_url):
        response = requests.get(image_url, headers=headers)
        # 图片是二进制流
        data = response.content
        with open("meizitu/%s.jpg" % file_name, "wb") as f:
            f.write(data)

    def run(self):
        ret_list = self.first_scarpy()
        self.second_scarpy(ret_list)

if __name__ == '__main__':
    MeiziTuScrapy().run()
