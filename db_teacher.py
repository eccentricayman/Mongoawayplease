from pymongo import MongoClient

server = MongoClient('127.0.0.1')
db = server.RefinedStorage

col = db.teachers

f = open("teachers.csv", "r")
paramHeaders = f.readline().strip().split(",")

restOfFile = f.readlines()

for line in restOfFile:
    lineList = line.strip().split(",")
    teacherDoc = { }
    for index in range(len(paramHeaders)):
        teacherDoc[ paramHeaders[index] ] = lineList[index] 

    students = []
    for student in db.students.find():
        for course in student['courses']:
            #print( "Student Course:"+str(course)+", Teacher's Code:"+teacherDoc['code'] )
            if course[0] == teacherDoc['code']:
                students.append( student['_id'])


    teacherDoc['students'] = students
    col.insert_one( teacherDoc )
