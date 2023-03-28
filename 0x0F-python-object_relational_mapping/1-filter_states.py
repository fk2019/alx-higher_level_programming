#!/usr/bin/python3
"""Get all states starting with N: Use BINARY to enable case
   sensitivity
"""


if __name__ == "__main__":
    import MySQLdb
    import sys
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                           passwd=password, db=database, charset="utf8")
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM states WHERE BINARY states.name LIKE 'N%' \
        ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()