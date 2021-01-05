#
# change help docs, try to first welcome the user with more prompt to redirect
# the to a different database command docs for example: type p help for PostgreSQL
# help docs ... etc. everything in one place looks very cluttered.
#


# outputs all of the commands in the app
def help_docs():
    '''
        Function name: help_docs()
        Desc: No need for parameters, the function just outputs all of the
              commands that can be used in the app.
    '''
    docs = ("\nHelper Commands:\n"
            "\n"
            "`help posgres `     -- Lists PostgreSQL ORM Commands\n"
            "`help sqlite`       -- Lists SQLite ORM Commandss\n"
            "`help mongo`        -- Lists MongoDB ORM Commands\n"
            "`help redis`        -- Lists Redis ORM Commands\n"
            "`quit`              -- For quiting the program"
            "\n"
            )
    print(docs)


# outputs just the PostgreSQL commands
def help_docs_postgres():
    '''
        Function name: help_docs_postgres()
        Desc: No need for parameters, the function just outputs the commands
              that can be used in postgres command line ORM
    '''
    docs = ("\n# PostgreSQL Commands:\n"
            "\n"
            "`create table`      -- For creating tables\n"
            "`drop table`        -- For deleting tables\n"
            "`insert row`        -- For entering data to a table\n"
            "`delete row`        -- For deleting data from a table\n"
            "`list tables`       -- For listing all the tables in the db\n"
            "`list rows`         -- For listing the rows of a table\n"
            "`update all rows`   -- For updating all rows in a single column\n"
            "`update single row` -- For updating a single row of column\n"
            "`limit rows`        -- For limiting the rows\n"
            "`limit between`     -- For limiting between the rows\n"
            "`order by`          -- For ordering the table\n"
            "`populate db`       -- If you are lazy to enter inserts \n"
            "`quit`              -- For quiting the program"
            "\n"
            )
    print(docs)


# outputs just the Sqlite3 commands
def help_docs_sqlite():
    '''

    '''
    docs = ("sqlite docs")
    print(docs)


# outputs just the MongoDB commands
def help_docs_mognodb():
    '''

    '''
    docs = ("mongo docs")
    print(docs)


# outputs just the Redis commands
def help_docs_redis():
    '''

    '''
    docs = ("redis docs")
    print(docs)
