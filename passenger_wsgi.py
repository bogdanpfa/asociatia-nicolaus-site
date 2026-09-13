"""Punct de intrare WSGI pentru cPanel (Phusion Passenger).
Cand creezi aplicatia Python din cPanel ("Setup Python App"), cPanel genereaza
automat un fisier passenger_wsgi.py in radacina aplicatiei -- inlocuieste-l cu
acesta (sau lipeste continutul de mai jos peste el)."""
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from app import app as application  # noqa: E402
