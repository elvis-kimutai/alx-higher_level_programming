#!/usr/bin/python3
""" module that lists all states starting with N from the database """
import MySQLdb
from sys import argv

if __name__ == '__main__':

    # connects to the database
    the_db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                             passwd=argv[2], db=argv[3])

    the_cursor = the_db.cursor()
    the_cursor.execute("SELECT * FROM states WHERE name\
                       LIKE BINARY 'N%' ORDER BY id ASC")

    thedata = the_cursor.fetchall()
    for rows in thedata:
        print(rows)
    # Closes up process
    the_cursor.close()
    the_db.close()
