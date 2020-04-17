#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/17 15:57
# @Author  : tanxw

a = 6

# print(type(6))
#
# print(isinstance(a, str))

class A:
    pass
class B(A):
    pass
print(isinstance(A(), A))
print(isinstance(B(), A))
print(type(A()) == A)
print(type(B()) == A)

"""
isinstance() 函数来判断一个对象是否是一个已知的类型，类似 type()。
isinstance() 与 type() 区别：
type() 不会认为子类是一种父类类型，不考虑继承关系。
isinstance() 会认为子类是一种父类类型，考虑继承关系。
如果要判断两个类型是否相同推荐使用 isinstance()。
"""