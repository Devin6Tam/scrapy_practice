# -*- coding: utf-8 -*-
import scrapy
from lxml import etree
from scrapy_demo01.items import CourseListItem, CourseDetailItem

class SixstarSpider(scrapy.Spider):
    # 爬虫名称
    name = 'sixstar'
    # 允许爬取域名网站地址集合
    allowed_domains = ['sixstaredu.com']
    # 开始爬取的页面
    base_url = 'http://www.sixstaredu.com/course/explore?page={}'

    # A.如已确定总页面数，可以遍历生成url，然后存在start_urls集合中
    page = 1
    start_urls = []
    for i in range(1, 3):
        url = base_url.format(i)
        start_urls.append(url)

    # B 方案注释内容
    # page = 1
    # url = base_url.format(page)
    # start_urls = [url]

    # 数据提取的方法 接收下载中间件传过来的response
    def parse(self, response):
        # names = response.xpath('//div[@class="course-img"]/a/img/@alt')
        name_list = response.xpath('//div[@class="course-img"]/a')
        # for name in names:
        #     print(name.extract())
        # 如果没有数据，爬取要结束
        # if not name_list:
        #     return
        if self.page == 3:
            return

        for dc in name_list:
            item = CourseListItem()
            # 提取课程的名字 dc.xpath(".//img/@alt")[0].extract() 不存在，根据索引取提示异常
            item["name"] = dc.xpath(".//img/@alt").extract_first()
            # 提取课程封面 dc.xpath(".//img/@src")[0].extract() 不存在，根据索引取提示异常
            item["image"] = dc.xpath(".//img/@src").extract_first()
            # 提取课程链接 dc.xpath(".//@href")[0].extract() 不存在，根据索引取提示异常
            item["url"] = dc.xpath(".//@href").extract_first()
            # print(item)
            yield item
            # yield 在这里能够传递对象有：BaseItem,Request,dict,None

            detail_url = "http://www.sixstaredu.com" + dc.xpath(".//@href").extract_first()
            print(detail_url)
            yield scrapy.Request(detail_url, callback=self.parse_detail, dont_filter=True)
            self.page += 1

        # B.不确定网站有多少页，可以根据页面显示条数比较，是不是最末的一页
        # if len(name_list) == 20:
        #     self.page += 1
        #     print(self.page)
        #     url = self.base_url.format(self.page)
        #     print(url)
        #     # 递归请求抓取
        #     yield scrapy.Request(url, callback=self.parse, dont_filter=True)

    def parse_detail(self, response):
        print("详情页解析")
        detail_list = response.xpath('//div[@class="course-detail-content"]')
        detail_item = CourseDetailItem()
        for detail in detail_list:
            detail_item['corse_intro'] = detail.xpath('.//div[1]/div[2]/p[1]//text()').extract_first()
            detail_item['corse_target'] = detail.xpath('.//div[1]/div[2]/p[1]/text()').extract_first()
            detail_item['corse_suitable_crowds'] = detail.xpath('.//div[3]/div[2]/ul/li/text()').extract_first()
            print(detail_item)
            yield detail_item
"""
A,B 方案不可并用

A 方案遍历start_urls,抓取每个链接页面的内容,无序爬取
B 递归执行parse方法,每次递归请求前，生成新的链接地址，以便抓取新的链接页面的内容，有序爬取
"""