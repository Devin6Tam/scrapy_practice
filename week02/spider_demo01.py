#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/12 22:50
# @Author  : tanxw
# @Desc    : 爬虫示例1 - 抓取豆瓣影视信息

import requests
import json

class DoubanSpider(object):

    def __init__(self):
        self.start_url = "https://m.douban.com/rexxar/api/v2/subject_collection/tv_american/items?os=ios&for_mobile=1&callback=jsonp1&start={}&count=18&loc_id=108288&_=0"
        # 跳过反爬策略，需要加上referer
        self.headers = {
            "Referer": "https://m.douban.com/tv/chinese",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
        }

    def parse_url(self, url):
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def get_content_list(self, json_str):
        json_str = json_str[8:-2:]
        print(json_str)
        dict_ret = json.loads(json_str)
        content_list = dict_ret["subject_collection_items"]
        return content_list

    def save_content_list(self, content_list):
        with open("douban.txt", "a", encoding="utf8") as f:
            for x in content_list:
                f.write(json.dumps(x, ensure_ascii=False))
                f.write("\n")  # 写入换行符进行换行

    def run(self):
        # 1.构造连接
        num = 0
        while True:
            url = self.start_url.format(num)
            # 2.发送请求 获得响应
            json_str = self.parse_url(url)
            # 3.提取数据
            content_list = self.get_content_list(json_str)
            # 4.保存文件
            self.save_content_list(content_list)
            if len(content_list) < 18:
                break
            print(num)
            num += 18

if __name__ == '__main__':
    spider = DoubanSpider()
    spider.run()