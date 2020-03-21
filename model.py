#!/usr/bin/python
# -*- coding: utf-8 -*-
from neo4j import GraphDatabase, basic_auth
import scrapy
import json
from config import config 

class Neo4J(object):

    def __init__(self):
        self.driver = GraphDatabase.driver( config['neo4j']['address'],  auth=basic_auth( config['neo4j']['user'], config['neo4j']['password']), max_connection_lifetime=3600*24*30, keep_alive=True)

    def close(self):
        self.driver.close()

    def update_data(self, data_dict):
        sess = self.driver.session()

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

    def update_source(self, source_dict):
        sess = self.driver.session() 

        sess.run("""\
            MERGE (s:Source {name: {name}})
            SET s.link = {link}
            SET s.last_updated = {last_updated}
            """,{"name":source_dict['name'], "last_updated": source_dict['last_updated'], "link": source_dict['link']})
        print('Saved')

        sess.close()

    def get_by_name(self, name):
        sess = self.driver.session()
        properties = sess.run(""" 
                MATCH (n:Country {name:{value}}), (s:Source)
                RETURN properties(n), properties(s)
                """,{"value": name})

        sess.close()

        properties_dict = [row for row in properties]
        properties_json = json.dumps(properties_dict)

        return properties_json 

    def get_all(self):
        sess = self.driver.session()

        database = sess.run("""
                MATCH (n:Country), (s:Source)
                RETURN properties(n), properties(s)
                """)
        
        database_dict = [row for row in database]
        database_json = json.dumps(database_dict)

        sess.close()

        return database_json
