from pymongo import MongoClient

server = MongoClient('127.0.0.1')
#server = MongoClient('149.89.160.100')
db = server.firstDB
col = db.students

f1 = open("peeps.csv", "r")
firstLine = f1.readline()

paramNames = firstLine.strip().split(",")

f2 = open("courses.csv", "r")
firstLineF2 = f2.readline()

paramNamesF2 = firstLineF2.strip().split(",")

index2 = paramNamesF2.index('id') # For use Later. Initialized here to increase efficiency
index1 = paramNames.index('id') # For use Later.

courseIndex = paramNamesF2.index('code')
markIndex = paramNamesF2.index('mark')

f2Lines = f2.readlines() #For use later

for line in f1.readlines():
    lineList = line.strip().split(",")
    studentDoc = { }
    #length of paramNames should match length of lineList. If not, then something is wrong
    for i in range( len(paramNames) ):
        try:
            lineList[i] = int(lineList[i])
        except ValueError:
            # not an int.
            # do nothing?
            lineList[i] = lineList[i]
        studentDoc[paramNames[i]] = lineList[i]

    studentDoc['courses'] = []

    for line2 in f2Lines:
        lineList2 = line2.strip().split(',')
        #print "comparing ids : [%d] with [%d]"%( int(lineList[index1]), int(lineList2[index2] ))
        if int(lineList[index1]) == int(lineList2[index2]): #If IDs match
            studentDoc['courses'].append( [ lineList2[courseIndex], int(lineList2[markIndex]) ] )
            
    col.insert(studentDoc);
        


## StudentDoc:
''' 
{
   id : 0,
   age : 0,

}
'''
