import pymongo
import os

M_HOST = os.environ.get('MONGO_HOST', 'localhost')
client = pymongo.MongoClient(f'mongodb://root:example@{M_HOST}:27017/')
database = client['crm_db']
contacts_collection = database['contacts']
