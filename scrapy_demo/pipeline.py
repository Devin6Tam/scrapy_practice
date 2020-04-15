#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/15 17:59
# @Author  : tanxw

# 管道处理
class Pipeline(object):

    # 解析下载数据
    def process_item(self, item):
        print("test...")
        return item