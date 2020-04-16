#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/16 17:33
# @Author  : tanxw
# @Desc    : jira 使用
# pip install jira

# jira模块使用
from jira import JIRA

# 连接jira服务，需要在服务器上构建
# server,username,password
jira = JIRA(server='http://192.168.43.199:8080', basic_auth=('root', 'a123456'))

jira.user(jira.current_user())
projects = jira.projects()
for project in projects:
    print(project)