#!/usr/bin/python3
"""
This script prints the states listed in the table of select states sql
"""
import MySQLdb
db = MySQLdb.connect(host = local_host, user = root, passwd = root, db = hbtn_0e_0_usa)
cur = db.cursor()
cur.execute("SELECT * FROM states ORDER BY states.id ASC;")
