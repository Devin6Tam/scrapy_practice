# -*- coding: utf-8 -*-
import json

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# 管道（负责清洗，保存数据）
class ScrapyDemo01Pipeline(object):
    # 爬虫开启 打开文件
    def open_spider(self, spider):
        self.file = open('course2.txt', 'w', encoding='utf8')

    # 爬虫关闭 关闭文件
    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        print("================启动管道===============")
        # with open('course.txt', 'a', encoding='utf8') as f:
        #     # 1.转成字典 IO优化 硬盘读写
        #     dict_data = dict(item)
        #     # 2.转成json字符串
        #     str_data = json.dumps(dict_data, ensure_ascii=False) + "\n"
        #     f.write(str_data)
        # print(spider.name)
        dict_data = dict(item)
        str_data = json.dumps(dict_data, ensure_ascii=False) + "\n"
        self.file.write(str_data)
        print("================结束管道===============")
        return item
