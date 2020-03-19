from flask import Flask, request 
from scrapy.crawler import CrawlerRunner 
from spiders import WorldOMeterSpider
from db_creator import create_data_db 
from stats_query import name_query
import atexit
import json
from multiprocessing import Process, Queue
from twisted.internet import reactor

from apscheduler.schedulers.background import BackgroundScheduler 

app = Flask(__name__) 

def run_spider(): 
    # Start the crawler 

    print('RUNNING SPIDER')
    results = {}

    def f(): 
        runner = CrawlerRunner()
        deferred = runner.crawl(WorldOMeterSpider, results=results) 
        deferred.addBoth(lambda _: reactor.stop()) 
        reactor.run()

    p = Process(target=f) 
    p.start()


@app.route('/data/<string:country_name>', methods=['GET'])
def get_country_data(country_name): 
    # Call funcion that makes a query to the databse            

    query_result = {} 

    query_result[country_name.upper()] = json.loads(name_query(country_name))[0]

    return query_result
 
if __name__ == '__main__':
    print('STARTING APPLICATION')
    # scheduler = BackgroundScheduler()
    # scheduler.add_job(func=run_spider, trigger="interval", seconds=60000) 
    # scheduler.start()
    
    run_spider()

    # atexit.register(lambda: scheduler.shutdown())
    app.run(debug=True)

