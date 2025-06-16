# check_db.py
import sqlite3

DB_NAME = "macromatch.db"

def print_all_unternehmen():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM unternehmen")
        rows = cursor.fetchall()

        if not rows:
            print("📭 Keine Unternehmen in der Datenbank.")
        else:
            col_names = [description[0] for description in cursor.description]
            print("📋 Spalten:", col_names)
            print("🔍 Einträge:")
            for row in rows:
                print(row)

    except sqlite3.Error as e:
        print("❌ Fehler beim Zugriff auf die Datenbank:", e)
    finally:
        conn.close()

if __name__ == "__main__":
    print_all_unternehmen()
