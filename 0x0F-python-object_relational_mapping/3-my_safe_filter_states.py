#!/usr/bin/python3
"""
matches the argument. But this time,
write one that is safe from MySQL injections!
"""
import sys
import MySQLdb

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    stateNameSearched = sys.argv[4]
    connection = MySQLdb.Connect(host="localhost",
                                 port=3306,
                                 user=username,
                                 passwd=password,
                                 db=dbname,
                                 charset="utf8")
    cursor_exe = connection.cursor()
    cursor_exe.execute('''
                        SELECT * FROM states
                        WHERE name = %s ORDER BY id ASC
                       ''', (stateNameSearched,))
    qRows = cursor_exe.fetchall()
    for rows in qRows:
        print(rows)
    cursor_exe.close()
    connection.close()
