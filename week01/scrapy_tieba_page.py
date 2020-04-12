#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/11 1:29
# @Author  : tanxw
# @Desc    : 爬取贴吧某个页面
import requests

# class TiebaSpider(object):
#
#     def __init__(self):
#         self.base_url = "http://tieba.baidu.com/f"
#         self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"}
#
#     # 1.请求
#     def send_request(self, tieba_params):
#         response = requests.get(self.base_url, headers=self.headers, params=tieba_params)
#         data = response.content
#         return data
#
#     # 2.保存数据
#     def write_file(self, data):
#         with open("tieba.html", "wb") as f:
#             f.write(data)
#
#     def run(self):
#         # 1.拼接参数
#         tieba_params = {
#             "kw": "美食",
#             "pn": 0
#         }
#         # 发起请求
#         data = self.send_request(tieba_params)
#         # 保存数据
#         self.write_file(data)
#
#
# if __name__ == '__main__':
#     tool = TiebaSpider()
#     tool.run()

class TiebaSpider(object):
    def __init__(self):
        self.tieba_name = input("请输入贴吧的名字：")
        self.start_page = int(input("开始页数："))
        self.end_page = int(input("结束页数："))

        self.base_url = "http://tieba.baidu.com/f"
        self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"}

    # 1.请求
    def send_request(self, tieba_params):
        response = requests.get(self.base_url, headers=self.headers, params=tieba_params)
        data = response.content
        return data

    # 2.保存数据
    def write_file(self, data, page):
        file_pat = "Tieba/" + str(page) + ".html"
        print("正在抓取{}页面...".format(page))
        with open(file_pat, "wb") as f:
            f.write(data)

    def run(self):
        for page in range(self.start_page, self.end_page + 1):
            # 1.拼接参数
            tieba_params = {
                "kw": self.tieba_name,
                "pn": (page-1) * 50
            }
            # 发起请求
            data = self.send_request(tieba_params)
            # 保存数据
            self.write_file(data, page)


if __name__ == '__main__':
    tool = TiebaSpider()
    tool.run()