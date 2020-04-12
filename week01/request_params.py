#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/11 17:33
# @Author  : tanxw
# @Desc    ：使用字典推导式获取Get请求地址中参数信息

a = "ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd=美女&oq=%25E7%25BE%258E%25E5%25A5%25B3&rsv_pq=c5b373120008fe0f&rsv_t=d395wla6YQdEj168mrQWmErvB8X2AkY1cvZrFb0RsIjY6T4QGlO3o83M2Qc&rqlang=cn&rsv_enter=0&rsv_dl=tb"

# 字典推导式
b = {x.split('=')[0]: x.split('=')[1] for x in a.split('&')}

print(b.get('wd'))