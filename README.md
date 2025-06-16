# Macromatch 🤝

**Macromatch** ist eine webbasierte Anwendung zur Verwaltung und Analyse von Kontaktdaten regionaler Unternehmen im Rahmen der *Studentischen INITIATIVE* an der Hochschule Macromedia.

## Funktionen

- 📋 **Neues Unternehmen erfassen**: Eingabeformular zur strukturierten Erfassung
- 🌟 **Filter & Darstellung**: Unternehmen nach Studiengang & Größe filtern und anzeigen
- 🛠️ **Eintrag bearbeiten oder löschen**: Bestehende Daten aktualisieren oder entfernen
- 📧 **E-Mail-Vorlage generieren**: Automatisiertes Anschreiben zur Kontaktaufnahme
- 📊 **Statistiken**: Visualisierung der Verteilung nach Größe, Studiengang & Kontaktstatus

## Technologien

- [Streamlit](https://streamlit.io/) – für die Weboberfläche
- [SQLite](https://www.sqlite.org/) – als lokale Datenbank
- [Pandas](https://pandas.pydata.org/) – zur Datenverarbeitung
- [Plotly](https://plotly.com/python/) – für interaktive Diagramme

## Projektstruktur

```bash
macromatch/
├── app.py                 # Haupt-Streamlit-Anwendung
├── database.py           # Datenbanklogik (CRUD)
├── schema.sql            # Tabellenstruktur für SQLite
├── requirements.txt      # Benötigte Python-Bibliotheken
├── __init__.py           # Package-Kennzeichnung
```

## Installation

```bash
git clone https://github.com/lisa-smn/macromatch.git
cd macromatch
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```