from neo4j import GraphDatabase, basic_auth
import scrapy
import json
import os

driver = GraphDatabase.driver("bolt://192.168.0.30:7687",  auth=basic_auth("neo4j", "nindoo123"))
sess = driver.session()

def create_data_db(data_dict):
    for country in data_dict:
        #print(data_dict[country])
        sess.run("""
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
    print("--- Dataset Criado ---")

def create_context_db(context_dict):

    pass



##node do tipo (sintoma,etc) -> node contexto, transformar cada c