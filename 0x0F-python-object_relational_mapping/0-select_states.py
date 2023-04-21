#!/usr/bin/python3
"""
script that lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

user = sys.argv[1]
pw = sys.argv[2]
db = sys.argv[3]
con = MySQLdb.connect(host="localhost", port=3306, user=user, passwd=pw, db=db)
cursor = connection.cursor()

query = "SELECT * FROM states ORDER BY id ASC"
cursor.execute(query)

results = cursor.fetchall()
for row in results:
    print(row)
cursor.close()
connection.close()
