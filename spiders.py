# -*- coding: utf-8 -*-
import scrapy
from model import update_db
from utils import split_array, clear_data, empty_for_zero
from countries import get_pt_name

class WorldOMeterSpider(scrapy.Spider):
    name = 'WorldOMeter'
    allowed_domains = ['worldometers.info']
    start_urls = ['https://www.worldometers.info/coronavirus/']


    def parse(self, response):    
        # Get table data 
        countries_data = response.css("table#main_table_countries_today tbody ::text").extract()
        # Clear data 
        countries_data = clear_data(countries_data)
        # Swap empty for zero
        countries_data = empty_for_zero(countries_data)
        # Split table lines
        countries_data = split_array(countries_data, 11 )

        # Remove initial empty cells 
        countries_data = [ item[2:] for item in countries_data]
        
        results = {}   

        print(len(countries_data))

        i = 0
        for item in countries_data:
            pt_name = get_pt_name(item[0])

            results[pt_name] = {
                'total_cases': item[1].replace(',',''), 
                'new_cases': item[2].replace(',',''), 
                'total_deaths': item[3].replace(',',''), 
                'new_deaths': item[4].replace(',',''), 
                'total_recovered': item[5].replace(',',''), 
                'active_cases': item[6].replace(',',''), 
                'serious_critical': item[7].replace(',',''), 
                'total_cases_per_million': item[8].replace(',','')
            } 
            i += 1
        
        print(i)
        # Save data to neo4j 
        update_db(results)

        

                
