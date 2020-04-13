#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/13 16:56
# @Author  : tanxw

# https://tieba.baidu.com/f?ie=utf-8&kw=美食吧&fr=search&pn=0&
import requests, json
from fake_useragent import UserAgent
from lxml import etree

# ua = UserAgent()
# start_url = "https://tieba.baidu.com/mo/q/m?kw=%E7%BE%8E%E9%A3%9F&pn=0&lp=5024&forum_recommend=1&lm=0&cid=0&has_url_param=90&pn=0&is_ajax=1"
# headers = {"User-Agent": ua.random}
# r = requests.get(start_url, headers=headers)
# html = r.content.decode()
# # print(html)
# html_dict = json.loads(html)["data"]["content"]
# # print(html_dict)
# t = etree.HTML(html_dict)
# href_list = t.xpath('//li[@class="tl_shadow tl_shadow_new "]/a/@href')
# print(href_list)
# #https://tieba.baidu.com/p/6355219109?lp=5028&mo_device=1&is_jingpost=0

class TiebaSpider(object):
    def __init__(self):
        ua = UserAgent()
        self.base_url = "http://tieba.baidu.com/f"
        self.headers = {"User-Agent": ua.random}

    # 1. 发送请求
    def send_request(self, url, tieba_params={}):
        response = requests.get(url, headers=self.headers, params=tieba_params)
        data = response.content
        print(data.decode())
        return data

    # 2.解析数据
    def parse_data(self, data, rule):
        # 1.转类型
        html_data = etree.HTML(data)
        # 2. XPATH
        result_list = html_data.xpath(rule)
        return result_list

    # 3.保存图片数据
    def write_file(self, data, img_name): # 1.png
        print(img_name)
        img_path = "images/" + img_name
        with open(img_path, "wb") as f:
            f.write(data)

    # 4.调度方法
    def run(self):
        #1.发送
        tieba_params = {"kw": "美食", "pn": 1}
        list_data = self.send_request(self.base_url, tieba_params)
        # 正则获取被注释的源码
        detail_rule = '//div[@class="t_con cleafix"]/div/div/div/a/@href'
        # 2.获取详情页URL
        detail_url_list = self.parse_data(list_data, detail_rule)
        print(detail_url_list)
        # 3. 发送详情页的请求
        for detail in detail_url_list:
            detail_url = "http://tieba.baidu.com" + detail
            detail_data = self.send_request(detail_url)

            # 解析图片
            image_rule = '//img[@class="BDE_Image"]/@src'
            image_url_list = self.parse_data(detail_data, image_rule)

            # 发送图片的请求
            for img_url in image_url_list:
                img_data = self.send_request(img_url)

                # 图片的名字
                img_name = img_url[-15:]
                # 保存图片
                self.write_file(img_data, img_name)

class DoubanSpider(object):
    def __init__(self):
        ua = UserAgent()
        self.base_url = "https://movie.douban.com/top250?filter=&start="
        self.headers = {"User-Agent": ua.random}
        self.count = 0
    # 1.请求
    def send_request(self, url):
        response = requests.get(url, headers=self.headers)
        data = response.content
        return data

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
        for page in range(0,255+1,25):
            # 拼接url
            url = self.base_url + str(page)
            data = self.send_request(url)
            # 解析数据
            self.parse_file(data)

        print(self.count)

if __name__ == '__main__':
    # BaiduTieba = TiebaSpider()
    # BaiduTieba.run()
    DoubanSpider().run()



