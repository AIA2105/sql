# For SQL Commands and methods on Course


from DataAccess.Connection import Connection
from entities.Course import Course

class CourseDB:

    def FetchAll():
        lst=[]
        conn = Connection.getConnection()
        cur = conn.cursor()
        cur.execute('select * from course')
        data = cur.fetchall()
        for course in data:
            lst.append(Course(course[0],course[1],course[2],course[3],course[4]))
        return lst
