import sqlite3
import os

con = sqlite3.connect(os.environ['SQLITE_DB'])
cur = con.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS notifications (
        school text, dep text, category text, title text, url text
    )
""")
con.commit()

def exists(content):
    cur.execute(f"""
        SELECT 1 FROM notifications
        WHERE school = :year AND
        dep = :dep AND
        category = :category AND
        title = :title AND
        url = :url
    """, content)
    result = cur.fetchall()
    cur.commit()
    return len(result) > 0

def insert(content):
    cur.execute("""
        INSERT INTO notifications (school, dep, category, title, url) 
        VALUES (:year, :dep, :category, :title, :url)
    """, content)
    con.commit()

def close():
    con.close()