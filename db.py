import sqlite3

conn = sqlite3.connect('dev.db')  # You can create a new database by changing the name within the quotes
c = conn.cursor() # The database will be saved in the location where your 'py' file is saved
# Create table - song
c.execute('''CREATE TABLE SONGS
             ([id] INTEGER PRIMARY KEY,
              [album] text,
              [year] integer,
              [song] text,
              [lyrics] text)''')

conn.commit()
