
# some sample queries to be used in an initial exploratory analysis

# all records
all = """
    SELECT * FROM songplays;
"""

# count total number of records
total_records = """
    SELECT COUNT(*)
    FROM songplays;
"""

# count number of non-NULL records in song and artist columns
non_null_songs = """
    SELECT COUNT(*)
    FROM songplays
    WHERE song_id IS NOT NULL;

"""

non_null_artists = """
    SELECT COUNT(*)
    FROM songplays
    WHERE artist_id IS NOT NULL;
"""


# count number of songs
songs_count = """
    SELECT COUNT(*)
    FROM songs;

"""

songs_list = """
    SELECT *
    FROM songs;

"""


# count number of artists
artist_count = """
    SELECT COUNT(*)
    FROM artists;

"""

artist_list = """
    SELECT *
    FROM artists;

"""


# songs jointed with artists
songs_with_artists = """
    SELECT *
    FROM songs
    JOIN artists USING(artist_id)

"""


# how many users are there
user_table = """
    SELECT * 
    FROM users

"""