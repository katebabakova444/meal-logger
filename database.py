import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS meals (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT NOT NULL,
             calories REAL,
             protein REAL,
             fat REAL,
             carbs REAL,
             date TEXT DEFAULT (DATE('now'))
        )
    ''')
    conn.commit()
    conn.close()
def insert_meal(name: str, calories: float, protein: float, fat: float, carbs: float):
    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO meals (name, calories, protein, fat, carbs)
        VALUES (?, ?, ?, ?, ?)
    ''', (name, calories, protein, fat, carbs))

    conn.commit()
    conn.close()

def get_all_meals():
    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM meals")
    meals = cursor.fetchall()

    conn.close()
    return meals

def get_meals_by_date(date=None):
    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()

    if not date:
        date = datetime.today().strftime("%Y-%m-%d")

    cursor.execute("SELECT * FROM meals WHERE date = ?", (date,))
    meals = cursor.fetchall()

    conn.close()
    return meals

def delete_meal_by_id(meal_id):
    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM meals WHERE id = ?", (meal_id,))
    conn.commit()
    conn.close()

def update_meal_by_id(meal_id, name, calories, protein, fat, carbs):
    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()

    cursor.execute('''
    UPDATE meals
    SET name = ?, calories = ?, protein = ?, fat = ?, carbs = ?
    WHERE id = ?
    ''', (name, calories, protein, fat, carbs, meal_id))

    conn.commit()
    conn.close()


