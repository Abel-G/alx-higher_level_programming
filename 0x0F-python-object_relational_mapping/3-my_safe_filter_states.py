#!/usr/bin/python3
"""
a script that takes in an argument and
displays all values in the states table
of hbtn_0e_0_usa where name matches the argument
"""
if __name__ == '__main__':
    import MySQLdb
    import sys

    user = sys.argv[1]
    pw = sys.argv[2]
    db = sys.argv[3]
    state_name = sys.argv[4]
    con = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        password=pw,
        database=db)
    cursor = con.cursor()

    cursor.execute(
        "SELECT * FROM states \
 WHERE name LIKE BINARY %s ORDER BY id ASC", (state_name,))

    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    con.close()
