#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/20 10:08
# @Author  : tanxw
# @Desc    : 统一运行爬虫的入口文件
from scrapy import cmdline
# 运行方式一
# cmdline.execute(['scrapy','crawl', 'cnbeta'])
# 运行方式二
cmdline.execute('scrapy crawl cnbeta'.split())