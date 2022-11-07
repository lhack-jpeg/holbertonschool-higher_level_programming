#!/usr/bin/python3
'''This Module returns the states listed in the database.'''


if __name__ == '__main__':
    '''
    Return rows from cities with state attached.
    '''

    from sys import argv
    import MySQLdb

    db_username = argv[1]
    db_password = argv[2]
    db_name = argv[3]

    db = MySQLdb.connect(
        host='localhost',
        user=db_username,
        passwd=db_password,
        db=db_name)

    cur = db.cursor()
    SQL = "SELECT cities.id, cities.name, states.name FROM cities"
    JOIN = "INNER JOIN states ON cities.state_id = states.id"
    SQL_JOIN = f'{SQL} {JOIN}'
    cur.execute(SQL_JOIN)
    rows = cur.fetchall()
    for row in rows:
        print(row)
