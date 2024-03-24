#!/usr/bin/python3
"""
cript that lists all states from the database hbtn_0e_0_us
"""

import MySQLdb
from sys import sys

if __name__ == "__main__":
    datab = MySQLdb.connect(
         datab = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    )
    c = datab.cursor()
    c.execute("SELECT * FROM states ORDER BY states.id")
    [print(state) for state in c.fetchall()]