# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisSpider, RedisCrawlSpider
# 用于处理原始内容信息
from w3lib import html
from lxml import etree

from scrapy_demo04.items import CnbetaDetailItem


class CnbetaSpider(RedisCrawlSpider):
    name = 'cnbeta_crawlredis'
    allowed_domains = ['cnbeta.com']
    # start_urls = ['http://www.cnbeta.com/']
    # 指纹
    redis_key = "cnbeta_crawlredis:start_urls"
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
        # referer = response.xpath('//div[@class="cnbeta-article"]/header/div[@class="meta"]/span[@class="source"]/a/span/text()').get()
        referer_origin = response.xpath('//div[@class="cnbeta-article"]/header/div[@class="meta"]/span[@class="source"]').get()
        referer = html.remove_tags(referer_origin, which_ones=('a', 'span')).strip()
        # 内容来源
        content_origin = response.xpath('//div[@class="cnbeta-article-body"]/div[@class="article-content"]').get()
        # 内容来源二次解析,除了img之外网页标签全部删除，只保留文本和配置保留的标签
        content = html.remove_tags(content_origin, keep=('img',)).strip()
        # 与上面解析方式相反，只删除这个指定的标签
        # content = html.remove_tags(content_origin, which_ones=('img',))
        content_html = etree.HTML(content)
        # 内容里的网站url地址列表
        image_urls = content_html.xpath('//img/@src')

        item = CnbetaDetailItem()
        item['title'] = title
        item['publish_time'] = publish_time
        item['referer'] = referer
        item['content'] = content
        item['image_urls'] = image_urls

        print(title)
        print(publish_time)
        print(referer)
        # print(content)
        print(image_urls)
        return item
