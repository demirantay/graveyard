# PostgreSQL Commandline ORM

Table of Contents:
- [Setup](#setup)
- [Usage](#usage)
  - [create table](#create-table)
  - [drop table](#drop-table)
  - [insert row](#insert-row)
  - [delete row](#delete-row)
  - [list tables](#list-tables)
  - [list rows](#list-rows)
  - [update all rows](#update-all-rows)
  - [update single row](#update-single-row)
  - [limit rows](#limit-rows)
  - [limit between](#limit-between)
  - [order by](#oreder-by)
  - [populate-db](#populate-db)

## Setup

First you need to download the repo and than if you want to use the repo you need to have `PostgreSQL` installed on your computer.

You need to create a postgresql database before running this program. In order to create a database simply start your postgresql server and type:
```
$ createdb <db_name>
```
Voila, after that you can download the program and run it like this:

```
$ git clone https://github.com/demirantay/py-psql.git
$ cd py-psql
$ python main.py
```

## Usage

After you run the program you will get a prompt wanting you to type your database name:
```
$ python run.py

Database name: <type_your_db_name>
```
After that you are in your database and you can query whatever you want. Unfortunately, at the moment the program only supports the following:
- `create table` -- For creating tables
- `drop table`   -- For deleting tables
- `insert row`   -- For entering data to a table
- `delete row`   -- For deleting data from a table
- `list tables`  -- For listing all the tables in the db
- `list rows`    -- For listing the rows of a table
- `update all rows` -- For updating all rows in a single column
- `update single row` -- For updating a single row of a column
- `limit rows` -- For limiting rows
- `limit between` --For limiting between the rows
- `order by` -- For ordering the table
- `populate db` -- Creates a table with 30 rows of test data
- `quit`         -- For quiting the program

You could also get this list of commands within the program by simply typing `help` which shows the documentation

### create table

When you run this command you will be prompted to enter a name and the column descriptions. Be aware! you should not enter a `id` column the program already implements all `tables[0]` column as a auto incrementing primary key which is named `id`.

Example usage:

```
$ create table
Table name ? Cars
How many columns ? 2
Column 1 name: Name
Column 1 type (text or int or float): text
Column 2 name: Price
Column 2 type (text or int or float): int
```

### drop table

You can delete your table very easily you just need to give its name but be aware once you delete a table there is no way getting back the data the table contains.

Usage:
```
$ drop table
Table name ? Cars
Are you sure ? (yes or no) yes
```

### insert row

You can insert new data(row) to the table with the `insert row` command. You will be prompet to enter values for each columns.

 Be aware if your columns type is a text you need to put `"foo"` quotation marks around your input. If you are entering a int or a float just enter it normally.

Lets assume we didnt drop the `Cars` table above and instead we are adding data to it for example usage:
```
$ insert row
Table name ? Cars
Name: 'Mustang'
Price: 25000
```

### delete row

You can easily delete rows by telling which table it is that you want the row to be removed and you need to give the `id` of the row for the program to remove it.

You should use `list rows` if you do not know what is the `id` of the row you want to delete

```
$ delete row
Table name ? Cars
Row id ? 1
```

### list tables

You can list all of your tables in the database you entered at the beginning easily with the command above. Lets see a simple usage:

```
$ list tables
('table_1',)
('table_2',)
('table_3',)
```

### list rows

You can list all of the rows of a table with the simple `list rows` command all you have to do is give it a table name

Lets view our `Cars` table built above:
```
$ list rows
Table name ? cars
(1, 'Mustang', 25000)
```

### update all rows

If you want to update all the rows in a tables specific column, you can use this command. See the code below:
```
$ update all rows
Table name: <insert_table_name>
Column name: <insert_col_name>
New value: <insert_value>
```

### update single row

Instead of updating all of the rows of a column in a table you can update a single rows column data. All of the tables you createa already have a serial primary key named `id` so while selcting the specific row you need to pass the id of the row that you want to edit. See the code below:
```
$ update single row
Table name: <insert_table_name>
Row id: <id_num>
column name: <col_name>
New value: <insert_value>
```

### limit rows

Lets say that you have a table with 30 rows inside it and you want to get the first 5 of them. You can use limit rows to get the amount of rows you want. After that the program will print out the selected rows to the screen.
```
$ limit rows
Table name: foo
How many rows you want: 5
(1, 'fooName', 18, 4343)
(2, 'fooName', 18, 4343)
(3, 'fooName', 18, 4343)
(5, 'fooName', 18, 4343)
(6, 'fooName', 18, 4343)
```

### limit between

As you have seen above we can limit our rows but that funciton only lets us start from the first element of the table. Instead with limit between we can choose our starting point:
```
$ limit between
Table name: foo
Starting from which row: 10
How many rows you want: 5
```


### order by

You can order your content inside a table from a acsending or a descending order. You just need to give the program a table and the column you want to order:
```
$ order by
Table name: <insert_table_name>
Order by (col name): <insert_column_name>
Ordering way (desc or asc): desc
```

### populate db

If you are lazy to write few insert commands into the table, then you are in luck! You can use this command, give the table a name and then et volia you have a new table with 30 rows inside it. The schema of the table is (id, name, age, salary)
```
$ populate db
What do you want to name your table: <insert_name>
```


## FAQ

Q: Why even code something like this ?

A: I was learning postgresql and needed a project to test out what I have learned (the content of the program is insignificant)
