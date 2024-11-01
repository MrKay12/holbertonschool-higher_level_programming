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
    query = """
    SELECT states.name, cities.id, cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC;
    """
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(f"{row[0]}: ({row[1]}) {row[2]}")
    cur.close()
    db.close()
