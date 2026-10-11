@echo off
chcp 65001 >nul
REM ============================================================
REM  Publica pe asociatianicolaus.ro modificarile facute in admin.
REM  IMPORTANT: inchide mai intai fereastra neagra a serverului
REM  local (cea deschisa de "1-porneste-admin.bat"), altfel baza
REM  de date poate fi blocata in timpul exportului.
REM ============================================================

cd /d "%~dp0"

echo ============================================================
echo  Pasul 1/4 - Regeneram fisierele statice (docs\)...
echo ============================================================
python scripts\export_static.py
if errorlevel 1 (
    echo.
    echo EROARE la export! Nu continuam cu publicarea.
    echo Citeste mesajul de mai sus - daca nu-ti dai seama ce inseamna,
    echo trimite-l lui Claude.
    pause
    exit /b 1
)

echo.
echo ============================================================
echo  Pasul 2/4 - Pregatim si salvam modificarile (commit)...
echo ============================================================
git add -A

set MESAJ=
set /p MESAJ="Descriere scurta a modificarii (Enter = mesaj automat): "
if "%MESAJ%"=="" set MESAJ=Actualizare site - %date% %time%

git commit -m "%MESAJ%"
if errorlevel 1 (
    echo.
    echo Nu era nimic nou de salvat ^(nicio modificare^) sau a aparut o eroare.
    echo Daca ai facut o modificare si vezi mesajul asta, trimite-i captura lui Claude.
    pause
    exit /b 0
)

echo.
echo ============================================================
echo  Pasul 3/4 - Verificam daca mai sunt modificari pe GitHub...
echo ============================================================
git pull --no-rebase --no-edit
if errorlevel 1 (
    echo.
    echo ============================================================
    echo  ATENTIE: a aparut un conflict intre modificarile tale si
    echo  cele de pe GitHub. NU s-a trimis nimic inca - modificarile
    echo  tale sunt salvate in siguranta local ^(commit facut^).
    echo.
    echo  NU incerca sa rezolvi singur - trimite-i lui Claude mesajul
    echo  de mai sus si spune-i "conflict la publica-pe-site.bat".
    echo ============================================================
    pause
    exit /b 1
)

echo.
echo ============================================================
echo  Pasul 4/4 - Trimitem pe GitHub...
echo ============================================================
git push
if errorlevel 1 (
    echo.
    echo EROARE la trimitere pe GitHub! Poate fi nevoie sa te autentifici.
    echo Modificarile sunt salvate local ^(commit facut^) - nu s-a pierdut nimic.
    echo Reincearca, sau cere ajutorul lui Claude cu mesajul de eroare de mai sus.
    pause
    exit /b 1
)

echo.
echo ============================================================
echo  Gata! Modificarile au fost trimise.
echo  GitHub Pages le publica automat in 1-3 minute.
echo  Verifica pe https://asociatianicolaus.ro/ dupa cateva minute.
echo ============================================================
echo.
pause
