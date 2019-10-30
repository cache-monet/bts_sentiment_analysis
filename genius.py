import lyricsgenius
import os

genius = lyricsgenius.Genius(os.environ['GENIUS_API'])

def get_lyrics(song):
  song = genius.search_song("{} english translation".format(song), 'BTS')
  lyrics = song.lyrics if song else ''
  return "\n".join(filter(lambda line: not line.startswith("["), lyrics.split("\n")))
