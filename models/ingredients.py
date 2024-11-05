#this is ingredient
import sqlite3

DATABASE = 'db/chocolate_house.db'

def addingIngredient(ingredientName, Quantity):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Ingredients (ingredientName, Quantity) VALUES (?, ?)", 
                       (ingredientName, Quantity))
        conn.commit()

def getAllIngredients():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Ingredients")
        return cursor.fetchall()
