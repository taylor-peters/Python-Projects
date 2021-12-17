import sqlite3

conn = sqlite3.connect('submission.db')

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
    if file.endswith('.txt'):
         with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_items(file_name) VALUES (?) ", (file,))
            print(file)
    conn.commit()
conn.close()
