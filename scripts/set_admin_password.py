"""Rulează asta local ca să creezi sau să schimbi parola de admin.
Nu punem nicio parolă implicită in cod -- o alegi tu, aici, interactiv."""
import getpass
import sqlite3
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from config import DB_PATH
from werkzeug.security import generate_password_hash

def main():
    username = input("Utilizator admin [mihai]: ").strip() or "mihai"
    pw1 = getpass.getpass("Parolă nouă: ")
    pw2 = getpass.getpass("Repetă parola: ")
    if pw1 != pw2:
        print("Parolele nu coincid. Nu am schimbat nimic.")
        return
    if len(pw1) < 8:
        print("Prea scurtă -- foloseste cel putin 8 caractere. Nu am schimbat nimic.")
        return
    con = sqlite3.connect(DB_PATH)
    con.execute(
        "INSERT INTO admin_users (username, password_hash) VALUES (?,?) "
        "ON CONFLICT(username) DO UPDATE SET password_hash=excluded.password_hash",
        (username, generate_password_hash(pw1)),
    )
    con.commit()
    con.close()
    print(f"Gata -- contul '{username}' poate intra acum in /admin/login.")

if __name__ == "__main__":
    main()
