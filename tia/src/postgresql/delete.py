# Delete
# ---------
# This module will contain objects for deleting data, rows, tables even db's
# This module will be improved in the future


# DROP TABLE
def drop_table(cursor):
    '''
        Function name: drop_table()
        Desc: ...
    '''
    name = input("Table name: ")
    verification = input("Are you sure ? (y or n) ")
    if (verification == "y"):
        query = "DROP TABLE IF EXISTS " + str(name)
    # Execute the SQL query
    cursor.execute(query)


# DELETE ROW
# --------------
# This function deletes a specific row from the table
def delete_row(cursor):
    '''
        Function name: delete_row()
        Desc: ...
    '''
    name = input("Table name: ")
    id = input('Row id: ')
    query = "DELETE FROM " + str(name) + " WHERE id = " + id + ";"

    cursor.execute(query)
