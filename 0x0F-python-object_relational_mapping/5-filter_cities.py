#!/usr/bin/python3
"""
a script that takes in the name of a state as
an argument and lists all cities of that state,
using the database hbtn_0e_4_usa
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
        "SELECT cities.name, states.name  FROM cities \
        JOIN states ON cities.state_id = states.id \
        WHERE states.name LIKE %s \
        ORDER BY cities.id ASC", (state_name,))

    rows = cursor.fetchall()
    print(", ".join(row[1] for row in query_rows))
    cursor.close()
    con.close()