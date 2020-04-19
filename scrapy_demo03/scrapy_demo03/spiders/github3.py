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
    name = "github3"
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/login']

    def parse(self, response):
        print(response)

        formdata = {
            "login": "XXX",
            "password": "XXX",
        }
        # 发起请求(根据响应的路径)
        yield scrapy.FormRequest.from_response(response, formdata=formdata, callback=self.login_parse, dont_filter=True)

    def login_parse(self, response):
        with open("code3.html", 'wb') as f:
            print(response)
            f.write(response.body)


"""
总结：


scrapy中的cookies参数详解
COOKIES_ENABLED
默认： True

是否启用cookiesmiddleware。如果关闭，cookies将不会发送给web server。

COOKIES_DEBUG
默认： False

如果启用，Scrapy将记录所有在request(cookie 请求头)发送的cookies及response接收到的cookies（set-cookie接收头）




1.对于爬取普通网站，不需要验证码，不需要登入的界面，我们一般用scrapy.Request类直接去爬取信息就行。其中url，即要爬取的目标网站是必填的，其他的是选填的，method=‘GET’，说明此类是get请求，实例化该对象后，会得到一个response

2.scrapy.FormRequest与scrapy.http.FormRequest
（1）普通请求使用scrapy.Request类就可以实现，但是遇到模拟表单或Ajax提交post请求的时候，Request类就不如 子类 FormRequest类方便了，因为他自带 formdata ，专门用来设置表单字段数据，即填写账号、密码，实现登入，默认method也是POST。
（2）FormRequest相当于是手动指定post。
（3）事实上，scrapy.FormRequest()与scrapy.http.FormRequest()使用起来的区别不大，你可以将两种方法等价互换。

3.scrapy.FormRequest与FormRequest.from_response 的区别：

1.什么情况下分别使用什么
先找到填写表单时发送的post请求的地址

发现页面没有表单信息（也就是没有填写账号、密码的地方），所以，我们只能采用scrapy.FormRequest，手动的去发送post请求。
如果浏览器访问某post网址时，里面有表单信息，这时候你可以用FormRequest.from_response也可以用scrapy.FormRequest实现模拟登入

2.参数的不一样
scrapy.FormRequest的必填参数是目标网址，而FormRequest.from_response的必填参数是response
总的来说，scrapy.FormRequest的功能更加强大，如果FormRequest.from_response 不能解决就用scrapy.FormRequest来解决模拟登入，毕竟是手动设置目标网址，比自动识别要精准。
"""