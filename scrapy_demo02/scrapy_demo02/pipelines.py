# -*- coding: utf-8 -*-
from scrapy.exporters import JsonItemExporter

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class NewsDetailPipeline(object):
    def open_spider(self, spider):
        # w 写入字符创   wb 写入二进制
        self.file = open('detail_rednet.json', 'wb')
        # 写入器
        self.writer = JsonItemExporter(self.file)
        # 开启
        self.writer.start_exporting()

    def close_spider(self, spider):
        # 关闭写入器
        self.writer.finish_exporting()
        # 关闭文件
        self.file.close()

    def process_item(self, item, spider):

        print("==============启动管道============")
        self.writer.export_item(item)
        return item
