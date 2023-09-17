#!/usr/bin/python3
"""A script that takes in the name of a state as an arg
and lsits all cities.
"""
import MySQLdb
import sys

if __name__ == "__main__":

    state = sys.argv[4]
    the_db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
        )
    the_cursor = the_db.cursor()
    the_cursor.execute("SELECT cities.name FROM cities INNER JOIN\
            states ON state_id = states.id WHERE states.name\
              = %s", (state, ))
    thedata = the_cursor.fetchall()
    cities = ', '.join(city[0] for city in thedata)

    print(cities)
    the_cursor.close()
    the_db.close()
