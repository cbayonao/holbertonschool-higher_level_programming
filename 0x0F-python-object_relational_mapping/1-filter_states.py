#!/usr/bin/python3
"""
Script that lists all states with a name starting with N
(upper N) from the database hbtn_0e_0_usa.
"""
if __name__ == '__main__':
    try:
        import MySQLdb
        import sys
        db = MySQLdb.connect(host='localhost', port=3306,
                             user=sys.argv[1], passwd=sys.argv[2],
                             db=sys.argv[3])
        cur = db.cursor()
        cur.execute("""SELECT * FROM states WHERE name
                LIKE BINARY 'N%' ORDER BY states.id ASC""")
        m = cur.fetchall()
        for state in m:
            print(state)
    except:
        print("Can't connect to database")
