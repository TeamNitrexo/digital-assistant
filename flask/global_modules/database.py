from mongoengine import connect
from .config import DB_HOSTNAME, DB_USER, DB_PASSWORD, MONGO_SERVICE_NAME, MONGO_SERVICE_PORT
from pymongo import MongoClient

DB_NAME = 'nitrexo'
COLLECTION_1_NAME = 'messages' # chatbot responses (OLD IMPLEMENTATION)
COLLECTION_2_NAME = 'knowledge' # chatbot answers to thermal-related questions; Q&A are in 'tmr/data/Knowledge Base.csv' (NEW IMPLEMENTATION)

mongo_client = MongoClient(
    host=DB_HOSTNAME,
    port=MONGO_SERVICE_PORT,
    username=DB_USER,
    password=DB_PASSWORD,
    authSource="admin"
)
db = mongo_client[DB_NAME]
col_messages = db[COLLECTION_1_NAME]
col_knowledge = db[COLLECTION_2_NAME]

connect(host=f"mongodb://{DB_USER}:{DB_PASSWORD}@{MONGO_SERVICE_NAME}:{MONGO_SERVICE_PORT}/{DB_NAME}?authSource=admin")