from flask import Flask, render_template, url_for
import sqlite3 

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('favorites.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('about.html')

@app.route('/books')
def books():
    conn = get_db_connection()
    books = conn.execute('SELECT * FROM books').fetchall()
    conn.close()
    return render_template('books.html', books=books)

@app.route('/movies')
def movies():
    conn = get_db_connection()
    movies = conn.execute('SELECT * FROM movies').fetchall()
    conn.close()
    return render_template('movies.html', movies=movies)

@app.route('/shows')
def shows():
    conn = get_db_connection()
    shows = conn.execute('SELECT * FROM shows').fetchall()
    conn.close()
    return render_template('shows.html', shows=shows)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)


