# -*- coding: utf-8 -*-
# 中间件定义及使用
from fake_useragent import UserAgent
import random
# USER_AGENT_LIST = []
# ua = UserAgent()
# for i in range(1, 21):
#     USER_AGENT_LIST.append(ua.random)
#
# print(USER_AGENT_LIST)

# 利用中间件反反爬
class UserAgentMiddleware(object):
    def process_request(self, request, spider):
        # 1.随机的ua
        # random_ua = random.choice(USER_AGENT_LIST)
        ua = UserAgent()
        random_ua = ua.random
        # 2.request.headers['USER_AGNET']
        request.headers['USER_AGENT'] = random_ua

        # 演示测试一下 传递请求是否生效

    def process_response(self, request, response, spider):
        print("#" * 100)
        print(request.headers['USER_AGENT'])
        return response

class ProxyMiddleware(object):
    def process_request(self, request, spider):
        # 拦截框架的请求request
        # 以前的代理
        # proxy = {"http":"IP:prot"}
        #框架里
        proxy = "http://192.168.0.6:8888"
        #设置
        request.meta['proxy'] = proxy