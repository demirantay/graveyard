# Create
# ------------
# This module will contain objects for creating, populating inserting data to
# the database e.g. creating tables, populating tables, inserting single rows
# and much more this module will be improved in the future

import random


# CREATE TABLE
# --------------
# This functions creates a table for the user
def create_table(cursor):
    '''
        Function name: create_table()
        Desc: ...
    '''
    name = input("Table name: ")
    columns = int(input("How many columns: "))

    # Drop the table if it exists in the database
    cursor.execute("DROP TABLE IF EXISTS " + name)

    query = "CREATE TABLE " + str(name) + \
            "(id SERIAL PRIMARY KEY"
    i = 0
    while (i < columns):
        col_name = input("Column " + str(i + 1) + " name: ")
        col_type = input(
            "Column " + str(i + 1) + " type (text or int or float): "
        )
        query += ", " + str(col_name) + " " + str(col_type).upper()
        i += 1
    query += "); "
    # Execute the SQL query
    cursor.execute(query)


# INSERT ROW
# -------------
def insert_row(cursor):
    '''
        Function name: insert_row(param)
        desc: ...
    '''
    name = input("Table name: ")
    cursor.execute("SELECT column_name FROM information_schema.columns\
                    WHERE table_name = \'" + str(name) + "'")
    columns = cursor.fetchall()

    query = "INSERT INTO " + str(name) + "("
    values = ""
    i = 1  # `i` starts at 1 because the `0` is a auto incrementing int
    while (i < len(columns)):
        query += str(columns[i][0]) + ", "
        user_data = input(str(columns[i][0] + ": "))
        values += user_data + ", "
        i += 1
    query = query[:-2]
    query += ") VALUES(" + values
    query = query[:-2]
    query += ");"

    # Execute the SQL query
    cursor.execute(query)


# POPULATE DB
# --------------
# If you do not want to write too much insert row queries into the database or
# if you are just lazy like me you can use this function to populate the table
# with rows
def populate_db(cursor):
    '''
        Function: populate_db(cursor) {...}
        Desc: This function requires a db.connection.cursor as a arg. The main
              of this function is to create a dummy table named by the user
              and populates it
    '''
    table_name = input("What do you want to name your table: ")

    # Drop the table if it exists in the database
    cursor.execute("DROP TABLE IF EXISTS " + table_name)

    # Creating the table
    create_table = (
        "CREATE TABLE " + str(table_name) + "( " +
        "id SERIAL PRIMARY KEY, " +
        "Name TEXT, " +
        "Age INT, " +
        "Salary INT" +
        ");"
    )

    cursor.execute(create_table)

    # Populating the database
    dummy_data_names = ["Emily", "Hannah", "Madison", "Ashley", "Sarah",
                        "Samantha", "Jessica", "Elizabeth", "Taylor", "Lauren",
                        "Alyssa", "Kayla", "Victoria", "Rachel", "Jasmine",
                        "Abigail", "Brianna", "Olivia", "Emma", "Megan",
                        "Anna", "Sydney", "Destiny", "Morgan", "Jennifer",
                        "Kaitlyn", "Nicole", "Amanda", "Katherine", "Natalie",
                        "Savannah", "Chloe", "Rebecca", "Stephanie", "Maria",
                        "Allison", "Isabella", "Amber", "Mary", "Danielle",
                        "Brooke", "Michelle", "Sierra", "Katelyn", "Andrea",
                        "Kimberly", "Courtney", "Erin", "Hailey", "Alexandra",
                        "Sophia", "Mackenzie", "Gabrielle", "Jordan"]

    # Populate the data with 30 entries in the future I will add the feature
    # so that the user can select how many entries they want.
    for i in range(0, 50, 1):
        query = (
            "INSERT INTO " + table_name +
            " (Name, Age, Salary) VALUES (" +
            "'" + dummy_data_names[random.randint(0, 54)] + "', "
            + str(random.randint(0, 100)) + ", " +
            str(random.randint(1000, 5000))
            + ");"
        )
        cursor.execute(query)
