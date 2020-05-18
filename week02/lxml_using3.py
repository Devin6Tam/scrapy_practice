#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/15 23:27
# @Author  : tanxw
# @Desc    : 描述使用说明
import json

import requests
from lxml import etree

with open('guokr_question.json', 'a', encoding='utf8') as f:
    url = 'https://www.guokr.com/ask/highlight?page=1'
    text = requests.get(url).text
    # print(text)

    html = etree.HTML(text)
    nodes = html.xpath('//div[@class="ask-list-detials"]')
    # nodes 是20个问题的节点列表

    for node in nodes:
        dict_data = {}
        dict_data['title'] = node.xpath(".//h2/a/text()")[0]
        dict_data['url'] = node.xpath(".//h2/a/@href")[0]
        # dict_data['content'] = node.xpath(".//p/text()")[0]
        # print(dict_data)
        detail_text = requests.get(dict_data['url']).text
        detail_html = etree.HTML(detail_text)
        dict_data['question'] = '没有问题的详情页'
        try:
            dict_data['question'] = detail_html.xpath("//div[@id='questionDesc']/p[2]/text()")[0]
        except Exception as e:
            pass
        dict_data['answer'] = detail_html.xpath("//div[@class='answer-r']/div[3]/p/text()")[0]
        print(dict_data)
        f.write(json.dumps(dict_data, ensure_ascii=False) + '\n')
