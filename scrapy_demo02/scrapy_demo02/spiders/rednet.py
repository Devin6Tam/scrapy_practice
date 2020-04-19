# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_demo02.items import NewDetailItem

class RednetSpider(CrawlSpider):
    name = 'rednet'
    allowed_domains = ['rednet.cn']
    start_urls = ['https://news.rednet.cn/channel/8394.html']

    rules = (
        # 新闻列表页面 follow 循环提取
        Rule(LinkExtractor(allow=r'/channel/8394'), callback='parse_item', follow=True),
        # 新闻详情页面
        Rule(LinkExtractor(allow=r'/content/2020/04'), callback='parse_detail', follow=True),
    )

    def parse_item(self, response):
        print("=" * 100)
        print(response.url)
        pass


    def parse_detail(self, response):
        print("-"*100)
        print(response.url)
        detail_item = NewDetailItem()
        detail_item['title'] = response.xpath('//main/section[@class="overf block"]/section[@class="box_left f_left"]/h1/text()').extract_first()
        detail_item['writer'] = response.xpath('//article/section[2]/p[@class="f14 m_t_5 m_b_5 h20"]/text()').extract_first()
        detail_item['referer'] = response.xpath('//article/section[2]/p[@class="f14 m_t_50 m_b_5 h20"]/text()').extract_first()
        print(detail_item)
        yield detail_item
