#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/15 16:32
# @Author  : tanxw
# @Desc    : 自动化-获取平台短信

from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.XXXX.com/sz/")
driver.find_element_by_class_name("js-close-finance-pop").click()
driver.find_element_by_id('js-login-new').click()
with open('sms_list.txt', 'r', encoding='utf8') as f:
    # 输入手机号，点击获取验证码
    phone_input = driver.find_element_by_name('phone')
    phone_input.clear()
    # phone_input.send_keys('13838383838')
    phone_input.send_keys(f.readline())
    driver.find_element_by_class_name('get-code').click()
driver.close()