# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from w3lib import html

class CnbetaSpider(CrawlSpider):
    name = 'cnbeta'
    allowed_domains = ['cnbeta.com']
    start_urls = ['http://cnbeta.com/']

    rules = (
        Rule(LinkExtractor(allow=r'articles/.*'), callback='parse_detail', follow=True),
    )

    def parse_detail(self, response):
        item = {}
        # 标题
        title = response.xpath('//div[@class="cnbeta-article"]/header/h1/text()').get()
        # 发布时间
        publish_time = response.xpath('//div[@class="cnbeta-article"]/header/div[@class="meta"]/span[1]/text()').get()
        # 来源
        referer = response.xpath('//div[@class="cnbeta-article"]/header/div[@class="meta"]/span[@class="source"]/a/span/text()').get()
        # 内容
        content = response.xpath('//div[@class="cnbeta-article-body"]/div[@class="article-content"]/').get()

        print(title)
        print(publish_time)
        print(referer)
        print(content)
        return item
