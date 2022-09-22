import pymongo
import os
from functools import lru_cache

MONGO_CONNECTION_STRING = "mongodb://dbadmin:H8EU%253ZSerj%2ARmuW@10.161.24.213:27017,10.161.24.214:27017,10.161.24.216:27017/grpc_sample_service?authSource=admin&replicaSet=covidrep"
GRPC_PORT = 8080

@lru_cache
def get_db():
    client = pymongo.MongoClient(MONGO_CONNECTION_STRING)
    return client.get_default_database()

