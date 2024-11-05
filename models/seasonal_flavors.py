# models/seasonal_flavors.py
import sqlite3

DATABASE = 'db/chocolate_house.db'

def add_flavor(flavor_name, description):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO SeasonalFlavors (flavor_name, description) VALUES (?, ?)", 
                       (flavor_name, description))
        conn.commit()

def get_flavors():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM SeasonalFlavors")
        return cursor.fetchall()
