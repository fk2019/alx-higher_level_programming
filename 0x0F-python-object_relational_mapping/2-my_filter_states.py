#!/usr/bin/python3
"""Filter states by input
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
    SELECT * FROM states WHERE BINARY states.name = '{user_input}'
    ORDER BY id ASC
    """
    qry = qry.format(user_input=user_input)
    cur.execute(qry)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
