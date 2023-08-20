#!/usr/bin/python3

"""
script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
import sys

username = sys.argv[1]
password = sys.argv[2]
database_name = sys.argv[3]
state_name = sys.argv[4]

connection = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database_name,
        port=3306
)

c = connection.cursos()

query = "SELECT * FROM states WHERE name = %s ORDER BY state.id ASC"

c.execute(query, (state_name,))

results = c.fetchall()

for state in results:
    print(state)

c.close()
connection.close()

if __name__ == "__main__":
    main()
