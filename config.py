"""Configurație centrală. Versiunea aplicației se citește doar de aici (vezi footer)."""
import os
import secrets
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
INSTANCE_DIR = BASE_DIR / "instance"
INSTANCE_DIR.mkdir(exist_ok=True)

DB_PATH = INSTANCE_DIR / "nicolaus.db"

APP_VERSION = "0.2.3"

_secret_file = INSTANCE_DIR / "secret_key.txt"
if not _secret_file.exists():
    _secret_file.write_text(secrets.token_hex(32), encoding="utf-8")
SECRET_KEY = os.environ.get("NICOLAUS_SECRET_KEY") or _secret_file.read_text(encoding="utf-8").strip()
