import sqlite3

def prepare_db(cursor: sqlite3.Cursor):

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS restaurants (
        restaurant_id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        city TEXT,
        lat REAL,
        lon REAL,
        opening_time TEXT,
        closing_time TEXT,
        start_breakfast_time TEXT,
        end_breakfast_time TEXT
    )
    ''')
    cursor.execute('DELETE FROM restaurants')
    cursor.connection.commit()