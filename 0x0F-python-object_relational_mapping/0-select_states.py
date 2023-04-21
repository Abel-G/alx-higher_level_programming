#!/usr/bin/python3

if __name__ == "__main__":
    import MySQLdb
    db = MySQLdb.connect(user=argv[1], password=argv[2], database = argv[3], host ="localhost", port=3306)
    cur = db.cursor()
    cur.execute(SELECT * FROM states ORDER BY states.id ASC)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
