from pymongo import MongoClient

#server = MongoClient('149.89.150.100')
server = MongoClient('127.0.0.1')

db = server.RefinedStorage
col = db.students

cur = col.find()

for student in cur:
    total = 0
    ctr = 0
    for course in student['courses']:
        total += course[1]
        ctr += 1

    print "Name: %s"%(student['name'])
    print "ID: %d"%(student['id'])
    print "Average: %d"%(float(total) / float(ctr))
    print
