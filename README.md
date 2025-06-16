# 🎯 Macromatch – Unternehmensdatenbank für Hochschulkooperationen

**Macromatch** ist ein interaktives Web-Tool zur Erfassung, Verwaltung und Auswertung potenzieller Kooperationsunternehmen für praxisorientierte Hochschulprojekte.

## 🚀 Ziel

Die Anwendung soll studentischen Projektveranstaltungen ermöglichen, gezielt passende Unternehmen (z. B. aus Hamburg) zu finden – basierend auf Größe, Branche und Relevanz für bestimmte Studiengänge.

## 🛠 Funktionen

* ✅ Unternehmen anlegen, bearbeiten und löschen
* ✅ Relevanz für bestimmte Studiengänge zuweisen
* ✅ Farbcodierter Kontaktstatus (offen, angeschrieben, interessiert, kein Interesse)
* ✅ CSV-Import (z. B. aus Recherche)
* ✅ Filterfreie Ansicht aller Einträge
* ✅ Statistische Auswertung nach Studiengängen
* ✅ CSV-Export aller Unternehmen oder gefilterter Listen

## 🎓 Studiengänge

Unternehmen können als relevant für folgende Studiengänge markiert werden:

* Animation & Illustration
* Brandmanagement
* Business Management
* Design
* Eventmanagement
* Fashion Management
* Fußballmanagement
* Immobilienwirtschaft
* Journalismus
* Marketingmanagement
* Medien- und Kommunikationsdesign
* Medienmanagement
* Musikmanagement
* Psychologie
* Sportjournalismus
* Sportmanagement
* Wirtschaftspsychologie
* u. f. w.

## ⚙️ Installation

1. **Projekt klonen:**

   ```bash
   git clone https://github.com/dein-nutzername/macromatch.git
   cd macromatch
   ```

2. **Virtuelle Umgebung erstellen:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Abhängigkeiten installieren:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Datenbank initialisieren:**

   ```bash
   python setup.py
   ```

5. **App starten:**

   ```bash
   streamlit run app.py
   ```

## 📃 CSV-Import (optional)

Um größere Datenmengen schnell zu importieren, kannst du eine CSV-Datei wie folgt vorbereiten:

```csv
name,groesse,relevant_fuer,branche,website,kontakt_email,telefonnummer,standort,notizen
```

Beispiel-Datei: `unternehmen_import.csv`

Import via:

```bash
python import_csv.py
```

## 📂 Projektstruktur

```text
macromatch/
│
├── app.py                # Haupt-UI mit Streamlit
├── database.py           # Datenbankfunktionen (CRUD)
├── import_csv.py         # CSV-Import-Skript
├── check_db.py           # Test-Skript zur Datenbankanzeige
├── setup.py              # Initialisierung der DB
├── schema.sql            # SQLite-Datenbankschema
├── unternehmen.csv       # Beispieldatei für CSV-Import
├── macromatch.db         # SQLite-Datenbank (nach Setup)
├── requirements.txt      # Abhängigkeiten
├── README.md             # Dieses Dokument
└── LICENSE               # Lizenz
```

## 📌 Hinweise

* Die Datenbank verhindert Dopplungen durch Namensabgleich beim Import.
* Kontaktstatus ist standardmäßig „offen“, das Datum kann leer sein.
* Beim CSV-Import sind valide Studiengangnamen wichtig (siehe oben).

---

**Stand:** Juni 2025
**Lizenz:** MIT
**Autorin:** Lisa Simon
