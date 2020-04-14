#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/14 13:56
# @Author  : tanxw
# @Desc    : 使用进程爬取豆瓣数据，仅学习使用

import time
import requests
from lxml import etree
from multiprocessing.dummy import Pool
from fake_useragent import UserAgent
import gevent
from gevent import monkey

# 使用gevent.sleep 代替 monkey.patch_all
# monkey.patch_all()
gevent.sleep(2)
class DoubanSpider(object):

    def __init__(self):
        ua = UserAgent()
        self.base_url = "https://movie.douban.com/top250?filter=&start="
        self.headers = {"User-Agent": ua.random}
        self.count = 0

    # 1.请求
    def send_request(self, url):
        time.sleep(1)
        response = requests.get(url, headers=self.headers)
        data = response.content
        # return data
        self.parse_file(data)

    # 2.解析数据
    def parse_file(self, data):
        # 1.转类型
        html_data = etree.HTML(data)
        # 2. XPATH
        result_list = html_data.xpath('//div[@id="content"]/div/div[1]/ol/li/div/div[2]/div[1]/a/span[1]/text()')
        for name in result_list:
            print(name)
            self.count += 1

    def run(self):
        # 发起请求
        # 记录开始的时间
        start_time = time.time()
        url_list = []
        for page in range(0,255+1,25):
            # 拼接url
            url = self.base_url + str(page)
            # 放入列表
            url_list.append(url)

        # 1.创建池子 ？多大
        pools = Pool(len(url_list))

        # 2.给任务
        pools.map(self.send_request, url_list)

        # 3.关闭
        pools.close()

        # 4.等待
        pools.join()


        end_time = time.time()
        t = end_time - start_time
        print(self.count)
        print(t)

class DoubanSpider2(object):
    def __init__(self):
        ua = UserAgent()
        self.base_url = "https://movie.douban.com/top250?filter=&start="
        self.headers = {"User-Agent": ua.random}
        self.count = 0
    # 1.请求
    def send_request(self, url):
        time.sleep(1)
        response = requests.get(url, headers=self.headers)
        data = response.content
        # return data
        self.parse_file(data)

    # 2.解析数据
    def parse_file(self, data):
        # 1.转类型
        html_data = etree.HTML(data)
        # 2. XPATH
        result_list = html_data.xpath('//div[@id="content"]/div/div[1]/ol/li/div/div[2]/div[1]/a/span[1]/text()')
        for name in result_list:
            print(name)
            self.count += 1

    def run(self):
        # 发起请求
        # 记录开始的时间
        start_time = time.time()
        gevent_list = []
        for page in range(0,255+1,25):
            # 拼接url
            url = self.base_url + str(page)
            # 1.创建
            gevents = gevent.spawn(self.send_request, url)
            # 2.放入列表
            gevent_list.append(gevents)

        # 主线程等待
        gevent.joinall(gevent_list)

        end_time = time.time()
        t = end_time - start_time
        print(self.count)
        print(t)

if __name__ == '__main1__':
    Db250 = DoubanSpider2()
    Db250.run()