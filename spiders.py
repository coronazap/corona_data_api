# -*- coding: utf-8 -*-
import scrapy
from db_creator import create_data_db

class WorldOMeterSpider(scrapy.Spider):
    name = 'WorldOMeter'
    allowed_domains = ['worldometers.info']
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
            new_array = [] 
            for i, item in enumerate(array):
                
                if '\n' not in item: 
                    # Remove empty spaces from cell value 
                    new_array.append(item.replace(' ', '')) 
                elif '\n' in item and '\n' in array[i - 1]:
                    if i < len(array) - 1 and 'Total' not in array[i + 1]: 
                        new_array.append('0')
            return new_array

        def empty_for_zero(array): 
            new_array = []
            for item in array: 
                if item == '': 
                    new_array.append('0') 
                else: 
                    new_array.append(item)             
            return new_array

        # Get table data 
        countries_data = response.css("table#main_table_countries_today tbody ::text").extract()
        
        # Clear data 
        countries_data = clear_data(countries_data)
        
        # Swap empty for zero
        countries_data = empty_for_zero(countries_data)

        # Split table lines
        countries_data = split(countries_data, 11 )

        # Remove initial empty cells 
        countries_data = [ item[2:] for item in countries_data]
        
        for item in countries_data:
            self.results[item[0].lower()] = {
                'total_cases': item[1].replace(',',''), 
                'new_cases': item[2].replace(',',''), 
                'total_deaths': item[3].replace(',',''), 
                'new_deaths': item[4].replace(',',''), 
                'total_recovered': item[5].replace(',',''), 
                'active_cases': item[6].replace(',',''), 
                'serious_critical': item[7].replace(',',''), 
                'total_cases_per_million': item[8].replace(',','')
            } 

        create_data_db(self.results)

        

                
