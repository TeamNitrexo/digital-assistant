SECRET_KEY = b'_5#y2L"F4Q8z\n\xec]/'


# the following are all specified in docker-compose.yml in the root folder
DB_HOSTNAME = 'nitrexodb'
DB_USER = 'root'
DB_PASSWORD = 'NitroZiko83r'
MONGO_SERVICE_NAME = 'mongo'
MONGO_SERVICE_PORT = 27017


UPLOAD_FOLDER = '/uploads'
ALLOWED_EXTENSIONS = {'agg', 'bdf', 'con', 'ctl', 'csv', 'gdf', 'ldf', 'nco', 'nsd', 'ovl', 'sdf', 'tdf', 'txt', 'tmd', 'TMD'}


MAIL_SERVER = 'nitrexo.com'
MAIL_PORT = 587
# MAIL_USERNAME = 'soham.more@nitrexo.com'
# MAIL_PASSWORD = 'Thinkpadt420!'
MAIL_USE_TLS = True
MAIL_USE_SSL = False