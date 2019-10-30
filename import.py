import sqlite3
import pandas as pd
from pandas import DataFrame

conn = sqlite3.connect('dev.db')  
c = conn.cursor()

read_songs = pd.read_csv (r'./lyrics.csv')
read_songs.to_sql('SONGS', conn, if_exists='append', index = False) # Insert the values from the csv file into the table 'SONGS' 

# c.execute('''
# INSERT INTO SONGS(album, year, song, lyrics)
          # ''')

c.execute('''SELECT DISTINCT * FROM SONGS''')
#print(c.fetchall())

# df = DataFrame(c.fetchall(), columns=['album','year','song','lyrics'])
# print (df) # To display the results after an insert query, you'll need to add this type of syntax above: 'c.execute(''' SELECT * from latest table ''')
# export_csv = df.to_csv (r'C:\Users\Ron\Desktop\Client\export_list.csv', index = None, header=True) # Uncomment this syntax if you wish to export the results to CSV. Make sure to adjust the path name
# Don't forget to add '.csv' at the end of the path (as well a