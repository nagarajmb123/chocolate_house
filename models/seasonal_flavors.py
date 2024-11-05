#this is seasonalflavors
import sqlite3

DATABASE = 'db/chocolate_house.db'

def addingSeasonalFlavors(flavor_name, description):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO SeasonalFlavors (flavor_name, description) VALUES (?, ?)", 
                       (flavor_name, description))
        conn.commit()

def getSeasonalFlavors():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM SeasonalFlavors")
        return cursor.fetchall()
