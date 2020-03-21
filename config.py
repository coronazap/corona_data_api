#!/usr/bin/python
# -*- coding: utf-8 -*-
import os 

config = {
    'neo4j': {
        'address': os.getenv('NEO4J_ADDRESS'), 
        'user': os.getenv('NEO4J_USER'),
        'password': os.getenv('NEO4J_PASSWORD')
    }
}