# For Establish Connection

import mysql.connector as connection


class Connection:

    @staticmethod
    def getConnection():
        if connection.connect(host='localhost', user='root', passwd='', database='project'):
            return connection.connect(host='localhost', user='root',passwd='', database='project')
