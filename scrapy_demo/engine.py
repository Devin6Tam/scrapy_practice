#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/15 17:54
# @Author  : tanxw

# 引擎，负责调度每个模块
from .scheduler import Scheduler
from .spider import Spider
from .downloader import Downloader
from .pipeline import Pipeline

class Engine(object):
    def __init__(self):
        self.spider = Spider()
        self.scheduler = Scheduler()
        self.downloader = Downloader()
        self.pipeline = Pipeline()

    def run(self):
        pass