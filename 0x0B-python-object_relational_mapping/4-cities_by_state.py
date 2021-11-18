#!/usr/bin/python3
'''
This script lists all cities from the database
'''
from sys import argv
import MySQLdb
if __name__ == '__main__':
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name\
                FROM cities INNER JOIN states\
                ON states.id = cities.state_id\
                ORDER BY cities.id ASC;")
    cities = cur.fetchall()
    for i in cities:
        print(i)
    cur.close()
    db.close()
