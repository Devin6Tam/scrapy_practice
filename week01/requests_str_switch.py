#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/16 13:58
# @Author  : tanxw
# @Desc    : string与bytes类型转换

#  1.网络当中数据传输都是用的bytes类型
#  2.bytes类型转string类型  decode() 解码
#  3.string类型转bytes类型  encode() 编码
#  4.用什么类型编码，就要用什么类型解码


str_data = "晚上好"

bytes_data = str_data.encode('utf-8')
print(bytes_data)

print(bytes_data.decode('utf-8'))
