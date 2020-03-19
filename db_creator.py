from neo4j import GraphDatabase, basic_auth
import scrapy

import bot
### rodar da pasta spiders: scrapy runspider WorldOMeter.py
driver = GraphDatabase.driver( "bolt://localhost:7687",  auth=basic_auth("neo4j", "nindoo123"))
cd
sess = driver.session()

def get_dict():