from pymongo import MongoClient

#server = MongoClient('149.89.150.100')
server = MongoClient('127.0.0.1')

db = server.RefinedStorage
col = db.students

cur = col.find()

for i in cur:
    
