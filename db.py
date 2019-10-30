from genius import genius, get_lyrics
import json
import sqlite3

def init():
  conn = sqlite3.connect('dev.db')
  cursor = conn.cursor()
  # Create table - SONGS
  cursor.execute('''CREATE TABLE SONGS
              ([id] INTEGER PRIMARY KEY,
                [album] text,
                [year] integer,
                [song] text,
                [lyrics] text)''')

  conn.commit()

def connect():
  try:
    conn = sqlite3.connect('dev.db')
    cursor = conn.cursor()
  except Error as e:
    print(e)
  return (conn, cursor) 

# insert data
def insert_data():
  conn, cursor = connect()
  with open('discography.json') as f:
    discography = json.load(f)
    albums = discography['albums']
    for a in albums:
      for song in a['tracks']:
        lyrics = get_lyrics(song)
        cursor.execute("insert into SONGS (album, year, song, lyrics) values (?, ?, ?, ?)",
          (a['album'], a['year'], song, lyrics))
        # cursor.execute(sqlite_insert_query, (album, year, song, lyrics))
        print("Record inserted successfully into SONGS table ", cursor.rowcount)
        conn.commit()
  cursor.close()

