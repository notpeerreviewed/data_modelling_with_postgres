
# Creates all necessary SQL statements used in the processing of song data
# and population of database tables in the sparkify database.

# This file is referenced by the following scripts:
# create_tables.py, etl.py


# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS song_plays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
    CREATE TABLE songplays (
        songplay_id serial PRIMARY KEY,
        start_time timestamp NOT NULL,
        user_id int NOT NULL REFERENCES users (user_id) ON DELETE CASCADE,
        level varchar,
        song_id varchar REFERENCES songs (song_id) ON DELETE RESTRICT,
        artist_id varchar REFERENCES artists (artist_id) ON DELETE RESTRICT,
        session_id int,
        location varchar,
        user_agent varchar
    )
""")

user_table_create = ("""
    CREATE TABLE users (
        user_id int PRIMARY KEY,
        first_name varchar,
        last_name varchar,
        gender varchar,
        level varchar
    )
""")

song_table_create = ("""
    CREATE TABLE songs (
        song_id varchar PRIMARY KEY NOT NULL,
        title varchar NOT NULL,
        artist_id varchar,
        year int,
        duration numeric NOT NULL
    )
""")

artist_table_create = ("""
    CREATE TABLE artists (
        artist_id varchar PRIMARY KEY NOT NULL,
        name varchar NOT NULL,
        location varchar,
        latitude float,
        longitude float
    )
""")

time_table_create = ("""
    CREATE TABLE time (
        id SERIAL PRIMARY KEY,
        start_time timestamp,
        hour int,
        day int,
        week int,
        month int,
        year int,
        weekday int
    )
""")

# INSERT RECORDS
songplay_table_insert = ("""
    INSERT INTO songplays ("start_time", "user_id", "level", "song_id", "artist_id", "session_id", "location", "user_agent") 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT DO NOTHING
""")

user_table_insert = ("""
    INSERT INTO users ("user_id", "first_name", "last_name", "gender", "level") 
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (user_id) 
    DO
        UPDATE SET 
            first_name = EXCLUDED.first_name,
            last_name = EXCLUDED.last_name,
            gender = EXCLUDED.gender,
            level = EXCLUDED.level
""")

song_table_insert = ("""
    INSERT INTO songs ("song_id", "title", "artist_id", "year", "duration") 
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (song_id) 
    DO
        UPDATE SET 
            title = EXCLUDED.title,
            artist_id = EXCLUDED.artist_id,
            year = EXCLUDED.year,
            duration = EXCLUDED.duration
                    
""")

artist_table_insert = ("""
    INSERT INTO artists ("artist_id", "name", "location", "latitude", "longitude") 
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (artist_id)
    DO
        UPDATE SET 
            name = EXCLUDED.name,
            location = EXCLUDED.location,
            latitude = EXCLUDED.latitude,
            longitude = EXCLUDED.longitude
""")


time_table_insert = ("""
    INSERT INTO time ("start_time", "hour", "day", "week", "month", "year", "weekday") 
        VALUES (%s, %s, %s, %s, %s, %s, %s)
""")

# FIND SONGS
song_select = ("""
    SELECT 
        songs.song_id,
        songs.artist_id
    FROM songs
    JOIN artists ON ((songs.title = %s) AND (artists.name = %s) AND (songs.duration = %s));
""")

# QUERY LISTS

create_table_queries = [user_table_create, song_table_create, artist_table_create, time_table_create, songplay_table_create]
drop_table_queries = [user_table_drop, song_table_drop, artist_table_drop, time_table_drop, songplay_table_drop]