"""Site public Asociația Nicolaus -- Flask + SQLite.
Structura si deciziile sunt in JURNAL_Brosura_si_Site.md, un nivel mai sus."""
import functools
import re
import sqlite3
import time
import unicodedata
from datetime import datetime
from pathlib import Path

from flask import Flask, g, redirect, render_template, request, session, url_for, flash, abort
from werkzeug.security import check_password_hash, generate_password_hash
from PIL import Image, ImageOps

import config

app = Flask(__name__)
app.config.from_object(config)

IDENTITATE = {
    "denumire": "Asociația Nicolaus",
    "adresa": "Sat Satu Nou, Com. Belcești, Jud. Iași",
    "cif": "31450986",
    "iban": "RO65 BRDE 240S V300 9000 2400",
    "nr_registru": "1027/A/2013",
    "nr_registru_special": "519/239/2013",
    "instanta": "Judecătoria Hârlău",
    "data_inregistrare": "13.04.2013",
    "telefon": "0723 339081",
    "email_contact": "mihai.pavaluc@asociatianicolaus.ro",
    "facebook": "https://www.facebook.com/asociatianicolaus/",
}


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(config.DB_PATH)
        g.db.row_factory = sqlite3.Row
    return g.db


@app.teardown_appcontext
def close_db(exc=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()


@app.context_processor
def inject_globals():
    return {
        "identitate": IDENTITATE,
        "app_version": config.APP_VERSION,
        "an_curent": datetime.now().year,
    }


def login_necesar(view):
    @functools.wraps(view)
    def wrapped(*args, **kwargs):
        if not session.get("admin_user"):
            return redirect(url_for("admin_login", next=request.path))
        return view(*args, **kwargs)
    return wrapped


# ---------- pagini publice ----------

@app.route("/")
def acasa():
    ultimele = get_db().execute(
        "SELECT * FROM jurnal_intrari ORDER BY id DESC LIMIT 3"
    ).fetchall()
    return render_template("index.html", ultimele=ultimele, continut=get_continut())


@app.route("/proiectul")
def proiectul():
    return render_template("proiectul.html", continut=get_continut())


@app.route("/jurnal-de-santier")
def santier():
    # filtrarea pe categorie s-a mutat pe client (JS), ca sa functioneze si pe exportul static --
    # ruta intoarce mereu toate intrarile, la fel ca Galeria.
    intrari = get_db().execute("SELECT * FROM jurnal_intrari ORDER BY id DESC").fetchall()
    return render_template("santier.html", intrari=intrari)


@app.route("/galerie")
def galerie():
    return render_template("galerie.html")


@app.route("/cum-ajuti")
def cum_ajuti():
    return render_template("cum_ajuti.html")


@app.route("/transparenta")
def transparenta():
    return render_template("transparenta.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        nume = request.form.get("nume", "").strip()
        email = request.form.get("email", "").strip()
        mesaj = request.form.get("mesaj", "").strip()
        # anti-spam: camp-capcana (honeypot) -- daca e completat, e un bot
        capcana = request.form.get("website", "").strip()
        # anti-spam: time-trap -- respingem trimiterile facute in sub 3 secunde de la incarcarea paginii
        incarcat_la = request.form.get("incarcat_la", "")
        prea_rapid = False
        try:
            prea_rapid = (time.time() - float(incarcat_la)) < 3
        except ValueError:
            prea_rapid = True
        gdpr_bifat = request.form.get("gdpr") == "on"
        if capcana or prea_rapid:
            # raspundem ca si cum ar fi mers, ca sa nu dam indicii unui bot
            flash("Mulțumim! Am primit mesajul și revenim cât de curând.", "succes")
            return redirect(url_for("contact"))
        if not nume or not email or not mesaj:
            flash("Completează toate câmpurile, te rog -- lipsește ceva.", "eroare")
        elif not gdpr_bifat:
            flash("Trebuie să bifezi acordul de prelucrare a datelor, ca să putem răspunde.", "eroare")
        else:
            get_db().execute(
                "INSERT INTO mesaje_contact (nume, email, mesaj) VALUES (?,?,?)",
                (nume, email, mesaj),
            )
            get_db().commit()
            flash("Mulțumim! Am primit mesajul și revenim cât de curând.", "succes")
            return redirect(url_for("contact"))
    return render_template("contact.html", acum=time.time())


@app.route("/confidentialitate")
def confidentialitate():
    return render_template("confidentialitate.html")


@app.route("/cookies")
def cookies():
    return render_template("cookies.html")


@app.errorhandler(404)
def pagina_lipsa(e):
    return render_template("404.html"), 404


# ---------- zona de administrare ----------

@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        parola = request.form.get("parola", "")
        rand = get_db().execute(
            "SELECT * FROM admin_users WHERE username = ?", (username,)
        ).fetchone()
        if rand and check_password_hash(rand["password_hash"], parola):
            session.clear()
            session["admin_user"] = username
            return redirect(request.args.get("next") or url_for("admin_santier"))
        flash("Utilizator sau parolă greșită.", "eroare")
    return render_template("admin/login.html")


@app.route("/admin/logout")
def admin_logout():
    session.clear()
    return redirect(url_for("admin_login"))


def slugifica(text):
    """Transforma un titlu romanesc intr-un nume de fisier simplu, fara diacritice."""
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = re.sub(r"[^a-zA-Z0-9]+", "-", text).strip("-").lower()
    return text[:40] or "poza"


def proceseaza_si_salveaza_foto(fisier, prefix):
    """Redimensioneaza, elimina EXIF/GPS si salveaza o poza incarcata din admin.
    Returneaza calea relativa (pentru foto_path) sau None daca nu s-a incarcat nimic."""
    if not fisier or not fisier.filename:
        return None
    imagine = Image.open(fisier)
    imagine = ImageOps.exif_transpose(imagine).convert("RGB")
    max_latime = 1600
    if imagine.width > max_latime:
        h = int(imagine.height * (max_latime / imagine.width))
        imagine = imagine.resize((max_latime, h), Image.LANCZOS)
    nume = f"{prefix}-{int(time.time())}-{slugifica(prefix)}.jpg"
    cale_disc = Path(app.static_folder) / "img" / nume
    imagine.save(cale_disc, "JPEG", quality=82, optimize=True)
    return f"img/{nume}"


def salveaza_foto_jurnal(fisier, titlu):
    return proceseaza_si_salveaza_foto(fisier, "jurnal")


def get_continut():
    """Blocurile de continut editabile din Proiectul si Acasa, indexate dupa cheie."""
    randuri = get_db().execute("SELECT * FROM continut_editabil").fetchall()
    return {r["cheie"]: r for r in randuri}


@app.route("/admin/santier", methods=["GET", "POST"])
@login_necesar
def admin_santier():
    if request.method == "POST":
        titlu = request.form.get("titlu", "").strip()
        data_eveniment = request.form.get("data_eveniment", "").strip()
        categorie = request.form.get("categorie", "Constructie")
        text = request.form.get("text", "").strip()
        if titlu and data_eveniment and text:
            foto_path = None
            try:
                foto_path = salveaza_foto_jurnal(request.files.get("foto"), titlu)
            except Exception:
                flash("Intrarea a fost salvata, dar poza nu a putut fi procesata (verifica ca e o imagine valida).", "eroare")
            get_db().execute(
                "INSERT INTO jurnal_intrari (titlu, data_eveniment, categorie, text, foto_path) VALUES (?,?,?,?,?)",
                (titlu, data_eveniment, categorie, text, foto_path),
            )
            get_db().commit()
            flash("Intrare adăugată.", "succes")
        else:
            flash("Completează titlu, dată și text.", "eroare")
        return redirect(url_for("admin_santier"))
    intrari = get_db().execute("SELECT * FROM jurnal_intrari ORDER BY id DESC").fetchall()
    return render_template("admin/santier.html", intrari=intrari)


@app.route("/admin/santier/<int:intrare_id>/sterge", methods=["POST"])
@login_necesar
def admin_santier_sterge(intrare_id):
    get_db().execute("DELETE FROM jurnal_intrari WHERE id = ?", (intrare_id,))
    get_db().commit()
    flash("Intrare ștearsă.", "succes")
    return redirect(url_for("admin_santier"))


@app.route("/admin/continut", methods=["GET", "POST"])
@login_necesar
def admin_continut():
    chei_valide = {"tronson1", "tronson2", "tronson3", "biserica", "acasa_hero"}
    if request.method == "POST":
        cheie = request.form.get("cheie", "")
        if cheie not in chei_valide:
            abort(400)
        titlu = request.form.get("titlu", "").strip() or None
        text = request.form.get("text", "").strip() or None
        try:
            foto_path_noua = proceseaza_si_salveaza_foto(request.files.get("foto"), cheie)
        except Exception:
            flash("Textul a fost salvat, dar poza nu a putut fi procesată (verifică să fie o imagine validă).", "eroare")
            foto_path_noua = None
        if foto_path_noua:
            get_db().execute(
                "UPDATE continut_editabil SET titlu=?, text=?, foto_path=? WHERE cheie=?",
                (titlu, text, foto_path_noua, cheie),
            )
        else:
            get_db().execute(
                "UPDATE continut_editabil SET titlu=?, text=? WHERE cheie=?",
                (titlu, text, cheie),
            )
        get_db().commit()
        flash("Conținut actualizat.", "succes")
        return redirect(url_for("admin_continut"))
    return render_template("admin/continut.html", continut=get_continut())


@app.route("/admin/schimba-parola", methods=["GET", "POST"])
@login_necesar
def admin_schimba_parola():
    if request.method == "POST":
        parola_curenta = request.form.get("parola_curenta", "")
        parola_noua = request.form.get("parola_noua", "")
        parola_noua_confirmare = request.form.get("parola_noua_confirmare", "")
        rand = get_db().execute(
            "SELECT * FROM admin_users WHERE username = ?", (session["admin_user"],)
        ).fetchone()
        if not rand or not check_password_hash(rand["password_hash"], parola_curenta):
            flash("Parola curentă e greșită.", "eroare")
        elif len(parola_noua) < 8:
            flash("Parola nouă trebuie să aibă cel puțin 8 caractere.", "eroare")
        elif parola_noua != parola_noua_confirmare:
            flash("Parola nouă și confirmarea nu coincid.", "eroare")
        else:
            get_db().execute(
                "UPDATE admin_users SET password_hash = ? WHERE username = ?",
                (generate_password_hash(parola_noua), session["admin_user"]),
            )
            get_db().commit()
            flash("Parola a fost schimbată.", "succes")
            return redirect(url_for("admin_santier"))
    return render_template("admin/schimba-parola.html")


if __name__ == "__main__":
    app.run(debug=True, port=5050)
