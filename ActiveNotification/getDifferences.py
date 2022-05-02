import sqlite3
import os

class getDifferences:
    def __init__(self):
        self.open()

    def open(self):
        self.con = sqlite3.connect(os.environ['SQLITE_DB'])
        self.cur = self.con.cursor()

        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS notifications (
                school text, dep text, category text, title text, url text
            )
        """)
        self.con.commit()

    def exists(self, content):
        self.cur.execute(f"""
            SELECT 1 FROM notifications
            WHERE school = :school AND
            dep = :dep AND
            category = :category AND
            title = :title AND
            url = :url
        """, content)
        result = self.cur.fetchall()
        self.con.commit()
        return len(result) > 0

    def insert(self, content):
        self.cur.execute("""
            INSERT INTO notifications (school, dep, category, title, url) 
            VALUES (:school, :dep, :category, :title, :url)
        """, content)
        self.con.commit()

    def close(self):
        self.con.close()