#!/usr/bin/python3
"""
 script that lists all states with aname starting with N
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3]
    )
    c = db.cursor()
    c.execute("SELECT * FROM states ORDER BY states.id")
    [print(state) for state in c.fetchall() if state[1].startswith("N")]
