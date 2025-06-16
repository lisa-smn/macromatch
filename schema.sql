DROP TABLE IF EXISTS unternehmen;

CREATE TABLE IF NOT EXISTS unternehmen (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,  -- 🔒 Name darf nur einmal vorkommen
    groesse TEXT CHECK(groesse IN ('Startup', 'Klein', 'Mittel', 'Groß')) NOT NULL,
    relevant_fuer TEXT NOT NULL,
    branche TEXT,
    website TEXT,
    kontakt_email TEXT,
    telefonnummer TEXT,
    standort TEXT,
    letzter_kontakt DATE,
    kontakt_status TEXT CHECK(kontakt_status IN ('offen', 'angeschrieben', 'interessiert', 'kein Interesse')) DEFAULT 'offen',
    notizen TEXT
);
