#!/usr/bin/python3
"""
lists all states from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    connection = MySQLdb.Connect(host="localhost",
                                 port=3306,
                                 user=username,
                                 passwd=password,
                                 db=dbname,
                                 charset="utf8")
    cursor_exe = connection.cursor()
    cursor_exe.execute("SELECT * FROM states ORDER BY id ASC")
    qRows = cursor_exe.fetchall()
    for rows in qRows:
        print(rows)
    cursor_exe.close()
    connection.close()
