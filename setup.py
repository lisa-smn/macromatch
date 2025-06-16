# setup.py
# --------------------------------------------
# 🚧 Dieses Skript initialisiert die Datenbank
# --------------------------------------------
# Führe dieses Skript **nur einmal** aus, um die Tabelle "unternehmen" gemäß der schema.sql-Datei anzulegen.
# Achtung: Bei wiederholter Ausführung können vorhandene Daten überschrieben oder gelöscht werden,
# je nachdem, wie die schema.sql aufgebaut ist (z. B. bei DROP TABLE).
#
# Verwende dieses Skript also nur beim ersten Setup oder wenn du bewusst ein frisches Datenbankschema brauchst.
# --------------------------------------------

from database import init_db

init_db()
print("✅ Datenbank wurde erfolgreich initialisiert.")
