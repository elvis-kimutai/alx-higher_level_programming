#!/usr/bin/python3
"""
Module that connects a python script
that lists all cities from the database
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":

    # Connects to database
    the_db = MySQLdb.connect(host='localhost',
        user=argv[1],
        password=argv[2],
        db=argv[3],
        port=3306
    )

    the_cursor = the_db.cursor()
    the_cursor.execute(
        """SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states
        ON states.id = cities.state_id
        ORDER BY cities.id"""
    )

    thedata = the_cursor.fetchall()

    for rows in thedata:
        print(rows)

    # Close all process
    the_cursor.close()
    the_db.close()
