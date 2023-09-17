#!/usr/bin/python3
"""
module that takes in an argument and displys value
that matches the argumentbut safe from MySQL injections!
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':

    # connects to the database
    the_db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                             passwd=argv[2], db=argv[3])

    the_cursor = the_db.cursor()
    the_cursor.execute(
            "SELECT * FROM states WHERE BINARY name = %s", [argv[4]])

    thedata = the_cursor.fetchall()
    for rows in thedata:
        print(rows)
    # Close up process
    the_cursor.close()
    the_db.close()
