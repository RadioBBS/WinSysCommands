# WinSysCommands – Zeigt Windows-Systembefehle und 20 Befehlskategorien in Tabellen mit Kurz- und Langbeschreibung und startet den gewaehlten Eintrag. Deshalb 3 x 7 Buttons.

```
WinSysCommands – Zeigt Windows-Systembefehle und 20 Befehlskategorien in Tabellen mit Kurz- und Langbeschreibung und startet den gewaehlten Eintrag.

Projekt:     WinSysCommands
Modul:       README.md
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

## Zweck

Das war mir zu Aufwändig, immer WINTaste+R, dann Befehle eintippen oder Start Zahnrad Einstellung. Eine Tabelle zeigt jetzt die Windows-Systembefehle und 20 Befehlskategorien in Tabellen mit Kurz- und Langbeschreibung und startet den gewaehlten Eintrag. Meistens, da auch Win7/8 XP, Win10 Einträge gelistet wurden. Ca. 65 Control Commands und 680 Win+R Commands/Plugins/Snaps etc.

Die erste Registerkarte listet Steuerungsprogramme, `*.cpl`-Applets, MMC-Snap-Ins, Diagnose und Zubehoer. Links steht der Befehl als Aufruflink, daneben die Kurzbeschreibung. Das rechte Drittel zeigt den Langtext und die Startzeile. Zwanzig weitere Karten nehmen Windows-Schemes auf (`shell:`, `ms-settings:`, `control.exe`, `rundll32`, Explorer-URI, MMC, Admin, GodMode, Netzwerk, Speicher, Hyper-V, Remote, Geraeteklassen, Sicherheit, Registry, Win10, Win11, Deep, versteckte Dialoge, veraltete Eintraege). Das Repo ist Maschinenlesbar, also gerne selbt durch KI Einsatz Aktualisieren.

Dieses Produkt ist unabhaengige Open-Source-Software und nicht die Microsoft-Store-App *System Commands* (Herausgeber Million). Auf Github wurden ebenfalls keine ähnlichen Produkte gefunden.

## Voraussetzungen

- Python >= 3.11 mit Standardbibliothek (`tkinter`, `argparse`)
- Windows fuer das Starten der Eintraege (`explorer.exe`, `cmd.exe`, PowerShell)
- `--help`, `--version` und `--list` laufen ohne diese Systemprogramme

Keine fest verdrahteten Benutzer- oder Rechnernamen.

## Installation

Keine Extra-Software unter Windows, wenn Python mit Tcl/Tk installiert ist. Skript nicht per `chmod` markieren (Windows).

Falls unter Linux nur Tests oder `--list` gewuenscht sind:

```bash
sudo apt-get install python3-tk
```

Abhaengigkeitsdatei (No-Op, keine Paketzeilen):

```powershell
python -m pip install -r requirements.txt
```

```bash
python3 -m pip install -r requirements.txt
```

## Aufruf / Nutzung

`--help` und `--version` ohne Fachlauf und ohne `explorer.exe`. Der GUI-Fachlauf braucht Windows.

```powershell
python winsyscommands.py
python winsyscommands.py --kategorie shell:
python winsyscommands.py --list
python winsyscommands.py --starten "shell:Desktop"
python winsyscommands.py --help
python winsyscommands.py --version
```

Parameter:

| Name        | Typ  | Standard      | Beschreibung                      | Beispiel                 |
| ----------- | ---- | ------------- | --------------------------------- | ------------------------ |
| --kategorie | str  | Systembefehle | Registerkarte oeffnen oder listen | --kategorie shell:       |
| --list      | flag | aus           | Textkatalog ohne GUI              | --list                   |
| --starten   | str  | leer          | Befehl aus dem Katalog starten    | --starten shell:Desktop  |
| --yes       | flag | aus           | Keine Rueckfrage bei Risiko       | --yes --starten shutdown |
| --Ende / -E | flag | aus           | Wartet am Ende auf Taste          | --Ende                   |
| --help / -h | flag | aus           | Hilfe, kein Fachlauf              | --help                   |
| --version   | flag | aus           | Version und Zweck                 | --version                |

In der Tabelle startet ein Klick auf den blauen Befehl den Eintrag. Ein Klick auf die Kurzbeschreibung fuellt nur die rechte Spalte. Destruktive Befehle (zum Beispiel `diskpart`, `format`, `shutdown`) verlangen eine Bestaetigung, ausser `--yes` ist gesetzt.

Die GitHub-Katze in der Kopfzeile oeffnet das Repository. Sie ist nicht das Fenstericon (GitHub-Logo-Policy). Das Python-Powered-Logo daneben zeigt, dass das Programm in der Programmiersprache Python geschrieben ist (PSF, unveraendertes Logo).

## Risiken

- Gestartete Systemdialoge aendern Einstellungen am Rechner.
- Manche Snap-Ins und PowerShell-Cmdlets fehlen in Home-Editionen oder ohne optionale Features (Hyper-V, RSAT).
- Veraltete und Deep-System-Eintraege koennen fehlschlagen; das ist kein Programmfehler.
- Sysinternals-Werkzeuge starten nur, wenn sie auf dem PATH liegen.
- Keine Verbindung zur Store-App; deren Hilfetexte und Binaries werden nicht mitgeliefert.
- Einige Einträge konnten nicht getestet werden, da Fehlermeldung. shell:temp kennt mein Windows nicht!
- Ob ein Snap-in gestartet werden kann hängt auch von dem Stand der Updates ab.
- Das Invertocat in der Kopfzeile ist eine Marke von GitHub, Inc. und oeffnet nur das Repository; es ist nicht das Produkticon.
- Das Python-Powered-Logo ist eine Marke der Python Software Foundation und kennzeichnet nur die Programmiersprache; es ist nicht das Produkticon.

## Test

```powershell
python -m unittest tests.test_winsyscommands
```

## Lizenz

MIT. SPDX-License-Identifier: MIT

"Python" und die Python-Logos sind Marken der Python Software Foundation.
