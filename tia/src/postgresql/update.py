# Update
# ----------
# This module contains the objects that update the databases, alter its rows,
# ids, and such ... this module will be improved in the future


# UPDATE ALL ROWS
# -----------------
# Desc: Updates all the data inside a table
def update_all_rows(cursor):
    '''
        Function: update_all_rows(cursor) {...}
        Desc: This program requires a parameter which is a dbconnection.cursor
              The functions updates all of the data inside a table
    '''
    table_name = input("Table name: ")
    column_name = input("Column name: ")
    new_value = input("New value: ")

    query = (
        "UPDATE " + str(table_name) + " SET " + str(column_name) + " = "
        + str(new_value) + ";"
    )

    cursor.execute(query)


# UPDATE SINGLE ROW
# ------------------
# Desc: Updates a single rows speficic data of a column
def update_single_row(cursor):
    '''
        Function: update_single_row(cursor) {...}
        Desc: This program  requires a parmeter which is a dbconnection.cursor
              The function updates a single data in a row of a specific column
    '''
    table_name = input("Table name: ")
    row_id = input("Row id: ")
    column_name = input("column name: ")
    new_value = input("New value: ")

    query = (
        "UPDATE " + str(table_name) + " SET " + str(column_name) + " = " +
        str(new_value) + " WHERE id = " + str(row_id) + ";"
    )

    cursor.execute(query)
