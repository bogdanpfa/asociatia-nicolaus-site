# Changelog — site asociatianicolaus.ro

Format: [Keep a Changelog](https://keepachangelog.com/ro/), română.

## [0.2.3] — 2026-09-13

### Schimbat
- Folderul de lucru al site-ului mutat de Bogdan din Dropbox în OneDrive (`Documente\! Claude!\Siteuri create\AsociatiaNicolaus.ro`) — motivul: blocajele repetate „disk I/O error" pe `instance/nicolaus.db` cauzate de sincronizarea Dropbox (vezi notele din v0.2.1 și v0.2.2). Toate fișierele (cod, poze, bază de date) au fost regăsite intacte la noua locație.

### Adăugat — pregătire pentru găzduire (romarg, cPanel)
- `passenger_wsgi.py` — punctul de intrare WSGI cerut de cPanel/Phusion Passenger pentru aplicații Python. La crearea aplicației din „Setup Python App" în cPanel, acest fișier înlocuiește stub-ul generat automat.
- `requirements.txt` completat cu `Pillow>=10.0` — lipsea, deși `app.py` îl folosește direct (redimensionare poze, eliminare EXIF/GPS la upload). Fără el, `pip install` pe server nu ar fi instalat Pillow și orice încărcare de poză din admin ar fi picat cu eroare la primul upload.

### Notă
- Deploy-ul propriu-zis (creare aplicație Python în cPanel, copiere fișiere, pip install, restart) nu s-a făcut încă — necesită acces la panoul cPanel, pe care nu îl accesăm cu parola lui Bogdan (politică fermă: nu introducem parole). Așteptăm ca Bogdan să se autentifice singur în Chrome, apoi continuăm din browser-ul deja autentificat.

## [0.2.2] — 2026-09-13

### Corectat
- Textul intrării „Sfințirea crucii" din jurnal, la cererea explicită a lui Bogdan: înlocuit cu „Săpături la fundație." (titlul și data rămân neschimbate).

### Notă tehnică importantă (urgent)
- Corecția de an 2025→2026 de la „Acoperișul tronsonului I" (v0.2.1) a fost găsită REVENITĂ la 2025 la verificarea ulterioară — Dropbox a resincronizat local o versiune veche a `nicolaus.db` peste modificarea făcută, la un moment nedeterminat după ce editarea fusese confirmată de trei ori. Am reaplicat corecția și am confirmat că ține după o pauză de 12 secunde, dar riscul de resincronizare silențioasă rămâne real și nu mai e doar teoretic. Recomandare fermă: exclude `site/instance/` din sincronizarea Dropbox (click dreapta pe folder → Ignore/Exclude) înainte de orice altă sesiune de editare a bazei de date — altfel orice modificare, a mea sau făcută de Bogdan din /admin, poate dispărea fără avertisment.

## [0.2.1] — 2026-09-13

### Adăugat
- Formularul 230 (redirecționare 3,5% din impozitul pe venit) — buton de lansare pe pagina „Cum ajuți", integrat prin scriptul de încorporare de la formular230.ro (cont deja legat de Bogdan la Asociația Nicolaus).
- Filtrare pe client (JS) pentru galerie — butoanele Toate/Construcție/Biserică/Evenimente/Aeriene erau doar decorative (`href="#"`), acum ascund/arată cardurile real, pe baza unei categorii atribuite fiecărei poze.

### Corectat
- Data intrării „Acoperișul tronsonului I" din jurnalul de șantier: 2025 → 2026 (era greșit, cele mai recente poze de șantier sunt din anul curent).
- Aceeași corecție de an pe două legende din Galerie (vedere de ansamblu, crucea de pe turlă).
- Legenda pozei cu Biblia din Galerie: „Carte de cult, folosită la slujbele de pe șantier" → „Biblia, folosită în timpul slujbei de sfințire a bisericii" (precizare de la Bogdan).

### Schimbat
- IBAN-ul de pe pagina „Cum ajuți" e acum într-un chenar vizibil, cu beneficiarul (Asociația Nicolaus) afișat explicit deasupra codului IBAN, mărit și îngroșat.

## [0.2.0] — 2026-09-12

### Adăugat
- Ecran nou de administrare, „Conținut Proiectul & Acasă" (`/admin/continut`) — Bogdan poate acum edita singur, fără cod: titlul și textul celor 4 carduri de pe Proiectul (Tronson I, Tronson II, Tronson III, Biserică) și poza fiecăruia, plus poza principală de pe Acasă.
- Tabelă nouă `continut_editabil` în baza de date — conținutul acestor blocuri nu mai e „turnat" în șabloane, ci vine din bază, la fel ca Jurnalul de șantier.

### Notă
- Rămân editabile doar din cod, deocamdată: textul de hero de pe Proiectul, secțiunile „Ce mai lipsește"/„Ce mai este nevoie", Galeria completă și datele de contact — Bogdan a ales să pornim cu sfera Proiectul + Acasă, cea mai frecvent schimbată.
- Când se înlocuiește o poză din acest ecran, fișierul vechi rămâne pe disc (neșters) — același comportament minor cunoscut ca la Jurnalul de șantier.

## [0.1.8] — 2026-09-12

### Adăugat
- Formular de schimbare a parolei de administrator (`/admin/schimba-parola`), accesibil din panoul de administrare — Bogdan își poate schimba singur parola de acum, fără să mai fie nevoie s-o schimb eu direct din bază de date.
- Link discret „Admin" în subsolul site-ului (devine „Administrare" când ești logat), pentru acces rapid la panou fără să mai fie nevoie să știi/tastezi adresa exactă.

### Schimbat
- Textul de subsol: „Site creat cu ajutorul AI de Pandapc.ro — proiect dezvoltat de Bogdan PĂVĂLUC" (înlocuiește formularea anterioară).

## [0.1.7] — 2026-09-12

### Adăugat
- Link către pagina de Facebook a asociației (facebook.com/asociatianicolaus), în subsol (cu iconiță) și pe pagina de Contact.

## [0.1.6] — 2026-09-12

### Adăugat
- Panou de administrare — poți acum încărca și poze la o intrare nouă din Jurnalul de șantier (`/admin/santier`), nu doar text. Se redimensionează automat și se elimină EXIF/GPS, la fel ca pozele integrate manual.
- Cont de administrator creat: utilizator `bogdan` (parola primită separat, în chat).

### Corectat
- Textul intrării „Sfințirea crucii" precizează acum că a avut loc chiar la momentul săpăturilor pentru fundație.

## [0.1.5] — 2026-09-12

### Adăugat
- Tronson III, în sfârșit — card propriu pe Proiectul (grid extins la 4 coloane), din al doilea lot de 15 poze noi trimise de Bogdan, verificate una câte una: fără persoane identificabile.
- Poza de hero pe Acasă înlocuită cu o vedere aeriană de ansamblu mult mai bună (toate tronsoanele + satul în fundal, fără watermark).
- Poza bisericii de pe Proiectul reînnoită cu o variantă mai recentă (2025) și mai clară.
- Mini-galerie „Mai multe poze — Tronson III și biserică" pe Proiectul, cu 4 fotografii suplimentare + link către galeria completă.
- 8 fotografii noi în Galeria principală (aeriene de ansamblu, curtea interioară, turla și crucea bisericii, prim-plan Tronson II).
- Descrieri vizibile sub fiecare poză din Galerie (nu doar text alternativ invizibil) — se vede clar ce reprezintă fiecare imagine.
- Lightbox: click pe orice fotografie din site (mai puțin harta) o mărește într-un pop-up, cu descrierea dedesubt.
- Buton flotant 🍪 permanent, pentru redeschiderea oricând a preferințelor de cookie-uri.
- Conținut real pe paginile Confidențialitate și Cookie-uri (erau schelete „de completat") — politică GDPR completă: ce date colectăm, de ce, cât le păstrăm, drepturile vizitatorului, ANSPDCP.
- Bifă de consimțământ GDPR pe formularul de contact, obligatorie la trimitere, cu link către politica de confidențialitate.
- Protecție anti-spam pe formular: câmp-capcană invizibil (honeypot) + respingere a trimiterilor făcute în sub 3 secunde de la încărcarea paginii.
- Rând de subsol: „Site dezvoltat cu ajutorul AI de PandaPC.ro — proiect al lui Bogdan Păvăluc".

### Corectat
- CIF-ul mutat pe rândul lui propriu în subsol, ca să nu se mai rupă la mijloc pe ecrane înguste.
- Copyright-ul din subsol acum spune explicit „© {an} Asociația Nicolaus", nu doar anul.

### Notă tehnică importantă
- Am găsit și reparat un jurnal SQLite orfan (`nicolaus.db-journal`) care bloca orice scriere/citire în baza de date montată prin Dropbox, cu eroare „disk I/O error". Cauza: SQLite are nevoie de blocare de fișiere (file locking) pe care unele foldere sincronizate prin Dropbox nu o oferă corect pe partajarea de rețea. Am validat separat, izolat, că formularul de contact (inclusiv anti-spam și GDPR) funcționează perfect corect — problema era strict de mediul local de testare, nu de cod. Recomandare: exclude folderul `instance/` din sincronizarea Dropbox (click dreapta → Ignore/Smart Sync), altfel riști să repeți blocajul ori de câte ori faci teste locale. Pe serverul real de găzduire (odată ce facem deploy), baza de date va sta pe disc local, fără acest risc.

## [0.1.4] — 2026-09-12

### Adăugat
- 20 de fotografii noi, curatoriate din 30 primite de la Bogdan cu denumiri exacte pe tronsoane/subiect (nu mai ghicim din arhiva generală) — folosite pe Tronson I, Tronson II, Biserică (exterior), aeriana de la „Montarea acoperișurilor" și 15+ poze noi în Galerie (fundație, cofraje, biserică în diverse etape, interioare la roșu).
- Terminologie „tronson" în loc de „corp" pe Proiectul, la cererea lui Bogdan.
- Harta de contact (Google Maps) — se încarcă abia la click pe buton, nu automat la deschiderea paginii, ca să nu tragem conținut de la Google înainte de o acțiune explicită a vizitatorului (cerință din skill-ul de site-uri de prezentare, secțiunea de consimțământ).

### Exclus
- „Slujba de sfințire.jpg" și „Lumânări.jpg" — persoane identificabile în cadru (fețe vizibile, chiar dacă parțial neclare la a doua). Nu se folosesc nicăieri.

### Corectat
- Poza aeriană folosită la intrarea „Montarea acoperișurilor" nu mai e cea ambiguă (posibil tronson III) — înlocuită cu o poză aeriană etichetată explicit de Bogdan.

## [0.1.3] — 2026-09-12

### Corectat
- Cardul „Corp I” de pe Proiectul afișa greșit fotografia aeriană generală (Bogdan a semnalat că, de fapt, arată tronsonul III) — revenit la placeholder până primim poza corectă, dedicată tronsonului I.

## [0.1.2] — 2026-09-12

### Adăugat
- Primele 4 fotografii reale din arhiva șantierului (`static/img/`): aeriană cu cele trei corpuri acoperite, frescă în lucru, sfințirea crucii (iulie 2019), șantier la început (iulie 2019). Toate redimensionate pentru web și fără date EXIF/GPS.
- Coloana `foto_path` din `jurnal_intrari` e acum folosită efectiv: intrările „Montarea acoperișurilor”, „Pictura bisericii” și „Sfințirea crucii” au poză reală; restul păstrează placeholder-ul de așteptare.
- Clasa CSS `.foto-card` pentru afișarea fotografiilor reale (object-fit: cover), păstrând dimensiunile placeholder-ului existent.

### Notă
- Nu s-au folosit fotografii din clusterul septembrie 2023 (eveniment religios în interior) — persoane clar identificabile, filigran personal. Exclus definitiv.

## [0.1.1] — 2026-09-12

### Corectat
- Cardurile din grile (Proiectul, Acasă) ieșeau din pagină pe ecrane late — cauza: comportamentul implicit al elementelor de grid CSS de a nu se micșora sub dimensiunea conținutului lor (`min-width:auto`), combinat cu blocurile foto cu `aspect-ratio`. Fix: `min-width:0` pe itemele de grid.
- Același bug producea suprapunerea de text de sub „Ultimele din șantier” — cardurile prea late împingeau imaginile prea înalte, care ieșeau peste conținutul de dedesubt.
- Butoanele din carduri erau întinse pe toată lățimea, inegal între carduri — acum au dimensiune naturală și se așază la baza cardului.

## [0.1.0] — 2026-09-12

### Adăugat
- Schelet Flask + SQLite pentru site-ul public, pe baza structurii stabilite în `JURNAL_Brosura_si_Site.md`.
- Opt pagini publice: Acasă, Proiectul, Jurnal de șantier (cu filtrare pe categorie), Galerie, Cum ajuți, Transparență, Contact (formular funcțional, salvează în DB), pagină 404.
- Politici Confidențialitate și Cookie-uri (conținut de completat — vezi paginile respective).
- Banner de consimțământ cookie-uri, granular (doar necesare / accept tot).
- Zonă de administrare (`/admin/login`) cu autentificare pe server (sesiune Flask, parolă hash) — adăugare și ștergere de intrări în jurnalul de șantier.
- Identitate vizuală: brun `#3D3025` / auriu `#C8871F` / crem `#FBF7EF`, Fraunces + Public Sans, mereu în variantă luminoasă (fără mod dark automat).
- Bază de date SQLite (`instance/nicolaus.db`) cu 3 intrări reale seedate în jurnalul de șantier.
- Identificare legală completă în footer, inclusiv nr. Registrul Asociațiilor și Fundațiilor (1027/A/2013, Judecătoria Hârlău, 13.04.2013).

### De făcut
- Fotografii reale (poze marcate „în curând" în tot site-ul).
- Trimitere reală de email pentru formularul de contact (acum doar salvează în DB) — necesită date SMTP de la romarg.
- Text final pentru Confidențialitate și Cookie-uri.
- PDF-uri reale pe pagina Transparență (act constitutiv, statut, dovadă ANAF).
- Poze membri + sigle parteneri.
- Găzduire pe romarg — de confirmat suport Python la deploy.
