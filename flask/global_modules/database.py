import mongoengine
from .config import pymongo_MESSAGES_COLLECTION, pymongo_DB, pymongo_URI, mongoengine_DB
from pymongo import MongoClient

mongo_client = MongoClient(pymongo_URI)
db = mongo_client[pymongo_DB]
col_messages = db[pymongo_MESSAGES_COLLECTION]

mongoengine.connect(mongoengine_DB)