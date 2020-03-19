from flask import Flask, request 
from scrapy.crawler import CrawlerRunner 
from spiders import WorldOMeterSpider
from db_creator import create_data_db 
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

    create_data_db(results)


@app.route('/data/<string:country_name>', methods=['GET'])
def get_country_data(country_name): 
    # Call funcion that makes a query to the databse            

    return country_name


if __name__ == '__main__':
    print('STARTING APPLICATION')
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=run_spider, trigger="interval", seconds=20) 
    scheduler.start()
    
    atexit.register(lambda: scheduler.shutdown())
    app.run(debug=True)

