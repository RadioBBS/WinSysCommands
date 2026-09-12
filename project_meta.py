"""
WinSysCommands – Zeigt Windows-Systembefehle und 20 Befehlskategorien in Tabellen mit Kurz- und Langbeschreibung und startet den gewaehlten Eintrag.

Projekt:     WinSysCommands
Modul:       project_meta.py
Version:     1.0.0
Stand:       2026-09-12
Abhaengig:   Python >= 3.10 Stdlib (tkinter, argparse); Windows: explorer, cmd, powershell; Tests: Python >= 3.10 Stdlib
Bezug:       requirements.txt (leer – Stdlib only)
Lizenz:      MIT
Upstream:    –
Erstellt mit: Cursor Grok 4.6
Autor:       (FFHB) / RadioBBS

Beschreibung
------------
Zeigt Windows-Systembefehle und 20 Befehlskategorien in Tabellen mit Kurz- und Langbeschreibung und startet den gewaehlten Eintrag.

Historie
--------
Version 1.0.0 – 2026-09-12 – Erste gemeinsame Metadatenquelle.
Version 1.0.0 – 2026-09-12 – GITHUB_URL fuer den Invertocat-Link.
Version 1.0.0 – 2026-09-13 – PYTHON_URL fuer den Python-Powered-Hinweis.

Aufruf / Nutzung
----------------
Wird importiert, nicht als Programm gestartet:

    python -c "import project_meta as m; print(m.VERSION, m.STAND)"
"""

from __future__ import annotations

PROJEKT = "WinSysCommands"
VERSION = "1.0.0"
STAND = "2026-09-12"
LIZENZ = "MIT"
UPSTREAM = "–"
AUTOR = "(FFHB) / RadioBBS"
PYTHON_MIN = "3.10"
ERSTELLT_MIT = "Cursor Grok 4.6"
SKRIPT = "winsyscommands.py"

BESCHREIBUNG = (
    "Zeigt Windows-Systembefehle und 20 Befehlskategorien in Tabellen mit "
    "Kurz- und Langbeschreibung und startet den gewaehlten Eintrag."
)

ABHAENGIG = (
    "Python >= 3.10 Stdlib (tkinter, argparse); Windows: explorer, cmd, "
    "powershell; Tests: Python >= 3.10 Stdlib"
)
BEZUG = "requirements.txt (leer – Stdlib only)"
LOG_STAMP = "%Y-%m-%d %H:%M:%S"
SYSTEM_KAT = "system"
WINDOW_TITLE = "WinSysCommands"
WINDOW_MIN_W = 1200
WINDOW_MIN_H = 700
GITHUB_URL = "https://github.com/RadioBBS/WinSysCommands"
PYTHON_URL = "https://www.python.org/"
LINK_FARBE = "#0563C1"
TABELLEN_RAND = "#808080"
HINTERGRUND = "#ffffff"
DETAIL_HG = "#f4f4f4"
SCHRIFT_FAMILIE = "Calibri"
SCHRIFT_GROESSE = 11
SCHRIFT_TITEL = 20
SCHRIFT_KOPF = 12
SCHRIFT_KNOPF = 11
