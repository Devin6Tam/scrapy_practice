#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/12 21:15
# @Author  : tanxw
# @Desc    : 爬取影评信息，仅个人示例练习
import json

import jsonpath
import requests


class DoubanSpider(object):
    # 初始化 变量信息
    def __init__(self):
        self.url = "https://m.douban.com/rexxar/api/v2/subject_collection/tv_american/items?os=windows%207&for_mobile=1&callback=jsonp{}&start={}&count={}&loc_id=108288&_=1589289727975"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36",
            "Referer": "https://m.douban.com/tv/american"
        }
        self.file = open('douban_movie.json', 'a', encoding='utf8')

    # 获取响应内容
    def get_response(self, url):
        r = requests.get(url, headers=self.headers)
        return r.content.decode('utf8')

    # 解析数据
    def parse(self, text):
        # print(text)
        dict_obj = json.loads(text[8:-2])
        # print(dict_obj)
        return dict_obj

    # 保存数据
    def save(self, dict_data):
        self.file.write(json.dumps(dict_data, ensure_ascii=False)+"\n")
        # with open('douban_movie.json', 'a', encoding='utf8') as f:
        #     f.write(json.dumps(dict_data, ensure_ascii=False)+"\n")

    # 销毁操作 - 文件关闭
    def __del__(self):
        self.file.close()

    # 统一的运行入口
    def run(self):
        current_page = 1
        start = 0
        count = 5
        for i in range(1, 10):
            url = self.url.format(current_page, start, count)
            print(url)
            text = self.get_response(url)
            dict_data = self.parse(text)
            result_list = jsonpath.jsonpath(dict_data, '$..subject_collection_items')[0]
            print(result_list)
            start = jsonpath.jsonpath(dict_data, '$..start')[0]
            count = jsonpath.jsonpath(dict_data, '$..count')[0]
            total = jsonpath.jsonpath(dict_data, '$..total')[0]
            start = current_page * count
            if count % 5 != 0:
                break
            elif start + count > total:
                count = total - start
            current_page += 1
            if result_list:
                for result in result_list:
                    self.save(result)


if __name__ == '__main__':
    doubanSpider = DoubanSpider()
    doubanSpider.run()
