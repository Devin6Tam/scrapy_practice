# !/usr/bin/env python
# _*_ coding:utf-8 _*_
import requests
import json
import time

# http://www.yundama.com/apidoc/ 帮助文档
# http://www.yundama.com/price.html 云打码价格表
# 云打码解析工具
class YDMHttp:
    apiurl = 'http://api.yundama.com/api.php'

    def __init__(self):
        self.username = 'tanxw'
        self.password = 'xxxxx'
        self.appid = '10552'
        self.appkey = '6ad073764da15cfa0ae6319134bce7d8'

    def request(self, fields, files=[]):
        response = self.post_url(self.apiurl, fields, files)
        response = json.loads(response)
        return response

    def balance(self):
        data = {'method': 'balance', 'username': self.username, 'password': self.password, 'appid': self.appid,
                'appkey': self.appkey}
        response = self.request(data)
        if (response):
            if (response['ret'] and response['ret'] < 0):
                return response['ret']
            else:
                return response['balance']
        else:
            return -9001

    def login(self):
        data = {'method': 'login', 'username': self.username, 'password': self.password, 'appid': self.appid,
                'appkey': self.appkey}
        response = self.request(data)
        if (response):
            if (response['ret'] and response['ret'] < 0):
                return response['ret']
            else:
                return response['uid']
        else:
            return -9001

    def upload(self, filename, codetype, timeout):
        data = {'method': 'upload', 'username': self.username, 'password': self.password, 'appid': self.appid,
                'appkey': self.appkey, 'codetype': str(codetype), 'timeout': str(timeout)}
        file = {'file': filename}
        response = self.request(data, file)
        if (response):
            if (response['ret'] and response['ret'] < 0):
                return response['ret']
            else:
                return response['cid']
        else:
            return -9001

    def result(self, cid):
        data = {'method': 'result', 'username': self.username, 'password': self.password, 'appid': self.appid,
                'appkey': self.appkey, 'cid': str(cid)}
        response = self.request(data)
        return response and response['text'] or ''

    def decode(self, filename, codetype, timeout):
        cid = self.upload(filename, codetype, timeout)
        if (cid > 0):
            for i in range(0, timeout):
                result = self.result(cid)
                if (result != ''):
                    return cid, result
                else:
                    time.sleep(1)
            return -3003, ''
        else:
            return cid, ''

    def post_url(self, url, fields, files=[]):
        # for key in files:
        #     files[key] = open(files[key], 'rb');
        res = requests.post(url, files=files, data=fields)
        return res.text

def indetify(response_content):
    # 初始化
    yundama = YDMHttp()
    # 登陆云打码
    uid = yundama.login()
    print('uid: %s' % uid)
    # 查询余额
    balance = yundama.balance()
    print('balance: %s' % balance)

    # 开始识别，图片路径，验证码类型ID，超时时间（秒），识别结果
    cid, result = yundama.decode(response_content, 6300, 60)
    print('cid: %s, result: %s' % (cid, result))
    return result

def indetify_by_filepath(file_path):
    # 初始化
    yundama = YDMHttp()
    # 登陆云打码
    uid = yundama.login()
    print('uid: %s' % uid)
    # 查询余额
    balance = yundama.balance()
    print('balance: %s' % balance)
    # 开始识别，图片路径，验证码类型ID，超时时间（秒），识别结果
    cid, result = yundama.decode(file_path, 6300, 60)
    print('cid: %s, result: %s' % (cid, result))
    return result