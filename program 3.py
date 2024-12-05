import sqlite3


conn = sqlite3.connect('phonebook.db')


cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS Entries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone_number TEXT NOT NULL
    )
''')

conn.commit()
conn.close()

print("Database 'phonebook.db' and table 'Entries' created successfully.")

# Matthew Beekman
# Program 3
# 12/4/2024