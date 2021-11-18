#!/usr/bin/python3
'''
This script filters by argument passed
'''
from sys import argv
import MySQLdb
if __name__ == '__main__':
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    item = argv[4]
    cur = db.cursor()
    cur.execute("SELECT * FROM states\
                WHERE name = %s \
                ORDER BY states.id ASC;", (item, ))
    states = cur.fetchall()
    for i in states:
        print(i)
    cur.close()
    db.close()
