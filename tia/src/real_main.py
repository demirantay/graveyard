# Name   : Py-Psql
# Purpose: I was learning postgresql and needed a project to test out what I
#          have learned, the content of the program is insignificant
# Author : Demir Antay (@demirantay)

# Main Imports
import psycopg2
import sqlite3

# Help Docs
from .help_docs.help import help_docs, help_docs_postgres, help_docs_mognodb
from .help_docs.help import help_docs_sqlite, help_docs_redis

# PostgreSQL ORM
from .postgresql.create import create_table, insert_row, populate_db
from .postgresql.read import list_tables, list_rows, limit_rows
from .postgresql.read import limit_between, order_by
from .postgresql.update import update_all_rows, update_single_row
from .postgresql.delete import drop_table, delete_row

# MySQL ORM
from .sqlite.create import sqlite_create_table

# SQLite ORM

# MongoDB ORM

# Redis ORM


################
# MAIN PROGRAM #
################

def postgresql_ORM():
    # Database connection
    dbname = None
    connection = None

    try:
        # Get the database name from the user
        dbname = input("\nDatabase name: ")
        connection = psycopg2.connect(dbname=str(dbname))
        cursor = connection.cursor()

        print("Type 'help' for docs")

        while(True):
            user_input = input("\n$ ")

            if (user_input == "help"):
                help_docs()
            elif (user_input == "help posgres"):
                help_docs_postgres()
            elif (user_input == "create table"):
                create_table(cursor)
            elif (user_input == "drop table"):
                drop_table(cursor)
            elif (user_input == "insert row"):
                insert_row(cursor)
            elif (user_input == "delete row"):
                delete_row(cursor)
            elif (user_input == "list tables"):
                list_tables(cursor)
            elif (user_input == "list rows"):
                list_rows(cursor)
            elif (user_input == "update all rows"):
                update_all_rows(cursor)
            elif (user_input == "update single row"):
                update_single_row(cursor)
            elif (user_input == "limit rows"):
                limit_rows(cursor)
            elif (user_input == "limit between"):
                limit_between(cursor)
            elif (user_input == "order by"):
                order_by(cursor)
            elif (user_input == "populate db"):
                populate_db(cursor)
            elif (user_input == "quit"):
                break
            else:
                print("You have entered invalid characters! Type `help`")

            connection.commit()
    except psycopg2.DatabaseError as e:
        print("Error: " + str(e))

    finally:
        if connection is True:
            connection.close()


def sqlite_ORM():
    """
    handles all of the ORM commands, db connections, exc handling for sqlite3
    """
    # Database connection
    db_name = None
    connection = None

    try:
        db_name = input("\nDatabase name: ")

        connection = sqlite3.connect(str(db_name))
        cursor = connection.cursor()

        print("Type 'help' for docs")

        while(True):
            user_input = input("\n$ ")

            if (user_input == "help"):
                help_docs()
            elif (user_input == "help posgres"):
                help_docs_postgres()
            elif (user_input == "help sqlite"):
                help_docs_sqlite()
            elif (user_input == "help mongo"):
                help_docs_mognodb()
            elif (user_input == "help redis"):
                help_docs_redis()

    except sqlite3.Error as e:
        print("Error: " + str(e))

    finally:
        if connection:
            connection.close()


def mongo_ORM():
    print("mongo")


def redis_ORM():
    print("redis")


def main():
    # Get the preferred Database type (posgres, sqlite, mongo .. etc.)
    db_type = input("\nDatabase type: (posgres, sqlite, mongo, redis) ")

    if (db_type == "posgres"):
        postgresql_ORM()
    elif (db_type == "sqlite"):
        #sqlite_ORM()
        print("sqlite not implemented yet")
    elif (db_type == "mongo"):
        #mongo_ORM()
        print("mongodb not implemented yet")
    elif (db_type == "redis"):
        #redis_ORM()
        print("redis not implemented yet")
    else:
        print("The database type you entered is not supported at the moment.")
