#!/usr/bin/python3
"""
script that lists all cities from the database hbtn_0e_4_usa
"""
from sys import argv
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.Connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         charset="utf8")
    cur = db.cursor()
    cur.execute('''
                SELECT cities.id, cities.name, states.name FROM cities
                JOIN states ON cities.state_id = states.id ORDER BY id ASC
                ''')
    rows = cur.fetchall()
    for rows in rows:
        print(rows)
    cur.close()
    db.close()
