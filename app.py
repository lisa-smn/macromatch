# ===============================================
# Macromatch – Streamlit App zur Unternehmensdatenbank
# ===============================================
# Funktionen:
# - Unternehmen erfassen (Formular)
# - Bestehende Einträge filtern und anzeigen
# - Einträge bearbeiten oder löschen
# - E-Mail-Vorlagen generieren
# - Statistische Auswertungen anzeigen

# === Setup & Initialisierung ===
import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import date
from database import init_db, get_all_unternehmen, insert_unternehmen, update_unternehmen, delete_unternehmen

# Initialisiere DB beim ersten Start

# init_db()  # Nur einmal manuell ausführen!


def status_farbe(status):
    farben = {
        "offen": "#FFF3CD",           # Gelb
        "angeschrieben": "#D1ECF1",   # Blau
        "interessiert": "#D4EDDA",    # Grün
        "kein Interesse": "#F8D7DA"    # Rot
    }
    return f"background-color: {farben.get(status, 'white')}" 

# --- Streamlit UI-Konfiguration ---
st.set_page_config(page_title="Macromatch", layout="centered")
st.title("🤝 Macromatch – Unternehmensdatenbank")
st.divider()

# === Eingabeformular ===
# - Erfassung neuer Unternehmen via Streamlit-Formular
st.subheader("📋 Neues Unternehmen hinzufügen")

STUDIENGAENGE = [
    "Alle",
    "Animation & Illustration",
    "Brandmanagement",
    "Business Management",
    "Design",
    "Eventmanagement",
    "Fashion Management",
    "Fußballmanagement",
    "Immobilienwirtschaft",
    "Journalismus",
    "Marketingmanagement",
    "Medien- und Kommunikationsdesign",
    "Medienmanagement",
    "Musikmanagement",
    "Sportjournalismus",
    "Sportmanagement",
    "Wirtschaftspsychologie",
    "Psychologie",
    "Brand Management (M.A.)",
    "Business Management (M.A.)",
    "Design Management (M.A.)",
    "Medien- und Kommunikationsmanagement (M.A.)",
]

KONTAKTSTATUS = ["offen", "angeschrieben", "interessiert", "kein Interesse"]

with st.form("unternehmen_formular"):
    name = st.text_input("Unternehmensname")
    groesse = st.selectbox("Größe", ["Startup", "Klein", "Mittel", "Groß"])
    relevant = st.multiselect("Relevant für", STUDIENGAENGE, default=["Alle"], key="relevant_fuer_neu")
    branche = st.text_input("Branche")
    website = st.text_input("Website")
    kontakt_email = st.text_input("Kontakt-E-Mail")
    telefonnummer = st.text_input("Telefonnummer")
    standort = st.text_input("Standort")
    kontakt_status = st.selectbox("Kontaktstatus", KONTAKTSTATUS)

    letzter_kontakt_input = st.date_input(
        "Letzter Kontakt",
        value=date.today(),
        key="kontakt_datum",
        disabled=(kontakt_status == "offen")
    )

    notizen = st.text_area("Notizen")

    if st.form_submit_button("Hinzufügen"):
        letzter_kontakt = (
            letzter_kontakt_input.isoformat()
            if kontakt_status != "offen"
            else None
        )
        relevant_str = ", ".join(relevant)  # Liste in kommagetrennten String umwandeln
        insert_unternehmen((
        name, groesse, relevant_str, branche, website, kontakt_email,
        telefonnummer, standort, letzter_kontakt, kontakt_status, notizen
        ))


        st.success("✅ Unternehmen hinzugefügt!")


# === Alle Unternehmen anzeigen ===
st.divider()
st.subheader("📊 Alle Unternehmen")

unternehmen = get_all_unternehmen()

# === Ausgabe ===
if unternehmen:
    df = pd.DataFrame(unternehmen, columns=[
        "ID", "Name", "Größe", "Relevanz", "Branche", "Website", "E-Mail",
        "Telefon", "Standort", "Letzter Kontakt", "Kontaktstatus", "Notizen"
    ])

    suchbegriff = st.text_input("🔍 Nach Studiengang in 'Relevanz' filtern")

    if suchbegriff:
        df = df[df["Relevanz"].str.contains(suchbegriff, case=False, na=False)]

    st.download_button(
        label="⬇️ Alle Unternehmen als CSV exportieren",
        data=df.to_csv(index=False),
        file_name="unternehmen_export.csv",
        mime="text/csv"
    )

    def highlight_status(row):
        return [status_farbe(row["Kontaktstatus"]) if col == "Kontaktstatus" else "" for col in df.columns]

    styled_df = df.style.apply(highlight_status, axis=1)
    st.write("📋 Farblich markiert nach Kontaktstatus:")
    st.dataframe(styled_df, use_container_width=True, hide_index=True)

else:
    st.info("Noch keine Einträge vorhanden.")


# === Bearbeiten & Löschen ===
st.divider()
st.subheader("🛠️ Eintrag bearbeiten oder löschen")

if unternehmen:
    unternehmen_liste = [(u[0], f"{u[1]} ({u[2]})") for u in unternehmen]
    auswahl_id = st.selectbox("Unternehmen auswählen", unternehmen_liste, format_func=lambda x: x[1])

    selected = next((u for u in unternehmen if u[0] == auswahl_id[0]), None)

    if selected:
        STUDIENGAENGE = [
            "Animation & Illustration", "Brandmanagement", "Business Management", "Design",
            "Eventmanagement", "Fashion Management", "Fußballmanagement", "Immobilienwirtschaft",
            "International/Business Management", "Journalismus", "Marketingmanagement",
            "Medien- und Kommunikationsdesign", "Medienmanagement", "Musikmanagement", "Psychologie",
            "Sportjournalismus", "Sportmanagement", "Technologie/Coding", "Wirtschaftspsychologie",
            "Brand Management (M.A.)", "Business Management (M.A.)", "Design Management (M.A.)",
            "Medien- und Kommunikationsmanagement (M.A.)"
        ]
        GROESSEN = ["Startup", "Klein", "Mittel", "Groß"]
        KONTAKTSTATUS = ["offen", "angeschrieben", "interessiert", "kein Interesse"]

        with st.form("bearbeiten_formular"):
            name = st.text_input("Name", selected[1])
            groesse = st.selectbox("Größe", GROESSEN, index=GROESSEN.index(selected[2]))

            # Sicherstellen, dass alle Werte in STUDIENGAENGE vorhanden sind
            relevant_vorbelegt = []
            if selected[3]:
                relevant_vorbelegt = [
                    eintrag.strip() for eintrag in selected[3].split(",")
                    if eintrag.strip() in STUDIENGAENGE
                ]

            relevant = st.multiselect(
                "Relevanz",
                options=STUDIENGAENGE,
                default=relevant_vorbelegt,
                key="relevant_bearbeiten"
            )

            branche = st.text_input("Branche", selected[4])
            website = st.text_input("Website", selected[5])
            email = st.text_input("E-Mail", selected[6])
            telefon = st.text_input("Telefonnummer", selected[7])
            standort = st.text_input("Standort", selected[8])
            kontakt_status = st.selectbox("Kontaktstatus", KONTAKTSTATUS,
                                          index=KONTAKTSTATUS.index(selected[10]))

            letzter_kontakt_input = None
            if kontakt_status != "offen":
                letzter_kontakt_input = st.date_input(
                    "Letzter Kontakt",
                    value=date.fromisoformat(selected[9]) if selected[9] else date.today(),
                    key="kontakt_datum_bearbeiten"
                )

            notizen = st.text_area("Notizen", selected[11])

            col1, col2 = st.columns(2)
            if col1.form_submit_button("📏 Änderungen speichern"):
                letzter_kontakt = letzter_kontakt_input.isoformat() if letzter_kontakt_input else None
                from database import update_unternehmen
                relevant_str = ", ".join(relevant)
                update_unternehmen((
                    name, groesse, relevant_str, branche, website, email,
                    telefon, standort, letzter_kontakt, kontakt_status,
                    notizen, selected[0]
                ))
                st.success("✅ Änderungen gespeichert.")
                st.rerun()

            if col2.form_submit_button("🗑️ Eintrag löschen"):
                from database import delete_unternehmen
                delete_unternehmen(selected[0])
                st.warning("🗑️ Eintrag gelöscht.")
                st.rerun()


# === E-Mail Generator ===
# - Template dynamisch gefüllt
# - Nutzer gibt Name & E-Mail an
# - Text kann kopiert werden
st.divider()
st.subheader("📧 E-Mail-Template für Kontaktaufnahme")

if unternehmen:
    unternehmen_liste_email = [(u[0], f"{u[1]} ({u[2]})") for u in unternehmen]
    auswahl_email = st.selectbox("Unternehmen auswählen für E-Mail", unternehmen_liste_email,
                                  format_func=lambda x: x[1], key="email-auswahl")
    selected_email = next((u for u in unternehmen if u[0] == auswahl_email[0]), None)

    if selected_email:
        absender_name = st.text_input("Dein Name", placeholder="Max Mustermann")
        absender_email = st.text_input("Deine E-Mail", placeholder="max@macromatch.de")

        betreff = "Gemeinsam Zukunft gestalten: Kooperation mit der Hochschule Macromedia"
        text = f"""Sehr geehrte Damen und Herren,

im Rahmen des Projekts **Studentische Inititiative** an der Hochschule Macromedia vernetzen wir engagierte Studierende mit innovativen Unternehmen aus der Region – wie {selected_email[1]}.

Studierende aus dem Bereich „{selected_email[3]}“ suchen nach praxisnahen Kooperationsmöglichkeiten – sei es in Form von Projektarbeiten, Fallstudien oder kreativen Challenges, bei denen beide Seiten voneinander profitieren.

Wir glauben, dass {selected_email[1]} und unsere Hochschule inhaltlich sehr gut zusammenpassen und möchten Sie herzlich einladen, mehr über die Vorteile einer Zusammenarbeit zu erfahren:

🔗 Partnerseite:  
https://www.macromedia-fachhochschule.de/en/lp/become-a-macromedia-partner/

Gerne stehe ich für Rückfragen oder ein persönliches Kennenlernen zur Verfügung.

Ich freue mich auf Ihre Rückmeldung!

Mit besten Grüßen  
{absender_name}  
{absender_email}"""

        st.code(f"Betreff: {betreff}\n\n{text}", language="markdown")
        st.button("📋 In Zwischenablage kopieren", on_click=lambda: st.toast("📄 Bitte manuell kopieren mit ⌘+C oder Symbol oben rechts."))

# === Statistikbereich ===
# - Auswertung nach Größe, Studiengang, Kontaktstatus
# - Darstellung mit Bar-Charts (Plotly & Streamlit)
st.divider()
st.subheader("📈 Statistiken")

if unternehmen:
    df = pd.DataFrame(unternehmen, columns=[
        "ID", "Name", "Größe", "Relevanz", "Branche", "Website", "E-Mail",
        "Telefon", "Standort", "Letzter Kontakt", "Kontaktstatus", "Notizen"
    ])

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### Unternehmen nach Größe")
        groesse_count = df["Größe"].value_counts().reset_index()
        groesse_count.columns = ["Größe", "Anzahl"]
        st.bar_chart(groesse_count.set_index("Größe"))

    with col2:
        st.markdown("#### Unternehmen nach Studiengang")

        # Leere Liste vorbereiten für alle Studiengänge
        statistik_df = pd.DataFrame({
            "Studiengang": STUDIENGAENGE[1:],  # ohne "Alle"
            "Anzahl": [df["Relevanz"].str.contains(sg, case=False, na=False).sum() for sg in STUDIENGAENGE[1:]]
        }).set_index("Studiengang")

        st.bar_chart(statistik_df)

    kontakt_count = df["Kontaktstatus"].value_counts().reset_index()
    kontakt_count.columns = ["Kontaktstatus", "Anzahl"]
    fig = px.bar(kontakt_count, x="Kontaktstatus", y="Anzahl",
                 title="Unternehmen nach Kontaktstatus",
                 labels={"Kontaktstatus": "Kontaktstatus", "Anzahl": "Anzahl"},
                 color="Kontaktstatus")
    st.plotly_chart(fig, use_container_width=True)

else:
    st.info("Noch keine Daten vorhanden für die Statistik.")
