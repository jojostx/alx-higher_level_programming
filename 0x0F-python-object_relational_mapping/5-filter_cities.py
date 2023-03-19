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

    cur.execute("SELECT cities.name \
    FROM cities JOIN states ON cities.state_id=states.id \
    WHERE states.name=%s \
    ORDER BY cities.id ASC;", (state_name,))

    states = cur.fetchall()

    print(", ".join([state[0] for state in states]))

    cur.close
    db.close()
