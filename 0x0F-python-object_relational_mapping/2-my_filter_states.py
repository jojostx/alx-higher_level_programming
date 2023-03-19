#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb

if __name__ == '__main__':
    argv = sys.argv[1:]

    user = argv[0]
    passwd = argv[1]
    db_name = argv[2]
    state_name = argv[3]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=user, passwd=passwd, db=db_name)

    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name='{}' ORDER BY id ASC"
                .format(state_name))

    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close
    db.close()
