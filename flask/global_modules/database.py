from mongoengine import connect
from .config import DB_HOSTNAME, DB_USER, DB_PASSWORD, MONGO_SERVICE_NAME, MONGO_SERVICE_PORT
from pymongo import MongoClient

"""
NOTE:
#1
You can find the chatbot's answers to thermal-related questions in 'tmr/data/Knowledge Base.csv'

#2
The 'messages' collection stores the responses for the chatbot (this is being changed because it's too messy).

The newer implementation uses JavaScripts's `XMLHttpRequest` to make requests to the backend routes. This sometimes involves passing JSON back and forth or just to one.

Please look at the JS files in 'static/js/chatbot' for examples on how to do this.

"""

DB_NAME = 'nitrexo'
COLLECTION_1_NAME = 'messages'

mongo_client = MongoClient(
    host=DB_HOSTNAME,
    port=MONGO_SERVICE_PORT,
    username=DB_USER,
    password=DB_PASSWORD,
    authSource="admin"
)
db = mongo_client[DB_NAME]
col_messages = db[COLLECTION_1_NAME]

connect(host=f"mongodb://{DB_USER}:{DB_PASSWORD}@{MONGO_SERVICE_NAME}:{MONGO_SERVICE_PORT}/{DB_NAME}?authSource=admin")