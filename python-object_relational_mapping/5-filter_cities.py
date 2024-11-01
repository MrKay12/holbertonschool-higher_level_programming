#!/usr/bin/python3

"""take name of state as argument + list cities of state from hbtn_0e_4_usa"""


import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
        )
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities \
                JOIN states ON cities.state_id = states.id \
                WHERE states.name = %s \
                ORDER BY cities.id ASC", (sys.argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(", ".join([city[0] for city in rows]))
    cur.close()
    db.close()
