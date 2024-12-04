import sqlite3

connection = sqlite3.connect('favorites.db')

with open('schema.sql') as f:
    try:
        connection.executescript(f.read())
        print("Tables created successfully.")
    except Exception as e:
        print("An error occurred while executing schema.sql:", e)

cur = connection.cursor()

# Insert favorite books
cur.execute("INSERT INTO books (title, author) VALUES (?, ?)",
            ('Sapiens: A Brief History of Humankind', 'Yuval Noah Harari'))
cur.execute("INSERT INTO books (title, author) VALUES (?, ?)",
            ('The Emperor of All Maladies: A Biography of Cancer', 'Siddhartha Mukherjee'))
cur.execute("INSERT INTO books (title, author) VALUES (?, ?)",
            ('The Emperor of All Maladies: A Biography of Cancer', 'Siddhartha Mukherjee'))
cur.execute("INSERT INTO books (title, author) VALUES (?, ?)",
            ('The Emperor of All Maladies: A Biography of Cancer', 'Siddhartha Mukherjee'))
cur.execute("INSERT INTO books (title, author) VALUES (?, ?)",
            ('The Emperor of All Maladies: A Biography of Cancer', 'Siddhartha Mukherjee'))

# Insert favorite movies
cur.execute("INSERT INTO movies (title, director) VALUES (?, ?)",
            ('Inception', 'Christopher Nolan'))
cur.execute("INSERT INTO movies (title, director) VALUES (?, ?)",
            ('The Matrix', 'Lana Wachowski, Lilly Wachowski'))

# Insert favorite shows
cur.execute("INSERT INTO shows (title, director) VALUES (?, ?)",
            ('Stranger Things', 'The Duffer Brothers'))
cur.execute("INSERT INTO shows (title, director) VALUES (?, ?)",
            ('Breaking Bad', 'Vince Gilligan'))

connection.commit()
connection.close()