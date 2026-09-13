"""Exporta site-ul Flask ca fisiere HTML statice, pentru GitHub Pages.

De ce exista acest script: gazduirea Romarg/pandapc.ro nu suporta Python (doar
PHP), asa ca site-ul public nu poate rula Flask live acolo. Solutia: Bogdan
continua sa lucreze exact ca acum, local, cu Flask + /admin ca sa adauge
poze/articole -- iar acest script "inghiata" rezultatul in fisiere HTML pure,
gata de urcat pe GitHub Pages (gratuit, suporta orice tip de continut static).

Rulare:  python scripts/export_static.py
Rezultat: folderul docs/ , gata de "git add . && git commit && git push".
(docs/ nu e intamplator -- e folderul pe care GitHub Pages il poate servi
direct din branch-ul main, fara pasi suplimentari de configurare/CI.)

IMPORTANT inainte de prima publicare: completeaza FORMSPREE_ID mai jos cu
ID-ul real, dupa ce Bogdan isi face cont gratuit pe https://formspree.io si
creeaza un formular nou (Settings -> ai un URL de forma
https://formspree.io/f/xxxxabcd -- partea de dupa /f/ e ID-ul).
"""
import shutil
import sys
from pathlib import Path

SITE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SITE_DIR))

# TODO Bogdan: inlocuieste cu ID-ul real de la formspree.io dupa ce iti faci cont.
FORMSPREE_ID = "PUNE_AICI_ID_FORMSPREE"

# Domeniul pentru fisierul CNAME (necesar de GitHub Pages ca sa stie ce domeniu
# propriu sa serveasca). Lasa gol ("") daca inca nu vrei sa legi domeniul.
DOMENIU = "asociatianicolaus.ro"

DIST_DIR = SITE_DIR / "docs"

# rute publice simple: (ruta_flask, nume_folder_in_dist)
# "" inseamna radacina (index.html chiar in dist/)
RUTE = [
    ("/", ""),
    ("/proiectul", "proiectul"),
    ("/jurnal-de-santier", "jurnal-de-santier"),
    ("/galerie", "galerie"),
    ("/cum-ajuti", "cum-ajuti"),
    ("/transparenta", "transparenta"),
    ("/confidentialitate", "confidentialitate"),
    ("/cookies", "cookies"),
]


def scrie_pagina(continut_html, folder_relativ):
    tinta = DIST_DIR if not folder_relativ else DIST_DIR / folder_relativ
    tinta.mkdir(parents=True, exist_ok=True)
    (tinta / "index.html").write_text(continut_html, encoding="utf-8")


def main():
    import app as appmod  # importa aplicatia Flask reala, cu toate rutele si contextul ei

    if DIST_DIR.exists():
        shutil.rmtree(DIST_DIR)
    DIST_DIR.mkdir(parents=True)

    client = appmod.app.test_client()

    esuate = []
    for ruta, folder in RUTE:
        r = client.get(ruta)
        if r.status_code != 200:
            esuate.append((ruta, r.status_code))
            continue
        scrie_pagina(r.get_data(as_text=True), folder)
        print(f"OK  {ruta:28s} -> {'index.html' if not folder else folder + '/index.html'}")

    # pagina de contact -- varianta statica, randata direct (nu prin ruta /contact,
    # care presupune un server Flask ce nu va mai exista pe gazduire)
    if FORMSPREE_ID == "PUNE_AICI_ID_FORMSPREE":
        print("\n⚠️  ATENTIE: FORMSPREE_ID nu e completat inca -- formularul de contact")
        print("   nu va trimite nimic pana nu pui ID-ul real in scripts/export_static.py.\n")
    with appmod.app.test_request_context("/contact"):
        from flask import render_template
        continut = render_template("contact_static.html", formspree_id=FORMSPREE_ID)
    scrie_pagina(continut, "contact")
    print(f"OK  /contact (static)          -> contact/index.html")

    # 404 -- GitHub Pages foloseste automat un fisier 404.html din radacina
    with appmod.app.test_request_context("/pagina-inexistenta"):
        from flask import render_template
        continut_404 = render_template("404.html")
    (DIST_DIR / "404.html").write_text(continut_404, encoding="utf-8")
    print("OK  404                        -> 404.html")

    # fisierele statice (css/js/img)
    static_sursa = SITE_DIR / "static"
    static_tinta = DIST_DIR / "static"
    if static_sursa.exists():
        shutil.copytree(static_sursa, static_tinta)
        print(f"OK  static/ copiat ({sum(1 for _ in static_tinta.rglob('*') if _.is_file())} fisiere)")

    # .nojekyll -- ii spune lui GitHub Pages sa nu proceseze fisierele ca Jekyll
    (DIST_DIR / ".nojekyll").write_text("", encoding="utf-8")

    # CNAME -- necesar pentru domeniul propriu pe GitHub Pages
    if DOMENIU:
        (DIST_DIR / "CNAME").write_text(DOMENIU + "\n", encoding="utf-8")
        print(f"OK  CNAME -> {DOMENIU}")

    if esuate:
        print("\n‼️  Rute care NU s-au exportat corect:")
        for ruta, cod in esuate:
            print(f"   {ruta} -> HTTP {cod}")
        sys.exit(1)

    print(f"\nGata. Fisierele sunt in {DIST_DIR}")
    print("Urmatorul pas: git add . && git commit -m \"...\" && git push")


if __name__ == "__main__":
    main()
