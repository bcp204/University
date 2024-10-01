import sqlite3
conn = sqlite3.connect("word_database.db")

cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS words_table (
        words TEXT
    )
""")
conn.commit()
conn.close()
try:
    with open("words.txt", "r") as file:
        for line in file:
            word = line.strip().replace("-", "")
            conn = sqlite3.connect("word_database.db")
            cur = conn.cursor()
            cur.execute("INSERT INTO words_table (words) VALUES (?)", (word,))
            conn.commit()
            conn.close()
except FileNotFoundError:
    print("Error: File 'words.txt' not found.")
