#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify
import os 

# Scrapy
from scrapy.crawler import CrawlerRunner 
from spiders import WorldOMeterSpider

from model import Neo4j # , get_all, get_by_name, update_data, update_source

import atexit
import json
from multiprocessing import Process, Queue
from twisted.internet import reactor

from apscheduler.schedulers.background import BackgroundScheduler 

app = Flask(__name__) 

def run_spider(): 
    db = Neo4j()
    # Start the crawler 
    def on_complete(results, source_dict):
        db.update_source(source_dict)
        db.update_data(results)
        db.close()
    
    def f(): 
        runner = CrawlerRunner()
        deferred = runner.crawl(WorldOMeterSpider, on_complete=on_complete) 
        deferred.addBoth(lambda _: reactor.stop()) 
        reactor.run()

    p = Process(target=f) 
    p.start()


@app.route('/api/<string:country_name>', methods=['GET'])
def get_country_data(country_name): 
    # Call funcion that makes a query to the databse   
    
    db = Neo4j()      
    query_result = {} 

    query_result['data'] = {}

    results = json.loads(db.get_by_name(country_name))       

    db.close()
    if len(results) == 0: 
        return 'Não há casos de COVID-19 neste país.'
    
    query_result['data'][country_name.upper()] = results[0][0]
    query_result['_source'] = results[0][1]

    db.close()
    return jsonify(query_result)


@app.route('/api', methods=['GET']) 
def get_data(): 

    db = Neo4j()
    query_result = {} 

    query_result['data'] = {}

    results = json.loads(db.get_all())

    db.close()

    for item in results: 
        query_result['data'][item[0]['name'].upper()] = item[0]

    query_result['_source'] = results[0][1]

    return jsonify(query_result)

run_spider()
scheduler = BackgroundScheduler()
scheduler.add_job(func=run_spider, trigger="interval", seconds=5) 
scheduler.start()

if __name__ == '__main__':
    # 
    app.run(debug=True)

