#!/usr/bin/python3
'''This Module returns the states listed in the database.'''


if __name__ == '__main__':
    '''Return row from user input'''

    from sys import argv
    import MySQLdb

    db_username = argv[1]
    db_password = argv[2]
    db_name = argv[3]
    user_input = argv[4]

    db = MySQLdb.connect(
        host='localhost',
        user=db_username,
        passwd=db_password,
        db=db_name)
    cur = db.cursor()
    SQL = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(
        user_input)
    cur.execute(SQL)
    rows = cur.fetchall()
    for row in rows:
        print(row)
