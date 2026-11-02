# WinSysCommands – Zeigt Windows-Systembefehle und 20 Befehlskategorien in Tabellen mit Kurz- und Langbeschreibung und startet den gewaehlten Eintrag.

```
WinSysCommands – Zeigt Windows-Systembefehle und 20 Befehlskategorien in Tabellen mit Kurz- und Langbeschreibung und startet den gewaehlten Eintrag.

Projekt:     WinSysCommands
Modul:       CHANGELOG.md
Version:     1.0.1
Stand:       2026-11-02
Abhaengig:   Python >= 3.11 Stdlib (tkinter, argparse); Windows: explorer, cmd, powershell; Tests: Python >= 3.11 Stdlib
Bezug:       requirements.txt (leer – Stdlib only)
Lizenz:      MIT
Upstream:    –
Erstellt mit: Cursor Grok 4.6
Autor:       (FFHB) / RadioBBS

Historie
--------
Version 1.0.1 – 2026-11-02 – Startausgabe und Python 3.11 nach Styleguide 2.1.0.
```

Format: `Version X.Y.Z – YYYY-MM-DD – Beschreibung` (neueste unten).

## Version 1.0.1 – 2026-11-02 – Startausgabe, Python 3.11, Plattformprüfung.

## Version 1.0.0 – 2026-09-12

- Oberflaeche mit Systembefehlen und 20 Kategorie-Registerkarten.
- Kategorien als 3 x 7 Knöpfe über die Fensterbreite.
- Calibri etwas groesser, mit Per-Monitor-DPI ohne Weichzeichnung.
- MMC- und Admin-Snap-Ins starten per Shell (nicht als EXE); shell:Temp oeffnet %TEMP%.
- Tabellen mit Aufruflinks links, Kurztext daneben, Langtext im rechten Drittel.
- Tabellen mit Aufruflinks links, Kurztext daneben, Langtext im rechten Drittel.
- CLI fuer Hilfe, Version, Textliste und Einzelstart mit Bestaetigung bei Risiko-Befehlen.
- Eigenes Fenstericon statt der Tcl/Tk-Feder; GitHub-Invertocat nur als Link zum Repository.
- Python-Powered-Logo in der Kopfzeile als Hinweis auf die Programmiersprache.
