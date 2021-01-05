# Read
# --------
# This module will contain the reading of the data from the database such as
# the select queries ...etc. and it will also have few helpful functions for
# command line handy-helpful documentation


# LISTING TABLES
# --------------
# You can view all of the tables inside a database with this function
def list_tables(cursor):
    '''
        Function name: list_tables()
        Desc: ...
    '''
    cursor.execute("SELECT table_name FROM information_schema.tables\
                    WHERE table_schema = 'public' ")
    tables = cursor.fetchall()

    for table in tables:
        print(table)


# LISTING ROWS
# --------------
# You can view all of the rows inside a table with this function
def list_rows(cursor):
    '''
        Function name: list_rows()
        Desc: ...
    '''
    name = input("Table name: ")
    cursor.execute("SELECT * FROM " + str(name))
    rows = cursor.fetchall()

    for row in rows:
        print(row)


# LIMITING ROWS
# --------------
# You can limit the amount of rows to be displayed on the screen with this fnc
def limit_rows(cursor):
    '''
        Function : limit_rows(cursor) {...}
        Desc: This function requires a cursor paramter which is a
              db.connection.cursor. and returns you the limited rows of a table
    '''
    table_name = input("Table name: ")
    limit = input("How many rows you want: ")

    query = "SELECT * FROM " + str(table_name) + " LIMIT " + str(limit) + ";"

    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        print(row)


# LIMITING BETWEEN
# ----------------
# You can limit the amount of rows while starting from a targeted starting poin
# -t of a row
def limit_between(cursor):
    '''
        Function: limit_between(cursor) {...}
        Desc: This function requires a db.connection.cursor parameter. It will
              print out the selected rows of a table to the terminal
    '''
    table_name = input("Table name: ")
    starting_row = input("Starting from which row: ")
    limit = input("How many rows you want: ")

    query = (
        "SELECT * FROM " + str(table_name) + " LIMIT " + str(limit) +
        " OFFSET " + starting_row + ";"
    )

    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        print(row)


# ORDER BY
# -----------
# This function just orders the rows with the desired column in a acsending or
# a descending order
def order_by(cursor):
    '''
        Function: order_by(cursor) {...}
        Desc: This function requires a db.connection.cursor parameter. It will
              print out the table in a acsending or decesnding order
    '''
    table_name = input("Table name: ")
    column_name = input("Order by (col name): ")
    ordering_way = input("Ordering way (desc or asc): ")

    query = (
        "SELECT * FROM " + str(table_name) + " ORDER BY " + str(column_name) +
        " " + str(ordering_way.upper()) + ";"
    )

    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        print(row)
