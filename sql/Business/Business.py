from DataAccess import studentDB as S


class Business:

    def StudentID(id):
        print('-----------------------------------------')
        if int(id)-1<len(S.StudentDB.FetchAll()):
            student = S.StudentDB.FetchAll()
            print('Student id: ', student[int(id)-1].id)
            print('Student name: ', student[int(id)-1].name)
            print('Student grade: ', student[int(id)-1].grade)
            print('Student phone: ', student[int(id)-1].phone)
        else:
            print('Error in ID')
        print('-----------------------------------------')

    def StudentExcellent():
        print('-----------------------------------------')
        student = S.StudentDB.FetchExcellent()
        for stu in student:
            print('Student id: ', stu.id)
            print('Student name: ', stu.name)
            print('Student grade: ', stu.grade)
            print('Student phone: ', stu.phone)
            print('-----------------------------------------')
