# -*- coding: utf-8 -*-
import scrapy


class WorldometerSpider(scrapy.Spider):
    name = 'WorldOMeter'
    allowed_domains = ['https://www.worldometers.info/coronavirus/']
    start_urls = ['https://www.worldometers.info/coronavirus/']

    def parse(self, response):

        # Get world data 
        world_data = response.css('div.maincounter-number span ::text').extract() 

        world_cases = int(data[0].replace(',', ''))
        world_deaths = int(data[1].replace(',', ''))
        world_recovered = int(data[2].replace(',', ''))
                
        yield { 'cases': world_cases, 'deaths': world_deaths, 'recovered': world_recovered }
