import pymongo

client = pymongo.MongoClient('mongodb://root:example@localhost:27017/')
database = client['crm_db']
contacts_collection = database['contacts']
