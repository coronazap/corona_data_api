# -*- coding: utf-8 -*-
import scrapy
from data_crawler.items import DataCrawlerItem
import json 
class WorldometerSpider(scrapy.Spider):
    name = 'WorldOMeter'
    allowed_domains = ['https://www.worldometers.info/coronavirus/']
    start_urls = ['https://www.worldometers.info/coronavirus/']

    def parse(self, response):

        def split(array, size): 
            # Splits an array into multiples arrays of size "size" 
            arrays = [] 
            while len(array) > size: 
                piece = array[:size] 
                arrays.append(piece) 
                array = array[size:] 
            arrays.append(array)
            return arrays

        def clear_data(array): 
            # Remove linebreaks and empty spaces from array 
            array_clear = [] 
            for i, item in enumerate(array):
                if '\n' not in item: 
                    # Remove empty spaces from cell value 
                    array_clear.append(item.replace(' ', '')) 
                elif '\n' in item and '\n' in array[i - 1]:
                    if i < len(array) - 1 and 'Total' not in array[i + 1]: 
                        array_clear.append('0')

            return array_clear

        # Get table data 
        countries_data = response.css("table#main_table_countries_today tbody ::text").extract()
        # print('Getted data')
        # print(countries_data)
        # print(' ')

        # Clear data 
        countries_data = clear_data(countries_data)
        # print('Cleared data')
        # print(countries_data)
        # print(' ')

        # Split table lines
        countries_data = split(countries_data, 11 )
        # print('Splitted data')
        # print(countries_data)
        # print(' ')

        # Remove initial empty cells 
        countries_data = [ item[2:] for item in countries_data]
        # print('Formatted data')
        # print(countries_data)
        # print(' ')

        countries_dict = {} 

        for item in countries_data: 
            countries_dict[item[0]] = {
                'total_cases': item[1], 
                'new_cases': item[2], 
                'total_deaths': item[3], 
                'new_deaths': item[4], 
                'total_recovered': item[5], 
                'active_cases': item[6], 
                'serious_critical': item[7], 
                'total_cases_per_million': item[8] 
            }
        #countries_dict
        data_json = json.dumps(countries_dict)
        f = open("data.json","w")
        f.write(data_json)
        f.close()
        

                
