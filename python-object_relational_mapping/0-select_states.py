#!/usr/bin/python3
"""
cript that lists all states from the database hbtn_0e_0_us
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3]
    )
    c = db.cursor()
    c.execute("SELECT * FROM states ORDER BY states.id")
    [print(state) for state in c.fetchall()]
