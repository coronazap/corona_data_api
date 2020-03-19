# -*- coding: utf-8 -*-
import scrapy

class WorldOMeterSpider(scrapy.Spider):
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

        # Clear data 
        countries_data = clear_data(countries_data)

        # Split table lines
        countries_data = split(countries_data, 11 )

        # Remove initial empty cells 
        countries_data = [ item[2:] for item in countries_data]

        for item in countries_data: 
            self.results[item[0].lower()] = {
                'total_cases': item[1], 
                'new_cases': item[2], 
                'total_deaths': item[3], 
                'new_deaths': item[4], 
                'total_recovered': item[5], 
                'active_cases': item[6], 
                'serious_critical': item[7], 
                'total_cases_per_million': item[8] 
            }

        

                
