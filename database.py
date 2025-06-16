import sqlite3
from contextlib import closing

DB_PATH = "macromatch.db"

def connect():
    return sqlite3.connect(DB_PATH, timeout=10)

def init_db():
    with connect() as conn, open("schema.sql", "r") as f:
        conn.executescript(f.read())
        conn.commit()

def get_all_unternehmen():
    with connect() as conn, closing(conn.cursor()) as cursor:
        cursor.execute("SELECT * FROM unternehmen")
        return cursor.fetchall()

def unternehmen_exists(name):
    with connect() as conn, closing(conn.cursor()) as cursor:
        cursor.execute("SELECT 1 FROM unternehmen WHERE name = ?", (name,))
        return cursor.fetchone() is not None


def insert_unternehmen(data):
    if unternehmen_exists(data[0]):  # Name ist erstes Feld
        print(f"⚠️ Unternehmen '{data[0]}' bereits vorhanden. Einfügen übersprungen.")
        return
    with connect() as conn, closing(conn.cursor()) as cursor:
        cursor.execute("""
            INSERT INTO unternehmen (
                name, groesse, relevant_fuer, branche, website, kontakt_email,
                telefonnummer, standort, letzter_kontakt, kontakt_status, notizen
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, data)
        conn.commit()


def update_unternehmen(data):
    with connect() as conn, closing(conn.cursor()) as cursor:
        cursor.execute("""
            UPDATE unternehmen SET
                name = ?, groesse = ?, relevant_fuer = ?, branche = ?, website = ?,
                kontakt_email = ?, telefonnummer = ?, standort = ?, letzter_kontakt = ?,
                kontakt_status = ?, notizen = ?
            WHERE id = ?
        """, data)
        conn.commit()

def delete_unternehmen(untern_id):
    with connect() as conn, closing(conn.cursor()) as cursor:
        cursor.execute("DELETE FROM unternehmen WHERE id = ?", (untern_id,))
        conn.commit()
