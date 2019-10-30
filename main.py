import json
import lyricsgenius
import os
import sqlite3

genius = lyricsgenius.Genius(os.environ['GENIUS_API'])


def get_lyrics(song):
  song = genius.search_song("{} english translation".format(song), 'BTS')
  lyrics = song.lyrics if song else ''
  return "\n".join(filter(lambda line: not line.startswith("["), lyrics.split("\n")))


try:
  sqliteConnection = sqlite3.connect('dev.db')
  cursor = sqliteConnection.cursor()
  print("Successfully Connected to SQLite")
except Error as e:
      print(e)

with open('discography.json') as f:
  discography = json.load(f)
  albums = discography['albums']
  for a in albums[:-6]:
    album, year = a['album'], a['year']
    for song in a['tracks']:
      lyrics = get_lyrics(song)
      cursor.execute("insert into SONGS (album, year, song, lyrics) values (?, ?, ?, ?)",
        (album, year, song, lyrics))
      # cursor.execute(sqlite_insert_query, (album, year, song, lyrics))
      print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
      sqliteConnection.commit()
cursor.close()