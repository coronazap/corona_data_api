from neo4j import GraphDatabase, basic_auth
import scrapy
import json
from config import config 

### rodar da pasta spiders: scrapy runspider WorldOMeter.py
driver = GraphDatabase.driver( config['neo4j']['address'],  auth=basic_auth( config['neo4j']['user'], config['neo4j']['password']) )
sess = driver.session()

def update_db(data_dict, source_dict):
    sess = driver.session()
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

    sess.run("""\
        UNWIND {features} AS data
        MERGE (a:Source {name: {name}})
        SET a.link = data.link 
        SET a.last_updated = data.last_updated
        """, { "name": source_dict.name, "features": source_dict })

    sess.close()

def get_by_name(name):
    sess = driver.session()
    properties = sess.run(""" 
            MATCH (n:Country {name:{value}}) 
            RETURN properties(n)
            """,{"value": name})

    sess.close()

    properties_dict = [row for row in properties]
    properties_json = json.dumps(properties_dict)

    return properties_json


def get_all():
    sess = driver.session()
    database = sess.run("""
            MATCH (n:Country)
            RETURN properties(n)
            """)
    database_dict = [row for row in database]
    database_json = json.dumps(database_dict)


    sess.close()

    return database_json
