# this is the customer suggestion
import sqlite3

DATABASE = 'db/chocolate_house.db'

def addingSuggestion(customerName, Suggestion, allergyConcern):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO CustomerSuggestions (customerName, Suggestion, allergyConcern) VALUES (?, ?, ?)", 
                       (customerName, Suggestion, allergyConcern))
        conn.commit()

def getALLSuggestions():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM CustomerSuggestions")
        return cursor.fetchall()
