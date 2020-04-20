# -*- coding: utf-8 -*-
from fake_useragent import UserAgent
from scrapy import Request
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline
from .items import CnbetaDetailItem
import pymysql

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class CnbetaDetailPipeline(ImagesPipeline):
    ua = UserAgent()
    default_headers = {
        'referer': 'http://www.cnbeta.com/',
        'User-Agent': ua.random
    }

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            self.default_headers['referer'] = image_url
            yield Request(image_url, headers=self.default_headers)

    def item_completed(self, results, item, info):
        # 列表推导式
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item

class RedisPipeline(object):

    def __init__(self):
        dbparams = {
            'host': '127.0.0.1',
            'port': 3306,
            'user': 'root',
            'password': '123456',
            'database': 'spider',
            'charset': 'utf8',
        }
        self.conn = pymysql.connect(**dbparams)
        self.cursor = self.conn.cursor()
        self._sql = None

    def process_item(self, item, spider):
        if isinstance(item, CnbetaDetailItem):
            self.cursor.execute(self.sql, (item['title'], item['publish_time'],
                                           item['referer'], item['content'], ','.join(item['image_urls'])))
            self.conn.commit()
        return item

    @property
    def sql(self):
        if not self._sql:
            self._sql = """
            insert into cnbeta(title,publish_time,referer,content,image_urls) values(%s,%s,%s,%s,%s)
            """
        return self._sql