from neo4j import GraphDatabase, basic_auth
import scrapy
import json
import os
### rodar da pasta spiders: scrapy runspider WorldOMeter.py
driver = GraphDatabase.driver( "bolt://192.168.0.30:7687",  auth=basic_auth("neo4j", "nindoo123"))
sess = driver.session()
def create_data_db(data_dict):
    for country in data_dict:
        sess.run("""\
            UNWIND {features} AS data
            MERGE (a:Country {name: {name}})
            SET a.total_cases =  toInt(data.total_cases)
            SET a.new_cases = toInt(data.new_cases)
            SET a.total_deaths = toInt(data.total_deaths)
            SET a.new_deaths = toInt(data.new_deaths)
            SET a.total_recovered = toInt(data.total_recovered)
            SET a.active_cases = toInt(data.active_cases)
            SET a.serious_critical = toInt(data.serious_critical)
            SET a.total_cases_per_million = toInt(data.total_cases_per_million)
            """,{"name":country, "features": data_dict[country]})
    sess.close()

with open('./data_crawler/data_crawler/spiders/data.json') as file_data:
    data  = json.load(file_data) 
    create_data_db(data)
    print("--- Dataset Estatisticos Criado ---")
          

##node do tipo (sintoma,etc) -> node contexto, transformar cada c