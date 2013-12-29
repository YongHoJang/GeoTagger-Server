from schemas import domain
from pymongo import MongoClient


SERVER_NAME = '127.0.0.1:5000'


# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
# individual items  (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

# MONGO CONFIG
MONGO_HOST = 'localhost'
MONGO_PORT = 27017
#MONGO_USERNAME = 'admin'
#MONGO_USERNAME = '@dmin!'
MONGO_DBNAME = 'api4k'

# Data Models
DOMAIN = domain







