#!/usr/bin/python3
'''
This script filters from the states database table
'''
from sys import argv
import MySQLdb
if __name__ == '__main__':
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states\
                WHERE name LIKE BINARY 'N%' \
                ORDER BY states.id ASC;")
    states = cur.fetchall()
    for i in states:
        print(i)
    cur.close()
    db.close()
