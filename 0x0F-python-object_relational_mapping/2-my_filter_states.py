#!/usr/bin/python3
"""
module that takes in an argument and displays all
states that matches the argument
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':

    # connects to the database
    the_db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                             passwd=argv[2], db=argv[3])

    the_cursor = the_db.cursor()
    dbs = "SELECT * FROM states WHERE name LIKE BINARY '{}'".format(argv[4])
    the_cursor.execute(dbs)

    thedata = the_cursor.fetchall()
    for rows in thedata:
        print(rows)
    # Closes up process
    the_cursor.close()
    the_db.close()
