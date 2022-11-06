#!/usr/bin/python3
'''This Module returns the states listed in the database'''


if '__name__' == '__main__':
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
    sql_statement = "SELECT * FROM states ORDER BY id ASC"
    results = cur.execute(sql_statement)
