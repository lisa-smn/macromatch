import csv
from database import insert_unternehmen

def import_unternehmen_from_csv(csv_path="unternehmen.csv"):
    valid_status = ["offen", "angeschrieben", "interessiert", "kein Interesse"]
    count = 0
    errors = []

    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for index, row in enumerate(reader, start=1):
            try:
                # Normalisierung & Fallbacks
                name = (row.get("name") or "").strip()
                groesse = (row.get("groesse") or "").strip()
                relevant_fuer = (row.get("relevant_fuer") or "").strip()
                branche = (row.get("branche") or "").strip()
                website = (row.get("website") or "").strip()
                kontakt_email = (row.get("kontakt_email") or "").strip()
                telefonnummer = (row.get("telefonnummer") or "").strip()
                standort = (row.get("standort") or "").strip()
                letzter_kontakt = None  # explizit leer (NULL in SQLite)
                kontakt_status = "offen"  # immer als Startwert
                notizen = (row.get("notizen") or "").strip()

                # Insert
                insert_unternehmen((
                    name, groesse, relevant_fuer, branche, website,
                    kontakt_email, telefonnummer, standort,
                    letzter_kontakt, kontakt_status, notizen
                ))
                count += 1
            except Exception as e:
                errors.append((index, row.get("name", "Unbekannt"), str(e)))

    print(f"✅ {count} Unternehmen erfolgreich importiert.")
    if errors:
        print("⚠️ Fehlerhafte Einträge:")
        for idx, name, msg in errors:
            print(f"  Zeile {idx}: {name} → {msg}")

if __name__ == "__main__":
    import_unternehmen_from_csv()
