import sqlite3

def connect():
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS store(id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn TEXT)")
    conn.commit()
    conn.close()
    
def insert(title, author, year, isbn):
        conn = sqlite3.connect("books.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO store VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
        conn.commit()
        conn.close()

def view():
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM store")
    rows = cursor.fetchall()
    conn.close()
    return rows
    
def delete(id):
        conn = sqlite3.connect("books.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM store WHERE id=?", (id,))
        conn.commit()
        conn.close()
def update(id, title, author, year, isbn):
       conn = sqlite3.connect("books.db")
       cursor = conn.cursor()
       cursor.execute("UPDATE store SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
       conn.commit()
       conn.close()
       
def search(title="", author="", year="", isbn=""):
       conn = sqlite3.connect("books.db")
       cursor = conn.cursor()
       cursor.execute("SELECT * FROM store WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
       rows = cursor.fetchall()
       conn.close()
       return rows
       
connect()

#print(view())
print(search(author="John Smith"))


