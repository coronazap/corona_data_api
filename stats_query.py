from neo4j import GraphDatabase, basic_auth
import json
driver = GraphDatabase.driver( "bolt://192.168.0.30:7687",  auth=basic_auth("neo4j", "nindoo123"))
sess = driver.session()

def name_query(name):
    properties = sess.run(""" 
            MATCH (n:Country {name:{value}}) 
            RETURN properties(n)
            """,{"value": name})
    properties_dict = [row for row in properties][0]
    properties_json = json.dumps(properties_dict)

    return properties_json

result = name_query('Brazil')
print(result)