#this is ingredient
import sqlite3

DATABASE = 'db/chocolate_house.db'

def addingIngredient(ingredient_name, quantity):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Ingredients (ingredient_name, quantity) VALUES (?, ?)", 
                       (ingredient_name, quantity))
        conn.commit()

def getAllIngredients():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Ingredients")
        return cursor.fetchall()
