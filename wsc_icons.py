"""
WinSysCommands – Zeigt Windows-Systembefehle und 20 Befehlskategorien in Tabellen mit Kurz- und Langbeschreibung und startet den gewaehlten Eintrag.

Projekt:     WinSysCommands
Modul:       wsc_icons.py
Version:     1.0.1
Stand:       2026-11-02
Abhaengig:   Python >= 3.11 Stdlib (tkinter, argparse); Windows: explorer, cmd, powershell; Tests: Python >= 3.11 Stdlib
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
Version 1.0.0 – 2026-09-12 – Eigenes Fenstericon; GitHub-Invertocat nur als Repo-Link.
Version 1.0.0 – 2026-09-13 – Offizielles Python-Powered-Logo als Sprachhinweis.
Version 1.0.1 – 2026-11-02 – Startausgabe und Python 3.11 nach Styleguide 2.1.0.

Aufruf / Nutzung
----------------
Wird importiert, nicht als Programm gestartet:

    python -c "import wsc_icons as i; print(i.APP_ICON.name)"
"""

from __future__ import annotations

import tkinter as tk
from pathlib import Path

ASSETS = Path(__file__).resolve().parent / "assets"
APP_ICON = ASSETS / "app-icon.png"
GITHUB_MARK = ASSETS / "github-mark.png"
PYTHON_POWERED = ASSETS / "python-powered.png"


def lade_png(pfad: Path, kantenlaenge: int = 0) -> tk.PhotoImage | None:
    """Laedt eine PNG-Datei fuer Tk, optional ganzzahlig verkleinert.

    Parameter
    ---------
    pfad:
        Vorhandene PNG-Datei.
    kantenlaenge:
        Zielkante in Pixeln; 0 laesst die Originalgroesse. Die Skalierung
        erfolgt nur per subsample, damit das Seitenverhaeltnis bleibt.

    Rueckgabe
    ---------
    PhotoImage oder None, wenn die Datei fehlt.

    Fehlerfaelle
    ------------
    TclError beim Lesen ergibt None, die GUI laeuft ohne Bild weiter.

    Beispiel
    --------
    >>> lade_png.__name__
    'lade_png'
    """
    if not pfad.is_file():
        return None
    try:
        bild = tk.PhotoImage(file=str(pfad))
    except tk.TclError:
        return None
    if kantenlaenge < 1:
        return bild
    faktor = max(1, bild.width() // kantenlaenge)
    if faktor > 1:
        return bild.subsample(faktor)
    return bild


def setze_fenstericon(fenster: tk.Misc) -> tk.PhotoImage | None:
    """Setzt das eigene App-Icon statt der Tcl/Tk-Feder.

    Das GitHub-Invertocat und das Python-Logo werden hier bewusst nicht
    verwendet: GitHub verbietet die Katze als Produkticon; das Python-Logo
    bleibt der Kennzeichnung der Programmiersprache vorbehalten.

    Parameter
    ---------
    fenster:
        Bereits erzeugtes Tk-Fenster.

    Rueckgabe
    ---------
    Das gesetzte PhotoImage oder None.

    Fehlerfaelle
    ------------
    Fehlende Datei oder TclError: Standardicon bleibt.

    Beispiel
    --------
    >>> setze_fenstericon.__name__
    'setze_fenstericon'
    """
    bild = lade_png(APP_ICON)
    if bild is None:
        return None
    fenster.iconphoto(True, bild)
    return bild
