#!/usr/bin/python3
"""
a script that lists all cities from the database hbtn_0e_4_usa
"""
if __name__ == '__main__':
    import MySQLdb
    import sys

    user = sys.argv[1]
    pw = sys.argv[2]
    db = sys.argv[3]
    con = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        password=pw,
        database=db)
    cursor = con.cursor()

    cursor.execute(
        "SELECT * FROM cities \
        ORDER BY id ASC")

    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    con.close()
