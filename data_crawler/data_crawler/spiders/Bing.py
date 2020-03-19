# -*- coding: utf-8 -*-
import scrapy


class BingSpider(scrapy.Spider):
    name = 'Bing'
    allowed_domains = ['https://www.bing.com/covid']
    start_urls = ['http://https://www.bing.com/covid/']

    def parse(self, response):
        pass
