import sqlite3

# Connects to database
conn = sqlite3.connect('submission.db')

# Creates 'tbl_items' table with two columns
with conn:
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS tbl_items( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        file_name TEXT  \
                  ) ')
    conn.commit()
conn.close()

fileList = ('information.docs', 'Hello.txt', 'myImage.png',
            'myMovie.mpg', 'World.txt', 'myPhoto.jpg')

conn = sqlite3.connect('submission.db')

for file in fileList:
    if file.endswith('.txt'):  # Checks ending portion of file name for ".txt"
         with conn:
            cur = conn.cursor()
            # Adds the index of the for loop as the value of the column
            cur.execute("INSERT INTO tbl_items(file_name) VALUES (?) ", (file,))
            print(file)
    conn.commit()
conn.close()
