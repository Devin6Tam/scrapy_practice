#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/18 1:30
# @Author  : tanxw

import scrapy
# requests
# 1. headers = {"Cookies":""}
# 2. cookies = {}
# 3. 代码登陆 requests.session()

# scrapy
# 1.cookies = {} 不支持请求头里放cookie
# 2.代码登陆scrapy 自动保存cookies
# 3.from_response() 自动解析from表单的参数url
class GithubSpider(scrapy.Spider):
    name = "github"
    allowed_domains = ['github.com']
    start_urls = ['https://github.com']

    def start_requests(self):
        # 字典推导式
        cookie_str = '_octo=GH1.1.830369861.1582905826; _ga=GA1.2.2016560025.1582905829; _device_id=8d316ad6a18d8645ed8a222d93037910; user_session=IKBwZVawlqhw4GA8pLYaWCZSwTDs4lC4KDn1tVFcTG7KE2cJ; logged_in=yes; dotcom_user=Devin6Tam; has_recent_activity=1; tz=Asia%2FShanghai; _gh_sess=ENgonYGzKC3yENqDqvEoM7NDqMFOtGT%2B%2FMB%2BsNYvFA3uZqrdxCcGnnmDQsnF4CzoY%2BdgA%2F%2FyC94jca2gs37PAT4a%2F7TqWvvhOH3oSU6RWASOpTMWUp0VegTnu3kYP9G3UBq09vT%2Fpeuo8xQknDLcEk3%2FaSBBGpc8r%2Bn381C5UYzu9zgGwrdr4QwQ580l%2B%2F4Y--I8hIsZlYjRhrNrUK--lfB2Rql8j%2B0if2pr5CmFPQ%3D%3D'
        dict_cookies = {i.split('=')[0]:i.split('=')[1] for i in cookie_str.split('; ')}
        print(dict_cookies)
        for url in self.start_urls:
            print(url)
            yield scrapy.Request(url, cookies=dict_cookies, callback=self.parse)
            print("="*100)

    def parse(self, response):
        with open("code.html", 'wb') as f:
            print(response)
            f.write(response.body)
