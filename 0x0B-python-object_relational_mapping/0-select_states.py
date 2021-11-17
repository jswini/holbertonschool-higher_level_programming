#!/usr/bin/python3
"""
This script prints the states listed in the table of select states sql
"""
from sys import argv
import MySQLdb
db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
cur = db.cursor()
cur.execute("SELECT * FROM states ORDER BY states.id ASC;")
states = cur.fetchall()
for i in states:
    print(i)
cur.close()
db.close()
