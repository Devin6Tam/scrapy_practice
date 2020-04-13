#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/14 0:43
# @Author  : tanxw

import time
import requests
from lxml import etree
from fake_useragent import UserAgent
import threading


class DouBanSpider(object):
    def __init__(self):
        ua = UserAgent()
        self.base_url = "https://movie.douban.com/top250?filter=&start="
        self.headers = {"User-Agent": ua.random}
        self.count = 0

    # 1.请求
    def send_request(self, url):
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
        thread_list = []
        for page in range(0, 255+1, 25):
            # 拼接url
            url = self.base_url + str(page)
            # 创建线程
            threads = threading.Thread(target=self.send_request, args=[url])
            # 开启线程
            threads.start()
            # 放入列表
            thread_list.append(threads)

        # 让主线程等待
        for t in thread_list:
            print(t)
            t.join()

        end_time = time.time()
        t = end_time - start_time
        print(self.count)
        print(t)


if __name__ == '__main__':
    Db250 = DouBanSpider()
    Db250.run()