import sqlite3


connection = sqlite3.connect('KFC_database.db')

cursor = connection.cursor()


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

res = cursor.execute(
    "SELECT * FROM restaurants WHERE city = 'Новосибирск' and start_breakfast_time < '08:30:00' and end_breakfast_time > '09:00:00'"
)

print(res.fetchall())