#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/15 0:03
# @Author  : tanxw
# @Desc    : 描述使用说明
import json

import lxml
import requests
from lxml import etree


class DoubanSpiderTop250(object):
    def __init__(self):
        self.url = 'https://movie.douban.com/top250?start={}&filter='
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
        }
        self.file = open('douban_movie_top250.json', 'a', encoding='utf-8')

    def get_repsponse(self, url):
        return requests.get(url, headers=self.header).text

    def parse(self, data):
        html = etree.HTML(data)
        nodes = html.xpath("//div[@class='info']")

        for node in nodes:
            content = {}
            content['url'] = node.xpath(".//div[@class='hd']/a/@href")[0]
            content['name'] = node.xpath(".//a/span[1]/text()")[0]
            content['introduce'] = node.xpath(".//p/span[@class='inq']/text()")[0]
            content['rating_num'] = node.xpath(".//span[@class='rating_num']/text()")[0]
            content['evaluate_num'] = node.xpath(".//div[@class='star']/span[4]/text()")[0]
            self.write_file(json.dumps(content, ensure_ascii=False) + ',\n')

    def write_file(self, content):
        self.file.write(content)

    def __del__(self):
        self.file.close()

    def run(self):
        i = 1
        while True:
            start = 25 * (i - 1)
            if start >= 250:
                break
            url = self.url.format(start)
            print(url)
            data = self.get_repsponse(url)
            self.parse(data)
            i += 1


if __name__ == '__main__':
    top250 = DoubanSpiderTop250()
    top250.run()