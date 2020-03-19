import json
import os
from neo4j import GraphDatabase, basic_auth

driver = GraphDatabase.driver( "bolt://192.168.0.30:7687",  auth=basic_auth("neo4j", "nindoo123"))
sess = driver.session()
def create_context_db(context_dict):
    for element in context_dict:
        print()
        print('title',context_dict[element][0]['title'])
        print('paragraphs',context_dict[element][0]['paragraphs'][0])
        sess.run("""
            MERGE (a:Category)
            SET a.title = {title}
            SET a.paragraphs = {paragraphs}

            """,{"title": context_dict[element][0]['title'], 'paragraphs':context_dict[element][0]['paragraphs']})

    
context_dir = '/Users/jpmc/Nindoo/nindoo-whatsapp-bot/raw/contexts'

for filename in os.listdir(context_dir):
    with open(os.path.join(context_dir, filename)) as context_file:
        context_dict = json.load(context_file)
        create_context_db(context_dict)
        #print(context_dict)
sess.close()        
print("--- Dataset de Contexto Criado ---")

        