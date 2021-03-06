#!/usr/bin/python
# -*- coding: utf-8 -*-
from neo4j import GraphDatabase, basic_auth
import scrapy
import json
from config import config 

class Neo4j(object):

    def __init__(self):
        self.driver = GraphDatabase.driver( config['neo4j']['address'],  auth=basic_auth( config['neo4j']['user'], config['neo4j']['password'] ))

    def close(self):
        self.driver.close()

    def update_data(self, data_dict): 

        result = None 

        while not result:
            try: 
                with self.driver.session() as session:
                    for country in data_dict:
                        result = session.run("""\
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
                    session.close()
            except Exception as e: 
                print('Error ', e)

    def update_source(self, source_dict):
        
        result = None 

        while not result:
            try: 
                with self.driver.session() as session:
                    result = session.run("""\
                        MERGE (s:Source {name: {name}})
                        SET s.link = {link}
                        SET s.last_updated = {last_updated}
                        """,{"name":source_dict['name'], "last_updated": source_dict['last_updated'], "link": source_dict['link']})
                    session.close()
            except Exception as e: 
                print('Error :', e)


    def get_by_name(self, name):

        properties = None

        while not properties:
            try: 
                with self.driver.session() as session:
                    print('GETTING DATA')
                    properties = session.run(""" 
                            MATCH (n:Country {name:{value}}), (s:Source)
                            RETURN properties(n), properties(s)
                            """,{"value": name})
                    session.close()
            except Exception as e: 
                print('Error ', e )

        properties_dict = [row for row in properties]
        properties_json = json.dumps(properties_dict)
        
        return properties_json 

    def get_all(self):
        
        database = None

        while not database: 
            try:
                with self.driver.session() as session:
                    database = session.run("""
                            MATCH (n:Country), (s:Source)
                            RETURN properties(n), properties(s)
                            """)
                    session.close()
            except Exception as e: 
                print('Error ', e )
        
        database_dict = [row for row in database]
        database_json = json.dumps(database_dict)


        return database_json
