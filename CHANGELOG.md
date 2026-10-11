# Changelog — site asociatianicolaus.ro

Format: [Keep a Changelog](https://keepachangelog.com/ro/), română.

## [0.3.5] — 2026-10-11

### Schimbat
- Partenerul STIZO NPC SRL: descrierea devine „Sponsor și executant al structurii așezământului: pereți, stâlpi, grinzi, acoperiș și învelitoarea din tablă zincată." — firma a și sponsorizat, a și lucrat (precizare de la Bogdan; corectează formularea „contra cost" din 0.3.4). Adăugat website-ul `https://stizo-npc.ro`, deci numele partenerului e acum link. Modificat pe o copie a bazei (`PRAGMA integrity_check` = ok), apoi copiat înapoi.
- `APP_VERSION` 0.3.4 → 0.3.5.

### De făcut / în așteptare
- `stizo-npc.ro` nu e încă online (se populează în curând) — până atunci linkul din pagina Parteneri duce la o adresă care nu răspunde. Verificăm după lansarea site-ului firmei.
- Sumele sponsorizate nu sunt menționate nicăieri (nici în revistă, nici pe site); de decis dacă vrem să le publicăm și cu acordul firmei.
- Decizie rămasă de la 0.3.4: dacă pagina „Parteneri" să aibă secțiuni separate (sponsori / executanți).

## [0.3.4] — 2026-10-11

### Adăugat
- Primul partener pe pagina „Parteneri": **STIZO NPC SRL** (CIF RO26873840, Iași) — firma care a executat structura așezământului (pereți, stâlpi, grinzi, acoperiș și învelitoarea din tablă zincată), contra cost. Rând nou în tabelul `parteneri` (inserat pe o copie a bazei, `PRAGMA integrity_check` = ok, apoi copiat înapoi conform protocolului), cu sigla în `static/img/parteneri/stizo-npc-srl.png`.
- Sigla a fost pregătită din imaginea primită: fundalul gri eliminat (fundal transparent), decupată pe conținut, 389×391 px — acceptabilă pentru cardul din pagină; nu s-a modificat conținutul grafic.

### Schimbat
- `APP_VERSION` 0.3.3 → 0.3.4.

### De făcut / în așteptare
- Site-ul firmei (stizo-npc.ro) nu e încă online — câmpul „website" a rămas gol, deci numele partenerului nu e link. Când site-ul apare: Admin → Parteneri → Editează → completează „website".
- Pagina „Parteneri" folosește formularea „sprijinul lor" pentru toți partenerii; STIZO a lucrat contra cost. Formularea de pe pagină rămâne neschimbată, dar descrierea partenerului spune doar „a executat" (fără „sponsor"). De decis dacă vrem o secțiune separată pentru executanți.
- Anul sfințirii crucii (2018/2019) — vezi 0.3.3.
- Publicare: `2-publica-pe-site.bat` (regenerează `docs/`, include noua pagină Parteneri și sigla).

## [0.3.3] — 2026-10-05

### Adăugat
- Pagina Proiectul, secțiune nouă **„Etapă cu etapă — ce s-a realizat, an cu an"**: cronologia din revista A4 (2013 înființarea → 2015–2018 proiect de execuție, avize, autorizații → 2019 sfințirea crucii, piatra de temelie, săpături la fundație → 2021–2024 zidărie, biserică, învelitoare din tablă zincată, tâmplărie, pictură → 2025–2026 pauză din lipsă de fonduri, cu stadiul actual). Plasată între „Stadiul lucrării, pe tronsoane" și „Ce mai lipsește până la deschidere". Stil nou `.cronologie` în `static/css/style.css` (an în auriu, rândul „2025–2026" în ton mai stins; pe telefon anul trece deasupra textului).
- Pagina Proiectul, secțiune nouă **„Hrană din pământul de alături"**: terenul agricol de 7 ha (legume și cereale), cu aceeași formulare ca în revista A4 (pagina 12).

### Schimbat
- `APP_VERSION` 0.3.2 → 0.3.3.

### De făcut / în așteptare
- Anul sfințirii crucii: cronologia folosește deocamdată **2019** (ca în rândul „01.07.2019" din revistă). Când Bogdan hotărăște 2018 sau 2019, se aliniază simultan cronologia, intrarea din Jurnal, legendele din Galerie, „Din 2019…" de pe Acasă și revista.

## [0.3.2] — 2026-10-05

Aliniere a site-ului cu revista A4 „Nicolaus 2026" (ediția cu modificările din 27 sept. – 5 oct.). Sursa cifrelor: Bogdan — capacitatea reală este de 48 de paturi, nu 50.

### Corectat
- Capacitatea așezământului: „50 de persoane/locuri" → **48** peste tot unde apărea — pagina Acasă (text de prezentare + cifra „locuri la deschidere"), pagina Proiectul (titlul „…un cămin pentru 48 de oameni", paragraful de introducere și cardul „Mobilier — pentru 48 de persoane") și meta-descrierea comună din `base.html` (cea care apare în rezultatele Google și la previzualizarea link-ului pe Facebook/WhatsApp).
- Textul cardului „Tronson I" (conținut editabil din admin): „uși și ferestre **montate**" → „uși și ferestre **realizate**" (formularea folosită și în revistă). Modificat direct în baza de date (`continut_editabil`, cheia `tronson1`), pe o copie, cu `PRAGMA integrity_check` = ok înainte de copiere înapoi.

### Adăugat
- Pagina Proiectul, secțiunea „Ce mai lipsește până la deschidere": cardul „Instalații termice" are acum și subtitlul „Încălzire și climatizare." (devizul din revistă prevede „instalații termice complete și climatizare").
- Pagina Proiectul, introducere: „spații adaptate persoanelor cu mobilitate redusă", alături de cabinetele medicale și zonele de recreere (cabinete medicale și zone de recreere erau deja menționate).

### Versiune
- `APP_VERSION` 0.3.1 → 0.3.2 (afișată în footer după publicare).

### De făcut / în așteptare
- **Anul sfințirii crucii** (2018 sau 2019 — decizia îi aparține lui Bogdan; același an trebuie folosit și în revistă): intrarea „Sfințirea crucii" din Jurnalul de șantier („Iulie 2019"), legendele din Galerie („Sfințirea crucii, iulie 2019", „Începutul șantierului, iulie 2019") și fraza „Din 2019, familia Păvăluc…" de pe Acasă. Neatinse în această versiune, pentru a nu introduce o dată greșită.
- Posibil de adăugat: cronologie pe ani pe pagina Proiectul (2013 înființare → 2015–2018 proiect de execuție, avize, autorizații → 2019 sfințirea crucii și piatra de temelie → … → 2025–2026 pauză din lipsă de fonduri), identică cu cea din revistă; plus mențiunea terenului agricol de 7 ha (legume și cereale).
- Publicare: rulează `2-publica-pe-site.bat` (regenerează `docs/`, face commit, `git pull`, `git push`). Folderul `docs/` local era rămas la v0.3.0 (exportul din 0.3.1 s-a publicat direct pe GitHub), deci un `git pull` poate semnala conflict pe câteva fișiere din `docs/` — în caz de conflict nu se rezolvă manual; se trimite mesajul.

## [0.3.1] — 2026-09-14

### Corectat
- Favicon lipsă la `/favicon.ico` (rădăcina site-ului) — link-ul `<link rel="icon">` din `<head>` era prezent și funcțional, dar multe browsere/unelte cer direct `/favicon.ico`, indiferent de tag-ul din HTML, și primeau 404. Generat un `.ico` multi-rezoluție (16/32/48/64/128/256px) din logo, servit acum atât din Flask (rută nouă `/favicon.ico`) cât și din exportul static pentru GitHub Pages. `static/img/favicon.png` redus de la 512×512/234KB la 192×192/44KB (era supradimensionat pentru un favicon).
- „Enforce HTTPS” activat în setările GitHub Pages — certificatul HTTPS exista deja și funcționa la accesare directă cu `https://`, dar vizitatorii care scriau `http://asociatianicolaus.ro` nu erau redirecționați automat. Acum orice acces pe `http://` sare automat pe `https://`.

## [0.3.0] — 2026-09-14

### Adăugat
- Logo-ul asociației (furnizat de Bogdan, format Canva) în antetul fiecărei pagini, lângă numele „Asociația Nicolaus", plus favicon în tab-ul browserului — pregătite din logo prin eliminarea fundalului alb (transparență) și decupare automată pe conținut.
- Pagină publică nouă „Parteneri" (`/parteneri`) — afișează firmele/instituțiile partenere: logo (sau inițiala numelui, dacă nu are logo încărcat), nume (link către website, dacă există), descriere scurtă a sprijinului și CIF. Stare goală tratată explicit („Lista e goală, deocamdată" + îndemn de a deveni partener), nu pagină albă.
- Secțiune nouă de administrare „Parteneri" (`/admin/parteneri`) — adaugă, editează și șterge parteneri, cu upload de logo (procesat separat de pozele din jurnal: păstrează transparența PNG, nu mai convertim la JPEG) și un comutator „afișat pe site" ca să poți ascunde temporar un partener fără să-l ștergi.
- Tabelul `parteneri` în baza de date (nume, cif, website, descriere, logo_path, ordine, activ) — migrat pe baza reală, cu backup înainte de scriere, conform protocolului.
- `scripts/init_db.py` completat cu tabelul `continut_editabil` (lipsea din schema scriptului, deși există deja în baza reală — o instalare nouă de la zero ar fi eșuat la /admin/continut) și cu tabelul `parteneri`, plus rândurile inițiale (seed) pentru cele 5 chei de conținut editabil.
- Ruta `/parteneri` adăugată în `scripts/export_static.py`, pentru ca pagina să fie inclusă la exportul static pentru GitHub Pages.

### Corectat
- `FORMSPREE_ID` din `scripts/export_static.py` era încă placeholder-ul („PUNE_AICI_ID_FORMSPREE") în copia locală, deși fusese completat direct pe GitHub (id real: `mzeblapg`) după ce formularul de contact a picat cu „Form not found" la primul test. Sincronizat acum și local, ca exporturile viitoare să nu mai regreseze la ID-ul greșit.

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
