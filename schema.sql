CREATE TABLE IF NOT EXISTS unternehmen (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    groesse TEXT CHECK(groesse IN ('Startup', 'Klein', 'Mittel', 'Groß')) NOT NULL,
    relevant_fuer TEXT CHECK(relevant_fuer IN (
    'International/Business', 'Technologie/Coding', 'Beide',
    'Animation & Illustration', 'Brandmanagement', 'Business Management',
    'Design', 'Eventmanagement', 'Fashion Management', 'Fußballmanagement',
    'Immobilienwirtschaft', 'Journalismus', 'Marketingmanagement',
    'Medien- und Kommunikationsdesign', 'Medienmanagement', 'Musikmanagement',
    'Sportjournalismus', 'Sportmanagement', 'Wirtschaftspsychologie',
    'Psychologie', 'Brand Management (M.A.)', 'Business Management (M.A.)',
    'Design Management (M.A.)', 'Medien- und Kommunikationsmanagement (M.A.)'
    )) NOT NULL,
    branche TEXT,
    website TEXT,
    kontakt_email TEXT,
    telefonnummer TEXT,
    standort TEXT,
    letzter_kontakt DATE,
    kontakt_status TEXT CHECK(kontakt_status IN ('offen', 'angeschrieben', 'interessiert', 'kein Interesse')) DEFAULT 'offen',
    notizen TEXT
);
