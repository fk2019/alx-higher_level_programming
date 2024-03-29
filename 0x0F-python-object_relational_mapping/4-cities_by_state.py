#!/usr/bin/python3
"""List cities by states
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
    qry = """
    SELECT cities.id, cities.name, states.name
    FROM cities INNER JOIN states
    ON cities.state_id = states.id
    ORDER BY cities.id ASC
    """
    cur.execute(qry)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
