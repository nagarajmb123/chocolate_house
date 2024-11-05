# models/customer_suggestions.py
import sqlite3

DATABASE = 'db/chocolate_house.db'

def add_suggestion(customer_name, suggestion, allergy_concern):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO CustomerSuggestions (customer_name, suggestion, allergy_concern) VALUES (?, ?, ?)", 
                       (customer_name, suggestion, allergy_concern))
        conn.commit()

def get_suggestions():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM CustomerSuggestions")
        return cursor.fetchall()
