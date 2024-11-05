#ingredients model
import sqlite3

DATABASE = 'db/chocolate_house.db'

def add_ingredient(ingredient_name, quantity):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Ingredients (ingredient_name, quantity) VALUES (?, ?)", 
                       (ingredient_name, quantity))
        conn.commit()

def get_ingredients():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Ingredients")
        return cursor.fetchall()

def delete_ingredient(ingredient_id):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Ingredients WHERE id = ?", (ingredient_id,))
        conn.commit()