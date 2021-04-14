# For SQL Commands and methods on Student

from DataAccess import Connection as C
from entities import student as S


class StudentDB:

    def FetchAll():
        lst = []
        conn = C.Connection.getConnection()
        cur = conn.cursor()
        cur.execute('select * from student')
        data = cur.fetchall()

        for student in data:
            lst.append(S.Student(student[0],student[1],student[2],student[3]))

        return lst

    def FetchExcellent():
        lst = []
        conn = C.Connection.getConnection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM `student` WHERE grade=\'Excellent\'')
        data = cur.fetchall()

        for student in data:
            lst.append(S.Student(student[0],student[1],student[2],student[3]))

        return lst
