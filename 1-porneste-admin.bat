@echo off
chcp 65001 >nul
REM ============================================================
REM  Porneste site-ul Nicolaus local si deschide panoul de admin.
REM  Ruleaza acest fisier (dublu-click) de fiecare data cand vrei
REM  sa adaugi/editezi ceva pe site: poze in jurnal, parteneri noi,
REM  continut pe Proiectul/Acasa, etc.
REM ============================================================

cd /d "%~dp0"

echo Pornim serverul local (Flask)...
start "Site Nicolaus - SERVER LOCAL (nu inchide!)" cmd /k python app.py

REM Asteptam cateva secunde ca serverul sa apuce sa porneasca.
timeout /t 3 /nobreak >nul

echo Deschidem panoul de administrare in browser...
start http://127.0.0.1:5050/admin/login

echo.
echo ============================================================
echo  Gata! S-a deschis o fereastra NEAGRA noua - aia e serverul.
echo  LAS-O DESCHISA cat timp lucrezi in admin.
echo.
echo  Cand termini de editat:
echo    1. Inchide fereastra neagra a serverului (sau Ctrl+C in ea)
echo    2. Ruleaza fisierul "2-publica-pe-site.bat" ca sa trimiti
echo       modificarile pe site-ul live.
echo ============================================================
echo.
pause
