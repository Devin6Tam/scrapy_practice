#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/14 14:38
# @Author  : tanxw
# @Desc    : selenium 使用
# pip install selenim
import time
from selenium import webdriver
# 1. 初始化浏览器对象
driver = webdriver.Firefox()

# 访问百度，并截屏
##########################################
# # 2.请求
# driver.get("https://www.baidu.com")
#
# # 3.截图 保存
# driver.save_screenshot("baidu.png")

# 访问json.cn,解析json并将结果转化为xml
##########################################
# driver.get("https://www.json.cn")
# # 给输入框输入内容
# input_element = driver.find_element_by_id('json-src')
# input_element.clear()
# input_element.send_keys('{"a":"10","b":"yes"}')
#
# # class="tip xml" // class="tip" class="xml"
# xml_element = driver.find_element_by_class_name('xml')
# xml_element.click()
#
# print(driver.page_source)

# driver.find_element_by_xpath('/html/body/footer/div[1]/a[2]').click()
# print(driver.window_handles)

# 登录QQ邮箱   XXXXXX 个人邮箱账号、密码
##########################################
# driver.get("https://mail.qq.com/")
# # driver.get("https://mail.qq.com/cgi-bin/loginpage?autologin=n&errtype=4&clientuin=XXXXXX&t=&vt=passport&param=&sp=003bf5eeca5e3aaMTU4Njg1ODI5Mw&tfcont=22%20serialization%3A%3Aarchive%205%200%200%206%200%200%200%208%20authtype%201%204%207%20spcache%2029%20003bf5eeca5e3aaMTU4Njg1ODI5Mw%202%20sp%2029%20003bf5eeca5e3aaMTU4Njg1ODI5Mw%209%20clientuin%209%20184514627%206%20domain%206%20qq.com%202%20vm%203%20wsk&r=a6496555710dcd5f1a1451914752249b")
# login_frame = driver.find_element_by_id("login_frame")
# driver.switch_to.frame(login_frame)
# driver.find_element_by_id("switcher_plogin").click()
#
# username = driver.find_element_by_id('u')
# username.clear()
# username.send_keys('XXXXXX')
#
# password = driver.find_element_by_id('p')
# password.clear()
# password.send_keys('Tan910312Wu')
#
# login_button = driver.find_element_by_class_name('login_button')
# login_button.click()
#
# try:
#     # 设置独立密码，会跳到这里... 这种情况有点复杂，直接使用下面的链接来登录
#     # "https://mail.qq.com/cgi-bin/loginpage?autologin=n&errtype=4&clientuin=XXXXXX&t=&vt=passport&param=&sp=003bf5eeca5e3aaMTU4Njg1ODI5Mw&tfcont=22%20serialization%3A%3Aarchive%205%200%200%206%200%200%200%208%20authtype%201%204%207%20spcache%2029%20003bf5eeca5e3aaMTU4Njg1ODI5Mw%202%20sp%2029%20003bf5eeca5e3aaMTU4Njg1ODI5Mw%209%20clientuin%209%20184514627%206%20domain%206%20qq.com%202%20vm%203%20wsk&r=a6496555710dcd5f1a1451914752249b"
#     to_password = driver.find_element_by_id('p')
#     if to_password:
#         to_password.send_keys("XXXXXX")
#
#         login_button = driver.find_element_by_class_name('login_button')
#         login_button.click()
# except Exception as e:
#     print(e.__str__())
#
# # 截屏
# driver.save_screenshot("mail.png")

# driver.close()

# 豆瓣
##########################################
# driver.get("https://www.douban.com/")
# ret2 = driver.find_element_by_tag_name('h1')
# print(type(ret2))
# print(ret2.text)

# ret = driver.find_elements_by_link_text('下载豆瓣 App') # 列表
# print(type(ret))
# href = ret[0].get_attribute("href")
# print(href) #https://www.douban.com/doubanapp/app?channel=nimingye
# ret[0].click()


# 登录框 是一个嵌套网页，需要跳转过去
# frame = driver.find_element_by_xpath("//iframe[contains(@src,'//accounts.douban.com/passport/login_popup?login_source=anony')]")
# driver.switch_to.frame(frame)
#
# # 登录框 提供了多种登录方式（短信验证码，密码，二维码）
# account_tab = driver.find_element_by_class_name('account-tab-account')
# account_tab.click()
#
#
# username = driver.find_element_by_id('username')
# username.clear()
# username.send_keys('18898750918')
#
# username = driver.find_element_by_id('password')
# username.clear()
# username.send_keys('a123456')
#
# login_button = driver.find_element_by_class_name('btn-account')
# login_button.click()
#
# error_str = driver.find_element_by_class_name("fatal-msg").text
# print(error_str)

"""
# HTML 标签名称，如iframe,body,footer,div等
driver.find_element_by_tag_name()
# Html 元素ID
driver.find_element_by_id()
# Html 元素名称
driver.find_element_by_name()
# 看成xml路径，然后填入路径 如：/html/body/footer/div[0]/a[2]
driver.find_element_by_xpath()
# css 样式 如：class=xml
driver.find_elements_by_class_name()
# css 标签选择器 如：'input[class="bn-submit"]'
driver.find_element_by_css_selector()
# 链接文本内容
driver.find_elements_by_link_text()
"""