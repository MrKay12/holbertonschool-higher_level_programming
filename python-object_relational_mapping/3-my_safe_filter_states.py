#!/usr/bin/python3

"""list states with spe name from hbtn_0e_0_usa"""


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
    cur.execute("SELECT * FROM states WHERE name = %s \
                ORDER BY id ASC", (sys.argv[4],))
    rows = cur.fetchall()
    for row in rows:
        if row[1] == sys.argv[4]:
            print(row)
    cur.close()
    db.close()
