#!/usr/bin/python3
"""
script that takes in an argument and displays
all values in the states table of hbtn_0e_0_usa
where name matches the argument.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=username, passwd=password,
                         db=database,)
    cur = db.cursor()
    cur.execute("SELECT * FROM `states` WHERE `name` LIKE BINARY\
                '{}' ORDER BY `id` ASC".format(state_name))

    query_row = cur.fetchall()

    for row in query_row:
        print(row)

    cur.close()
    db.close()
