#!/usr/bin/python3
"""List cities by state
"""


if __name__ == "__main__":
    import MySQLdb
    import sys
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    user_input = sys.argv[4]
    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                           passwd=password, db=database, charset="utf8")
    cur = conn.cursor()
    qry = """
    SELECT cities.name
    FROM cities INNER JOIN states
    ON cities.state_id = states.id
    WHERE BINARY states.name = %s
    ORDER BY cities.id ASC
    """
    cur.execute(qry, [user_input])
    query_rows = cur.fetchall()
    print(*[city for row in query_rows for city in row], sep=", ")
    cur.close()
    conn.close()
