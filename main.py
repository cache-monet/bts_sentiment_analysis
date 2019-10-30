import csv
import json
import lyricsgenius
import os

genius = lyricsgenius.Genius(os.environ['GENIUS_API'])


def get_lyrics(song):
	song = genius.search_song("{} english".format(song), 'BTS')
	return song.lyrics if song else ''

with open('lyrics.csv', mode='w+') as lyrics:
	fieldnames = ['album', 'year', 'song', 'lyrics']
	writer = csv.DictWriter(lyrics, fieldnames=fieldnames)
	writer.writeheader()

	with open('discography.json') as f:
		discography = json.load(f)
		albums = discography['albums']
		for a in albums[-3:]:
			meta = {'album': a ['album'], 'year': a['year']}
			for song in a['tracks']:
				meta['song'] = song
				meta['lyrics'] = get_lyrics(song)
				print(meta)
				writer.writerow(meta)
