# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DataCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    cases = scrapy.Field()
    deaths = scrapy.Field() 
    recovered = scrapy.Field()
    pass