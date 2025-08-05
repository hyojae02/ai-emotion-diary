import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect("diary.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS diary (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        text TEXT,
        translation TEXT,
        emotions TEXT
    )''')
    conn.commit()
    conn.close()

def save_diary_entry(text, translation, emotions):
    conn = sqlite3.connect("diary.db")
    c = conn.cursor()
    c.execute("INSERT INTO diary (date, text, translation, emotions) VALUES (?, ?, ?, ?)",
              (datetime.now().strftime("%Y-%m-%d"), text, translation, ",".join(emotions)))
    conn.commit()
    conn.close()
