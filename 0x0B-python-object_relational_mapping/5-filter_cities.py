#!/usr/bin/python3
'''
This script filters cities by argument passed
'''
from sys import argv
import MySQLdb
if __name__ == '__main__':
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    item = argv[4]
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities\
                INNER JOIN states\
                ON cities.state_id = states.id\
                WHERE states.name = %s\
                ORDER BY cities.id ASC;", (item, ))
    cities = cur.fetchall()
    cities_in_state = []
    for i in cities:
        cities_in_state.append(i[0])
    print(", ".join(cities_in_state))
    cur.close()
    db.close()
