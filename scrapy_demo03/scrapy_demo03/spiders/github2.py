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
    name = "github2"
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/login']

    def parse(self, response):
        print(response)
        # 登录的url
        login_url = 'https://github.com/session'
        # 登录信息
        authenticity_token = response.xpath('//*[@id="login"]/form/input[1]/@value').extract_first()
        ga_id = response.xpath('//*[@id="login"]/form/input[2]/@value').extract_first()
        timestamp = response.xpath('//*[@id="login"]/form/div[4]/input[7]/@value').extract_first()
        timestamp_secret = response.xpath('//*[@id="login"]/form/div[4]/input[8]/@value').extract_first()
        formdata = {
            "login": "XXX",
            "password": "XXX",
            "webauthn-support": "supported",
            "webauthn-iuvpaa-support": "unsupported",
            "authenticity_token": authenticity_token,
            "ga_id": ga_id,
            "timestamp": timestamp,
            "timestamp_secret": timestamp_secret,
            "commit": "Sign in",
        }
        print(formdata)
        # 发起请求 这里反反爬了

        yield scrapy.FormRequest(login_url, formdata=formdata, callback=self.login_parse, dont_filter=True)

    def login_parse(self, response):
        with open("code2.html", 'wb') as f:
            print(response)
            f.write(response.body)
