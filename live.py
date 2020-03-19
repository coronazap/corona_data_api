from flask import Flask, request 
import requests 
from twilio.twiml.messaging_response import MessagingResponse 
import json 
from scrapy.crawler import CrawlerProcess 
from spiders import WorldOMeterSpider
from db_creator import create_data_db

app = Flask(__name__) 
process = CrawlerProcess() 

brazil_data = {} 
scrape_in_progress = False 
scrape_complete = False 

@app.route('/crawl', methods=['GET'])
def crawl(): 
    # Start the crawler 
    results = {}
    process.crawl(WorldOMeterSpider, results=results) 
    process.start() 

    create_data_db(results)
    # eventual.addCallback(finished_scrape) 
    return 'PONG'
    
def finished_scrape(data): 
    return data

if __name__ == '__main__':
   app.run(debug=True)

