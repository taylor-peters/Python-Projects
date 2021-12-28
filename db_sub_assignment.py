import sqlite3

# Connects to database
conn = sqlite3.connect('db_and_py.db')

# Creates 'tbl_items' table with two columns
with conn:
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS tbl_people( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        Name TEXT,  \
        Species TEXT, \
        IQ INT \
        ) ')
    conn.commit()
conn.close()

conn = sqlite3.connect('db_and_py.db')

peopleValues = (('Jean Baptiste Zorg','Human',122),('Korben Dallas','Meat Popsicle',100),('Ak\'not','Mangalore', -5))

with conn:
    cur = conn.cursor()
    # Adds the index of the for loop as the value of the column
    cur.executemany("INSERT INTO tbl_people(Name, Species, IQ) VALUES (?, ?, ?)", peopleValues)
    conn.commit()
conn.close()
