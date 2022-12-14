#!/usr/bin/python3
'''This Module returns the states listed in the database.'''


if __name__ == '__main__':
    '''
    Return rows from cities with state attached.
    Filtered by state on user input
    '''

    from sys import argv
    import MySQLdb

    db_username = argv[1]
    db_password = argv[2]
    db_name = argv[3]
    user_input = argv[4]
    user_input = user_input.split(';')
    user_input = user_input[0].replace("\'", "")

    db = MySQLdb.connect(
        host='localhost',
        user=db_username,
        passwd=db_password,
        db=db_name)

    cur = db.cursor()
    SQL = "SELECT cities.name FROM cities"
    WHERE = f"WHERE states.name = '{user_input}'"
    JOIN = "INNER JOIN states ON cities.state_id = states.id"
    SQL_STATEMENT = f'{SQL} {JOIN} {WHERE}'
    cur.execute(SQL_STATEMENT)
    rows = cur.fetchall()
    result_list = []
    for row in rows:
        for col in row:
            result_list.append(col)

    print(', '.join(result_list))
