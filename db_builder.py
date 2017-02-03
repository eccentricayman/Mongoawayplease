from pymongo import MongoClient

server = MongoClient('127.0.0.1')
#database = MongoClient('149.89.160.100')
db = server.firstDB
col = db.students

f1 = open("courses.csv", "r")
firstLine = f1.readline()

