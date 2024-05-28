'''
Alexis Ayuso 
410921355
Introduction to Big Data Analytics
HW2: To practice one NoSQL database: MongoDB.
'''

from pymongo import MongoClient

# create to the mongoclient and get the MongoDB database connection (link to a cluster)
# if the database could not be found, then catch the exception
try:
    client = MongoClient("mongodb+srv://410921355:HAavyYIteYJEAKt0@big-data.qit6xeo.mongodb.net/?retryWrites=true&w=majority")
    print("\n~~~ Successfully connected to cluster in MongoDB! ~~~")
except Exception:
    print("\n~~~ Error:" + Exception)

# retrieve database called "HW2"
db = client.HW2



# ----------- FUNCTIONS ------------

# FUNCTION: prints all the documents in a collection
def print_collection(collection, search=""): 
    for document in collection.find(search, {"_id": 0}): print(document)


# FUNCTION: prints the "Students", "Courses", and "Grades" collections
def print_all_collections():
    print("\nDocuments in 'Students':"); print_collection(students_collection)
    print("\nDocuments in 'Courses':"); print_collection(courses_collection)
    print("\nDocuments in 'Grades':"); print_collection(grades_collection)


# FUNCTIONS: create and insert documents into "Students", "Courses" and "Grades" collection
def create_and_insert_documents():
    #create documents
    student_info = [
        { "student_id": "s2", "student_name": "Rick" },
        { "student_id": "s3", "student_name": "Susanna" },
        { "student_id": "s4", "student_name": "Jennifer" }
    ]
    course_info = [
        { "course_id": "c2", "course_name": "Home fusion made easy" },
        { "course_id": "c3", "course_name": "How to train an attack iguana" },
        { "course_id": "c4", "course_name": "Learn SQL for fun and profit" }
    ]
    grades_info = [
        { "student_id" : "s2", "course_id" : "c1", "grade" : "99" },
        { "student_id" : "s3", "course_id" : "c1", "grade" : "65" },
        { "student_id" : "s4", "course_id" : "c1", "grade" : "3" },
        { "student_id" : "s2", "course_id" : "c2", "grade" : "38" },
        { "student_id" : "s3", "course_id" : "c2", "grade" : "88" },
        { "student_id" : "s4", "course_id" : "c2", "grade" : "48" },
        { "student_id" : "s1", "course_id" : "c3", "grade" : "7" },
        { "student_id" : "s4", "course_id" : "c3", "grade" : "32" },
        { "student_id" : "s1", "course_id" : "c4", "grade" : "94" },
        { "student_id" : "s2", "course_id" : "c4", "grade" : "63" },
        { "student_id" : "s3", "course_id" : "c4", "grade" : "75" },
        { "student_id" : "s4", "course_id" : "c4", "grade" : "20" }
    ]
    
    # insert documents 
    try:
        students_collection.insert_many(student_info)
        courses_collection.insert_many(course_info)
        grades_collection.insert_many(grades_info)
        print("\n~~~ Documents were successfully inserted into the collections ~~~")
    except Exception:
        print("\n~~~ Error:" + Exception)

# FUNCTION: to query students who took the course named ”Home fusion made easy”
def query_course():
    # find the course_id for 'Home fusion made easy' in the 'Courses' collection
    # find the student_id of students who took the course in the 'Grades' collection
    # find the corresponding student_name of the student_id in 'Students' collection and then print
    courseID = courses_collection.find_one({'course_name' : 'Home fusion made easy'}, {'_id': 0, 'course_id': 1})

    print("\n~ Students in the course \'Home fusion made easy\':")
    for grades in grades_collection.find(courseID, {"_id": 0, 'student_id': 1}):
        for students in students_collection.find(grades,  {'_id': 0, 'student_name':1}):
            print('\t' + students['student_name'])

# FUNCTION: to query Jennifer’s grade on the course named "Learn SQL for fun and profit"
def jennifers_grade():
    # find Jennifer's student_id find the course_id of the course named "Learn SQL for fun and profit"
    # find the grade using the course_id and student_id
    theStudentID = (students_collection.find_one({'student_name': 'Jennifer'},  {'_id': 0, 'student_id':1})) ['student_id']
    theCourseID = (courses_collection.find_one({'course_name': 'Learn SQL for fun and profit'}, {"_id": 0, 'course_id': 1})) ['course_id']
    theGrade = grades_collection.find_one({'student_id': theStudentID, 'course_id': theCourseID}, {"_id": 0, 'grade': 1})
    print("\n~ Jennifer's grade in the course \'Learn SQL for fun and profit\':\n\t" + theGrade['grade'] + "\n")


# FUNCTION: deletes documents from collections
def delete_documents():
    students_collection.delete_many({})
    courses_collection.delete_many({})
    grades_collection.delete_many({})

# FUNCTION: inserts the first document of each collection
def insert_first_documents():
    students_collection.insert_one({ "student_id": "s1", "student_name": "Brett" })
    courses_collection.insert_one({ "course_id": "c1", "course_name": "Underwater basket weaving" })
    grades_collection.insert_one({ "student_id" : "s1", "course_id" : "c1", "grade" : "2" })

# FUNCTION: reset the database to have only one document in each collection
def reset_db():
    delete_documents()
    insert_first_documents()


# FUNCTION: to store the extra tasks that I decided to leave in my submitted homework because I can
def create_index():
    # create unique indeces for the collections 
    students_collection.create_index('student_id')
    courses_collection.create_index('course_id')
    grades_collection.create_index([('student_id', 1), ('course_id', 1)], name='student_course')  # compound index

    print("\nThe index information for Students, Courses, and Grades collection:")
    print(students_collection.index_information(), courses_collection.index_information(), grades_collection.index_information())

# ------ END OF FUNCTIONS SECTION ------


# retrieve collections "Students", "Courses" and "Grades" from database
students_collection = db.Students
courses_collection = db.Courses
grades_collection = db.Grades

# print the names of all collections in the "HW2" database 
print("\nThe collections in the database:")
print(db.list_collection_names())

# print all collections before inserting documents
print_all_collections()

# –– to insert other documents *****
create_and_insert_documents()

# –– to print all the data in your MongoDB (including the document created by the Atlas UI) *****
print("\n~ All the data in your MongoDB (including the document created by the Atlas UI):")
print_all_collections()

# –– to query students who took the course named ”Home fusion made easy” *****
query_course()
# –– to query Jennifer’s grade on the course named "Learn SQL for fun and profit" *****
jennifers_grade() 




# call function to reset database
reset_db()