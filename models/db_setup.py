# models/db_setup.py
import sqlite3

def create_tables():
    connection = sqlite3.connect('db/chocolate_house.db')
    cursor = connection.cursor()

    #to  Creating Seasonal Flavors Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS SeasonalFlavors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        flavor_name TEXT NOT NULL,
        description TEXT
    )
    ''')

    # Create Ingredients Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Ingredients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ingredient_name TEXT NOT NULL,
        quantity INTEGER NOT NULL
    )
    ''')

    # Create Customer Suggestions Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS CustomerSuggestions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_name TEXT,
        suggestion TEXT,
        allergy_concern TEXT
    )
    ''')

    connection.commit()
    connection.close()

# Run this script to initialize the tables
if __name__ == "__main__":
    create_tables()
