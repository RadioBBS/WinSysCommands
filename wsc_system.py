"""
WinSysCommands – Zeigt Windows-Systembefehle und 20 Befehlskategorien in Tabellen mit Kurz- und Langbeschreibung und startet den gewaehlten Eintrag.

Projekt:     WinSysCommands
Modul:       wsc_system.py
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
Version 1.0.0 – 2026-09-12 – Systembefehle analog zu control.exe und *.cpl.
Version 1.0.1 – 2026-11-02 – Startausgabe und Python 3.11 nach Styleguide 2.1.0.

Aufruf / Nutzung
----------------
Wird importiert, nicht als Programm gestartet.
"""

from __future__ import annotations

import project_meta as meta

# Abschnitte spiegeln die Store-App: Steuerungsprogramm, Parameter, Applets.
_CONTROL = (
    ("Control.exe", "control.exe", "Systemsteuerung",
     "Oeffnet die klassische Systemsteuerung. Aufruf: control.exe"),
    ("control system", "control.exe system", "Systemeigenschaften",
     "Oeffnet die Systemeigenschaften (Name, Hardware, Remote). Aufruf: control.exe system"),
    ("control color", "control.exe color", "Farbverwaltung",
     "Oeffnet die Farbverwaltung fuer Monitore und Drucker. Aufruf: control.exe color"),
    ("control desktop", "control.exe desktop", "Anzeige",
     "Oeffnet die Anzeige- und Desktropeinstellungen. Aufruf: control.exe desktop"),
    ("control fonts", "control.exe fonts", "Schriftarten",
     "Oeffnet den Schriftarten-Ordner. Aufruf: control.exe fonts"),
    ("control keyboard", "control.exe keyboard", "Tastatur",
     "Oeffnet die Tastatureigenschaften. Aufruf: control.exe keyboard"),
    ("control mouse", "control.exe mouse", "Maus",
     "Oeffnet die Mauseigenschaften. Aufruf: control.exe mouse"),
    ("control printers", "control.exe printers", "Drucker",
     "Oeffnet Geraete und Drucker. Aufruf: control.exe printers"),
    ("control admintools", "control.exe admintools", "Verwaltung",
     "Oeffnet den Ordner Windows-Verwaltungstools. Aufruf: control.exe admintools"),
    ("control folders", "control.exe folders", "Ordneroptionen",
     "Oeffnet die Explorer-Ordneroptionen. Aufruf: control.exe folders"),
    ("control netconnections", "control.exe netconnections", "Netzwerkverbindungen",
     "Oeffnet die Adapterliste der Netzwerkverbindungen. Aufruf: control.exe netconnections"),
    ("control userpasswords2", "control.exe userpasswords2", "Benutzerkonten",
     "Oeffnet die erweiterte Benutzerkontensteuerung. Aufruf: control.exe userpasswords2"),
    ("control schedtasks", "control.exe schedtasks", "Aufgabenplanung",
     "Oeffnet die Aufgabenplanung. Aufruf: control.exe schedtasks"),
    ("control international", "control.exe international", "Region",
     "Oeffnet Regions- und Sprachoptionen. Aufruf: control.exe international"),
)

_CPL = (
    ("appwiz.cpl", "appwiz.cpl", "Programme und Features",
     "Oeffnet Programme und Features zum Deinstallieren. Aufruf: appwiz.cpl"),
    ("bthprops.cpl", "bthprops.cpl", "Bluetooth",
     "Oeffnet die Bluetooth-Geraeteeinstellungen. Aufruf: bthprops.cpl"),
    ("desk.cpl", "desk.cpl", "Anzeige",
     "Oeffnet die Bildschirmaufloesung und Anzeige. Aufruf: desk.cpl"),
    ("firewall.cpl", "firewall.cpl", "Windows-Firewall",
     "Oeffnet die klassische Windows-Firewall. Aufruf: firewall.cpl"),
    ("hdwwiz.cpl", "hdwwiz.cpl", "Hardware-Assistent",
     "Startet den Hardware-Assistenten. Aufruf: hdwwiz.cpl"),
    ("inetcpl.cpl", "inetcpl.cpl", "Internetoptionen",
     "Oeffnet die Internetoptionen (IE/Edge-Legacy). Aufruf: inetcpl.cpl"),
    ("intl.cpl", "intl.cpl", "Region",
     "Oeffnet Regionsformat und Standort. Aufruf: intl.cpl"),
    ("irprops.cpl", "irprops.cpl", "Infrarot",
     "Oeffnet Infrarot-Einstellungen, sofern vorhanden. Aufruf: irprops.cpl"),
    ("joy.cpl", "joy.cpl", "Gamecontroller",
     "Oeffnet die Gamecontroller-Eigenschaften. Aufruf: joy.cpl"),
    ("main.cpl", "main.cpl", "Maus",
     "Oeffnet die Mauseigenschaften. Aufruf: main.cpl"),
    ("mmsys.cpl", "mmsys.cpl", "Sound",
     "Oeffnet Wiedergabe-, Aufnahme- und Soundschemas. Aufruf: mmsys.cpl"),
    ("ncpa.cpl", "ncpa.cpl", "Netzwerkverbindungen",
     "Oeffnet die Netzwerkadapter. Aufruf: ncpa.cpl"),
    ("powercfg.cpl", "powercfg.cpl", "Energieoptionen",
     "Oeffnet Energiesparplaene und Knopfeinstellungen. Aufruf: powercfg.cpl"),
    ("sysdm.cpl", "sysdm.cpl", "Systemeigenschaften",
     "Oeffnet Computername, Hardware, Erweitert, Schutz, Remote. Aufruf: sysdm.cpl"),
    ("tabletpc.cpl", "tabletpc.cpl", "Tablet-PC",
     "Oeffnet Stift- und Toucheinstellungen. Aufruf: tabletpc.cpl"),
    ("telephon.cpl", "telephon.cpl", "Telefonie",
     "Oeffnet Standortinformationen fuer Modems. Aufruf: telephon.cpl"),
    ("timedate.cpl", "timedate.cpl", "Datum und Uhrzeit",
     "Oeffnet Datum, Uhrzeit und Zeitzone. Aufruf: timedate.cpl"),
    ("wscui.cpl", "wscui.cpl", "Sicherheit und Wartung",
     "Oeffnet Sicherheit und Wartung (Action Center). Aufruf: wscui.cpl"),
    ("access.cpl", "access.cpl", "Eingabehilfen",
     "Oeffnet das Center fuer erleichterte Bedienung. Aufruf: access.cpl"),
)

_VERWALTUNG = (
    ("compmgmt.msc", "compmgmt.msc", "Computerverwaltung",
     "Oeffnet die Computerverwaltung (System, Speicher, Dienste). Aufruf: compmgmt.msc"),
    ("devmgmt.msc", "devmgmt.msc", "Geraete-Manager",
     "Oeffnet den Geraete-Manager. Aufruf: devmgmt.msc"),
    ("diskmgmt.msc", "diskmgmt.msc", "Datentraegerverwaltung",
     "Oeffnet Partitionen und Datentraeger. Aufruf: diskmgmt.msc"),
    ("eventvwr.msc", "eventvwr.msc", "Ereignisanzeige",
     "Oeffnet die Windows-Ereignisanzeige. Aufruf: eventvwr.msc"),
    ("services.msc", "services.msc", "Dienste",
     "Oeffnet die Diensteverwaltung. Aufruf: services.msc"),
    ("taskschd.msc", "taskschd.msc", "Aufgabenplanung",
     "Oeffnet geplante Aufgaben. Aufruf: taskschd.msc"),
    ("perfmon.msc", "perfmon.msc", "Leistungsueberwachung",
     "Oeffnet Systemmonitor und Leistungsindikatoren. Aufruf: perfmon.msc"),
    ("wf.msc", "wf.msc", "Firewall mit erweiterter Sicherheit",
     "Oeffnet die erweiterte Windows-Firewall. Aufruf: wf.msc"),
    ("lusrmgr.msc", "lusrmgr.msc", "Lokale Benutzer und Gruppen",
     "Oeffnet lokale Benutzer und Gruppen (nicht Home). Aufruf: lusrmgr.msc"),
    ("gpedit.msc", "gpedit.msc", "Gruppenrichtlinien",
     "Oeffnet den lokalen Gruppenrichtlinien-Editor (Pro/Enterprise). Aufruf: gpedit.msc"),
)

_DIAGNOSE = (
    ("msinfo32", "msinfo32.exe", "Systeminformationen",
     "Zeigt Hardware, Komponenten und Softwareumgebung. Aufruf: msinfo32.exe"),
    ("dxdiag", "dxdiag.exe", "DirectX-Diagnose",
     "Startet das DirectX-Diagnoseprogramm. Aufruf: dxdiag.exe"),
    ("winver", "winver.exe", "Windows-Version",
     "Zeigt Versions- und Lizenzdialog. Aufruf: winver.exe"),
    ("msconfig", "msconfig.exe", "Systemkonfiguration",
     "Oeffnet Start, Dienste und Tools. Aufruf: msconfig.exe"),
    ("resmon", "resmon.exe", "Ressourcenmonitor",
     "Zeigt CPU, Datentraeger, Netz und Speicher live. Aufruf: resmon.exe"),
    ("taskmgr", "taskmgr.exe", "Task-Manager",
     "Oeffnet den Task-Manager. Aufruf: taskmgr.exe"),
    ("cleanmgr", "cleanmgr.exe", "Datentraegerbereinigung",
     "Startet die Datentraegerbereinigung. Aufruf: cleanmgr.exe"),
    ("dfrgui", "dfrgui.exe", "Optimieren der Laufwerke",
     "Oeffnet Defragmentierung bzw. TRIM-Optimierung. Aufruf: dfrgui.exe"),
    ("OptionalFeatures", "OptionalFeatures.exe", "Windows-Features",
     "Oeffnet optionale Windows-Features. Aufruf: OptionalFeatures.exe"),
    ("SystemPropertiesAdvanced", "SystemPropertiesAdvanced.exe", "Erweiterte Systemeigenschaften",
     "Oeffnet direkt die Karte Erweitert. Aufruf: SystemPropertiesAdvanced.exe"),
)

_SHELL = (
    ("cmd.exe", "cmd.exe", "Eingabeaufforderung",
     "Startet eine neue Eingabeaufforderung. Aufruf: cmd.exe"),
    ("powershell.exe", "powershell.exe", "Windows PowerShell",
     "Startet Windows PowerShell. Aufruf: powershell.exe"),
    ("wt.exe", "wt.exe", "Windows-Terminal",
     "Startet Windows Terminal, sofern installiert. Aufruf: wt.exe"),
    ("regedit.exe", "regedit.exe", "Registrierungs-Editor",
     "Oeffnet den Registrierungs-Editor. Aufruf: regedit.exe"),
    ("explorer.exe", "explorer.exe", "Explorer",
     "Startet ein Explorer-Fenster. Aufruf: explorer.exe"),
    ("notepad.exe", "notepad.exe", "Editor",
     "Startet den Windows-Editor. Aufruf: notepad.exe"),
    ("calc.exe", "calc.exe", "Rechner",
     "Startet den Rechner. Aufruf: calc.exe"),
    ("mspaint.exe", "mspaint.exe", "Paint",
     "Startet Paint. Aufruf: mspaint.exe"),
    ("charmap.exe", "charmap.exe", "Zeichentabelle",
     "Oeffnet die Zeichentabelle. Aufruf: charmap.exe"),
    ("osk.exe", "osk.exe", "Bildschirmtastatur",
     "Startet die Bildschirmtastatur. Aufruf: osk.exe"),
    ("magnify.exe", "magnify.exe", "Bildschirmlupe",
     "Startet die Bildschirmlupe. Aufruf: magnify.exe"),
    ("SnippingTool.exe", "SnippingTool.exe", "Snipping Tool",
     "Startet das Snipping Tool. Aufruf: SnippingTool.exe"),
)

_ABSCHNITTE = (
    ("control.exe", "control.exe, Parameter", _CONTROL),
    ("cpl", "*.cpl (Systemsteuerungs-Applets)", _CPL),
    ("verwaltung", "Verwaltung (MMC)", _VERWALTUNG),
    ("diagnose", "Diagnose und Wartung", _DIAGNOSE),
    ("shell", "Shell, Editoren und Zubehoer", _SHELL),
)


def system_eintraege() -> list[dict[str, object]]:
    """Liefert die Eintraege der ersten Registerkarte Systembefehle.

    Rueckgabe
    ---------
    Liste von Katalogdicts mit Kategorie, Abschnitt, Befehl und Texten.

    Fehlerfaelle
    ------------
    Keine.

    Beispiel
    --------
    >>> system_eintraege()[0]["kategorie"] == meta.SYSTEM_KAT
    True
    """
    result: list[dict[str, object]] = []
    for abs_id, _titel, zeilen in _ABSCHNITTE:
        for befehl, start, kurz, lang in zeilen:
            result.append(
                {
                    "kategorie": meta.SYSTEM_KAT,
                    "abschnitt": abs_id,
                    "abschnitt_titel": _titel,
                    "befehl": befehl,
                    "start": start,
                    "kurz": kurz,
                    "lang": lang,
                    "destruktiv": False,
                }
            )
    return result


def system_abschnitte() -> list[tuple[str, str]]:
    """Liefert Abschnitt-IDs und Ueberschriften der Systembefehle.

    Rueckgabe
    ---------
    Paare aus interner ID und sichtbarer Tabellenueberschrift.

    Fehlerfaelle
    ------------
    Keine.

    Beispiel
    --------
    >>> system_abschnitte()[0][0]
    'control.exe'
    """
    return [(abs_id, titel) for abs_id, titel, _zeilen in _ABSCHNITTE]
