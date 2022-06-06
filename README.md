
# Production notes: Data Modelling with PostGRES

### Author: Jeff Lean
### Date: 31 May 2022


# Purpose
The project brief clearly identifies that the Sparkify company wants to be able to
conduct analyses of the data they have collected on songs and user activity.

Their analyics team have identified a particular focus on the songs their users are
listening to.

# Method

## Data 

The data for this project was provided in the form of two datasets - a songs dataset and a log dataset.
The songs dataset consists of 76 individual JSON files. Each file contains a single record of a song
and the artist of that song. Some records include NULL values.

The log dataset consists of 30 individual JSON files. Each file contains activity logs grouped by year
and month.

## Modelling approach
A simple star schema has been created for this project using four dimension tables and a single fact table.
The dimension tables include:

 - users
 - artists
 - songs
 - time
 
The fact table is called songplays and includes the data for each unique instance of a song being played.

This simple star schema is appropriate because the purpose of the project is to create a database which will
be primarily read-focused. This is an example of an OLAP database.

     
# User guide

## How to run the scripts

 - Open a terminal window
 - Type `python create_tables.py`. This will create the necessary tables in the database.
 - Type `python etl.py`. This will process the data and populate the database tables.


# File structure
The files in this project are:

 - sql_queries.py: 
     - The script begins by dropping all tables to ensure clean table creation.
     - This script then specifies the SQL code required to create each table in the database.
     - INSERT queries are then specified to add data to each table.
     - all queries are added 
 - create_tables.py: 
     - This script calls the sql_queries.py script which makes the queries available.
     - The sparkifydb database is created.
     - Tables are dropped.
     - Fresh tables are created.
 - etl.py:
     - This script calls the sql_queries.py script which makes the queries available.
     - Song files and log files are processed
 - test.ipynb:
     - This is a python notebook used for testing during development of the project.
     - It includes various tests on the structure of the tables
 - etl.ipynb:
     - This is a python notebook used to assist in the development of the project.
     - It was used to easily interact with the data during the development process.
     - Approaches are easily captured through the use of developer notes within the 
       notebook.


# Developer notes

## songplay table notes
When creating a table containing foreign keys it is important to make sure that all the parent
tables have already been created. I needed to modify the provided sql_queries.py script because
the create_table_queries list placed the songplay_table_create query first and this was the 
table that contained all my foreign keys.

The foreign key for user_id includes a reference to the users table. If the user is deleted from
the user table I have elected to cascade this to the songplay table to delete the record from
there as well.

The foreign keys for song_id and artist_id include ON DELETE RESTRICT clauses. This will prevent
deletion of any songs or artists if there is a record in the songplay table associated with them.


### General notes

- Found this handy reference for the SERIAL command for the Primary key for the songplays table https://stackoverflow.com/questions/787722/what-is-postgresql-equivalent-to-autoincrement
- I found that I needed to be more careful about the variable type for several tables. It was only at the very end of the process, when I ran the etl.py script, that I realised the artist_id and song_id should have been varchar instead of int.
- This reference was very useful when working through the foreign key specifications. https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-foreign-key/
- Reference for loading data to PostGRES using COPY. https://hakibenita.com/fast-load-data-python-postgresql
