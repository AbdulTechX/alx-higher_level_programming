#!/usr/bin/python3
"""
This script lists all cities from the
database `hbtn_0e_0_usa`.
"""

import MySQLdb
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=username, passwd=password,
                         db=database)
    cur = db.cursor()
    query = "SELECT cities.name FROM cities LEFT JOIN states\
            ON cities.state_id = states.id WHERE states.name = %s\
            ORDER BY cities.id"
    cur.execute(query, (state_name, ))
    query_row = cur.fetchall()
    if query_row is not None:
        for row in query_row:
            print(row)

    cur.close()
    db.close()
