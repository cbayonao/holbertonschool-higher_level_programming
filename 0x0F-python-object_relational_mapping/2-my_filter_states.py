#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in
the states table of hbtn_0e_0_usa where name matches the argument.
"""
if __name__ == '__main__':
    try:
        import MySQLdb
        import sys
        db = MySQLdb.connect(host='localhost', port=3306,
                             user=sys.argv[1], passwd=sys.argv[2],
                             db=sys.argv[3])
        cur = db.cursor()
        cur.execute("""SELECT * FROM states WHERE name LIKE BINARY '{}'
                ORDER BY states.id ASC""".format(sys.argv[4]))
        m = cur.fetchall()
        for state in m:
            print(state)
    except:
        print("Can't connect to database")
