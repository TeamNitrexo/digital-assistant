SECRET_KEY = b'_5#y2L"F4Q8z\n\xec]/'


# mongoengine_URI = 'mongodb://nitrexo:mongonitrexopassword@mongodb:27017/?authSource=admin' # production
mongoengine_URI = 'mongodb://localhost:27017/' # development
mongoengine_DB = 'nitrexo'


# pymongo_URI = 'mongodb://nitrexo:mongonitrexopassword@mongodb:27017/' # production
pymongo_URI = 'mongodb://localhost:27017' # development
pymongo_DB = 'nitrexo'
pymongo_MESSAGES_COLLECTION = 'messages'


UPLOAD_FOLDER = '/uploads'
ALLOWED_EXTENSIONS = {'agg', 'bdf', 'con', 'ctl', 'csv', 'gdf', 'ldf', 'nco', 'nsd', 'ovl', 'sdf', 'tdf', 'txt', 'tmd', 'TMD'}


MAIL_SERVER = 'nitrexo.com'
MAIL_PORT = 587
MAIL_USERNAME = 'soham.more@nitrexo.com'
MAIL_PASSWORD = 'Thinkpadt420!'
MAIL_USE_TLS = True
MAIL_USE_SSL = False