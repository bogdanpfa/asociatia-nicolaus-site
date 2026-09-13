"""Creează tabelele (dacă nu există) și seedează câteva intrări reale de jurnal.
Sigur de rulat de mai multe ori — nu duplică datele și nu șterge nimic existent."""
import sqlite3
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from config import DB_PATH

SCHEMA = """
CREATE TABLE IF NOT EXISTS jurnal_intrari (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titlu TEXT NOT NULL,
    data_eveniment TEXT NOT NULL,   -- text liber, ex: "Iulie 2019"
    categorie TEXT NOT NULL,        -- Constructie | Biserica | Evenimente
    text TEXT NOT NULL,
    foto_path TEXT,
    creat_la TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS mesaje_contact (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nume TEXT NOT NULL,
    email TEXT NOT NULL,
    mesaj TEXT NOT NULL,
    citit INTEGER NOT NULL DEFAULT 0,
    creat_la TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS admin_users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL
);
"""

SEED = [
    ("Sfințirea crucii", "Iulie 2019", "Evenimente",
     "Sfințirea crucii de pe locul viitorului așezământ, cu tot satul Satu Nou alături.", None),
    ("Montarea acoperișurilor", "2025", "Constructie",
     "Cele trei corpuri de clădire, acoperite integral — vedere aeriană asupra șantierului.", None),
    ("Pictura bisericii", "Iulie 2026", "Biserica",
     "Primele fresce în naos — pictura interioară a ajuns la aproximativ 30%.", None),
]

def main():
    con = sqlite3.connect(DB_PATH)
    con.executescript(SCHEMA)
    (n,) = con.execute("SELECT COUNT(*) FROM jurnal_intrari").fetchone()
    if n == 0:
        con.executemany(
            "INSERT INTO jurnal_intrari (titlu, data_eveniment, categorie, text, foto_path) VALUES (?,?,?,?,?)",
            SEED,
        )
        print(f"Seedate {len(SEED)} intrări reale în jurnalul de șantier.")
    else:
        print(f"jurnal_intrari are deja {n} intrări — nu ating nimic.")
    con.commit()
    con.execute("PRAGMA integrity_check")
    con.close()
    print("Baza de date e gata:", DB_PATH)

if __name__ == "__main__":
    main()
