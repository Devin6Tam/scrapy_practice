# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

# 在这里为您爬取的项目定义字段，以便于保存到item对象
class CourseListItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    image = scrapy.Field()
    url = scrapy.Field()

class CourseDetailItem(scrapy.Item):
    # define the fields for your item here like:
    corse_intro = scrapy.Field()
    corse_target = scrapy.Field()
    corse_suitable_crowds = scrapy.Field()
