"""
WinSysCommands – Zeigt Windows-Systembefehle und 20 Befehlskategorien in Tabellen mit Kurz- und Langbeschreibung und startet den gewaehlten Eintrag.

Projekt:     WinSysCommands
Modul:       wsc_daten.py
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
Version 1.0.0 – 2026-09-12 – Katalog der 20 Kategorien aus Windows-Befehlsschemes.

Aufruf / Nutzung
----------------
Wird importiert, nicht als Programm gestartet.
"""

from __future__ import annotations

import json

KATALOG = json.loads(r"""
{
  "kategorien": [
    {
      "id": "shell",
      "tab": "shell:",
      "titel": "shell: Befehle"
    },
    {
      "id": "ms-settings",
      "tab": "ms-settings:",
      "titel": "ms-settings: Befehle"
    },
    {
      "id": "control",
      "tab": "control.exe",
      "titel": "control.exe Dialoge"
    },
    {
      "id": "rundll32",
      "tab": "rundll32",
      "titel": "rundll32 Dialoge"
    },
    {
      "id": "explorer",
      "tab": "Explorer-URI",
      "titel": "Explorer-URI-Schemes"
    },
    {
      "id": "mmc",
      "tab": "MMC",
      "titel": "MMC-Snap-Ins"
    },
    {
      "id": "admin",
      "tab": "Admin",
      "titel": "Admin-Tools"
    },
    {
      "id": "godmode",
      "tab": "GodMode",
      "titel": "GodMode-Unterdialoge"
    },
    {
      "id": "netzwerk",
      "tab": "Netzwerk",
      "titel": "Netzwerk-Schemes"
    },
    {
      "id": "speicher",
      "tab": "Speicher",
      "titel": "Storage-Schemes"
    },
    {
      "id": "hyperv",
      "tab": "Hyper-V",
      "titel": "Hyper-V Schemes"
    },
    {
      "id": "remote",
      "tab": "Remote",
      "titel": "Remote-Management"
    },
    {
      "id": "geraete",
      "tab": "Geraete",
      "titel": "Geraeteklassen"
    },
    {
      "id": "sicherheit",
      "tab": "Sicherheit",
      "titel": "Sicherheits-Schemes"
    },
    {
      "id": "registry",
      "tab": "Registry",
      "titel": "Registry-URI-Schemes"
    },
    {
      "id": "win10",
      "tab": "Win10",
      "titel": "Windows-10-Legacy"
    },
    {
      "id": "win11",
      "tab": "Win11",
      "titel": "Windows-11-Schemes"
    },
    {
      "id": "deep",
      "tab": "Deep",
      "titel": "Deep-System-Schemes"
    },
    {
      "id": "versteckt",
      "tab": "Versteckt",
      "titel": "Versteckte Systemdialoge"
    },
    {
      "id": "veraltet",
      "tab": "Veraltet",
      "titel": "Deprecated-Schemes"
    }
  ],
  "eintraege": [
    {
      "kategorie": "shell",
      "befehl": "shell:AppsFolder",
      "start": "shell:AppsFolder",
      "kurz": "Installierte Apps",
      "lang": "Oeffnet den Windows-Shellordner 'Installierte Apps' im Explorer. Aufruf: explorer.exe shell:AppsFolder",
      "destruktiv": false
    },
    {
      "kategorie": "shell",
      "befehl": "shell:Desktop",
      "start": "shell:Desktop",
      "kurz": "Desktop",
      "lang": "Oeffnet den Windows-Shellordner 'Desktop' im Explorer. Aufruf: explorer.exe shell:Desktop",
      "destruktiv": false
    },
    {
      "kategorie": "shell",
      "befehl": "shell:Downloads",
      "start": "shell:Downloads",
      "kurz": "Downloads",
      "lang": "Oeffnet den Windows-Shellordner 'Downloads' im Explorer. Aufruf: explorer.exe shell:Downloads",
      "destruktiv": false
    },
    {
      "kategorie": "shell",
      "befehl": "shell:Documents",
      "start": "shell:Documents",
      "kurz": "Dokumente",
      "lang": "Oeffnet den Windows-Shellordner 'Dokumente' im Explorer. Aufruf: explorer.exe shell:Documents",
      "destruktiv": false
    },
    {
      "kategorie": "shell",
      "befehl": "shell:Pictures",
      "start": "shell:Pictures",
      "kurz": "Bilder",
      "lang": "Oeffnet den Windows-Shellordner 'Bilder' im Explorer. Aufruf: explorer.exe shell:Pictures",
      "destruktiv": false
    },
    {
      "kategorie": "shell",
      "befehl": "shell:Music",
      "start": "shell:Music",
      "kurz": "Musik",
      "lang": "Oeffnet den Windows-Shellordner 'Musik' im Explorer. Aufruf: explorer.exe shell:Music",
      "destruktiv": false
    },
    {
      "kategorie": "shell",
      "befehl": "shell:Videos",
      "start": "shell:Videos",
      "kurz": "Videos",
      "lang": "Oeffnet den Windows-Shellordner 'Videos' im Explorer. Aufruf: explorer.exe shell:Videos",
      "destruktiv": false
    },
    {
      "kategorie": "shell",
      "befehl": "shell:Profile",
      "start": "shell:Profile",
      "kurz": "Benutzerprofil",
      "lang": "Oeffnet den Windows-Shellordner 'Benutzerprofil' im Explorer. Aufruf: explorer.exe shell:Profile",
      "destruktiv": false
    },
    {
      "kategorie": "shell",
      "befehl": "shell:Recent",
      "start": "shell:Recent",
      "kurz": "Zuletzt verwendet",
      "lang": "Oeffnet den Windows-Shellordner 'Zuletzt verwendet' im Explorer. Aufruf: explorer.exe shell:Recent",
      "destruktiv": false
    },
    {
      "kategorie": "shell",
      "befehl": "shell:SendTo",
      "start": "shell:SendTo",
      "kurz": "Senden-an Menü",
      "lang": "Oeffnet den Windows-Shellordner 'Senden-an Menü' im Explorer. Aufruf: explorer.exe shell:SendTo",
      "destruktiv": false
    },
    {
      "kategorie": "shell",
      "befehl": "shell:Links",
      "start": "shell:Links",
      "kurz": "Schnellzugriff",
      "lang": "Oeffnet den Windows-Shellordner 'Schnellzugriff' im Explorer. Aufruf: explorer.exe shell:Links",
      "destruktiv": false
    },
    {
      "kategorie": "shell",
      "befehl": "shell:Favorites",
      "start": "shell:Favorites",
      "kurz": "IE Favoriten",
      "lang": "Oeffnet den Windows-Shellordner 'IE Favoriten' im Explorer. Aufruf: explorer.exe shell:Favorites",
      "destruktiv": false
    },
    {
      "kategorie": "shell",
      "befehl": "shell:AppData",
      "start": "shell:AppData",
      "kurz": "Roaming AppData",
      "lang": "Oeffnet den Windows-Shellordner 'Roaming AppData' im Explorer. Aufruf: explorer.exe shell:AppData",
      "destruktiv": false
    },
    {
      "kategorie": "shell",
      "befehl": "shell:LocalAppData",
      "start": "shell:LocalAppData",
      "kurz": "Lokale AppData",
      "lang": "Oeffnet den Windows-Shellordner 'Lokale AppData' im Explorer. Aufruf: explorer.exe shell:LocalAppData",
      "destruktiv": false
    },
    {
      "kategorie": "shell",
      "befehl": "shell:Common AppData",
      "start": "shell:Common AppData",
      "kurz": "Gemeinsame AppData",
      "lang": "Oeffnet den Windows-Shellordner 'Gemeinsame AppData' im Explorer. Aufruf: explorer.exe shell:Common AppData",
      "destruktiv": false
    },
    {
      "kategorie": "shell",
      "befehl": "shell:ProgramFiles",
      "start": "shell:ProgramFiles",
      "kurz": "Programme 64-bit",
      "lang": "Oeffnet den Windows-Shellordner 'Programme 64-bit' im Explorer. Aufruf: explorer.exe shell:ProgramFiles",
      "destruktiv": false
    },
    {
      "kategorie": "shell",
      "befehl": "shell:ProgramFilesX86",
      "start": "shell:ProgramFilesX86",
      "kurz": "Programme 32-bit",
      "lang": "Oeffnet den Windows-Shellordner 'Programme 32-bit' im Explorer. Aufruf: explorer.exe shell:ProgramFilesX86",
      "destruktiv": false
    },
    {
      "kategorie": "shell",
      "befehl": "shell:Programs",
      "start": "shell:Programs",
      "kurz": "Startmenü",
      "lang": "Oeffnet den Windows-Shellordner 'Startmenü' im Explorer. Aufruf: explorer.exe shell:Programs",
      "destruktiv": false
    },
    {
      "kategorie": "shell",
      "befehl": "shell:Common Programs",
      "start": "shell:Common Programs",
      "kurz": "Gemeinsames Startmenü",
      "lang": "Oeffnet den Windows-Shellordner 'Gemeinsames Startmenü' im Explorer. Aufruf: explorer.exe shell:Common Programs",
      "destruktiv": false
    },
    {
      "kategorie": "shell",
      "befehl": "shell:Startup",
      "start": "shell:Startup",
      "kurz": "Autostart",
      "lang": "Oeffnet den Windows-Shellordner 'Autostart' im Explorer. Aufruf: explorer.exe shell:Startup",
      "destruktiv": false
    },
    {
      "kategorie": "shell",
      "befehl": "shell:Common Startup",
      "start": "shell:Common Startup",
      "kurz": "Autostart alle Benutzer",
      "lang": "Oeffnet den Windows-Shellordner 'Autostart alle Benutzer' im Explorer. Aufruf: explorer.exe shell:Common Startup",
      "destruktiv": false
    },
    {
      "kategorie": "shell",
      "befehl": "shell:Windows",
      "start": "shell:Windows",
      "kurz": "Windows-Verzeichnis",
      "lang": "Oeffnet den Windows-Shellordner 'Windows-Verzeichnis' im Explorer. Aufruf: explorer.exe shell:Windows",
      "destruktiv": false
    },
    {
      "kategorie": "shell",
      "befehl": "shell:System",
      "start": "shell:System",
      "kurz": "System32",
      "lang": "Oeffnet den Windows-Shellordner 'System32' im Explorer. Aufruf: explorer.exe shell:System",
      "destruktiv": false
    },
    {
      "kategorie": "shell",
      "befehl": "shell:SystemX86",
      "start": "shell:SystemX86",
      "kurz": "SysWOW64",
      "lang": "Oeffnet den Windows-Shellordner 'SysWOW64' im Explorer. Aufruf: explorer.exe shell:SystemX86",
      "destruktiv": false
    },
    {
      "kategorie": "shell",
      "befehl": "shell:Temp",
      "start": "shell:Temp",
      "kurz": "Temp Ordner",
      "lang": "Oeffnet den Windows-Shellordner 'Temp Ordner' im Explorer. Aufruf: explorer.exe shell:Temp",
      "destruktiv": false
    },
    {
      "kategorie": "shell",
      "befehl": "shell:Cache",
      "start": "shell:Cache",
      "kurz": "Browser Cache",
      "lang": "Oeffnet den Windows-Shellordner 'Browser Cache' im Explorer. Aufruf: explorer.exe shell:Cache",
      "destruktiv": false
    },
    {
      "kategorie": "shell",
      "befehl": "shell:History",
      "start": "shell:History",
      "kurz": "Browser Historie",
      "lang": "Oeffnet den Windows-Shellordner 'Browser Historie' im Explorer. Aufruf: explorer.exe shell:History",
      "destruktiv": false
    },
    {
      "kategorie": "shell",
      "befehl": "shell:Cookies",
      "start": "shell:Cookies",
      "kurz": "Cookies",
      "lang": "Oeffnet den Windows-Shellordner 'Cookies' im Explorer. Aufruf: explorer.exe shell:Cookies",
      "destruktiv": false
    },
    {
      "kategorie": "shell",
      "befehl": "shell:SavedGames",
      "start": "shell:SavedGames",
      "kurz": "Gespeicherte Spiele",
      "lang": "Oeffnet den Windows-Shellordner 'Gespeicherte Spiele' im Explorer. Aufruf: explorer.exe shell:SavedGames",
      "destruktiv": false
    },
    {
      "kategorie": "shell",
      "befehl": "shell:Searches",
      "start": "shell:Searches",
      "kurz": "Suchordner",
      "lang": "Oeffnet den Windows-Shellordner 'Suchordner' im Explorer. Aufruf: explorer.exe shell:Searches",
      "destruktiv": false
    },
    {
      "kategorie": "shell",
      "befehl": "shell:Contacts",
      "start": "shell:Contacts",
      "kurz": "Kontakte",
      "lang": "Oeffnet den Windows-Shellordner 'Kontakte' im Explorer. Aufruf: explorer.exe shell:Contacts",
      "destruktiv": false
    },
    {
      "kategorie": "shell",
      "befehl": "shell:OneDrive",
      "start": "shell:OneDrive",
      "kurz": "OneDrive",
      "lang": "Oeffnet den Windows-Shellordner 'OneDrive' im Explorer. Aufruf: explorer.exe shell:OneDrive",
      "destruktiv": false
    },
    {
      "kategorie": "shell",
      "befehl": "shell:OneDriveDocuments",
      "start": "shell:OneDriveDocuments",
      "kurz": "OneDrive Dokumente",
      "lang": "Oeffnet den Windows-Shellordner 'OneDrive Dokumente' im Explorer. Aufruf: explorer.exe shell:OneDriveDocuments",
      "destruktiv": false
    },
    {
      "kategorie": "shell",
      "befehl": "shell:OneDrivePictures",
      "start": "shell:OneDrivePictures",
      "kurz": "OneDrive Bilder",
      "lang": "Oeffnet den Windows-Shellordner 'OneDrive Bilder' im Explorer. Aufruf: explorer.exe shell:OneDrivePictures",
      "destruktiv": false
    },
    {
      "kategorie": "ms-settings",
      "befehl": "ms-settings:windowsupdate",
      "start": "ms-settings:windowsupdate",
      "kurz": "Windows Update",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Windows Update'. URI: ms-settings:windowsupdate",
      "destruktiv": false
    },
    {
      "kategorie": "ms-settings",
      "befehl": "ms-settings:display",
      "start": "ms-settings:display",
      "kurz": "Anzeige",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Anzeige'. URI: ms-settings:display",
      "destruktiv": false
    },
    {
      "kategorie": "ms-settings",
      "befehl": "ms-settings:network",
      "start": "ms-settings:network",
      "kurz": "Netzwerk",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Netzwerk'. URI: ms-settings:network",
      "destruktiv": false
    },
    {
      "kategorie": "ms-settings",
      "befehl": "ms-settings:bluetooth",
      "start": "ms-settings:bluetooth",
      "kurz": "Bluetooth",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Bluetooth'. URI: ms-settings:bluetooth",
      "destruktiv": false
    },
    {
      "kategorie": "ms-settings",
      "befehl": "ms-settings:privacy",
      "start": "ms-settings:privacy",
      "kurz": "Datenschutz",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Datenschutz'. URI: ms-settings:privacy",
      "destruktiv": false
    },
    {
      "kategorie": "ms-settings",
      "befehl": "ms-settings:appsfeatures",
      "start": "ms-settings:appsfeatures",
      "kurz": "Apps & Features",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Apps & Features'. URI: ms-settings:appsfeatures",
      "destruktiv": false
    },
    {
      "kategorie": "ms-settings",
      "befehl": "ms-settings:storagesense",
      "start": "ms-settings:storagesense",
      "kurz": "Speicherverwaltung",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Speicherverwaltung'. URI: ms-settings:storagesense",
      "destruktiv": false
    },
    {
      "kategorie": "ms-settings",
      "befehl": "ms-settings:about",
      "start": "ms-settings:about",
      "kurz": "Info",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Info'. URI: ms-settings:about",
      "destruktiv": false
    },
    {
      "kategorie": "ms-settings",
      "befehl": "ms-settings:dateandtime",
      "start": "ms-settings:dateandtime",
      "kurz": "Datum & Uhrzeit",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Datum & Uhrzeit'. URI: ms-settings:dateandtime",
      "destruktiv": false
    },
    {
      "kategorie": "ms-settings",
      "befehl": "ms-settings:regionformat",
      "start": "ms-settings:regionformat",
      "kurz": "Region",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Region'. URI: ms-settings:regionformat",
      "destruktiv": true
    },
    {
      "kategorie": "ms-settings",
      "befehl": "ms-settings:keyboard",
      "start": "ms-settings:keyboard",
      "kurz": "Tastatur",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Tastatur'. URI: ms-settings:keyboard",
      "destruktiv": false
    },
    {
      "kategorie": "ms-settings",
      "befehl": "ms-settings:mouse",
      "start": "ms-settings:mouse",
      "kurz": "Maus",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Maus'. URI: ms-settings:mouse",
      "destruktiv": false
    },
    {
      "kategorie": "ms-settings",
      "befehl": "ms-settings:multitasking",
      "start": "ms-settings:multitasking",
      "kurz": "Multitasking",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Multitasking'. URI: ms-settings:multitasking",
      "destruktiv": false
    },
    {
      "kategorie": "ms-settings",
      "befehl": "ms-settings:gaming-gamebar",
      "start": "ms-settings:gaming-gamebar",
      "kurz": "Game Bar",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Game Bar'. URI: ms-settings:gaming-gamebar",
      "destruktiv": false
    },
    {
      "kategorie": "ms-settings",
      "befehl": "ms-settings:gaming-xboxnetworking",
      "start": "ms-settings:gaming-xboxnetworking",
      "kurz": "Xbox Networking",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Xbox Networking'. URI: ms-settings:gaming-xboxnetworking",
      "destruktiv": false
    },
    {
      "kategorie": "ms-settings",
      "befehl": "ms-settings:windowsdefender",
      "start": "ms-settings:windowsdefender",
      "kurz": "Windows Defender",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Windows Defender'. URI: ms-settings:windowsdefender",
      "destruktiv": false
    },
    {
      "kategorie": "ms-settings",
      "befehl": "ms-settings:troubleshoot",
      "start": "ms-settings:troubleshoot",
      "kurz": "Problembehandlung",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Problembehandlung'. URI: ms-settings:troubleshoot",
      "destruktiv": false
    },
    {
      "kategorie": "ms-settings",
      "befehl": "ms-settings:optionalfeatures",
      "start": "ms-settings:optionalfeatures",
      "kurz": "Optionale Features",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Optionale Features'. URI: ms-settings:optionalfeatures",
      "destruktiv": false
    },
    {
      "kategorie": "ms-settings",
      "befehl": "ms-settings:defaultapps",
      "start": "ms-settings:defaultapps",
      "kurz": "Standard-Apps",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Standard-Apps'. URI: ms-settings:defaultapps",
      "destruktiv": false
    },
    {
      "kategorie": "ms-settings",
      "befehl": "ms-settings:notifications",
      "start": "ms-settings:notifications",
      "kurz": "Benachrichtigungen",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Benachrichtigungen'. URI: ms-settings:notifications",
      "destruktiv": false
    },
    {
      "kategorie": "ms-settings",
      "befehl": "ms-settings:power",
      "start": "ms-settings:power",
      "kurz": "Energieoptionen",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Energieoptionen'. URI: ms-settings:power",
      "destruktiv": false
    },
    {
      "kategorie": "ms-settings",
      "befehl": "ms-settings:batterysaver",
      "start": "ms-settings:batterysaver",
      "kurz": "Batteriesparmodus",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Batteriesparmodus'. URI: ms-settings:batterysaver",
      "destruktiv": false
    },
    {
      "kategorie": "ms-settings",
      "befehl": "ms-settings:clipboard",
      "start": "ms-settings:clipboard",
      "kurz": "Zwischenablage",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Zwischenablage'. URI: ms-settings:clipboard",
      "destruktiv": false
    },
    {
      "kategorie": "ms-settings",
      "befehl": "ms-settings:display-advanced",
      "start": "ms-settings:display-advanced",
      "kurz": "Erweiterte Anzeige",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Erweiterte Anzeige'. URI: ms-settings:display-advanced",
      "destruktiv": false
    },
    {
      "kategorie": "ms-settings",
      "befehl": "ms-settings:network-wifi",
      "start": "ms-settings:network-wifi",
      "kurz": "WLAN",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'WLAN'. URI: ms-settings:network-wifi",
      "destruktiv": false
    },
    {
      "kategorie": "ms-settings",
      "befehl": "ms-settings:network-ethernet",
      "start": "ms-settings:network-ethernet",
      "kurz": "Ethernet",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Ethernet'. URI: ms-settings:network-ethernet",
      "destruktiv": false
    },
    {
      "kategorie": "ms-settings",
      "befehl": "ms-settings:network-vpn",
      "start": "ms-settings:network-vpn",
      "kurz": "VPN",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'VPN'. URI: ms-settings:network-vpn",
      "destruktiv": false
    },
    {
      "kategorie": "ms-settings",
      "befehl": "ms-settings:network-mobilehotspot",
      "start": "ms-settings:network-mobilehotspot",
      "kurz": "Mobiler Hotspot",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Mobiler Hotspot'. URI: ms-settings:network-mobilehotspot",
      "destruktiv": false
    },
    {
      "kategorie": "ms-settings",
      "befehl": "ms-settings:network-airplanemode",
      "start": "ms-settings:network-airplanemode",
      "kurz": "Flugmodus",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Flugmodus'. URI: ms-settings:network-airplanemode",
      "destruktiv": false
    },
    {
      "kategorie": "ms-settings",
      "befehl": "ms-settings:developers",
      "start": "ms-settings:developers",
      "kurz": "Entwickleroptionen",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Entwickleroptionen'. URI: ms-settings:developers",
      "destruktiv": false
    },
    {
      "kategorie": "ms-settings",
      "befehl": "ms-settings:windowsinsider",
      "start": "ms-settings:windowsinsider",
      "kurz": "Windows Insider",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Windows Insider'. URI: ms-settings:windowsinsider",
      "destruktiv": false
    },
    {
      "kategorie": "ms-settings",
      "befehl": "ms-settings:backup",
      "start": "ms-settings:backup",
      "kurz": "Backup",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Backup'. URI: ms-settings:backup",
      "destruktiv": false
    },
    {
      "kategorie": "ms-settings",
      "befehl": "ms-settings:sync",
      "start": "ms-settings:sync",
      "kurz": "Synchronisierung",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Synchronisierung'. URI: ms-settings:sync",
      "destruktiv": false
    },
    {
      "kategorie": "ms-settings",
      "befehl": "ms-settings:family",
      "start": "ms-settings:family",
      "kurz": "Familienoptionen",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Familienoptionen'. URI: ms-settings:family",
      "destruktiv": false
    },
    {
      "kategorie": "ms-settings",
      "befehl": "ms-settings:easeofaccess",
      "start": "ms-settings:easeofaccess",
      "kurz": "Barrierefreiheit",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Barrierefreiheit'. URI: ms-settings:easeofaccess",
      "destruktiv": false
    },
    {
      "kategorie": "ms-settings",
      "befehl": "ms-settings:display-advancedgraphics",
      "start": "ms-settings:display-advancedgraphics",
      "kurz": "GPU-Einstellungen",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'GPU-Einstellungen'. URI: ms-settings:display-advancedgraphics",
      "destruktiv": false
    },
    {
      "kategorie": "ms-settings",
      "befehl": "ms-settings:network-proxy",
      "start": "ms-settings:network-proxy",
      "kurz": "Proxy",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Proxy'. URI: ms-settings:network-proxy",
      "destruktiv": false
    },
    {
      "kategorie": "ms-settings",
      "befehl": "ms-settings:network-dialup",
      "start": "ms-settings:network-dialup",
      "kurz": "DFÜ",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'DFÜ'. URI: ms-settings:network-dialup",
      "destruktiv": false
    },
    {
      "kategorie": "ms-settings",
      "befehl": "ms-settings:network-directaccess",
      "start": "ms-settings:network-directaccess",
      "kurz": "DirectAccess",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'DirectAccess'. URI: ms-settings:network-directaccess",
      "destruktiv": false
    },
    {
      "kategorie": "ms-settings",
      "befehl": "ms-settings:network-mobile",
      "start": "ms-settings:network-mobile",
      "kurz": "Mobilfunk",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Mobilfunk'. URI: ms-settings:network-mobile",
      "destruktiv": false
    },
    {
      "kategorie": "ms-settings",
      "befehl": "ms-settings:signinoptions",
      "start": "ms-settings:signinoptions",
      "kurz": "Anmeldeoptionen",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Anmeldeoptionen'. URI: ms-settings:signinoptions",
      "destruktiv": false
    },
    {
      "kategorie": "ms-settings",
      "befehl": "ms-settings:lockscreen",
      "start": "ms-settings:lockscreen",
      "kurz": "Sperrbildschirm",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Sperrbildschirm'. URI: ms-settings:lockscreen",
      "destruktiv": false
    },
    {
      "kategorie": "ms-settings",
      "befehl": "ms-settings:personalization",
      "start": "ms-settings:personalization",
      "kurz": "Personalisierung",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Personalisierung'. URI: ms-settings:personalization",
      "destruktiv": false
    },
    {
      "kategorie": "ms-settings",
      "befehl": "ms-settings:themes",
      "start": "ms-settings:themes",
      "kurz": "Themes",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Themes'. URI: ms-settings:themes",
      "destruktiv": false
    },
    {
      "kategorie": "ms-settings",
      "befehl": "ms-settings:taskbar",
      "start": "ms-settings:taskbar",
      "kurz": "Taskleiste",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Taskleiste'. URI: ms-settings:taskbar",
      "destruktiv": false
    },
    {
      "kategorie": "ms-settings",
      "befehl": "ms-settings:language",
      "start": "ms-settings:language",
      "kurz": "Sprache",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Sprache'. URI: ms-settings:language",
      "destruktiv": false
    },
    {
      "kategorie": "ms-settings",
      "befehl": "ms-settings:windowsupdate-action",
      "start": "ms-settings:windowsupdate-action",
      "kurz": "Update-Aktionen",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Update-Aktionen'. URI: ms-settings:windowsupdate-action",
      "destruktiv": false
    },
    {
      "kategorie": "ms-settings",
      "befehl": "ms-settings:windowsupdate-history",
      "start": "ms-settings:windowsupdate-history",
      "kurz": "Update-Historie",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Update-Historie'. URI: ms-settings:windowsupdate-history",
      "destruktiv": false
    },
    {
      "kategorie": "ms-settings",
      "befehl": "ms-settings:windowsupdate-options",
      "start": "ms-settings:windowsupdate-options",
      "kurz": "Update-Optionen",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Update-Optionen'. URI: ms-settings:windowsupdate-options",
      "destruktiv": false
    },
    {
      "kategorie": "ms-settings",
      "befehl": "ms-settings:windowsupdate-restartoptions",
      "start": "ms-settings:windowsupdate-restartoptions",
      "kurz": "Neustartoptionen",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Neustartoptionen'. URI: ms-settings:windowsupdate-restartoptions",
      "destruktiv": false
    },
    {
      "kategorie": "control",
      "befehl": "control",
      "start": "control",
      "kurz": "Systemsteuerung",
      "lang": "Startet ein Systemsteuerungsfenster (Systemsteuerung). Aufruf: control",
      "destruktiv": false
    },
    {
      "kategorie": "control",
      "befehl": "control printers",
      "start": "control printers",
      "kurz": "Drucker",
      "lang": "Startet ein Systemsteuerungsfenster (Drucker). Aufruf: control printers",
      "destruktiv": false
    },
    {
      "kategorie": "control",
      "befehl": "control keyboard",
      "start": "control keyboard",
      "kurz": "Tastatur",
      "lang": "Startet ein Systemsteuerungsfenster (Tastatur). Aufruf: control keyboard",
      "destruktiv": false
    },
    {
      "kategorie": "control",
      "befehl": "control mouse",
      "start": "control mouse",
      "kurz": "Maus",
      "lang": "Startet ein Systemsteuerungsfenster (Maus). Aufruf: control mouse",
      "destruktiv": false
    },
    {
      "kategorie": "control",
      "befehl": "control netconnections",
      "start": "control netconnections",
      "kurz": "Netzwerkverbindungen",
      "lang": "Startet ein Systemsteuerungsfenster (Netzwerkverbindungen). Aufruf: control netconnections",
      "destruktiv": false
    },
    {
      "kategorie": "control",
      "befehl": "control powercfg.cpl",
      "start": "control powercfg.cpl",
      "kurz": "Energieoptionen",
      "lang": "Startet ein Systemsteuerungsfenster (Energieoptionen). Aufruf: control powercfg.cpl",
      "destruktiv": false
    },
    {
      "kategorie": "control",
      "befehl": "control sysdm.cpl",
      "start": "control sysdm.cpl",
      "kurz": "Systemeigenschaften",
      "lang": "Startet ein Systemsteuerungsfenster (Systemeigenschaften). Aufruf: control sysdm.cpl",
      "destruktiv": false
    },
    {
      "kategorie": "control",
      "befehl": "control timedate.cpl",
      "start": "control timedate.cpl",
      "kurz": "Datum & Uhrzeit",
      "lang": "Startet ein Systemsteuerungsfenster (Datum & Uhrzeit). Aufruf: control timedate.cpl",
      "destruktiv": false
    },
    {
      "kategorie": "control",
      "befehl": "control firewall.cpl",
      "start": "control firewall.cpl",
      "kurz": "Firewall",
      "lang": "Startet ein Systemsteuerungsfenster (Firewall). Aufruf: control firewall.cpl",
      "destruktiv": false
    },
    {
      "kategorie": "control",
      "befehl": "control inetcpl.cpl",
      "start": "control inetcpl.cpl",
      "kurz": "Internetoptionen",
      "lang": "Startet ein Systemsteuerungsfenster (Internetoptionen). Aufruf: control inetcpl.cpl",
      "destruktiv": false
    },
    {
      "kategorie": "control",
      "befehl": "control appwiz.cpl",
      "start": "control appwiz.cpl",
      "kurz": "Programme & Features",
      "lang": "Startet ein Systemsteuerungsfenster (Programme & Features). Aufruf: control appwiz.cpl",
      "destruktiv": false
    },
    {
      "kategorie": "control",
      "befehl": "control desk.cpl",
      "start": "control desk.cpl",
      "kurz": "Anzeige",
      "lang": "Startet ein Systemsteuerungsfenster (Anzeige). Aufruf: control desk.cpl",
      "destruktiv": false
    },
    {
      "kategorie": "control",
      "befehl": "control main.cpl",
      "start": "control main.cpl",
      "kurz": "Maus",
      "lang": "Startet ein Systemsteuerungsfenster (Maus). Aufruf: control main.cpl",
      "destruktiv": false
    },
    {
      "kategorie": "control",
      "befehl": "control mmsys.cpl",
      "start": "control mmsys.cpl",
      "kurz": "Sound",
      "lang": "Startet ein Systemsteuerungsfenster (Sound). Aufruf: control mmsys.cpl",
      "destruktiv": false
    },
    {
      "kategorie": "control",
      "befehl": "control ncpa.cpl",
      "start": "control ncpa.cpl",
      "kurz": "Netzwerkadapter",
      "lang": "Startet ein Systemsteuerungsfenster (Netzwerkadapter). Aufruf: control ncpa.cpl",
      "destruktiv": false
    },
    {
      "kategorie": "control",
      "befehl": "control hdwwiz.cpl",
      "start": "control hdwwiz.cpl",
      "kurz": "Geräte-Manager",
      "lang": "Startet ein Systemsteuerungsfenster (Geräte-Manager). Aufruf: control hdwwiz.cpl",
      "destruktiv": false
    },
    {
      "kategorie": "control",
      "befehl": "control fonts",
      "start": "control fonts",
      "kurz": "Schriftarten",
      "lang": "Startet ein Systemsteuerungsfenster (Schriftarten). Aufruf: control fonts",
      "destruktiv": false
    },
    {
      "kategorie": "control",
      "befehl": "control userpasswords2",
      "start": "control userpasswords2",
      "kurz": "Benutzerkonten",
      "lang": "Startet ein Systemsteuerungsfenster (Benutzerkonten). Aufruf: control userpasswords2",
      "destruktiv": false
    },
    {
      "kategorie": "control",
      "befehl": "control wscui.cpl",
      "start": "control wscui.cpl",
      "kurz": "Sicherheitscenter",
      "lang": "Startet ein Systemsteuerungsfenster (Sicherheitscenter). Aufruf: control wscui.cpl",
      "destruktiv": false
    },
    {
      "kategorie": "control",
      "befehl": "control admintools",
      "start": "control admintools",
      "kurz": "Verwaltung",
      "lang": "Startet ein Systemsteuerungsfenster (Verwaltung). Aufruf: control admintools",
      "destruktiv": false
    },
    {
      "kategorie": "control",
      "befehl": "control color",
      "start": "control color",
      "kurz": "Farbverwaltung",
      "lang": "Startet ein Systemsteuerungsfenster (Farbverwaltung). Aufruf: control color",
      "destruktiv": false
    },
    {
      "kategorie": "control",
      "befehl": "control folders",
      "start": "control folders",
      "kurz": "Ordneroptionen",
      "lang": "Startet ein Systemsteuerungsfenster (Ordneroptionen). Aufruf: control folders",
      "destruktiv": false
    },
    {
      "kategorie": "control",
      "befehl": "control gamecontrollers",
      "start": "control gamecontrollers",
      "kurz": "Gamecontroller",
      "lang": "Startet ein Systemsteuerungsfenster (Gamecontroller). Aufruf: control gamecontrollers",
      "destruktiv": false
    },
    {
      "kategorie": "control",
      "befehl": "control irprops.cpl",
      "start": "control irprops.cpl",
      "kurz": "Infrarot",
      "lang": "Startet ein Systemsteuerungsfenster (Infrarot). Aufruf: control irprops.cpl",
      "destruktiv": false
    },
    {
      "kategorie": "control",
      "befehl": "control joy.cpl",
      "start": "control joy.cpl",
      "kurz": "Joystick",
      "lang": "Startet ein Systemsteuerungsfenster (Joystick). Aufruf: control joy.cpl",
      "destruktiv": false
    },
    {
      "kategorie": "control",
      "befehl": "control telephon.cpl",
      "start": "control telephon.cpl",
      "kurz": "Telefonie",
      "lang": "Startet ein Systemsteuerungsfenster (Telefonie). Aufruf: control telephon.cpl",
      "destruktiv": false
    },
    {
      "kategorie": "control",
      "befehl": "control tabletpc.cpl",
      "start": "control tabletpc.cpl",
      "kurz": "Tablet PC Einstellungen",
      "lang": "Startet ein Systemsteuerungsfenster (Tablet PC Einstellungen). Aufruf: control tabletpc.cpl",
      "destruktiv": false
    },
    {
      "kategorie": "control",
      "befehl": "control access.cpl",
      "start": "control access.cpl",
      "kurz": "Eingabehilfen",
      "lang": "Startet ein Systemsteuerungsfenster (Eingabehilfen). Aufruf: control access.cpl",
      "destruktiv": false
    },
    {
      "kategorie": "control",
      "befehl": "control nusrmgr.cpl",
      "start": "control nusrmgr.cpl",
      "kurz": "Benutzerkonten (alt)",
      "lang": "Startet ein Systemsteuerungsfenster (Benutzerkonten (alt)). Aufruf: control nusrmgr.cpl",
      "destruktiv": false
    },
    {
      "kategorie": "control",
      "befehl": "control odbccp32.cpl",
      "start": "control odbccp32.cpl",
      "kurz": "ODBC-Datenquellen",
      "lang": "Startet ein Systemsteuerungsfenster (ODBC-Datenquellen). Aufruf: control odbccp32.cpl",
      "destruktiv": false
    },
    {
      "kategorie": "control",
      "befehl": "control password.cpl",
      "start": "control password.cpl",
      "kurz": "Kennwörter",
      "lang": "Startet ein Systemsteuerungsfenster (Kennwörter). Aufruf: control password.cpl",
      "destruktiv": false
    },
    {
      "kategorie": "control",
      "befehl": "control sapi.cpl",
      "start": "control sapi.cpl",
      "kurz": "Spracherkennung",
      "lang": "Startet ein Systemsteuerungsfenster (Spracherkennung). Aufruf: control sapi.cpl",
      "destruktiv": false
    },
    {
      "kategorie": "control",
      "befehl": "control srchadmin.dll",
      "start": "control srchadmin.dll",
      "kurz": "Sucheinstellungen",
      "lang": "Startet ein Systemsteuerungsfenster (Sucheinstellungen). Aufruf: control srchadmin.dll",
      "destruktiv": false
    },
    {
      "kategorie": "control",
      "befehl": "control storprop.dll",
      "start": "control storprop.dll",
      "kurz": "Speicherverwaltung",
      "lang": "Startet ein Systemsteuerungsfenster (Speicherverwaltung). Aufruf: control storprop.dll",
      "destruktiv": false
    },
    {
      "kategorie": "control",
      "befehl": "control themecpl.dll",
      "start": "control themecpl.dll",
      "kurz": "Themes",
      "lang": "Startet ein Systemsteuerungsfenster (Themes). Aufruf: control themecpl.dll",
      "destruktiv": false
    },
    {
      "kategorie": "control",
      "befehl": "control userpasswords",
      "start": "control userpasswords",
      "kurz": "Benutzerkonten",
      "lang": "Startet ein Systemsteuerungsfenster (Benutzerkonten). Aufruf: control userpasswords",
      "destruktiv": false
    },
    {
      "kategorie": "control",
      "befehl": "control wuaucpl.cpl",
      "start": "control wuaucpl.cpl",
      "kurz": "Windows Update (alt)",
      "lang": "Startet ein Systemsteuerungsfenster (Windows Update (alt)). Aufruf: control wuaucpl.cpl",
      "destruktiv": false
    },
    {
      "kategorie": "rundll32",
      "befehl": "rundll32.exe shell32.dll,Control_RunDLL",
      "start": "rundll32.exe shell32.dll,Control_RunDLL",
      "kurz": "Systemsteuerung",
      "lang": "Ruft eine System-DLL auf und oeffnet 'Systemsteuerung'. Aufruf: rundll32.exe shell32.dll,Control_RunDLL",
      "destruktiv": false
    },
    {
      "kategorie": "rundll32",
      "befehl": "rundll32.exe shell32.dll,Options_RunDLL 0",
      "start": "rundll32.exe shell32.dll,Options_RunDLL 0",
      "kurz": "Ordneroptionen",
      "lang": "Ruft eine System-DLL auf und oeffnet 'Ordneroptionen'. Aufruf: rundll32.exe shell32.dll,Options_RunDLL 0",
      "destruktiv": false
    },
    {
      "kategorie": "rundll32",
      "befehl": "rundll32.exe shell32.dll,SHHelpShortcuts_RunDLL",
      "start": "rundll32.exe shell32.dll,SHHelpShortcuts_RunDLL",
      "kurz": "Hilfe",
      "lang": "Ruft eine System-DLL auf und oeffnet 'Hilfe'. Aufruf: rundll32.exe shell32.dll,SHHelpShortcuts_RunDLL",
      "destruktiv": false
    },
    {
      "kategorie": "rundll32",
      "befehl": "rundll32.exe shell32.dll,Control_RunDLL hotplug.dll",
      "start": "rundll32.exe shell32.dll,Control_RunDLL hotplug.dll",
      "kurz": "Hardware sicher entfernen",
      "lang": "Ruft eine System-DLL auf und oeffnet 'Hardware sicher entfernen'. Aufruf: rundll32.exe shell32.dll,Control_RunDLL hotplug.dll",
      "destruktiv": false
    },
    {
      "kategorie": "rundll32",
      "befehl": "rundll32.exe shell32.dll,Control_RunDLL access.cpl",
      "start": "rundll32.exe shell32.dll,Control_RunDLL access.cpl",
      "kurz": "Eingabehilfen",
      "lang": "Ruft eine System-DLL auf und oeffnet 'Eingabehilfen'. Aufruf: rundll32.exe shell32.dll,Control_RunDLL access.cpl",
      "destruktiv": false
    },
    {
      "kategorie": "rundll32",
      "befehl": "rundll32.exe shell32.dll,Control_RunDLL nusrmgr.cpl",
      "start": "rundll32.exe shell32.dll,Control_RunDLL nusrmgr.cpl",
      "kurz": "Benutzerkonten",
      "lang": "Ruft eine System-DLL auf und oeffnet 'Benutzerkonten'. Aufruf: rundll32.exe shell32.dll,Control_RunDLL nusrmgr.cpl",
      "destruktiv": false
    },
    {
      "kategorie": "rundll32",
      "befehl": "rundll32.exe shell32.dll,Control_RunDLL powercfg.cpl",
      "start": "rundll32.exe shell32.dll,Control_RunDLL powercfg.cpl",
      "kurz": "Energieoptionen",
      "lang": "Ruft eine System-DLL auf und oeffnet 'Energieoptionen'. Aufruf: rundll32.exe shell32.dll,Control_RunDLL powercfg.cpl",
      "destruktiv": false
    },
    {
      "kategorie": "rundll32",
      "befehl": "rundll32.exe shell32.dll,Control_RunDLL appwiz.cpl",
      "start": "rundll32.exe shell32.dll,Control_RunDLL appwiz.cpl",
      "kurz": "Programme & Features",
      "lang": "Ruft eine System-DLL auf und oeffnet 'Programme & Features'. Aufruf: rundll32.exe shell32.dll,Control_RunDLL appwiz.cpl",
      "destruktiv": false
    },
    {
      "kategorie": "rundll32",
      "befehl": "rundll32.exe shell32.dll,Control_RunDLL firewall.cpl",
      "start": "rundll32.exe shell32.dll,Control_RunDLL firewall.cpl",
      "kurz": "Firewall",
      "lang": "Ruft eine System-DLL auf und oeffnet 'Firewall'. Aufruf: rundll32.exe shell32.dll,Control_RunDLL firewall.cpl",
      "destruktiv": false
    },
    {
      "kategorie": "rundll32",
      "befehl": "rundll32.exe shell32.dll,Control_RunDLL inetcpl.cpl",
      "start": "rundll32.exe shell32.dll,Control_RunDLL inetcpl.cpl",
      "kurz": "Internetoptionen",
      "lang": "Ruft eine System-DLL auf und oeffnet 'Internetoptionen'. Aufruf: rundll32.exe shell32.dll,Control_RunDLL inetcpl.cpl",
      "destruktiv": false
    },
    {
      "kategorie": "rundll32",
      "befehl": "rundll32.exe shell32.dll,Control_RunDLL timedate.cpl",
      "start": "rundll32.exe shell32.dll,Control_RunDLL timedate.cpl",
      "kurz": "Datum/Uhrzeit",
      "lang": "Ruft eine System-DLL auf und oeffnet 'Datum/Uhrzeit'. Aufruf: rundll32.exe shell32.dll,Control_RunDLL timedate.cpl",
      "destruktiv": false
    },
    {
      "kategorie": "rundll32",
      "befehl": "rundll32.exe shell32.dll,Control_RunDLL sysdm.cpl",
      "start": "rundll32.exe shell32.dll,Control_RunDLL sysdm.cpl",
      "kurz": "Systemeigenschaften",
      "lang": "Ruft eine System-DLL auf und oeffnet 'Systemeigenschaften'. Aufruf: rundll32.exe shell32.dll,Control_RunDLL sysdm.cpl",
      "destruktiv": false
    },
    {
      "kategorie": "rundll32",
      "befehl": "rundll32.exe shell32.dll,Control_RunDLL ncpa.cpl",
      "start": "rundll32.exe shell32.dll,Control_RunDLL ncpa.cpl",
      "kurz": "Netzwerkadapter",
      "lang": "Ruft eine System-DLL auf und oeffnet 'Netzwerkadapter'. Aufruf: rundll32.exe shell32.dll,Control_RunDLL ncpa.cpl",
      "destruktiv": false
    },
    {
      "kategorie": "rundll32",
      "befehl": "rundll32.exe shell32.dll,Control_RunDLL hdwwiz.cpl",
      "start": "rundll32.exe shell32.dll,Control_RunDLL hdwwiz.cpl",
      "kurz": "Geräte-Manager",
      "lang": "Ruft eine System-DLL auf und oeffnet 'Geräte-Manager'. Aufruf: rundll32.exe shell32.dll,Control_RunDLL hdwwiz.cpl",
      "destruktiv": false
    },
    {
      "kategorie": "rundll32",
      "befehl": "rundll32.exe shell32.dll,Control_RunDLL mmsys.cpl",
      "start": "rundll32.exe shell32.dll,Control_RunDLL mmsys.cpl",
      "kurz": "Sound",
      "lang": "Ruft eine System-DLL auf und oeffnet 'Sound'. Aufruf: rundll32.exe shell32.dll,Control_RunDLL mmsys.cpl",
      "destruktiv": false
    },
    {
      "kategorie": "rundll32",
      "befehl": "rundll32.exe shell32.dll,Control_RunDLL desk.cpl",
      "start": "rundll32.exe shell32.dll,Control_RunDLL desk.cpl",
      "kurz": "Anzeige",
      "lang": "Ruft eine System-DLL auf und oeffnet 'Anzeige'. Aufruf: rundll32.exe shell32.dll,Control_RunDLL desk.cpl",
      "destruktiv": false
    },
    {
      "kategorie": "rundll32",
      "befehl": "rundll32.exe shell32.dll,Control_RunDLL joy.cpl",
      "start": "rundll32.exe shell32.dll,Control_RunDLL joy.cpl",
      "kurz": "Joystick",
      "lang": "Ruft eine System-DLL auf und oeffnet 'Joystick'. Aufruf: rundll32.exe shell32.dll,Control_RunDLL joy.cpl",
      "destruktiv": false
    },
    {
      "kategorie": "rundll32",
      "befehl": "rundll32.exe shell32.dll,Control_RunDLL tabletpc.cpl",
      "start": "rundll32.exe shell32.dll,Control_RunDLL tabletpc.cpl",
      "kurz": "Tablet PC",
      "lang": "Ruft eine System-DLL auf und oeffnet 'Tablet PC'. Aufruf: rundll32.exe shell32.dll,Control_RunDLL tabletpc.cpl",
      "destruktiv": false
    },
    {
      "kategorie": "rundll32",
      "befehl": "rundll32.exe shell32.dll,Control_RunDLL telephon.cpl",
      "start": "rundll32.exe shell32.dll,Control_RunDLL telephon.cpl",
      "kurz": "Telefonie",
      "lang": "Ruft eine System-DLL auf und oeffnet 'Telefonie'. Aufruf: rundll32.exe shell32.dll,Control_RunDLL telephon.cpl",
      "destruktiv": false
    },
    {
      "kategorie": "rundll32",
      "befehl": "rundll32.exe shell32.dll,Control_RunDLL odbccp32.cpl",
      "start": "rundll32.exe shell32.dll,Control_RunDLL odbccp32.cpl",
      "kurz": "ODBC",
      "lang": "Ruft eine System-DLL auf und oeffnet 'ODBC'. Aufruf: rundll32.exe shell32.dll,Control_RunDLL odbccp32.cpl",
      "destruktiv": false
    },
    {
      "kategorie": "rundll32",
      "befehl": "rundll32.exe shell32.dll,Control_RunDLL srchadmin.dll",
      "start": "rundll32.exe shell32.dll,Control_RunDLL srchadmin.dll",
      "kurz": "Suche",
      "lang": "Ruft eine System-DLL auf und oeffnet 'Suche'. Aufruf: rundll32.exe shell32.dll,Control_RunDLL srchadmin.dll",
      "destruktiv": false
    },
    {
      "kategorie": "rundll32",
      "befehl": "rundll32.exe shell32.dll,Control_RunDLL color",
      "start": "rundll32.exe shell32.dll,Control_RunDLL color",
      "kurz": "Farbverwaltung",
      "lang": "Ruft eine System-DLL auf und oeffnet 'Farbverwaltung'. Aufruf: rundll32.exe shell32.dll,Control_RunDLL color",
      "destruktiv": false
    },
    {
      "kategorie": "explorer",
      "befehl": "explorer.exe shell:MyComputerFolder",
      "start": "explorer.exe shell:MyComputerFolder",
      "kurz": "Dieser PC",
      "lang": "Startet den Explorer mit einem bekannten Ordner oder einer URI (Dieser PC). Aufruf: explorer.exe shell:MyComputerFolder",
      "destruktiv": false
    },
    {
      "kategorie": "explorer",
      "befehl": "explorer.exe shell:NetworkPlacesFolder",
      "start": "explorer.exe shell:NetworkPlacesFolder",
      "kurz": "Netzwerk",
      "lang": "Startet den Explorer mit einem bekannten Ordner oder einer URI (Netzwerk). Aufruf: explorer.exe shell:NetworkPlacesFolder",
      "destruktiv": false
    },
    {
      "kategorie": "explorer",
      "befehl": "explorer.exe shell:RecycleBinFolder",
      "start": "explorer.exe shell:RecycleBinFolder",
      "kurz": "Papierkorb",
      "lang": "Startet den Explorer mit einem bekannten Ordner oder einer URI (Papierkorb). Aufruf: explorer.exe shell:RecycleBinFolder",
      "destruktiv": false
    },
    {
      "kategorie": "explorer",
      "befehl": "explorer.exe shell:ControlPanelFolder",
      "start": "explorer.exe shell:ControlPanelFolder",
      "kurz": "Systemsteuerung",
      "lang": "Startet den Explorer mit einem bekannten Ordner oder einer URI (Systemsteuerung). Aufruf: explorer.exe shell:ControlPanelFolder",
      "destruktiv": false
    },
    {
      "kategorie": "explorer",
      "befehl": "explorer.exe shell:Libraries",
      "start": "explorer.exe shell:Libraries",
      "kurz": "Bibliotheken",
      "lang": "Startet den Explorer mit einem bekannten Ordner oder einer URI (Bibliotheken). Aufruf: explorer.exe shell:Libraries",
      "destruktiv": false
    },
    {
      "kategorie": "explorer",
      "befehl": "explorer.exe shell:Downloads",
      "start": "explorer.exe shell:Downloads",
      "kurz": "Downloads",
      "lang": "Startet den Explorer mit einem bekannten Ordner oder einer URI (Downloads). Aufruf: explorer.exe shell:Downloads",
      "destruktiv": false
    },
    {
      "kategorie": "explorer",
      "befehl": "explorer.exe shell:HomeGroup",
      "start": "explorer.exe shell:HomeGroup",
      "kurz": "Heimnetzgruppe (Legacy)",
      "lang": "Startet den Explorer mit einem bekannten Ordner oder einer URI (Heimnetzgruppe (Legacy)). Aufruf: explorer.exe shell:HomeGroup",
      "destruktiv": false
    },
    {
      "kategorie": "explorer",
      "befehl": "explorer.exe shell:AppsFolder",
      "start": "explorer.exe shell:AppsFolder",
      "kurz": "Apps",
      "lang": "Startet den Explorer mit einem bekannten Ordner oder einer URI (Apps). Aufruf: explorer.exe shell:AppsFolder",
      "destruktiv": false
    },
    {
      "kategorie": "explorer",
      "befehl": "explorer.exe shell:OneDrive",
      "start": "explorer.exe shell:OneDrive",
      "kurz": "OneDrive",
      "lang": "Startet den Explorer mit einem bekannten Ordner oder einer URI (OneDrive). Aufruf: explorer.exe shell:OneDrive",
      "destruktiv": false
    },
    {
      "kategorie": "explorer",
      "befehl": "explorer.exe shell:OneDriveDocuments",
      "start": "explorer.exe shell:OneDriveDocuments",
      "kurz": "OneDrive Dokumente",
      "lang": "Startet den Explorer mit einem bekannten Ordner oder einer URI (OneDrive Dokumente). Aufruf: explorer.exe shell:OneDriveDocuments",
      "destruktiv": false
    },
    {
      "kategorie": "explorer",
      "befehl": "explorer.exe shell:OneDrivePictures",
      "start": "explorer.exe shell:OneDrivePictures",
      "kurz": "OneDrive Bilder",
      "lang": "Startet den Explorer mit einem bekannten Ordner oder einer URI (OneDrive Bilder). Aufruf: explorer.exe shell:OneDrivePictures",
      "destruktiv": false
    },
    {
      "kategorie": "explorer",
      "befehl": "explorer.exe shell:SavedGames",
      "start": "explorer.exe shell:SavedGames",
      "kurz": "Spiele",
      "lang": "Startet den Explorer mit einem bekannten Ordner oder einer URI (Spiele). Aufruf: explorer.exe shell:SavedGames",
      "destruktiv": false
    },
    {
      "kategorie": "explorer",
      "befehl": "explorer.exe shell:Searches",
      "start": "explorer.exe shell:Searches",
      "kurz": "Suchen",
      "lang": "Startet den Explorer mit einem bekannten Ordner oder einer URI (Suchen). Aufruf: explorer.exe shell:Searches",
      "destruktiv": false
    },
    {
      "kategorie": "explorer",
      "befehl": "explorer.exe shell:Contacts",
      "start": "explorer.exe shell:Contacts",
      "kurz": "Kontakte",
      "lang": "Startet den Explorer mit einem bekannten Ordner oder einer URI (Kontakte). Aufruf: explorer.exe shell:Contacts",
      "destruktiv": false
    },
    {
      "kategorie": "explorer",
      "befehl": "explorer.exe shell:Links",
      "start": "explorer.exe shell:Links",
      "kurz": "Schnellzugriff",
      "lang": "Startet den Explorer mit einem bekannten Ordner oder einer URI (Schnellzugriff). Aufruf: explorer.exe shell:Links",
      "destruktiv": false
    },
    {
      "kategorie": "explorer",
      "befehl": "explorer.exe shell:Favorites",
      "start": "explorer.exe shell:Favorites",
      "kurz": "Favoriten",
      "lang": "Startet den Explorer mit einem bekannten Ordner oder einer URI (Favoriten). Aufruf: explorer.exe shell:Favorites",
      "destruktiv": false
    },
    {
      "kategorie": "explorer",
      "befehl": "explorer.exe shell:Music",
      "start": "explorer.exe shell:Music",
      "kurz": "Musik",
      "lang": "Startet den Explorer mit einem bekannten Ordner oder einer URI (Musik). Aufruf: explorer.exe shell:Music",
      "destruktiv": false
    },
    {
      "kategorie": "explorer",
      "befehl": "explorer.exe shell:Videos",
      "start": "explorer.exe shell:Videos",
      "kurz": "Videos",
      "lang": "Startet den Explorer mit einem bekannten Ordner oder einer URI (Videos). Aufruf: explorer.exe shell:Videos",
      "destruktiv": false
    },
    {
      "kategorie": "mmc",
      "befehl": "mmc devmgmt.msc",
      "start": "mmc devmgmt.msc",
      "kurz": "Geräte-Manager",
      "lang": "Oeffnet das MMC-Snap-In 'Geräte-Manager'. Aufruf: mmc devmgmt.msc",
      "destruktiv": false
    },
    {
      "kategorie": "mmc",
      "befehl": "mmc compmgmt.msc",
      "start": "mmc compmgmt.msc",
      "kurz": "Computerverwaltung",
      "lang": "Oeffnet das MMC-Snap-In 'Computerverwaltung'. Aufruf: mmc compmgmt.msc",
      "destruktiv": false
    },
    {
      "kategorie": "mmc",
      "befehl": "mmc diskmgmt.msc",
      "start": "mmc diskmgmt.msc",
      "kurz": "Datenträgerverwaltung",
      "lang": "Oeffnet das MMC-Snap-In 'Datenträgerverwaltung'. Aufruf: mmc diskmgmt.msc",
      "destruktiv": false
    },
    {
      "kategorie": "mmc",
      "befehl": "mmc eventvwr.msc",
      "start": "mmc eventvwr.msc",
      "kurz": "Ereignisanzeige",
      "lang": "Oeffnet das MMC-Snap-In 'Ereignisanzeige'. Aufruf: mmc eventvwr.msc",
      "destruktiv": false
    },
    {
      "kategorie": "mmc",
      "befehl": "mmc gpedit.msc",
      "start": "mmc gpedit.msc",
      "kurz": "Gruppenrichtlinien",
      "lang": "Oeffnet das MMC-Snap-In 'Gruppenrichtlinien'. Aufruf: mmc gpedit.msc",
      "destruktiv": false
    },
    {
      "kategorie": "mmc",
      "befehl": "mmc secpol.msc",
      "start": "mmc secpol.msc",
      "kurz": "Lokale Sicherheitsrichtlinie",
      "lang": "Oeffnet das MMC-Snap-In 'Lokale Sicherheitsrichtlinie'. Aufruf: mmc secpol.msc",
      "destruktiv": false
    },
    {
      "kategorie": "mmc",
      "befehl": "mmc services.msc",
      "start": "mmc services.msc",
      "kurz": "Dienste",
      "lang": "Oeffnet das MMC-Snap-In 'Dienste'. Aufruf: mmc services.msc",
      "destruktiv": false
    },
    {
      "kategorie": "mmc",
      "befehl": "mmc taskschd.msc",
      "start": "mmc taskschd.msc",
      "kurz": "Aufgabenplanung",
      "lang": "Oeffnet das MMC-Snap-In 'Aufgabenplanung'. Aufruf: mmc taskschd.msc",
      "destruktiv": false
    },
    {
      "kategorie": "mmc",
      "befehl": "mmc perfmon.msc",
      "start": "mmc perfmon.msc",
      "kurz": "Leistungsüberwachung",
      "lang": "Oeffnet das MMC-Snap-In 'Leistungsüberwachung'. Aufruf: mmc perfmon.msc",
      "destruktiv": false
    },
    {
      "kategorie": "mmc",
      "befehl": "mmc printmanagement.msc",
      "start": "mmc printmanagement.msc",
      "kurz": "Druckerverwaltung",
      "lang": "Oeffnet das MMC-Snap-In 'Druckerverwaltung'. Aufruf: mmc printmanagement.msc",
      "destruktiv": false
    },
    {
      "kategorie": "mmc",
      "befehl": "mmc wf.msc",
      "start": "mmc wf.msc",
      "kurz": "Windows Firewall",
      "lang": "Oeffnet das MMC-Snap-In 'Windows Firewall'. Aufruf: mmc wf.msc",
      "destruktiv": false
    },
    {
      "kategorie": "mmc",
      "befehl": "mmc certmgr.msc",
      "start": "mmc certmgr.msc",
      "kurz": "Zertifikate",
      "lang": "Oeffnet das MMC-Snap-In 'Zertifikate'. Aufruf: mmc certmgr.msc",
      "destruktiv": false
    },
    {
      "kategorie": "mmc",
      "befehl": "mmc lusrmgr.msc",
      "start": "mmc lusrmgr.msc",
      "kurz": "Benutzer & Gruppen",
      "lang": "Oeffnet das MMC-Snap-In 'Benutzer & Gruppen'. Aufruf: mmc lusrmgr.msc",
      "destruktiv": false
    },
    {
      "kategorie": "mmc",
      "befehl": "mmc fsmgmt.msc",
      "start": "mmc fsmgmt.msc",
      "kurz": "Freigaben",
      "lang": "Oeffnet das MMC-Snap-In 'Freigaben'. Aufruf: mmc fsmgmt.msc",
      "destruktiv": false
    },
    {
      "kategorie": "mmc",
      "befehl": "mmc virtmgmt.msc",
      "start": "mmc virtmgmt.msc",
      "kurz": "Hyper-V Manager",
      "lang": "Oeffnet das MMC-Snap-In 'Hyper-V Manager'. Aufruf: mmc virtmgmt.msc",
      "destruktiv": false
    },
    {
      "kategorie": "mmc",
      "befehl": "mmc rsop.msc",
      "start": "mmc rsop.msc",
      "kurz": "Resultant Set of Policy",
      "lang": "Oeffnet das MMC-Snap-In 'Resultant Set of Policy'. Aufruf: mmc rsop.msc",
      "destruktiv": false
    },
    {
      "kategorie": "mmc",
      "befehl": "mmc tsmmc.msc",
      "start": "mmc tsmmc.msc",
      "kurz": "Terminal Services",
      "lang": "Oeffnet das MMC-Snap-In 'Terminal Services'. Aufruf: mmc tsmmc.msc",
      "destruktiv": false
    },
    {
      "kategorie": "mmc",
      "befehl": "mmc azman.msc",
      "start": "mmc azman.msc",
      "kurz": "Autorisierungsmanager",
      "lang": "Oeffnet das MMC-Snap-In 'Autorisierungsmanager'. Aufruf: mmc azman.msc",
      "destruktiv": false
    },
    {
      "kategorie": "mmc",
      "befehl": "mmc comexp.msc",
      "start": "mmc comexp.msc",
      "kurz": "COM+ Verwaltung",
      "lang": "Oeffnet das MMC-Snap-In 'COM+ Verwaltung'. Aufruf: mmc comexp.msc",
      "destruktiv": false
    },
    {
      "kategorie": "mmc",
      "befehl": "mmc dfrgui.msc",
      "start": "mmc dfrgui.msc",
      "kurz": "Defragmentierung",
      "lang": "Oeffnet das MMC-Snap-In 'Defragmentierung'. Aufruf: mmc dfrgui.msc",
      "destruktiv": false
    },
    {
      "kategorie": "mmc",
      "befehl": "mmc diskperf.msc",
      "start": "mmc diskperf.msc",
      "kurz": "Datenträgerleistung",
      "lang": "Oeffnet das MMC-Snap-In 'Datenträgerleistung'. Aufruf: mmc diskperf.msc",
      "destruktiv": false
    },
    {
      "kategorie": "mmc",
      "befehl": "mmc diskraid.msc",
      "start": "mmc diskraid.msc",
      "kurz": "RAID Verwaltung",
      "lang": "Oeffnet das MMC-Snap-In 'RAID Verwaltung'. Aufruf: mmc diskraid.msc",
      "destruktiv": false
    },
    {
      "kategorie": "mmc",
      "befehl": "mmc diskguid.msc",
      "start": "mmc diskguid.msc",
      "kurz": "Datenträger-GUID",
      "lang": "Oeffnet das MMC-Snap-In 'Datenträger-GUID'. Aufruf: mmc diskguid.msc",
      "destruktiv": false
    },
    {
      "kategorie": "mmc",
      "befehl": "mmc dnsmgmt.msc",
      "start": "mmc dnsmgmt.msc",
      "kurz": "DNS Verwaltung",
      "lang": "Oeffnet das MMC-Snap-In 'DNS Verwaltung'. Aufruf: mmc dnsmgmt.msc",
      "destruktiv": false
    },
    {
      "kategorie": "mmc",
      "befehl": "mmc domain.msc",
      "start": "mmc domain.msc",
      "kurz": "Domainverwaltung",
      "lang": "Oeffnet das MMC-Snap-In 'Domainverwaltung'. Aufruf: mmc domain.msc",
      "destruktiv": false
    },
    {
      "kategorie": "mmc",
      "befehl": "mmc dhcpmgmt.msc",
      "start": "mmc dhcpmgmt.msc",
      "kurz": "DHCP Verwaltung",
      "lang": "Oeffnet das MMC-Snap-In 'DHCP Verwaltung'. Aufruf: mmc dhcpmgmt.msc",
      "destruktiv": false
    },
    {
      "kategorie": "mmc",
      "befehl": "mmc adsi.msc",
      "start": "mmc adsi.msc",
      "kurz": "ADSI Editor",
      "lang": "Oeffnet das MMC-Snap-In 'ADSI Editor'. Aufruf: mmc adsi.msc",
      "destruktiv": false
    },
    {
      "kategorie": "mmc",
      "befehl": "mmc adfs.msc",
      "start": "mmc adfs.msc",
      "kurz": "ADFS Verwaltung",
      "lang": "Oeffnet das MMC-Snap-In 'ADFS Verwaltung'. Aufruf: mmc adfs.msc",
      "destruktiv": false
    },
    {
      "kategorie": "mmc",
      "befehl": "mmc adfsrapid.msc",
      "start": "mmc adfsrapid.msc",
      "kurz": "ADFS Schnellkonfiguration",
      "lang": "Oeffnet das MMC-Snap-In 'ADFS Schnellkonfiguration'. Aufruf: mmc adfsrapid.msc",
      "destruktiv": false
    },
    {
      "kategorie": "mmc",
      "befehl": "mmc adfsmonitor.msc",
      "start": "mmc adfsmonitor.msc",
      "kurz": "ADFS Monitoring",
      "lang": "Oeffnet das MMC-Snap-In 'ADFS Monitoring'. Aufruf: mmc adfsmonitor.msc",
      "destruktiv": false
    },
    {
      "kategorie": "mmc",
      "befehl": "mmc adfsclaims.msc",
      "start": "mmc adfsclaims.msc",
      "kurz": "ADFS Claims",
      "lang": "Oeffnet das MMC-Snap-In 'ADFS Claims'. Aufruf: mmc adfsclaims.msc",
      "destruktiv": false
    },
    {
      "kategorie": "mmc",
      "befehl": "mmc adfsproxy.msc",
      "start": "mmc adfsproxy.msc",
      "kurz": "ADFS Proxy",
      "lang": "Oeffnet das MMC-Snap-In 'ADFS Proxy'. Aufruf: mmc adfsproxy.msc",
      "destruktiv": false
    },
    {
      "kategorie": "mmc",
      "befehl": "mmc adfsservice.msc",
      "start": "mmc adfsservice.msc",
      "kurz": "ADFS Service",
      "lang": "Oeffnet das MMC-Snap-In 'ADFS Service'. Aufruf: mmc adfsservice.msc",
      "destruktiv": false
    },
    {
      "kategorie": "mmc",
      "befehl": "mmc adfsadmin.msc",
      "start": "mmc adfsadmin.msc",
      "kurz": "ADFS Admin",
      "lang": "Oeffnet das MMC-Snap-In 'ADFS Admin'. Aufruf: mmc adfsadmin.msc",
      "destruktiv": false
    },
    {
      "kategorie": "mmc",
      "befehl": "mmc adfsconfig.msc",
      "start": "mmc adfsconfig.msc",
      "kurz": "ADFS Konfiguration",
      "lang": "Oeffnet das MMC-Snap-In 'ADFS Konfiguration'. Aufruf: mmc adfsconfig.msc",
      "destruktiv": false
    },
    {
      "kategorie": "mmc",
      "befehl": "mmc adfsdiag.msc",
      "start": "mmc adfsdiag.msc",
      "kurz": "ADFS Diagnose",
      "lang": "Oeffnet das MMC-Snap-In 'ADFS Diagnose'. Aufruf: mmc adfsdiag.msc",
      "destruktiv": false
    },
    {
      "kategorie": "mmc",
      "befehl": "mmc adfshealth.msc",
      "start": "mmc adfshealth.msc",
      "kurz": "ADFS Health",
      "lang": "Oeffnet das MMC-Snap-In 'ADFS Health'. Aufruf: mmc adfshealth.msc",
      "destruktiv": false
    },
    {
      "kategorie": "mmc",
      "befehl": "mmc adfsreport.msc",
      "start": "mmc adfsreport.msc",
      "kurz": "ADFS Reports",
      "lang": "Oeffnet das MMC-Snap-In 'ADFS Reports'. Aufruf: mmc adfsreport.msc",
      "destruktiv": false
    },
    {
      "kategorie": "mmc",
      "befehl": "mmc adfsbackup.msc",
      "start": "mmc adfsbackup.msc",
      "kurz": "ADFS Backup",
      "lang": "Oeffnet das MMC-Snap-In 'ADFS Backup'. Aufruf: mmc adfsbackup.msc",
      "destruktiv": false
    },
    {
      "kategorie": "admin",
      "befehl": "secpol.msc",
      "start": "secpol.msc",
      "kurz": "Sicherheitsrichtlinie",
      "lang": "Oeffnet das MMC-Snap-In 'Sicherheitsrichtlinie'. Aufruf: secpol.msc",
      "destruktiv": false
    },
    {
      "kategorie": "admin",
      "befehl": "services.msc",
      "start": "services.msc",
      "kurz": "Dienste",
      "lang": "Oeffnet das MMC-Snap-In 'Dienste'. Aufruf: services.msc",
      "destruktiv": false
    },
    {
      "kategorie": "admin",
      "befehl": "taskschd.msc",
      "start": "taskschd.msc",
      "kurz": "Aufgabenplanung",
      "lang": "Oeffnet das MMC-Snap-In 'Aufgabenplanung'. Aufruf: taskschd.msc",
      "destruktiv": false
    },
    {
      "kategorie": "admin",
      "befehl": "wf.msc",
      "start": "wf.msc",
      "kurz": "Firewall",
      "lang": "Oeffnet das MMC-Snap-In 'Firewall'. Aufruf: wf.msc",
      "destruktiv": false
    },
    {
      "kategorie": "admin",
      "befehl": "certmgr.msc",
      "start": "certmgr.msc",
      "kurz": "Zertifikate",
      "lang": "Oeffnet das MMC-Snap-In 'Zertifikate'. Aufruf: certmgr.msc",
      "destruktiv": false
    },
    {
      "kategorie": "admin",
      "befehl": "lusrmgr.msc",
      "start": "lusrmgr.msc",
      "kurz": "Benutzer & Gruppen",
      "lang": "Oeffnet das MMC-Snap-In 'Benutzer & Gruppen'. Aufruf: lusrmgr.msc",
      "destruktiv": false
    },
    {
      "kategorie": "admin",
      "befehl": "compmgmt.msc",
      "start": "compmgmt.msc",
      "kurz": "Computerverwaltung",
      "lang": "Oeffnet das MMC-Snap-In 'Computerverwaltung'. Aufruf: compmgmt.msc",
      "destruktiv": false
    },
    {
      "kategorie": "admin",
      "befehl": "perfmon.msc",
      "start": "perfmon.msc",
      "kurz": "Leistungsüberwachung",
      "lang": "Oeffnet das MMC-Snap-In 'Leistungsüberwachung'. Aufruf: perfmon.msc",
      "destruktiv": false
    },
    {
      "kategorie": "admin",
      "befehl": "printmanagement.msc",
      "start": "printmanagement.msc",
      "kurz": "Druckerverwaltung",
      "lang": "Oeffnet das MMC-Snap-In 'Druckerverwaltung'. Aufruf: printmanagement.msc",
      "destruktiv": false
    },
    {
      "kategorie": "admin",
      "befehl": "fsmgmt.msc",
      "start": "fsmgmt.msc",
      "kurz": "Freigaben",
      "lang": "Oeffnet das MMC-Snap-In 'Freigaben'. Aufruf: fsmgmt.msc",
      "destruktiv": false
    },
    {
      "kategorie": "admin",
      "befehl": "diskmgmt.msc",
      "start": "diskmgmt.msc",
      "kurz": "Datenträgerverwaltung",
      "lang": "Oeffnet das MMC-Snap-In 'Datenträgerverwaltung'. Aufruf: diskmgmt.msc",
      "destruktiv": false
    },
    {
      "kategorie": "admin",
      "befehl": "eventvwr.msc",
      "start": "eventvwr.msc",
      "kurz": "Ereignisanzeige",
      "lang": "Oeffnet das MMC-Snap-In 'Ereignisanzeige'. Aufruf: eventvwr.msc",
      "destruktiv": false
    },
    {
      "kategorie": "admin",
      "befehl": "gpedit.msc",
      "start": "gpedit.msc",
      "kurz": "Gruppenrichtlinien",
      "lang": "Oeffnet das MMC-Snap-In 'Gruppenrichtlinien'. Aufruf: gpedit.msc",
      "destruktiv": false
    },
    {
      "kategorie": "admin",
      "befehl": "rsop.msc",
      "start": "rsop.msc",
      "kurz": "Richtlinienauswertung",
      "lang": "Oeffnet das MMC-Snap-In 'Richtlinienauswertung'. Aufruf: rsop.msc",
      "destruktiv": false
    },
    {
      "kategorie": "admin",
      "befehl": "azman.msc",
      "start": "azman.msc",
      "kurz": "Autorisierungsmanager",
      "lang": "Oeffnet das MMC-Snap-In 'Autorisierungsmanager'. Aufruf: azman.msc",
      "destruktiv": false
    },
    {
      "kategorie": "admin",
      "befehl": "comexp.msc",
      "start": "comexp.msc",
      "kurz": "COM+ Verwaltung",
      "lang": "Oeffnet das MMC-Snap-In 'COM+ Verwaltung'. Aufruf: comexp.msc",
      "destruktiv": false
    },
    {
      "kategorie": "admin",
      "befehl": "dfrgui.msc",
      "start": "dfrgui.msc",
      "kurz": "Defragmentierung",
      "lang": "Oeffnet das MMC-Snap-In 'Defragmentierung'. Aufruf: dfrgui.msc",
      "destruktiv": false
    },
    {
      "kategorie": "admin",
      "befehl": "devmgmt.msc",
      "start": "devmgmt.msc",
      "kurz": "Geräte-Manager",
      "lang": "Oeffnet das MMC-Snap-In 'Geräte-Manager'. Aufruf: devmgmt.msc",
      "destruktiv": false
    },
    {
      "kategorie": "admin",
      "befehl": "virtmgmt.msc",
      "start": "virtmgmt.msc",
      "kurz": "Hyper-V Manager",
      "lang": "Oeffnet das MMC-Snap-In 'Hyper-V Manager'. Aufruf: virtmgmt.msc",
      "destruktiv": false
    },
    {
      "kategorie": "admin",
      "befehl": "dnsmgmt.msc",
      "start": "dnsmgmt.msc",
      "kurz": "DNS Verwaltung",
      "lang": "Oeffnet das MMC-Snap-In 'DNS Verwaltung'. Aufruf: dnsmgmt.msc",
      "destruktiv": false
    },
    {
      "kategorie": "admin",
      "befehl": "dhcpmgmt.msc",
      "start": "dhcpmgmt.msc",
      "kurz": "DHCP Verwaltung",
      "lang": "Oeffnet das MMC-Snap-In 'DHCP Verwaltung'. Aufruf: dhcpmgmt.msc",
      "destruktiv": false
    },
    {
      "kategorie": "admin",
      "befehl": "adsi.msc",
      "start": "adsi.msc",
      "kurz": "ADSI Editor",
      "lang": "Oeffnet das MMC-Snap-In 'ADSI Editor'. Aufruf: adsi.msc",
      "destruktiv": false
    },
    {
      "kategorie": "admin",
      "befehl": "adfs.msc",
      "start": "adfs.msc",
      "kurz": "ADFS Verwaltung",
      "lang": "Oeffnet das MMC-Snap-In 'ADFS Verwaltung'. Aufruf: adfs.msc",
      "destruktiv": false
    },
    {
      "kategorie": "admin",
      "befehl": "adfsmonitor.msc",
      "start": "adfsmonitor.msc",
      "kurz": "ADFS Monitoring",
      "lang": "Oeffnet das MMC-Snap-In 'ADFS Monitoring'. Aufruf: adfsmonitor.msc",
      "destruktiv": false
    },
    {
      "kategorie": "admin",
      "befehl": "adfsclaims.msc",
      "start": "adfsclaims.msc",
      "kurz": "ADFS Claims",
      "lang": "Oeffnet das MMC-Snap-In 'ADFS Claims'. Aufruf: adfsclaims.msc",
      "destruktiv": false
    },
    {
      "kategorie": "admin",
      "befehl": "adfsproxy.msc",
      "start": "adfsproxy.msc",
      "kurz": "ADFS Proxy",
      "lang": "Oeffnet das MMC-Snap-In 'ADFS Proxy'. Aufruf: adfsproxy.msc",
      "destruktiv": false
    },
    {
      "kategorie": "admin",
      "befehl": "adfsservice.msc",
      "start": "adfsservice.msc",
      "kurz": "ADFS Service",
      "lang": "Oeffnet das MMC-Snap-In 'ADFS Service'. Aufruf: adfsservice.msc",
      "destruktiv": false
    },
    {
      "kategorie": "admin",
      "befehl": "adfsadmin.msc",
      "start": "adfsadmin.msc",
      "kurz": "ADFS Admin",
      "lang": "Oeffnet das MMC-Snap-In 'ADFS Admin'. Aufruf: adfsadmin.msc",
      "destruktiv": false
    },
    {
      "kategorie": "admin",
      "befehl": "adfsconfig.msc",
      "start": "adfsconfig.msc",
      "kurz": "ADFS Konfiguration",
      "lang": "Oeffnet das MMC-Snap-In 'ADFS Konfiguration'. Aufruf: adfsconfig.msc",
      "destruktiv": false
    },
    {
      "kategorie": "admin",
      "befehl": "adfsdiag.msc",
      "start": "adfsdiag.msc",
      "kurz": "ADFS Diagnose",
      "lang": "Oeffnet das MMC-Snap-In 'ADFS Diagnose'. Aufruf: adfsdiag.msc",
      "destruktiv": false
    },
    {
      "kategorie": "admin",
      "befehl": "adfshealth.msc",
      "start": "adfshealth.msc",
      "kurz": "ADFS Health",
      "lang": "Oeffnet das MMC-Snap-In 'ADFS Health'. Aufruf: adfshealth.msc",
      "destruktiv": false
    },
    {
      "kategorie": "admin",
      "befehl": "adfsreport.msc",
      "start": "adfsreport.msc",
      "kurz": "ADFS Reports",
      "lang": "Oeffnet das MMC-Snap-In 'ADFS Reports'. Aufruf: adfsreport.msc",
      "destruktiv": false
    },
    {
      "kategorie": "admin",
      "befehl": "adfsbackup.msc",
      "start": "adfsbackup.msc",
      "kurz": "ADFS Backup",
      "lang": "Oeffnet das MMC-Snap-In 'ADFS Backup'. Aufruf: adfsbackup.msc",
      "destruktiv": false
    },
    {
      "kategorie": "admin",
      "befehl": "diskraid.msc",
      "start": "diskraid.msc",
      "kurz": "RAID Verwaltung",
      "lang": "Oeffnet das MMC-Snap-In 'RAID Verwaltung'. Aufruf: diskraid.msc",
      "destruktiv": false
    },
    {
      "kategorie": "admin",
      "befehl": "diskperf.msc",
      "start": "diskperf.msc",
      "kurz": "Datenträgerleistung",
      "lang": "Oeffnet das MMC-Snap-In 'Datenträgerleistung'. Aufruf: diskperf.msc",
      "destruktiv": false
    },
    {
      "kategorie": "admin",
      "befehl": "diskguid.msc",
      "start": "diskguid.msc",
      "kurz": "Datenträger-GUID",
      "lang": "Oeffnet das MMC-Snap-In 'Datenträger-GUID'. Aufruf: diskguid.msc",
      "destruktiv": false
    },
    {
      "kategorie": "admin",
      "befehl": "tsmmc.msc",
      "start": "tsmmc.msc",
      "kurz": "Terminal Services",
      "lang": "Oeffnet das MMC-Snap-In 'Terminal Services'. Aufruf: tsmmc.msc",
      "destruktiv": false
    },
    {
      "kategorie": "godmode",
      "befehl": "GodMode",
      "start": "shell:::{ED7BA470-8E54-465E-825C-99712043E01C}",
      "kurz": "Alle Einstellungen",
      "lang": "Oeffnet den Shell-Namespace 'Alle Einstellungen' ueber die CLSID. Aufruf: explorer.exe shell:::{ED7BA470-8E54-465E-825C-99712043E01C}",
      "destruktiv": false
    },
    {
      "kategorie": "godmode",
      "befehl": "GodMode: Administrative Tools",
      "start": "control.exe /name Microsoft.AdministrativeTools",
      "kurz": "Administrative Tools",
      "lang": "Startet ein Systemsteuerungsfenster (Administrative Tools). Aufruf: control.exe /name Microsoft.AdministrativeTools",
      "destruktiv": false
    },
    {
      "kategorie": "godmode",
      "befehl": "GodMode: AutoPlay",
      "start": "control.exe /name Microsoft.AutoPlay",
      "kurz": "AutoPlay",
      "lang": "Startet ein Systemsteuerungsfenster (AutoPlay). Aufruf: control.exe /name Microsoft.AutoPlay",
      "destruktiv": false
    },
    {
      "kategorie": "godmode",
      "befehl": "GodMode: Backup and Restore",
      "start": "control.exe /name Microsoft.BackupAndRestore",
      "kurz": "Backup and Restore",
      "lang": "Startet ein Systemsteuerungsfenster (Backup and Restore). Aufruf: control.exe /name Microsoft.BackupAndRestore",
      "destruktiv": false
    },
    {
      "kategorie": "godmode",
      "befehl": "GodMode: BitLocker Drive Encryption",
      "start": "control.exe /name Microsoft.BitLockerDriveEncryption",
      "kurz": "BitLocker Drive Encryption",
      "lang": "Startet ein Systemsteuerungsfenster (BitLocker Drive Encryption). Aufruf: control.exe /name Microsoft.BitLockerDriveEncryption",
      "destruktiv": false
    },
    {
      "kategorie": "godmode",
      "befehl": "GodMode: Color Management",
      "start": "control.exe /name Microsoft.ColorManagement",
      "kurz": "Color Management",
      "lang": "Startet ein Systemsteuerungsfenster (Color Management). Aufruf: control.exe /name Microsoft.ColorManagement",
      "destruktiv": false
    },
    {
      "kategorie": "godmode",
      "befehl": "GodMode: Credential Manager",
      "start": "control.exe /name Microsoft.CredentialManager",
      "kurz": "Credential Manager",
      "lang": "Startet ein Systemsteuerungsfenster (Credential Manager). Aufruf: control.exe /name Microsoft.CredentialManager",
      "destruktiv": false
    },
    {
      "kategorie": "godmode",
      "befehl": "GodMode: Date and Time",
      "start": "control.exe /name Microsoft.DateAndTime",
      "kurz": "Date and Time",
      "lang": "Startet ein Systemsteuerungsfenster (Date and Time). Aufruf: control.exe /name Microsoft.DateAndTime",
      "destruktiv": false
    },
    {
      "kategorie": "godmode",
      "befehl": "GodMode: Default Programs",
      "start": "control.exe /name Microsoft.DefaultPrograms",
      "kurz": "Default Programs",
      "lang": "Startet ein Systemsteuerungsfenster (Default Programs). Aufruf: control.exe /name Microsoft.DefaultPrograms",
      "destruktiv": false
    },
    {
      "kategorie": "godmode",
      "befehl": "GodMode: Device Manager",
      "start": "control.exe /name Microsoft.DeviceManager",
      "kurz": "Device Manager",
      "lang": "Startet ein Systemsteuerungsfenster (Device Manager). Aufruf: control.exe /name Microsoft.DeviceManager",
      "destruktiv": false
    },
    {
      "kategorie": "godmode",
      "befehl": "GodMode: Devices and Printers",
      "start": "control.exe /name Microsoft.DevicesAndPrinters",
      "kurz": "Devices and Printers",
      "lang": "Startet ein Systemsteuerungsfenster (Devices and Printers). Aufruf: control.exe /name Microsoft.DevicesAndPrinters",
      "destruktiv": false
    },
    {
      "kategorie": "godmode",
      "befehl": "GodMode: Display",
      "start": "control.exe /name Microsoft.Display",
      "kurz": "Display",
      "lang": "Startet ein Systemsteuerungsfenster (Display). Aufruf: control.exe /name Microsoft.Display",
      "destruktiv": false
    },
    {
      "kategorie": "godmode",
      "befehl": "GodMode: Ease of Access Center",
      "start": "control.exe /name Microsoft.EaseOfAccessCenter",
      "kurz": "Ease of Access Center",
      "lang": "Startet ein Systemsteuerungsfenster (Ease of Access Center). Aufruf: control.exe /name Microsoft.EaseOfAccessCenter",
      "destruktiv": false
    },
    {
      "kategorie": "godmode",
      "befehl": "GodMode: File History",
      "start": "control.exe /name Microsoft.FileHistory",
      "kurz": "File History",
      "lang": "Startet ein Systemsteuerungsfenster (File History). Aufruf: control.exe /name Microsoft.FileHistory",
      "destruktiv": false
    },
    {
      "kategorie": "godmode",
      "befehl": "GodMode: Folder Options",
      "start": "control.exe /name Microsoft.FolderOptions",
      "kurz": "Folder Options",
      "lang": "Startet ein Systemsteuerungsfenster (Folder Options). Aufruf: control.exe /name Microsoft.FolderOptions",
      "destruktiv": false
    },
    {
      "kategorie": "godmode",
      "befehl": "GodMode: Fonts",
      "start": "control.exe /name Microsoft.Fonts",
      "kurz": "Fonts",
      "lang": "Startet ein Systemsteuerungsfenster (Fonts). Aufruf: control.exe /name Microsoft.Fonts",
      "destruktiv": false
    },
    {
      "kategorie": "godmode",
      "befehl": "GodMode: Indexing Options",
      "start": "control.exe /name Microsoft.IndexingOptions",
      "kurz": "Indexing Options",
      "lang": "Startet ein Systemsteuerungsfenster (Indexing Options). Aufruf: control.exe /name Microsoft.IndexingOptions",
      "destruktiv": false
    },
    {
      "kategorie": "godmode",
      "befehl": "GodMode: Internet Options",
      "start": "control.exe /name Microsoft.InternetOptions",
      "kurz": "Internet Options",
      "lang": "Startet ein Systemsteuerungsfenster (Internet Options). Aufruf: control.exe /name Microsoft.InternetOptions",
      "destruktiv": false
    },
    {
      "kategorie": "godmode",
      "befehl": "GodMode: Keyboard",
      "start": "control.exe /name Microsoft.Keyboard",
      "kurz": "Keyboard",
      "lang": "Startet ein Systemsteuerungsfenster (Keyboard). Aufruf: control.exe /name Microsoft.Keyboard",
      "destruktiv": false
    },
    {
      "kategorie": "godmode",
      "befehl": "GodMode: Language",
      "start": "control.exe /name Microsoft.Language",
      "kurz": "Language",
      "lang": "Startet ein Systemsteuerungsfenster (Language). Aufruf: control.exe /name Microsoft.Language",
      "destruktiv": false
    },
    {
      "kategorie": "godmode",
      "befehl": "GodMode: Mouse",
      "start": "control.exe /name Microsoft.Mouse",
      "kurz": "Mouse",
      "lang": "Startet ein Systemsteuerungsfenster (Mouse). Aufruf: control.exe /name Microsoft.Mouse",
      "destruktiv": false
    },
    {
      "kategorie": "godmode",
      "befehl": "GodMode: Network and Sharing Center",
      "start": "control.exe /name Microsoft.NetworkAndSharingCenter",
      "kurz": "Network and Sharing Center",
      "lang": "Startet ein Systemsteuerungsfenster (Network and Sharing Center). Aufruf: control.exe /name Microsoft.NetworkAndSharingCenter",
      "destruktiv": false
    },
    {
      "kategorie": "godmode",
      "befehl": "GodMode: Notification Area Icons",
      "start": "control.exe /name Microsoft.NotificationAreaIcons",
      "kurz": "Notification Area Icons",
      "lang": "Startet ein Systemsteuerungsfenster (Notification Area Icons). Aufruf: control.exe /name Microsoft.NotificationAreaIcons",
      "destruktiv": false
    },
    {
      "kategorie": "godmode",
      "befehl": "GodMode: Pen and Touch",
      "start": "control.exe /name Microsoft.PenAndTouch",
      "kurz": "Pen and Touch",
      "lang": "Startet ein Systemsteuerungsfenster (Pen and Touch). Aufruf: control.exe /name Microsoft.PenAndTouch",
      "destruktiv": false
    },
    {
      "kategorie": "godmode",
      "befehl": "GodMode: Personalization",
      "start": "control.exe /name Microsoft.Personalization",
      "kurz": "Personalization",
      "lang": "Startet ein Systemsteuerungsfenster (Personalization). Aufruf: control.exe /name Microsoft.Personalization",
      "destruktiv": false
    },
    {
      "kategorie": "godmode",
      "befehl": "GodMode: Phone and Modem",
      "start": "control.exe /name Microsoft.PhoneAndModemOptions",
      "kurz": "Phone and Modem",
      "lang": "Startet ein Systemsteuerungsfenster (Phone and Modem). Aufruf: control.exe /name Microsoft.PhoneAndModemOptions",
      "destruktiv": false
    },
    {
      "kategorie": "godmode",
      "befehl": "GodMode: Power Options",
      "start": "control.exe /name Microsoft.PowerOptions",
      "kurz": "Power Options",
      "lang": "Startet ein Systemsteuerungsfenster (Power Options). Aufruf: control.exe /name Microsoft.PowerOptions",
      "destruktiv": false
    },
    {
      "kategorie": "godmode",
      "befehl": "GodMode: Programs and Features",
      "start": "control.exe /name Microsoft.ProgramsAndFeatures",
      "kurz": "Programs and Features",
      "lang": "Startet ein Systemsteuerungsfenster (Programs and Features). Aufruf: control.exe /name Microsoft.ProgramsAndFeatures",
      "destruktiv": false
    },
    {
      "kategorie": "godmode",
      "befehl": "GodMode: Recovery",
      "start": "control.exe /name Microsoft.Recovery",
      "kurz": "Recovery",
      "lang": "Startet ein Systemsteuerungsfenster (Recovery). Aufruf: control.exe /name Microsoft.Recovery",
      "destruktiv": false
    },
    {
      "kategorie": "godmode",
      "befehl": "GodMode: Region",
      "start": "control.exe /name Microsoft.RegionAndLanguage",
      "kurz": "Region",
      "lang": "Startet ein Systemsteuerungsfenster (Region). Aufruf: control.exe /name Microsoft.RegionAndLanguage",
      "destruktiv": false
    },
    {
      "kategorie": "godmode",
      "befehl": "GodMode: RemoteApp and Desktop Connections",
      "start": "control.exe /name Microsoft.RemoteAppAndDesktopConnections",
      "kurz": "RemoteApp and Desktop Connections",
      "lang": "Startet ein Systemsteuerungsfenster (RemoteApp and Desktop Connections). Aufruf: control.exe /name Microsoft.RemoteAppAndDesktopConnections",
      "destruktiv": false
    },
    {
      "kategorie": "godmode",
      "befehl": "GodMode: Security and Maintenance",
      "start": "control.exe /name Microsoft.ActionCenter",
      "kurz": "Security and Maintenance",
      "lang": "Startet ein Systemsteuerungsfenster (Security and Maintenance). Aufruf: control.exe /name Microsoft.ActionCenter",
      "destruktiv": false
    },
    {
      "kategorie": "godmode",
      "befehl": "GodMode: Sound",
      "start": "control.exe /name Microsoft.Sound",
      "kurz": "Sound",
      "lang": "Startet ein Systemsteuerungsfenster (Sound). Aufruf: control.exe /name Microsoft.Sound",
      "destruktiv": false
    },
    {
      "kategorie": "godmode",
      "befehl": "GodMode: Speech Recognition",
      "start": "control.exe /name Microsoft.SpeechRecognition",
      "kurz": "Speech Recognition",
      "lang": "Startet ein Systemsteuerungsfenster (Speech Recognition). Aufruf: control.exe /name Microsoft.SpeechRecognition",
      "destruktiv": false
    },
    {
      "kategorie": "godmode",
      "befehl": "GodMode: Storage Spaces",
      "start": "control.exe /name Microsoft.StorageSpaces",
      "kurz": "Storage Spaces",
      "lang": "Startet ein Systemsteuerungsfenster (Storage Spaces). Aufruf: control.exe /name Microsoft.StorageSpaces",
      "destruktiv": false
    },
    {
      "kategorie": "godmode",
      "befehl": "GodMode: Sync Center",
      "start": "control.exe /name Microsoft.SyncCenter",
      "kurz": "Sync Center",
      "lang": "Startet ein Systemsteuerungsfenster (Sync Center). Aufruf: control.exe /name Microsoft.SyncCenter",
      "destruktiv": false
    },
    {
      "kategorie": "godmode",
      "befehl": "GodMode: System",
      "start": "control.exe /name Microsoft.System",
      "kurz": "System",
      "lang": "Startet ein Systemsteuerungsfenster (System). Aufruf: control.exe /name Microsoft.System",
      "destruktiv": false
    },
    {
      "kategorie": "godmode",
      "befehl": "GodMode: Tablet PC Settings",
      "start": "control.exe /name Microsoft.TabletPCSettings",
      "kurz": "Tablet PC Settings",
      "lang": "Startet ein Systemsteuerungsfenster (Tablet PC Settings). Aufruf: control.exe /name Microsoft.TabletPCSettings",
      "destruktiv": false
    },
    {
      "kategorie": "godmode",
      "befehl": "GodMode: Taskbar and Navigation",
      "start": "control.exe /name Microsoft.Taskbar",
      "kurz": "Taskbar and Navigation",
      "lang": "Startet ein Systemsteuerungsfenster (Taskbar and Navigation). Aufruf: control.exe /name Microsoft.Taskbar",
      "destruktiv": false
    },
    {
      "kategorie": "godmode",
      "befehl": "GodMode: Troubleshooting",
      "start": "control.exe /name Microsoft.Troubleshooting",
      "kurz": "Troubleshooting",
      "lang": "Startet ein Systemsteuerungsfenster (Troubleshooting). Aufruf: control.exe /name Microsoft.Troubleshooting",
      "destruktiv": false
    },
    {
      "kategorie": "godmode",
      "befehl": "GodMode: User Accounts",
      "start": "control.exe /name Microsoft.UserAccounts",
      "kurz": "User Accounts",
      "lang": "Startet ein Systemsteuerungsfenster (User Accounts). Aufruf: control.exe /name Microsoft.UserAccounts",
      "destruktiv": false
    },
    {
      "kategorie": "godmode",
      "befehl": "GodMode: Windows Defender Firewall",
      "start": "control.exe /name Microsoft.WindowsFirewall",
      "kurz": "Windows Defender Firewall",
      "lang": "Startet ein Systemsteuerungsfenster (Windows Defender Firewall). Aufruf: control.exe /name Microsoft.WindowsFirewall",
      "destruktiv": false
    },
    {
      "kategorie": "godmode",
      "befehl": "GodMode: Windows Mobility Center",
      "start": "control.exe /name Microsoft.MobilityCenter",
      "kurz": "Windows Mobility Center",
      "lang": "Startet ein Systemsteuerungsfenster (Windows Mobility Center). Aufruf: control.exe /name Microsoft.MobilityCenter",
      "destruktiv": false
    },
    {
      "kategorie": "godmode",
      "befehl": "GodMode: Windows Update",
      "start": "control.exe /name Microsoft.WindowsUpdate",
      "kurz": "Windows Update",
      "lang": "Startet ein Systemsteuerungsfenster (Windows Update). Aufruf: control.exe /name Microsoft.WindowsUpdate",
      "destruktiv": false
    },
    {
      "kategorie": "godmode",
      "befehl": "GodMode: Work Folders",
      "start": "control.exe /name Microsoft.WorkFolders",
      "kurz": "Work Folders",
      "lang": "Startet ein Systemsteuerungsfenster (Work Folders). Aufruf: control.exe /name Microsoft.WorkFolders",
      "destruktiv": false
    },
    {
      "kategorie": "godmode",
      "befehl": "GodMode: Workgroup",
      "start": "sysdm.cpl",
      "kurz": "Workgroup",
      "lang": "Startet 'Workgroup' als Windows-Befehl. Aufruf: sysdm.cpl",
      "destruktiv": false
    },
    {
      "kategorie": "godmode",
      "befehl": "GodMode: File Explorer Options",
      "start": "control.exe /name Microsoft.FolderOptions",
      "kurz": "File Explorer Options",
      "lang": "Startet ein Systemsteuerungsfenster (File Explorer Options). Aufruf: control.exe /name Microsoft.FolderOptions",
      "destruktiv": false
    },
    {
      "kategorie": "godmode",
      "befehl": "GodMode: Game Controllers",
      "start": "control.exe /name Microsoft.GameControllers",
      "kurz": "Game Controllers",
      "lang": "Startet ein Systemsteuerungsfenster (Game Controllers). Aufruf: control.exe /name Microsoft.GameControllers",
      "destruktiv": false
    },
    {
      "kategorie": "godmode",
      "befehl": "GodMode: Infrared",
      "start": "control.exe /name Microsoft.Infrared",
      "kurz": "Infrared",
      "lang": "Startet ein Systemsteuerungsfenster (Infrared). Aufruf: control.exe /name Microsoft.Infrared",
      "destruktiv": false
    },
    {
      "kategorie": "godmode",
      "befehl": "GodMode: ODBC Data Sources",
      "start": "control.exe /name Microsoft.ODBCDataSourceAdministrator",
      "kurz": "ODBC Data Sources",
      "lang": "Startet ein Systemsteuerungsfenster (ODBC Data Sources). Aufruf: control.exe /name Microsoft.ODBCDataSourceAdministrator",
      "destruktiv": false
    },
    {
      "kategorie": "godmode",
      "befehl": "GodMode: Spelling",
      "start": "control.exe /name Microsoft.Language",
      "kurz": "Spelling",
      "lang": "Startet ein Systemsteuerungsfenster (Spelling). Aufruf: control.exe /name Microsoft.Language",
      "destruktiv": false
    },
    {
      "kategorie": "godmode",
      "befehl": "GodMode: System Restore",
      "start": "rstrui.exe",
      "kurz": "System Restore",
      "lang": "Startet 'System Restore' als Windows-Befehl. Aufruf: rstrui.exe",
      "destruktiv": false
    },
    {
      "kategorie": "godmode",
      "befehl": "GodMode: Windows Tools",
      "start": "control.exe /name Microsoft.AdministrativeTools",
      "kurz": "Windows Tools",
      "lang": "Startet ein Systemsteuerungsfenster (Windows Tools). Aufruf: control.exe /name Microsoft.AdministrativeTools",
      "destruktiv": false
    },
    {
      "kategorie": "godmode",
      "befehl": "GodMode: Windows Features",
      "start": "control.exe /name Microsoft.WindowsOptionalFeatures",
      "kurz": "Windows Features",
      "lang": "Startet ein Systemsteuerungsfenster (Windows Features). Aufruf: control.exe /name Microsoft.WindowsOptionalFeatures",
      "destruktiv": false
    },
    {
      "kategorie": "godmode",
      "befehl": "GodMode: Windows Insider Program",
      "start": "control.exe /name Microsoft.WindowsInsiderProgram",
      "kurz": "Windows Insider Program",
      "lang": "Startet ein Systemsteuerungsfenster (Windows Insider Program). Aufruf: control.exe /name Microsoft.WindowsInsiderProgram",
      "destruktiv": false
    },
    {
      "kategorie": "godmode",
      "befehl": "GodMode: Windows Security",
      "start": "control.exe /name Microsoft.WindowsDefender",
      "kurz": "Windows Security",
      "lang": "Startet ein Systemsteuerungsfenster (Windows Security). Aufruf: control.exe /name Microsoft.WindowsDefender",
      "destruktiv": false
    },
    {
      "kategorie": "netzwerk",
      "befehl": "ms-settings:network",
      "start": "ms-settings:network",
      "kurz": "Netzwerk",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Netzwerk'. URI: ms-settings:network",
      "destruktiv": false
    },
    {
      "kategorie": "netzwerk",
      "befehl": "ms-settings:network-wifi",
      "start": "ms-settings:network-wifi",
      "kurz": "WLAN",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'WLAN'. URI: ms-settings:network-wifi",
      "destruktiv": false
    },
    {
      "kategorie": "netzwerk",
      "befehl": "ms-settings:network-ethernet",
      "start": "ms-settings:network-ethernet",
      "kurz": "Ethernet",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Ethernet'. URI: ms-settings:network-ethernet",
      "destruktiv": false
    },
    {
      "kategorie": "netzwerk",
      "befehl": "ms-settings:network-vpn",
      "start": "ms-settings:network-vpn",
      "kurz": "VPN",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'VPN'. URI: ms-settings:network-vpn",
      "destruktiv": false
    },
    {
      "kategorie": "netzwerk",
      "befehl": "ms-settings:network-mobilehotspot",
      "start": "ms-settings:network-mobilehotspot",
      "kurz": "Hotspot",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Hotspot'. URI: ms-settings:network-mobilehotspot",
      "destruktiv": false
    },
    {
      "kategorie": "netzwerk",
      "befehl": "ms-settings:network-airplanemode",
      "start": "ms-settings:network-airplanemode",
      "kurz": "Flugmodus",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Flugmodus'. URI: ms-settings:network-airplanemode",
      "destruktiv": false
    },
    {
      "kategorie": "netzwerk",
      "befehl": "ms-settings:network-proxy",
      "start": "ms-settings:network-proxy",
      "kurz": "Proxy",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Proxy'. URI: ms-settings:network-proxy",
      "destruktiv": false
    },
    {
      "kategorie": "netzwerk",
      "befehl": "ms-settings:network-dialup",
      "start": "ms-settings:network-dialup",
      "kurz": "DFÜ",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'DFÜ'. URI: ms-settings:network-dialup",
      "destruktiv": false
    },
    {
      "kategorie": "netzwerk",
      "befehl": "ms-settings:network-directaccess",
      "start": "ms-settings:network-directaccess",
      "kurz": "DirectAccess",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'DirectAccess'. URI: ms-settings:network-directaccess",
      "destruktiv": false
    },
    {
      "kategorie": "netzwerk",
      "befehl": "ms-settings:network-mobile",
      "start": "ms-settings:network-mobile",
      "kurz": "Mobilfunk",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Mobilfunk'. URI: ms-settings:network-mobile",
      "destruktiv": false
    },
    {
      "kategorie": "netzwerk",
      "befehl": "ncpa.cpl",
      "start": "ncpa.cpl",
      "kurz": "Netzwerkadapter",
      "lang": "Startet 'Netzwerkadapter' als Windows-Befehl. Aufruf: ncpa.cpl",
      "destruktiv": false
    },
    {
      "kategorie": "netzwerk",
      "befehl": "netstat",
      "start": "netstat",
      "kurz": "Netzwerkstatus",
      "lang": "Startet 'Netzwerkstatus' als Windows-Befehl. Aufruf: netstat",
      "destruktiv": false
    },
    {
      "kategorie": "netzwerk",
      "befehl": "ipconfig",
      "start": "ipconfig",
      "kurz": "IP-Konfiguration",
      "lang": "Startet 'IP-Konfiguration' als Windows-Befehl. Aufruf: ipconfig",
      "destruktiv": false
    },
    {
      "kategorie": "netzwerk",
      "befehl": "ping",
      "start": "ping",
      "kurz": "Netzwerkdiagnose",
      "lang": "Startet 'Netzwerkdiagnose' als Windows-Befehl. Aufruf: ping",
      "destruktiv": false
    },
    {
      "kategorie": "netzwerk",
      "befehl": "tracert",
      "start": "tracert",
      "kurz": "Routing",
      "lang": "Startet 'Routing' als Windows-Befehl. Aufruf: tracert",
      "destruktiv": false
    },
    {
      "kategorie": "netzwerk",
      "befehl": "pathping",
      "start": "pathping",
      "kurz": "Routinganalyse",
      "lang": "Startet 'Routinganalyse' als Windows-Befehl. Aufruf: pathping",
      "destruktiv": false
    },
    {
      "kategorie": "netzwerk",
      "befehl": "netsh",
      "start": "netsh",
      "kurz": "Netzwerksteuerung",
      "lang": "Startet 'Netzwerksteuerung' als Windows-Befehl. Aufruf: netsh",
      "destruktiv": false
    },
    {
      "kategorie": "netzwerk",
      "befehl": "net use",
      "start": "net use",
      "kurz": "Netzlaufwerke",
      "lang": "Startet 'Netzlaufwerke' als Windows-Befehl. Aufruf: net use",
      "destruktiv": false
    },
    {
      "kategorie": "netzwerk",
      "befehl": "net session",
      "start": "net session",
      "kurz": "Sitzungen",
      "lang": "Startet 'Sitzungen' als Windows-Befehl. Aufruf: net session",
      "destruktiv": false
    },
    {
      "kategorie": "netzwerk",
      "befehl": "net share",
      "start": "net share",
      "kurz": "Freigaben",
      "lang": "Startet 'Freigaben' als Windows-Befehl. Aufruf: net share",
      "destruktiv": false
    },
    {
      "kategorie": "netzwerk",
      "befehl": "net accounts",
      "start": "net accounts",
      "kurz": "Konten",
      "lang": "Startet 'Konten' als Windows-Befehl. Aufruf: net accounts",
      "destruktiv": false
    },
    {
      "kategorie": "netzwerk",
      "befehl": "net localgroup",
      "start": "net localgroup",
      "kurz": "Gruppen",
      "lang": "Startet 'Gruppen' als Windows-Befehl. Aufruf: net localgroup",
      "destruktiv": false
    },
    {
      "kategorie": "netzwerk",
      "befehl": "net group",
      "start": "net group",
      "kurz": "Domain-Gruppen",
      "lang": "Startet 'Domain-Gruppen' als Windows-Befehl. Aufruf: net group",
      "destruktiv": false
    },
    {
      "kategorie": "netzwerk",
      "befehl": "net computer",
      "start": "net computer",
      "kurz": "Domain-Computer",
      "lang": "Startet 'Domain-Computer' als Windows-Befehl. Aufruf: net computer",
      "destruktiv": false
    },
    {
      "kategorie": "speicher",
      "befehl": "diskmgmt.msc",
      "start": "diskmgmt.msc",
      "kurz": "Datenträgerverwaltung",
      "lang": "Oeffnet das MMC-Snap-In 'Datenträgerverwaltung'. Aufruf: diskmgmt.msc",
      "destruktiv": false
    },
    {
      "kategorie": "speicher",
      "befehl": "diskpart",
      "start": "diskpart",
      "kurz": "Partitionierung",
      "lang": "Achtung: Dieser Befehl kann das System aendern oder Daten loeschen (Partitionierung). Aufruf nur nach Bestaetigung: diskpart",
      "destruktiv": true
    },
    {
      "kategorie": "speicher",
      "befehl": "diskperf",
      "start": "diskperf",
      "kurz": "Datenträgerleistung",
      "lang": "Startet 'Datenträgerleistung' als Windows-Befehl. Aufruf: diskperf",
      "destruktiv": false
    },
    {
      "kategorie": "speicher",
      "befehl": "diskraid",
      "start": "diskraid",
      "kurz": "RAID Verwaltung",
      "lang": "Startet 'RAID Verwaltung' als Windows-Befehl. Aufruf: diskraid",
      "destruktiv": false
    },
    {
      "kategorie": "speicher",
      "befehl": "diskguid",
      "start": "diskguid",
      "kurz": "Datenträger-GUID",
      "lang": "Startet 'Datenträger-GUID' als Windows-Befehl. Aufruf: diskguid",
      "destruktiv": false
    },
    {
      "kategorie": "speicher",
      "befehl": "storprop.dll",
      "start": "storprop.dll",
      "kurz": "Speicherverwaltung",
      "lang": "Startet 'Speicherverwaltung' als Windows-Befehl. Aufruf: storprop.dll",
      "destruktiv": false
    },
    {
      "kategorie": "speicher",
      "befehl": "defrag",
      "start": "defrag",
      "kurz": "Defragmentierung",
      "lang": "Startet 'Defragmentierung' als Windows-Befehl. Aufruf: defrag",
      "destruktiv": false
    },
    {
      "kategorie": "speicher",
      "befehl": "chkdsk",
      "start": "chkdsk",
      "kurz": "Datenträgerprüfung",
      "lang": "Achtung: Dieser Befehl kann das System aendern oder Daten loeschen (Datenträgerprüfung). Aufruf nur nach Bestaetigung: chkdsk",
      "destruktiv": true
    },
    {
      "kategorie": "speicher",
      "befehl": "format",
      "start": "format",
      "kurz": "Formatierung",
      "lang": "Achtung: Dieser Befehl kann das System aendern oder Daten loeschen (Formatierung). Aufruf nur nach Bestaetigung: format",
      "destruktiv": true
    },
    {
      "kategorie": "speicher",
      "befehl": "mountvol",
      "start": "mountvol",
      "kurz": "Volumes",
      "lang": "Startet 'Volumes' als Windows-Befehl. Aufruf: mountvol",
      "destruktiv": false
    },
    {
      "kategorie": "speicher",
      "befehl": "wbadmin",
      "start": "wbadmin",
      "kurz": "Backup",
      "lang": "Startet 'Backup' als Windows-Befehl. Aufruf: wbadmin",
      "destruktiv": false
    },
    {
      "kategorie": "speicher",
      "befehl": "fsutil",
      "start": "fsutil",
      "kurz": "Dateisystem",
      "lang": "Startet 'Dateisystem' als Windows-Befehl. Aufruf: fsutil",
      "destruktiv": false
    },
    {
      "kategorie": "speicher",
      "befehl": "vssadmin",
      "start": "vssadmin",
      "kurz": "Shadow Copies",
      "lang": "Startet 'Shadow Copies' als Windows-Befehl. Aufruf: vssadmin",
      "destruktiv": false
    },
    {
      "kategorie": "speicher",
      "befehl": "powercfg",
      "start": "powercfg",
      "kurz": "Energieoptionen",
      "lang": "Startet 'Energieoptionen' als Windows-Befehl. Aufruf: powercfg",
      "destruktiv": false
    },
    {
      "kategorie": "speicher",
      "befehl": "reagentc",
      "start": "reagentc",
      "kurz": "Wiederherstellung",
      "lang": "Startet 'Wiederherstellung' als Windows-Befehl. Aufruf: reagentc",
      "destruktiv": false
    },
    {
      "kategorie": "speicher",
      "befehl": "bcdedit",
      "start": "bcdedit",
      "kurz": "Boot-Konfiguration",
      "lang": "Achtung: Dieser Befehl kann das System aendern oder Daten loeschen (Boot-Konfiguration). Aufruf nur nach Bestaetigung: bcdedit",
      "destruktiv": true
    },
    {
      "kategorie": "speicher",
      "befehl": "bootsect",
      "start": "bootsect",
      "kurz": "Bootsektor",
      "lang": "Achtung: Dieser Befehl kann das System aendern oder Daten loeschen (Bootsektor). Aufruf nur nach Bestaetigung: bootsect",
      "destruktiv": true
    },
    {
      "kategorie": "hyperv",
      "befehl": "virtmgmt.msc",
      "start": "virtmgmt.msc",
      "kurz": "Hyper‑V Manager",
      "lang": "Oeffnet das MMC-Snap-In 'Hyper‑V Manager'. Aufruf: virtmgmt.msc",
      "destruktiv": false
    },
    {
      "kategorie": "hyperv",
      "befehl": "vmconnect.exe",
      "start": "vmconnect.exe",
      "kurz": "VM‑Konsole",
      "lang": "Startet 'VM‑Konsole' als Windows-Befehl. Aufruf: vmconnect.exe",
      "destruktiv": false
    },
    {
      "kategorie": "hyperv",
      "befehl": "hvremote.wsf",
      "start": "hvremote.wsf",
      "kurz": "Remote‑Hyper‑V",
      "lang": "Startet 'Remote‑Hyper‑V' als Windows-Befehl. Aufruf: hvremote.wsf",
      "destruktiv": false
    },
    {
      "kategorie": "hyperv",
      "befehl": "powershell: Get-VM",
      "start": "powershell: Get-VM",
      "kurz": "VM‑Liste",
      "lang": "Fuehrt das PowerShell-Cmdlet 'Get-VM' in einer neuen Konsole aus (VM‑Liste). Die Konsole bleibt offen.",
      "destruktiv": false
    },
    {
      "kategorie": "hyperv",
      "befehl": "powershell: New-VM",
      "start": "powershell: New-VM",
      "kurz": "Neue VM",
      "lang": "Fuehrt das PowerShell-Cmdlet 'New-VM' in einer neuen Konsole aus (Neue VM). Die Konsole bleibt offen.",
      "destruktiv": false
    },
    {
      "kategorie": "hyperv",
      "befehl": "powershell: Start-VM",
      "start": "powershell: Start-VM",
      "kurz": "VM starten",
      "lang": "Fuehrt das PowerShell-Cmdlet 'Start-VM' in einer neuen Konsole aus (VM starten). Die Konsole bleibt offen.",
      "destruktiv": false
    },
    {
      "kategorie": "hyperv",
      "befehl": "powershell: Stop-VM",
      "start": "powershell: Stop-VM",
      "kurz": "VM stoppen",
      "lang": "Fuehrt das PowerShell-Cmdlet 'Stop-VM' in einer neuen Konsole aus (VM stoppen). Die Konsole bleibt offen.",
      "destruktiv": false
    },
    {
      "kategorie": "hyperv",
      "befehl": "powershell: Restart-VM",
      "start": "powershell: Restart-VM",
      "kurz": "VM neu starten",
      "lang": "Fuehrt das PowerShell-Cmdlet 'Restart-VM' in einer neuen Konsole aus (VM neu starten). Die Konsole bleibt offen.",
      "destruktiv": false
    },
    {
      "kategorie": "hyperv",
      "befehl": "powershell: Remove-VM",
      "start": "powershell: Remove-VM",
      "kurz": "VM löschen",
      "lang": "Fuehrt das PowerShell-Cmdlet 'Remove-VM' in einer neuen Konsole aus (VM löschen). Die Konsole bleibt offen.",
      "destruktiv": true
    },
    {
      "kategorie": "hyperv",
      "befehl": "powershell: Set-VM",
      "start": "powershell: Set-VM",
      "kurz": "VM konfigurieren",
      "lang": "Fuehrt das PowerShell-Cmdlet 'Set-VM' in einer neuen Konsole aus (VM konfigurieren). Die Konsole bleibt offen.",
      "destruktiv": false
    },
    {
      "kategorie": "hyperv",
      "befehl": "powershell: Get-VMNetworkAdapter",
      "start": "powershell: Get-VMNetworkAdapter",
      "kurz": "VM‑Netzwerkadapter",
      "lang": "Fuehrt das PowerShell-Cmdlet 'Get-VMNetworkAdapter' in einer neuen Konsole aus (VM‑Netzwerkadapter). Die Konsole bleibt offen.",
      "destruktiv": false
    },
    {
      "kategorie": "hyperv",
      "befehl": "powershell: Add-VMNetworkAdapter",
      "start": "powershell: Add-VMNetworkAdapter",
      "kurz": "Netzwerkadapter hinzufügen",
      "lang": "Fuehrt das PowerShell-Cmdlet 'Add-VMNetworkAdapter' in einer neuen Konsole aus (Netzwerkadapter hinzufügen). Die Konsole bleibt offen.",
      "destruktiv": false
    },
    {
      "kategorie": "hyperv",
      "befehl": "powershell: Remove-VMNetworkAdapter",
      "start": "powershell: Remove-VMNetworkAdapter",
      "kurz": "Netzwerkadapter entfernen",
      "lang": "Fuehrt das PowerShell-Cmdlet 'Remove-VMNetworkAdapter' in einer neuen Konsole aus (Netzwerkadapter entfernen). Die Konsole bleibt offen.",
      "destruktiv": true
    },
    {
      "kategorie": "hyperv",
      "befehl": "powershell: Get-VMSwitch",
      "start": "powershell: Get-VMSwitch",
      "kurz": "Virtuelle Switches",
      "lang": "Fuehrt das PowerShell-Cmdlet 'Get-VMSwitch' in einer neuen Konsole aus (Virtuelle Switches). Die Konsole bleibt offen.",
      "destruktiv": false
    },
    {
      "kategorie": "hyperv",
      "befehl": "powershell: New-VMSwitch",
      "start": "powershell: New-VMSwitch",
      "kurz": "Neuen Switch erstellen",
      "lang": "Fuehrt das PowerShell-Cmdlet 'New-VMSwitch' in einer neuen Konsole aus (Neuen Switch erstellen). Die Konsole bleibt offen.",
      "destruktiv": false
    },
    {
      "kategorie": "hyperv",
      "befehl": "powershell: Remove-VMSwitch",
      "start": "powershell: Remove-VMSwitch",
      "kurz": "Switch löschen",
      "lang": "Fuehrt das PowerShell-Cmdlet 'Remove-VMSwitch' in einer neuen Konsole aus (Switch löschen). Die Konsole bleibt offen.",
      "destruktiv": true
    },
    {
      "kategorie": "hyperv",
      "befehl": "powershell: Set-VMSwitch",
      "start": "powershell: Set-VMSwitch",
      "kurz": "Switch konfigurieren",
      "lang": "Fuehrt das PowerShell-Cmdlet 'Set-VMSwitch' in einer neuen Konsole aus (Switch konfigurieren). Die Konsole bleibt offen.",
      "destruktiv": false
    },
    {
      "kategorie": "hyperv",
      "befehl": "powershell: Get-VHD",
      "start": "powershell: Get-VHD",
      "kurz": "Virtuelle Festplatten",
      "lang": "Fuehrt das PowerShell-Cmdlet 'Get-VHD' in einer neuen Konsole aus (Virtuelle Festplatten). Die Konsole bleibt offen.",
      "destruktiv": false
    },
    {
      "kategorie": "hyperv",
      "befehl": "powershell: New-VHD",
      "start": "powershell: New-VHD",
      "kurz": "Neue VHD",
      "lang": "Fuehrt das PowerShell-Cmdlet 'New-VHD' in einer neuen Konsole aus (Neue VHD). Die Konsole bleibt offen.",
      "destruktiv": false
    },
    {
      "kategorie": "hyperv",
      "befehl": "powershell: Resize-VHD",
      "start": "powershell: Resize-VHD",
      "kurz": "VHD vergrößern",
      "lang": "Fuehrt das PowerShell-Cmdlet 'Resize-VHD' in einer neuen Konsole aus (VHD vergrößern). Die Konsole bleibt offen.",
      "destruktiv": false
    },
    {
      "kategorie": "hyperv",
      "befehl": "powershell: Mount-VHD",
      "start": "powershell: Mount-VHD",
      "kurz": "VHD mounten",
      "lang": "Fuehrt das PowerShell-Cmdlet 'Mount-VHD' in einer neuen Konsole aus (VHD mounten). Die Konsole bleibt offen.",
      "destruktiv": false
    },
    {
      "kategorie": "hyperv",
      "befehl": "powershell: Dismount-VHD",
      "start": "powershell: Dismount-VHD",
      "kurz": "VHD unmounten",
      "lang": "Fuehrt das PowerShell-Cmdlet 'Dismount-VHD' in einer neuen Konsole aus (VHD unmounten). Die Konsole bleibt offen.",
      "destruktiv": false
    },
    {
      "kategorie": "hyperv",
      "befehl": "powershell: Optimize-VHD",
      "start": "powershell: Optimize-VHD",
      "kurz": "VHD optimieren",
      "lang": "Fuehrt das PowerShell-Cmdlet 'Optimize-VHD' in einer neuen Konsole aus (VHD optimieren). Die Konsole bleibt offen.",
      "destruktiv": false
    },
    {
      "kategorie": "hyperv",
      "befehl": "powershell: Get-VMHardDiskDrive",
      "start": "powershell: Get-VMHardDiskDrive",
      "kurz": "VM‑Festplatten",
      "lang": "Fuehrt das PowerShell-Cmdlet 'Get-VMHardDiskDrive' in einer neuen Konsole aus (VM‑Festplatten). Die Konsole bleibt offen.",
      "destruktiv": false
    },
    {
      "kategorie": "hyperv",
      "befehl": "powershell: Add-VMHardDiskDrive",
      "start": "powershell: Add-VMHardDiskDrive",
      "kurz": "Festplatte hinzufügen",
      "lang": "Fuehrt das PowerShell-Cmdlet 'Add-VMHardDiskDrive' in einer neuen Konsole aus (Festplatte hinzufügen). Die Konsole bleibt offen.",
      "destruktiv": false
    },
    {
      "kategorie": "hyperv",
      "befehl": "powershell: Remove-VMHardDiskDrive",
      "start": "powershell: Remove-VMHardDiskDrive",
      "kurz": "Festplatte entfernen",
      "lang": "Fuehrt das PowerShell-Cmdlet 'Remove-VMHardDiskDrive' in einer neuen Konsole aus (Festplatte entfernen). Die Konsole bleibt offen.",
      "destruktiv": true
    },
    {
      "kategorie": "remote",
      "befehl": "winrm.cmd",
      "start": "winrm.cmd",
      "kurz": "Windows Remote Management",
      "lang": "Startet 'Windows Remote Management' als Windows-Befehl. Aufruf: winrm.cmd",
      "destruktiv": false
    },
    {
      "kategorie": "remote",
      "befehl": "winrs",
      "start": "winrs",
      "kurz": "Remote Shell",
      "lang": "Startet 'Remote Shell' als Windows-Befehl. Aufruf: winrs",
      "destruktiv": false
    },
    {
      "kategorie": "remote",
      "befehl": "powershell: Enter-PSSession",
      "start": "powershell: Enter-PSSession",
      "kurz": "Remote PowerShell",
      "lang": "Fuehrt das PowerShell-Cmdlet 'Enter-PSSession' in einer neuen Konsole aus (Remote PowerShell). Die Konsole bleibt offen.",
      "destruktiv": false
    },
    {
      "kategorie": "remote",
      "befehl": "powershell: Exit-PSSession",
      "start": "powershell: Exit-PSSession",
      "kurz": "Remote Sitzung beenden",
      "lang": "Fuehrt das PowerShell-Cmdlet 'Exit-PSSession' in einer neuen Konsole aus (Remote Sitzung beenden). Die Konsole bleibt offen.",
      "destruktiv": false
    },
    {
      "kategorie": "remote",
      "befehl": "powershell: Invoke-Command",
      "start": "powershell: Invoke-Command",
      "kurz": "Remote Command",
      "lang": "Fuehrt das PowerShell-Cmdlet 'Invoke-Command' in einer neuen Konsole aus (Remote Command). Die Konsole bleibt offen.",
      "destruktiv": false
    },
    {
      "kategorie": "remote",
      "befehl": "powershell: New-PSSession",
      "start": "powershell: New-PSSession",
      "kurz": "Neue Remote‑Sitzung",
      "lang": "Fuehrt das PowerShell-Cmdlet 'New-PSSession' in einer neuen Konsole aus (Neue Remote‑Sitzung). Die Konsole bleibt offen.",
      "destruktiv": false
    },
    {
      "kategorie": "remote",
      "befehl": "powershell: Get-PSSession",
      "start": "powershell: Get-PSSession",
      "kurz": "Sitzungen anzeigen",
      "lang": "Fuehrt das PowerShell-Cmdlet 'Get-PSSession' in einer neuen Konsole aus (Sitzungen anzeigen). Die Konsole bleibt offen.",
      "destruktiv": false
    },
    {
      "kategorie": "remote",
      "befehl": "powershell: Remove-PSSession",
      "start": "powershell: Remove-PSSession",
      "kurz": "Sitzung löschen",
      "lang": "Fuehrt das PowerShell-Cmdlet 'Remove-PSSession' in einer neuen Konsole aus (Sitzung löschen). Die Konsole bleibt offen.",
      "destruktiv": false
    },
    {
      "kategorie": "remote",
      "befehl": "mstsc.exe",
      "start": "mstsc.exe",
      "kurz": "Remote Desktop",
      "lang": "Startet 'Remote Desktop' als Windows-Befehl. Aufruf: mstsc.exe",
      "destruktiv": false
    },
    {
      "kategorie": "remote",
      "befehl": "tscon.exe",
      "start": "tscon.exe",
      "kurz": "Session Control",
      "lang": "Startet 'Session Control' als Windows-Befehl. Aufruf: tscon.exe",
      "destruktiv": false
    },
    {
      "kategorie": "remote",
      "befehl": "tsdiscon.exe",
      "start": "tsdiscon.exe",
      "kurz": "Session Disconnect",
      "lang": "Achtung: Dieser Befehl kann das System aendern oder Daten loeschen (Session Disconnect). Aufruf nur nach Bestaetigung: tsdiscon.exe",
      "destruktiv": true
    },
    {
      "kategorie": "remote",
      "befehl": "qwinsta",
      "start": "qwinsta",
      "kurz": "Sitzungsstatus",
      "lang": "Startet 'Sitzungsstatus' als Windows-Befehl. Aufruf: qwinsta",
      "destruktiv": false
    },
    {
      "kategorie": "remote",
      "befehl": "rwinsta",
      "start": "rwinsta",
      "kurz": "Sitzung zurücksetzen",
      "lang": "Achtung: Dieser Befehl kann das System aendern oder Daten loeschen (Sitzung zurücksetzen). Aufruf nur nach Bestaetigung: rwinsta",
      "destruktiv": true
    },
    {
      "kategorie": "remote",
      "befehl": "query user",
      "start": "query user",
      "kurz": "Benutzer abfragen",
      "lang": "Startet 'Benutzer abfragen' als Windows-Befehl. Aufruf: query user",
      "destruktiv": false
    },
    {
      "kategorie": "remote",
      "befehl": "query session",
      "start": "query session",
      "kurz": "Sitzungen abfragen",
      "lang": "Startet 'Sitzungen abfragen' als Windows-Befehl. Aufruf: query session",
      "destruktiv": false
    },
    {
      "kategorie": "remote",
      "befehl": "query process",
      "start": "query process",
      "kurz": "Prozesse abfragen",
      "lang": "Startet 'Prozesse abfragen' als Windows-Befehl. Aufruf: query process",
      "destruktiv": false
    },
    {
      "kategorie": "remote",
      "befehl": "logoff",
      "start": "logoff",
      "kurz": "Benutzer abmelden",
      "lang": "Achtung: Dieser Befehl kann das System aendern oder Daten loeschen (Benutzer abmelden). Aufruf nur nach Bestaetigung: logoff",
      "destruktiv": true
    },
    {
      "kategorie": "remote",
      "befehl": "shutdown",
      "start": "shutdown",
      "kurz": "Remote Shutdown",
      "lang": "Achtung: Dieser Befehl kann das System aendern oder Daten loeschen (Remote Shutdown). Aufruf nur nach Bestaetigung: shutdown",
      "destruktiv": true
    },
    {
      "kategorie": "remote",
      "befehl": "psexec",
      "start": "psexec",
      "kurz": "Remote Prozess (Sysinternals)",
      "lang": "Startet 'Remote Prozess (Sysinternals)' als Windows-Befehl. Aufruf: psexec",
      "destruktiv": false
    },
    {
      "kategorie": "remote",
      "befehl": "pskill",
      "start": "pskill",
      "kurz": "Remote Kill (Sysinternals)",
      "lang": "Startet 'Remote Kill (Sysinternals)' als Windows-Befehl. Aufruf: pskill",
      "destruktiv": false
    },
    {
      "kategorie": "remote",
      "befehl": "pslist",
      "start": "pslist",
      "kurz": "Remote Prozessliste",
      "lang": "Startet 'Remote Prozessliste' als Windows-Befehl. Aufruf: pslist",
      "destruktiv": false
    },
    {
      "kategorie": "remote",
      "befehl": "psloggedon",
      "start": "psloggedon",
      "kurz": "Remote Login‑Status",
      "lang": "Startet 'Remote Login‑Status' als Windows-Befehl. Aufruf: psloggedon",
      "destruktiv": false
    },
    {
      "kategorie": "remote",
      "befehl": "psservice",
      "start": "psservice",
      "kurz": "Remote Dienste",
      "lang": "Startet 'Remote Dienste' als Windows-Befehl. Aufruf: psservice",
      "destruktiv": false
    },
    {
      "kategorie": "remote",
      "befehl": "psinfo",
      "start": "psinfo",
      "kurz": "Remote Systeminfo",
      "lang": "Startet 'Remote Systeminfo' als Windows-Befehl. Aufruf: psinfo",
      "destruktiv": false
    },
    {
      "kategorie": "remote",
      "befehl": "plink",
      "start": "plink",
      "kurz": "SSH Remote (PuTTY)",
      "lang": "Startet 'SSH Remote (PuTTY)' als Windows-Befehl. Aufruf: plink",
      "destruktiv": false
    },
    {
      "kategorie": "remote",
      "befehl": "ssh",
      "start": "ssh",
      "kurz": "SSH",
      "lang": "Startet 'SSH' als Windows-Befehl. Aufruf: ssh",
      "destruktiv": false
    },
    {
      "kategorie": "remote",
      "befehl": "scp",
      "start": "scp",
      "kurz": "Secure Copy",
      "lang": "Startet 'Secure Copy' als Windows-Befehl. Aufruf: scp",
      "destruktiv": false
    },
    {
      "kategorie": "remote",
      "befehl": "sftp",
      "start": "sftp",
      "kurz": "Secure FTP",
      "lang": "Startet 'Secure FTP' als Windows-Befehl. Aufruf: sftp",
      "destruktiv": false
    },
    {
      "kategorie": "remote",
      "befehl": "winmgmt",
      "start": "winmgmt",
      "kurz": "WMI Verwaltung",
      "lang": "Startet 'WMI Verwaltung' als Windows-Befehl. Aufruf: winmgmt",
      "destruktiv": false
    },
    {
      "kategorie": "remote",
      "befehl": "wmic",
      "start": "wmic",
      "kurz": "WMI Konsole",
      "lang": "Startet 'WMI Konsole' als Windows-Befehl. Aufruf: wmic",
      "destruktiv": false
    },
    {
      "kategorie": "remote",
      "befehl": "wbemtest",
      "start": "wbemtest",
      "kurz": "WMI Testtool",
      "lang": "Startet 'WMI Testtool' als Windows-Befehl. Aufruf: wbemtest",
      "destruktiv": false
    },
    {
      "kategorie": "geraete",
      "befehl": "devmgmt.msc",
      "start": "devmgmt.msc",
      "kurz": "Geräte‑Manager",
      "lang": "Oeffnet das MMC-Snap-In 'Geräte‑Manager'. Aufruf: devmgmt.msc",
      "destruktiv": false
    },
    {
      "kategorie": "geraete",
      "befehl": "hdwwiz.cpl",
      "start": "hdwwiz.cpl",
      "kurz": "Hardware-Assistent",
      "lang": "Startet 'Hardware-Assistent' als Windows-Befehl. Aufruf: hdwwiz.cpl",
      "destruktiv": false
    },
    {
      "kategorie": "geraete",
      "befehl": "control hdwwiz.cpl",
      "start": "control hdwwiz.cpl",
      "kurz": "Hardware-Assistent",
      "lang": "Startet ein Systemsteuerungsfenster (Hardware-Assistent). Aufruf: control hdwwiz.cpl",
      "destruktiv": false
    },
    {
      "kategorie": "geraete",
      "befehl": "rundll32.exe devmgr.dll DeviceManager_Execute",
      "start": "rundll32.exe devmgr.dll DeviceManager_Execute",
      "kurz": "Geräte‑Manager",
      "lang": "Ruft eine System-DLL auf und oeffnet 'Geräte‑Manager'. Aufruf: rundll32.exe devmgr.dll DeviceManager_Execute",
      "destruktiv": false
    },
    {
      "kategorie": "geraete",
      "befehl": "shell:::{4d36e967-e325-11ce-bfc1-08002be10318}",
      "start": "shell:::{4d36e972-e325-11ce-bfc1-08002be10318}",
      "kurz": "Netzwerkadapter",
      "lang": "Oeffnet den Shell-Namespace 'Netzwerkadapter' ueber die CLSID. Aufruf: explorer.exe shell:::{4d36e972-e325-11ce-bfc1-08002be10318}",
      "destruktiv": false
    },
    {
      "kategorie": "geraete",
      "befehl": "shell:::{4d36e968-e325-11ce-bfc1-08002be10318}",
      "start": "shell:::{4d36e979-e325-11ce-bfc1-08002be10318}",
      "kurz": "Drucker",
      "lang": "Oeffnet den Shell-Namespace 'Drucker' ueber die CLSID. Aufruf: explorer.exe shell:::{4d36e979-e325-11ce-bfc1-08002be10318}",
      "destruktiv": false
    },
    {
      "kategorie": "geraete",
      "befehl": "shell:::{4d36e96a-e325-11ce-bfc1-08002be10318}",
      "start": "shell:::{4d36e97b-e325-11ce-bfc1-08002be10318}",
      "kurz": "SCSI Controller",
      "lang": "Oeffnet den Shell-Namespace 'SCSI Controller' ueber die CLSID. Aufruf: explorer.exe shell:::{4d36e97b-e325-11ce-bfc1-08002be10318}",
      "destruktiv": false
    },
    {
      "kategorie": "geraete",
      "befehl": "shell:::{4d36e96b-e325-11ce-bfc1-08002be10318}",
      "start": "shell:::{4d36e96b-e325-11ce-bfc1-08002be10318}",
      "kurz": "Mediengeräte",
      "lang": "Oeffnet den Shell-Namespace 'Mediengeräte' ueber die CLSID. Aufruf: explorer.exe shell:::{4d36e96b-e325-11ce-bfc1-08002be10318}",
      "destruktiv": false
    },
    {
      "kategorie": "geraete",
      "befehl": "shell:::{4d36e96c-e325-11ce-bfc1-08002be10318}",
      "start": "shell:::{4d36e96b-e325-11ce-bfc1-08002be10318}",
      "kurz": "Tastaturen",
      "lang": "Oeffnet den Shell-Namespace 'Tastaturen' ueber die CLSID. Aufruf: explorer.exe shell:::{4d36e96b-e325-11ce-bfc1-08002be10318}",
      "destruktiv": false
    },
    {
      "kategorie": "geraete",
      "befehl": "shell:::{4d36e96d-e325-11ce-bfc1-08002be10318}",
      "start": "shell:::{4d36e96d-e325-11ce-bfc1-08002be10318}",
      "kurz": "Mäuse",
      "lang": "Oeffnet den Shell-Namespace 'Mäuse' ueber die CLSID. Aufruf: explorer.exe shell:::{4d36e96d-e325-11ce-bfc1-08002be10318}",
      "destruktiv": false
    },
    {
      "kategorie": "geraete",
      "befehl": "shell:::{4d36e96f-e325-11ce-bfc1-08002be10318}",
      "start": "shell:::{4d36e96e-e325-11ce-bfc1-08002be10318}",
      "kurz": "Monitore",
      "lang": "Oeffnet den Shell-Namespace 'Monitore' ueber die CLSID. Aufruf: explorer.exe shell:::{4d36e96e-e325-11ce-bfc1-08002be10318}",
      "destruktiv": false
    },
    {
      "kategorie": "geraete",
      "befehl": "shell:::{4d36e970-e325-11ce-bfc1-08002be10318}",
      "start": "shell:::{4d36e96c-e325-11ce-bfc1-08002be10318}",
      "kurz": "Multimedia",
      "lang": "Oeffnet den Shell-Namespace 'Multimedia' ueber die CLSID. Aufruf: explorer.exe shell:::{4d36e96c-e325-11ce-bfc1-08002be10318}",
      "destruktiv": false
    },
    {
      "kategorie": "geraete",
      "befehl": "shell:::{4d36e972-e325-11ce-bfc1-08002be10318}",
      "start": "shell:::{4d36e978-e325-11ce-bfc1-08002be10318}",
      "kurz": "Ports (COM & LPT)",
      "lang": "Oeffnet den Shell-Namespace 'Ports (COM & LPT)' ueber die CLSID. Aufruf: explorer.exe shell:::{4d36e978-e325-11ce-bfc1-08002be10318}",
      "destruktiv": false
    },
    {
      "kategorie": "geraete",
      "befehl": "shell:::{4d36e973-e325-11ce-bfc1-08002be10318}",
      "start": "shell:::{4d36e96a-e325-11ce-bfc1-08002be10318}",
      "kurz": "Speichercontroller",
      "lang": "Oeffnet den Shell-Namespace 'Speichercontroller' ueber die CLSID. Aufruf: explorer.exe shell:::{4d36e96a-e325-11ce-bfc1-08002be10318}",
      "destruktiv": false
    },
    {
      "kategorie": "geraete",
      "befehl": "shell:::{4d36e974-e325-11ce-bfc1-08002be10318}",
      "start": "shell:::{4d36e974-e325-11ce-bfc1-08002be10318}",
      "kurz": "Systemgeräte",
      "lang": "Oeffnet den Shell-Namespace 'Systemgeräte' ueber die CLSID. Aufruf: explorer.exe shell:::{4d36e974-e325-11ce-bfc1-08002be10318}",
      "destruktiv": false
    },
    {
      "kategorie": "geraete",
      "befehl": "shell:::{4d36e975-e325-11ce-bfc1-08002be10318}",
      "start": "shell:::{4d36e975-e325-11ce-bfc1-08002be10318}",
      "kurz": "USB‑Controller",
      "lang": "Oeffnet den Shell-Namespace 'USB‑Controller' ueber die CLSID. Aufruf: explorer.exe shell:::{4d36e975-e325-11ce-bfc1-08002be10318}",
      "destruktiv": false
    },
    {
      "kategorie": "geraete",
      "befehl": "shell:::{4d36e976-e325-11ce-bfc1-08002be10318}",
      "start": "shell:::{6bdd1fc1-810f-11d0-bec7-08002be2092f}",
      "kurz": "FireWire",
      "lang": "Oeffnet den Shell-Namespace 'FireWire' ueber die CLSID. Aufruf: explorer.exe shell:::{6bdd1fc1-810f-11d0-bec7-08002be2092f}",
      "destruktiv": false
    },
    {
      "kategorie": "geraete",
      "befehl": "shell:::{4d36e977-e325-11ce-bfc1-08002be10318}",
      "start": "shell:::{4d36e977-e325-11ce-bfc1-08002be10318}",
      "kurz": "PCMCIA",
      "lang": "Oeffnet den Shell-Namespace 'PCMCIA' ueber die CLSID. Aufruf: explorer.exe shell:::{4d36e977-e325-11ce-bfc1-08002be10318}",
      "destruktiv": false
    },
    {
      "kategorie": "geraete",
      "befehl": "shell:::{4d36e978-e325-11ce-bfc1-08002be10318}",
      "start": "shell:::{4d36e96d-e325-11ce-bfc1-08002be10318}",
      "kurz": "Modems",
      "lang": "Oeffnet den Shell-Namespace 'Modems' ueber die CLSID. Aufruf: explorer.exe shell:::{4d36e96d-e325-11ce-bfc1-08002be10318}",
      "destruktiv": false
    },
    {
      "kategorie": "geraete",
      "befehl": "shell:::{4d36e979-e325-11ce-bfc1-08002be10318}",
      "start": "shell:::{4d36e96c-e325-11ce-bfc1-08002be10318}",
      "kurz": "Soundkarten",
      "lang": "Oeffnet den Shell-Namespace 'Soundkarten' ueber die CLSID. Aufruf: explorer.exe shell:::{4d36e96c-e325-11ce-bfc1-08002be10318}",
      "destruktiv": false
    },
    {
      "kategorie": "geraete",
      "befehl": "shell:::{4d36e97a-e325-11ce-bfc1-08002be10318}",
      "start": "shell:::{4d36e97a-e325-11ce-bfc1-08002be10318}",
      "kurz": "Video‑Controller",
      "lang": "Oeffnet den Shell-Namespace 'Video‑Controller' ueber die CLSID. Aufruf: explorer.exe shell:::{4d36e97a-e325-11ce-bfc1-08002be10318}",
      "destruktiv": false
    },
    {
      "kategorie": "geraete",
      "befehl": "shell:::{4d36e97b-e325-11ce-bfc1-08002be10318}",
      "start": "shell:::{4d36e97b-e325-11ce-bfc1-08002be10318}",
      "kurz": "Speichergeräte",
      "lang": "Oeffnet den Shell-Namespace 'Speichergeräte' ueber die CLSID. Aufruf: explorer.exe shell:::{4d36e97b-e325-11ce-bfc1-08002be10318}",
      "destruktiv": false
    },
    {
      "kategorie": "geraete",
      "befehl": "shell:::{4d36e97d-e325-11ce-bfc1-08002be10318}",
      "start": "shell:::{e0cbf06c-cd8b-4647-bb8a-263b43f0f974}",
      "kurz": "Bluetooth",
      "lang": "Oeffnet den Shell-Namespace 'Bluetooth' ueber die CLSID. Aufruf: explorer.exe shell:::{e0cbf06c-cd8b-4647-bb8a-263b43f0f974}",
      "destruktiv": false
    },
    {
      "kategorie": "geraete",
      "befehl": "shell:::{4d36e97e-e325-11ce-bfc1-08002be10318}",
      "start": "shell:::{4d36e972-e325-11ce-bfc1-08002be10318}",
      "kurz": "WLAN",
      "lang": "Oeffnet den Shell-Namespace 'WLAN' ueber die CLSID. Aufruf: explorer.exe shell:::{4d36e972-e325-11ce-bfc1-08002be10318}",
      "destruktiv": false
    },
    {
      "kategorie": "geraete",
      "befehl": "shell:::{4d36e97f-e325-11ce-bfc1-08002be10318}",
      "start": "shell:::{4d36e97b-e325-11ce-bfc1-08002be10318}",
      "kurz": "RAID Controller",
      "lang": "Oeffnet den Shell-Namespace 'RAID Controller' ueber die CLSID. Aufruf: explorer.exe shell:::{4d36e97b-e325-11ce-bfc1-08002be10318}",
      "destruktiv": false
    },
    {
      "kategorie": "geraete",
      "befehl": "shell:::{4d36e980-e325-11ce-bfc1-08002be10318}",
      "start": "shell:::{4d36e980-e325-11ce-bfc1-08002be10318}",
      "kurz": "SD‑Controller",
      "lang": "Oeffnet den Shell-Namespace 'SD‑Controller' ueber die CLSID. Aufruf: explorer.exe shell:::{4d36e980-e325-11ce-bfc1-08002be10318}",
      "destruktiv": false
    },
    {
      "kategorie": "geraete",
      "befehl": "shell:::{4d36e981-e325-11ce-bfc1-08002be10318}",
      "start": "shell:::{5175d334-c371-4806-b3ba-71fd53c9258d}",
      "kurz": "Sensoren",
      "lang": "Oeffnet den Shell-Namespace 'Sensoren' ueber die CLSID. Aufruf: explorer.exe shell:::{5175d334-c371-4806-b3ba-71fd53c9258d}",
      "destruktiv": false
    },
    {
      "kategorie": "geraete",
      "befehl": "shell:::{4d36e982-e325-11ce-bfc1-08002be10318}",
      "start": "shell:::{ca3e7ab9-b4c3-4ae6-8251-579ef933890f}",
      "kurz": "Kamera",
      "lang": "Oeffnet den Shell-Namespace 'Kamera' ueber die CLSID. Aufruf: explorer.exe shell:::{ca3e7ab9-b4c3-4ae6-8251-579ef933890f}",
      "destruktiv": false
    },
    {
      "kategorie": "geraete",
      "befehl": "shell:::{4d36e983-e325-11ce-bfc1-08002be10318}",
      "start": "shell:::{53d29ef7-377c-4d14-864b-eb3a85769359}",
      "kurz": "Fingerprint",
      "lang": "Oeffnet den Shell-Namespace 'Fingerprint' ueber die CLSID. Aufruf: explorer.exe shell:::{53d29ef7-377c-4d14-864b-eb3a85769359}",
      "destruktiv": false
    },
    {
      "kategorie": "geraete",
      "befehl": "shell:::{4d36e984-e325-11ce-bfc1-08002be10318}",
      "start": "shell:::{d94ee5d8-d189-4994-83d2-f68d7d41b0e6}",
      "kurz": "TPM",
      "lang": "Oeffnet den Shell-Namespace 'TPM' ueber die CLSID. Aufruf: explorer.exe shell:::{d94ee5d8-d189-4994-83d2-f68d7d41b0e6}",
      "destruktiv": false
    },
    {
      "kategorie": "geraete",
      "befehl": "shell:::{4d36e985-e325-11ce-bfc1-08002be10318}",
      "start": "shell:::{4d36e97d-e325-11ce-bfc1-08002be10318}",
      "kurz": "Virtual Devices",
      "lang": "Oeffnet den Shell-Namespace 'Virtual Devices' ueber die CLSID. Aufruf: explorer.exe shell:::{4d36e97d-e325-11ce-bfc1-08002be10318}",
      "destruktiv": false
    },
    {
      "kategorie": "geraete",
      "befehl": "shell:::{4d36e986-e325-11ce-bfc1-08002be10318}",
      "start": "shell:::{4d36e986-e325-11ce-bfc1-08002be10318}",
      "kurz": "Hyper‑V Devices",
      "lang": "Oeffnet den Shell-Namespace 'Hyper‑V Devices' ueber die CLSID. Aufruf: explorer.exe shell:::{4d36e986-e325-11ce-bfc1-08002be10318}",
      "destruktiv": false
    },
    {
      "kategorie": "geraete",
      "befehl": "shell:::{4d36e987-e325-11ce-bfc1-08002be10318}",
      "start": "shell:::{4d36e97d-e325-11ce-bfc1-08002be10318}",
      "kurz": "Remote Devices",
      "lang": "Oeffnet den Shell-Namespace 'Remote Devices' ueber die CLSID. Aufruf: explorer.exe shell:::{4d36e97d-e325-11ce-bfc1-08002be10318}",
      "destruktiv": false
    },
    {
      "kategorie": "geraete",
      "befehl": "shell:::{4d36e988-e325-11ce-bfc1-08002be10318}",
      "start": "shell:::{4d36e988-e325-11ce-bfc1-08002be10318}",
      "kurz": "HID Geräte",
      "lang": "Oeffnet den Shell-Namespace 'HID Geräte' ueber die CLSID. Aufruf: explorer.exe shell:::{4d36e988-e325-11ce-bfc1-08002be10318}",
      "destruktiv": false
    },
    {
      "kategorie": "geraete",
      "befehl": "shell:::{4d36e989-e325-11ce-bfc1-08002be10318}",
      "start": "shell:::{4d36e97d-e325-11ce-bfc1-08002be10318}",
      "kurz": "Dockingstation",
      "lang": "Oeffnet den Shell-Namespace 'Dockingstation' ueber die CLSID. Aufruf: explorer.exe shell:::{4d36e97d-e325-11ce-bfc1-08002be10318}",
      "destruktiv": false
    },
    {
      "kategorie": "geraete",
      "befehl": "shell:::{4d36e98a-e325-11ce-bfc1-08002be10318}",
      "start": "shell:::{72631e54-78a4-11d0-bcf7-00aa00b7b32a}",
      "kurz": "Batterien",
      "lang": "Oeffnet den Shell-Namespace 'Batterien' ueber die CLSID. Aufruf: explorer.exe shell:::{72631e54-78a4-11d0-bcf7-00aa00b7b32a}",
      "destruktiv": false
    },
    {
      "kategorie": "geraete",
      "befehl": "shell:::{4d36e98b-e325-11ce-bfc1-08002be10318}",
      "start": "shell:::{4d36e98b-e325-11ce-bfc1-08002be10318}",
      "kurz": "ACPI Geräte",
      "lang": "Oeffnet den Shell-Namespace 'ACPI Geräte' ueber die CLSID. Aufruf: explorer.exe shell:::{4d36e98b-e325-11ce-bfc1-08002be10318}",
      "destruktiv": false
    },
    {
      "kategorie": "geraete",
      "befehl": "shell:::{4d36e98c-e325-11ce-bfc1-08002be10318}",
      "start": "shell:::{4d36e98c-e325-11ce-bfc1-08002be10318}",
      "kurz": "PCI Geräte",
      "lang": "Oeffnet den Shell-Namespace 'PCI Geräte' ueber die CLSID. Aufruf: explorer.exe shell:::{4d36e98c-e325-11ce-bfc1-08002be10318}",
      "destruktiv": false
    },
    {
      "kategorie": "geraete",
      "befehl": "shell:::{4d36e98d-e325-11ce-bfc1-08002be10318}",
      "start": "shell:::{4d36e98d-e325-11ce-bfc1-08002be10318}",
      "kurz": "ISA Geräte",
      "lang": "Oeffnet den Shell-Namespace 'ISA Geräte' ueber die CLSID. Aufruf: explorer.exe shell:::{4d36e98d-e325-11ce-bfc1-08002be10318}",
      "destruktiv": false
    },
    {
      "kategorie": "geraete",
      "befehl": "shell:::{4d36e98e-e325-11ce-bfc1-08002be10318}",
      "start": "shell:::{4d36e98e-e325-11ce-bfc1-08002be10318}",
      "kurz": "Legacy Geräte",
      "lang": "Oeffnet den Shell-Namespace 'Legacy Geräte' ueber die CLSID. Aufruf: explorer.exe shell:::{4d36e98e-e325-11ce-bfc1-08002be10318}",
      "destruktiv": false
    },
    {
      "kategorie": "geraete",
      "befehl": "shell:::{4d36e98f-e325-11ce-bfc1-08002be10318}",
      "start": "shell:::{4d36e98f-e325-11ce-bfc1-08002be10318}",
      "kurz": "Unbekannte Geräte",
      "lang": "Oeffnet den Shell-Namespace 'Unbekannte Geräte' ueber die CLSID. Aufruf: explorer.exe shell:::{4d36e98f-e325-11ce-bfc1-08002be10318}",
      "destruktiv": false
    },
    {
      "kategorie": "sicherheit",
      "befehl": "wscui.cpl",
      "start": "wscui.cpl",
      "kurz": "Sicherheitscenter",
      "lang": "Startet 'Sicherheitscenter' als Windows-Befehl. Aufruf: wscui.cpl",
      "destruktiv": false
    },
    {
      "kategorie": "sicherheit",
      "befehl": "secpol.msc",
      "start": "secpol.msc",
      "kurz": "Lokale Sicherheitsrichtlinie",
      "lang": "Oeffnet das MMC-Snap-In 'Lokale Sicherheitsrichtlinie'. Aufruf: secpol.msc",
      "destruktiv": false
    },
    {
      "kategorie": "sicherheit",
      "befehl": "wf.msc",
      "start": "wf.msc",
      "kurz": "Firewall",
      "lang": "Oeffnet das MMC-Snap-In 'Firewall'. Aufruf: wf.msc",
      "destruktiv": false
    },
    {
      "kategorie": "sicherheit",
      "befehl": "powershell: Get-MpComputerStatus",
      "start": "powershell: Get-MpComputerStatus",
      "kurz": "Defender Status",
      "lang": "Fuehrt das PowerShell-Cmdlet 'Get-MpComputerStatus' in einer neuen Konsole aus (Defender Status). Die Konsole bleibt offen.",
      "destruktiv": false
    },
    {
      "kategorie": "sicherheit",
      "befehl": "powershell: Update-MpSignature",
      "start": "powershell: Update-MpSignature",
      "kurz": "Defender Signaturen",
      "lang": "Fuehrt das PowerShell-Cmdlet 'Update-MpSignature' in einer neuen Konsole aus (Defender Signaturen). Die Konsole bleibt offen.",
      "destruktiv": false
    },
    {
      "kategorie": "sicherheit",
      "befehl": "powershell: Start-MpScan",
      "start": "powershell: Start-MpScan",
      "kurz": "Defender Scan",
      "lang": "Fuehrt das PowerShell-Cmdlet 'Start-MpScan' in einer neuen Konsole aus (Defender Scan). Die Konsole bleibt offen.",
      "destruktiv": false
    },
    {
      "kategorie": "sicherheit",
      "befehl": "powershell: Set-MpPreference",
      "start": "powershell: Set-MpPreference",
      "kurz": "Defender Einstellungen",
      "lang": "Fuehrt das PowerShell-Cmdlet 'Set-MpPreference' in einer neuen Konsole aus (Defender Einstellungen). Die Konsole bleibt offen.",
      "destruktiv": false
    },
    {
      "kategorie": "sicherheit",
      "befehl": "powershell: Get-MpThreat",
      "start": "powershell: Get-MpThreat",
      "kurz": "Bedrohungen",
      "lang": "Fuehrt das PowerShell-Cmdlet 'Get-MpThreat' in einer neuen Konsole aus (Bedrohungen). Die Konsole bleibt offen.",
      "destruktiv": false
    },
    {
      "kategorie": "sicherheit",
      "befehl": "powershell: Get-MpThreatCatalog",
      "start": "powershell: Get-MpThreatCatalog",
      "kurz": "Bedrohungskatalog",
      "lang": "Fuehrt das PowerShell-Cmdlet 'Get-MpThreatCatalog' in einer neuen Konsole aus (Bedrohungskatalog). Die Konsole bleibt offen.",
      "destruktiv": false
    },
    {
      "kategorie": "sicherheit",
      "befehl": "powershell: Get-MpPerformanceReport",
      "start": "powershell: Get-MpPerformanceReport",
      "kurz": "Defender Performance",
      "lang": "Fuehrt das PowerShell-Cmdlet 'Get-MpPerformanceReport' in einer neuen Konsole aus (Defender Performance). Die Konsole bleibt offen.",
      "destruktiv": false
    },
    {
      "kategorie": "sicherheit",
      "befehl": "powershell: Get-MpRemediation",
      "start": "powershell: Get-MpRemediation",
      "kurz": "Bereinigung",
      "lang": "Fuehrt das PowerShell-Cmdlet 'Get-MpRemediation' in einer neuen Konsole aus (Bereinigung). Die Konsole bleibt offen.",
      "destruktiv": false
    },
    {
      "kategorie": "sicherheit",
      "befehl": "powershell: Get-MpScanLog",
      "start": "powershell: Get-MpScanLog",
      "kurz": "Scanlog",
      "lang": "Fuehrt das PowerShell-Cmdlet 'Get-MpScanLog' in einer neuen Konsole aus (Scanlog). Die Konsole bleibt offen.",
      "destruktiv": false
    },
    {
      "kategorie": "sicherheit",
      "befehl": "powershell: Get-MpSignature",
      "start": "powershell: Get-MpSignature",
      "kurz": "Signaturen",
      "lang": "Fuehrt das PowerShell-Cmdlet 'Get-MpSignature' in einer neuen Konsole aus (Signaturen). Die Konsole bleibt offen.",
      "destruktiv": false
    },
    {
      "kategorie": "sicherheit",
      "befehl": "powershell: Get-MpThreatDetection",
      "start": "powershell: Get-MpThreatDetection",
      "kurz": "Erkennung",
      "lang": "Fuehrt das PowerShell-Cmdlet 'Get-MpThreatDetection' in einer neuen Konsole aus (Erkennung). Die Konsole bleibt offen.",
      "destruktiv": false
    },
    {
      "kategorie": "sicherheit",
      "befehl": "powershell: Get-MpPreference",
      "start": "powershell: Get-MpPreference",
      "kurz": "Einstellungen",
      "lang": "Fuehrt das PowerShell-Cmdlet 'Get-MpPreference' in einer neuen Konsole aus (Einstellungen). Die Konsole bleibt offen.",
      "destruktiv": false
    },
    {
      "kategorie": "registry",
      "befehl": "regedit.exe",
      "start": "regedit.exe",
      "kurz": "Registry Editor",
      "lang": "Startet 'Registry Editor' als Windows-Befehl. Aufruf: regedit.exe",
      "destruktiv": false
    },
    {
      "kategorie": "registry",
      "befehl": "regedt32.exe",
      "start": "regedt32.exe",
      "kurz": "Registry Editor (alt)",
      "lang": "Startet 'Registry Editor (alt)' als Windows-Befehl. Aufruf: regedt32.exe",
      "destruktiv": false
    },
    {
      "kategorie": "registry",
      "befehl": "reg query",
      "start": "reg query",
      "kurz": "Registry abfragen",
      "lang": "Startet 'Registry abfragen' als Windows-Befehl. Aufruf: reg query",
      "destruktiv": false
    },
    {
      "kategorie": "registry",
      "befehl": "reg add",
      "start": "reg add",
      "kurz": "Registry hinzufügen",
      "lang": "Achtung: Dieser Befehl kann das System aendern oder Daten loeschen (Registry hinzufügen). Aufruf nur nach Bestaetigung: reg add",
      "destruktiv": true
    },
    {
      "kategorie": "registry",
      "befehl": "reg delete",
      "start": "reg delete",
      "kurz": "Registry löschen",
      "lang": "Achtung: Dieser Befehl kann das System aendern oder Daten loeschen (Registry löschen). Aufruf nur nach Bestaetigung: reg delete",
      "destruktiv": true
    },
    {
      "kategorie": "registry",
      "befehl": "reg copy",
      "start": "reg copy",
      "kurz": "Registry kopieren",
      "lang": "Startet 'Registry kopieren' als Windows-Befehl. Aufruf: reg copy",
      "destruktiv": false
    },
    {
      "kategorie": "registry",
      "befehl": "reg save",
      "start": "reg save",
      "kurz": "Registry sichern",
      "lang": "Startet 'Registry sichern' als Windows-Befehl. Aufruf: reg save",
      "destruktiv": false
    },
    {
      "kategorie": "registry",
      "befehl": "reg restore",
      "start": "reg restore",
      "kurz": "Registry wiederherstellen",
      "lang": "Achtung: Dieser Befehl kann das System aendern oder Daten loeschen (Registry wiederherstellen). Aufruf nur nach Bestaetigung: reg restore",
      "destruktiv": true
    },
    {
      "kategorie": "registry",
      "befehl": "reg compare",
      "start": "reg compare",
      "kurz": "Registry vergleichen",
      "lang": "Startet 'Registry vergleichen' als Windows-Befehl. Aufruf: reg compare",
      "destruktiv": false
    },
    {
      "kategorie": "registry",
      "befehl": "reg export",
      "start": "reg export",
      "kurz": "Registry exportieren",
      "lang": "Startet 'Registry exportieren' als Windows-Befehl. Aufruf: reg export",
      "destruktiv": false
    },
    {
      "kategorie": "registry",
      "befehl": "reg import",
      "start": "reg import",
      "kurz": "Registry importieren",
      "lang": "Achtung: Dieser Befehl kann das System aendern oder Daten loeschen (Registry importieren). Aufruf nur nach Bestaetigung: reg import",
      "destruktiv": true
    },
    {
      "kategorie": "registry",
      "befehl": "shell:::{00000000-0000-0000-0000-000000000000}",
      "start": "shell:::{00000000-0000-0000-0000-000000000000}",
      "kurz": "Root",
      "lang": "Oeffnet den Shell-Namespace 'Root' ueber die CLSID. Aufruf: explorer.exe shell:::{00000000-0000-0000-0000-000000000000}",
      "destruktiv": false
    },
    {
      "kategorie": "registry",
      "befehl": "shell:::{20D04FE0-3AEA-1069-A2D8-08002B30309D}",
      "start": "shell:::{20D04FE0-3AEA-1069-A2D8-08002B30309D}",
      "kurz": "Dieser PC",
      "lang": "Oeffnet den Shell-Namespace 'Dieser PC' ueber die CLSID. Aufruf: explorer.exe shell:::{20D04FE0-3AEA-1069-A2D8-08002B30309D}",
      "destruktiv": false
    },
    {
      "kategorie": "registry",
      "befehl": "shell:::{F02C1A0D-BE21-4350-88B0-7367FC96EF3C}",
      "start": "shell:::{F02C1A0D-BE21-4350-88B0-7367FC96EF3C}",
      "kurz": "Netzwerk",
      "lang": "Oeffnet den Shell-Namespace 'Netzwerk' ueber die CLSID. Aufruf: explorer.exe shell:::{F02C1A0D-BE21-4350-88B0-7367FC96EF3C}",
      "destruktiv": false
    },
    {
      "kategorie": "registry",
      "befehl": "shell:::{645FF040-5081-101B-9F08-00AA002F954E}",
      "start": "shell:::{645FF040-5081-101B-9F08-00AA002F954E}",
      "kurz": "Papierkorb",
      "lang": "Oeffnet den Shell-Namespace 'Papierkorb' ueber die CLSID. Aufruf: explorer.exe shell:::{645FF040-5081-101B-9F08-00AA002F954E}",
      "destruktiv": false
    },
    {
      "kategorie": "registry",
      "befehl": "shell:::{ED7BA470-8E54-465E-825C-99712043E01C}",
      "start": "shell:::{ED7BA470-8E54-465E-825C-99712043E01C}",
      "kurz": "GodMode",
      "lang": "Oeffnet den Shell-Namespace 'GodMode' ueber die CLSID. Aufruf: explorer.exe shell:::{ED7BA470-8E54-465E-825C-99712043E01C}",
      "destruktiv": false
    },
    {
      "kategorie": "registry",
      "befehl": "shell:::{1F4DE370-D627-11D1-BA4F-00A0C91EEDBA}",
      "start": "shell:::{1F4DE370-D627-11D1-BA4F-00A0C91EEDBA}",
      "kurz": "Systemsteuerung",
      "lang": "Oeffnet den Shell-Namespace 'Systemsteuerung' ueber die CLSID. Aufruf: explorer.exe shell:::{1F4DE370-D627-11D1-BA4F-00A0C91EEDBA}",
      "destruktiv": false
    },
    {
      "kategorie": "registry",
      "befehl": "shell:::{26EE0668-A00A-44D7-9371-BEB064C98683}",
      "start": "shell:::{26EE0668-A00A-44D7-9371-BEB064C98683}",
      "kurz": "Alle Einstellungen",
      "lang": "Oeffnet den Shell-Namespace 'Alle Einstellungen' ueber die CLSID. Aufruf: explorer.exe shell:::{26EE0668-A00A-44D7-9371-BEB064C98683}",
      "destruktiv": false
    },
    {
      "kategorie": "registry",
      "befehl": "shell:::{D20A3E47-8B2F-4F85-9BB5-DBF9A1C3D1C3}",
      "start": "shell:::{D20A3E47-8B2F-4F85-9BB5-DBF9A1C3D1C3}",
      "kurz": "Verwaltung",
      "lang": "Oeffnet den Shell-Namespace 'Verwaltung' ueber die CLSID. Aufruf: explorer.exe shell:::{D20A3E47-8B2F-4F85-9BB5-DBF9A1C3D1C3}",
      "destruktiv": false
    },
    {
      "kategorie": "registry",
      "befehl": "shell:::{E9950154-C418-419e-A90A-20C5287AE24B}",
      "start": "shell:::{E9950154-C418-419e-A90A-20C5287AE24B}",
      "kurz": "Sicherheit",
      "lang": "Oeffnet den Shell-Namespace 'Sicherheit' ueber die CLSID. Aufruf: explorer.exe shell:::{E9950154-C418-419e-A90A-20C5287AE24B}",
      "destruktiv": false
    },
    {
      "kategorie": "registry",
      "befehl": "shell:::{A3C414DC-1D3A-4B3B-9C1E-5A1E2F1F1F1F}",
      "start": "shell:::{A3C414DC-1D3A-4B3B-9C1E-5A1E2F1F1F1F}",
      "kurz": "Geräte",
      "lang": "Oeffnet den Shell-Namespace 'Geräte' ueber die CLSID. Aufruf: explorer.exe shell:::{A3C414DC-1D3A-4B3B-9C1E-5A1E2F1F1F1F}",
      "destruktiv": false
    },
    {
      "kategorie": "win10",
      "befehl": "ms-settings:home",
      "start": "ms-settings:home",
      "kurz": "Startseite Einstellungen",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Startseite Einstellungen'. URI: ms-settings:home",
      "destruktiv": false
    },
    {
      "kategorie": "win10",
      "befehl": "ms-settings:privacy-location",
      "start": "ms-settings:privacy-location",
      "kurz": "Standort",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Standort'. URI: ms-settings:privacy-location",
      "destruktiv": false
    },
    {
      "kategorie": "win10",
      "befehl": "ms-settings:privacy-webcam",
      "start": "ms-settings:privacy-webcam",
      "kurz": "Kamera",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Kamera'. URI: ms-settings:privacy-webcam",
      "destruktiv": false
    },
    {
      "kategorie": "win10",
      "befehl": "ms-settings:privacy-microphone",
      "start": "ms-settings:privacy-microphone",
      "kurz": "Mikrofon",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Mikrofon'. URI: ms-settings:privacy-microphone",
      "destruktiv": false
    },
    {
      "kategorie": "win10",
      "befehl": "ms-settings:privacy-accountinfo",
      "start": "ms-settings:privacy-accountinfo",
      "kurz": "Kontoinformationen",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Kontoinformationen'. URI: ms-settings:privacy-accountinfo",
      "destruktiv": false
    },
    {
      "kategorie": "win10",
      "befehl": "ms-settings:privacy-contacts",
      "start": "ms-settings:privacy-contacts",
      "kurz": "Kontakte",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Kontakte'. URI: ms-settings:privacy-contacts",
      "destruktiv": false
    },
    {
      "kategorie": "win10",
      "befehl": "ms-settings:privacy-calendar",
      "start": "ms-settings:privacy-calendar",
      "kurz": "Kalender",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Kalender'. URI: ms-settings:privacy-calendar",
      "destruktiv": false
    },
    {
      "kategorie": "win10",
      "befehl": "ms-settings:privacy-callhistory",
      "start": "ms-settings:privacy-callhistory",
      "kurz": "Anrufverlauf",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Anrufverlauf'. URI: ms-settings:privacy-callhistory",
      "destruktiv": false
    },
    {
      "kategorie": "win10",
      "befehl": "ms-settings:privacy-email",
      "start": "ms-settings:privacy-email",
      "kurz": "E-Mail",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'E-Mail'. URI: ms-settings:privacy-email",
      "destruktiv": false
    },
    {
      "kategorie": "win10",
      "befehl": "ms-settings:privacy-messaging",
      "start": "ms-settings:privacy-messaging",
      "kurz": "Messaging",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Messaging'. URI: ms-settings:privacy-messaging",
      "destruktiv": false
    },
    {
      "kategorie": "win10",
      "befehl": "ms-settings:privacy-radios",
      "start": "ms-settings:privacy-radios",
      "kurz": "Funkgeräte",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Funkgeräte'. URI: ms-settings:privacy-radios",
      "destruktiv": false
    },
    {
      "kategorie": "win10",
      "befehl": "ms-settings:privacy-otherdevices",
      "start": "ms-settings:privacy-otherdevices",
      "kurz": "Andere Geräte",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Andere Geräte'. URI: ms-settings:privacy-otherdevices",
      "destruktiv": false
    },
    {
      "kategorie": "win10",
      "befehl": "ms-settings:privacy-feedback",
      "start": "ms-settings:privacy-feedback",
      "kurz": "Feedback",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Feedback'. URI: ms-settings:privacy-feedback",
      "destruktiv": false
    },
    {
      "kategorie": "win10",
      "befehl": "ms-settings:privacy-backgroundapps",
      "start": "ms-settings:privacy-backgroundapps",
      "kurz": "Hintergrund-Apps",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Hintergrund-Apps'. URI: ms-settings:privacy-backgroundapps",
      "destruktiv": false
    },
    {
      "kategorie": "win10",
      "befehl": "ms-settings:privacy-appdiagnostics",
      "start": "ms-settings:privacy-appdiagnostics",
      "kurz": "App-Diagnose",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'App-Diagnose'. URI: ms-settings:privacy-appdiagnostics",
      "destruktiv": false
    },
    {
      "kategorie": "win10",
      "befehl": "ms-settings:privacy-activityhistory",
      "start": "ms-settings:privacy-activityhistory",
      "kurz": "Aktivitätsverlauf",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Aktivitätsverlauf'. URI: ms-settings:privacy-activityhistory",
      "destruktiv": false
    },
    {
      "kategorie": "win10",
      "befehl": "ms-settings:privacy-speech",
      "start": "ms-settings:privacy-speech",
      "kurz": "Sprache",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Sprache'. URI: ms-settings:privacy-speech",
      "destruktiv": false
    },
    {
      "kategorie": "win10",
      "befehl": "ms-settings:privacy-general",
      "start": "ms-settings:privacy-general",
      "kurz": "Allgemein",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Allgemein'. URI: ms-settings:privacy-general",
      "destruktiv": false
    },
    {
      "kategorie": "win10",
      "befehl": "ms-settings:privacy-broadfilesystemaccess",
      "start": "ms-settings:privacy-broadfilesystemaccess",
      "kurz": "Dateisystemzugriff",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Dateisystemzugriff'. URI: ms-settings:privacy-broadfilesystemaccess",
      "destruktiv": false
    },
    {
      "kategorie": "win10",
      "befehl": "ms-settings:privacy-motion",
      "start": "ms-settings:privacy-motion",
      "kurz": "Bewegung",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Bewegung'. URI: ms-settings:privacy-motion",
      "destruktiv": false
    },
    {
      "kategorie": "win10",
      "befehl": "ms-settings:privacy-notifications",
      "start": "ms-settings:privacy-notifications",
      "kurz": "Benachrichtigungen",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Benachrichtigungen'. URI: ms-settings:privacy-notifications",
      "destruktiv": false
    },
    {
      "kategorie": "win10",
      "befehl": "ms-settings:privacy-tasks",
      "start": "ms-settings:privacy-tasks",
      "kurz": "Aufgaben",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Aufgaben'. URI: ms-settings:privacy-tasks",
      "destruktiv": false
    },
    {
      "kategorie": "win10",
      "befehl": "ms-settings:privacy-documents",
      "start": "ms-settings:privacy-documents",
      "kurz": "Dokumente",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Dokumente'. URI: ms-settings:privacy-documents",
      "destruktiv": false
    },
    {
      "kategorie": "win10",
      "befehl": "ms-settings:privacy-pictures",
      "start": "ms-settings:privacy-pictures",
      "kurz": "Bilder",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Bilder'. URI: ms-settings:privacy-pictures",
      "destruktiv": false
    },
    {
      "kategorie": "win10",
      "befehl": "ms-settings:privacy-videos",
      "start": "ms-settings:privacy-videos",
      "kurz": "Videos",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Videos'. URI: ms-settings:privacy-videos",
      "destruktiv": false
    },
    {
      "kategorie": "win10",
      "befehl": "ms-settings:privacy-fileSystem",
      "start": "ms-settings:privacy-fileSystem",
      "kurz": "Dateisystem",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Dateisystem'. URI: ms-settings:privacy-fileSystem",
      "destruktiv": false
    },
    {
      "kategorie": "win10",
      "befehl": "ms-settings:gaming-gamebar",
      "start": "ms-settings:gaming-gamebar",
      "kurz": "Game Bar",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Game Bar'. URI: ms-settings:gaming-gamebar",
      "destruktiv": false
    },
    {
      "kategorie": "win10",
      "befehl": "ms-settings:gaming-gamedvr",
      "start": "ms-settings:gaming-gamedvr",
      "kurz": "Game DVR",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Game DVR'. URI: ms-settings:gaming-gamedvr",
      "destruktiv": false
    },
    {
      "kategorie": "win10",
      "befehl": "ms-settings:gaming-broadcasting",
      "start": "ms-settings:gaming-broadcasting",
      "kurz": "Broadcasting",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Broadcasting'. URI: ms-settings:gaming-broadcasting",
      "destruktiv": false
    },
    {
      "kategorie": "win10",
      "befehl": "ms-settings:gaming-gamemode",
      "start": "ms-settings:gaming-gamemode",
      "kurz": "Game Mode",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Game Mode'. URI: ms-settings:gaming-gamemode",
      "destruktiv": false
    },
    {
      "kategorie": "win10",
      "befehl": "ms-settings:gaming-xboxnetworking",
      "start": "ms-settings:gaming-xboxnetworking",
      "kurz": "Xbox Networking",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Xbox Networking'. URI: ms-settings:gaming-xboxnetworking",
      "destruktiv": false
    },
    {
      "kategorie": "win10",
      "befehl": "ms-settings:mobile-devices",
      "start": "ms-settings:mobile-devices",
      "kurz": "Mobile Geräte",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Mobile Geräte'. URI: ms-settings:mobile-devices",
      "destruktiv": false
    },
    {
      "kategorie": "win10",
      "befehl": "ms-settings:mobile-devices-addphone",
      "start": "ms-settings:mobile-devices-addphone",
      "kurz": "Telefon hinzufügen",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Telefon hinzufügen'. URI: ms-settings:mobile-devices-addphone",
      "destruktiv": false
    },
    {
      "kategorie": "win11",
      "befehl": "ms-settings:display-advanced",
      "start": "ms-settings:display-advanced",
      "kurz": "Erweiterte Anzeige",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Erweiterte Anzeige'. URI: ms-settings:display-advanced",
      "destruktiv": false
    },
    {
      "kategorie": "win11",
      "befehl": "ms-settings:display-advancedgraphics",
      "start": "ms-settings:display-advancedgraphics",
      "kurz": "GPU Einstellungen",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'GPU Einstellungen'. URI: ms-settings:display-advancedgraphics",
      "destruktiv": false
    },
    {
      "kategorie": "win11",
      "befehl": "ms-settings:multitasking-snap",
      "start": "ms-settings:multitasking-snap",
      "kurz": "Snap Layouts",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Snap Layouts'. URI: ms-settings:multitasking-snap",
      "destruktiv": false
    },
    {
      "kategorie": "win11",
      "befehl": "ms-settings:taskbar",
      "start": "ms-settings:taskbar",
      "kurz": "Taskleiste",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Taskleiste'. URI: ms-settings:taskbar",
      "destruktiv": false
    },
    {
      "kategorie": "win11",
      "befehl": "ms-settings:taskbar-behavior",
      "start": "ms-settings:taskbar-behavior",
      "kurz": "Taskleistenverhalten",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Taskleistenverhalten'. URI: ms-settings:taskbar-behavior",
      "destruktiv": false
    },
    {
      "kategorie": "win11",
      "befehl": "ms-settings:personalization-start",
      "start": "ms-settings:personalization-start",
      "kurz": "Startmenü",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Startmenü'. URI: ms-settings:personalization-start",
      "destruktiv": false
    },
    {
      "kategorie": "win11",
      "befehl": "ms-settings:personalization-colors",
      "start": "ms-settings:personalization-colors",
      "kurz": "Farben",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Farben'. URI: ms-settings:personalization-colors",
      "destruktiv": false
    },
    {
      "kategorie": "win11",
      "befehl": "ms-settings:personalization-themes",
      "start": "ms-settings:personalization-themes",
      "kurz": "Themes",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Themes'. URI: ms-settings:personalization-themes",
      "destruktiv": false
    },
    {
      "kategorie": "win11",
      "befehl": "ms-settings:personalization-background",
      "start": "ms-settings:personalization-background",
      "kurz": "Hintergrund",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Hintergrund'. URI: ms-settings:personalization-background",
      "destruktiv": false
    },
    {
      "kategorie": "win11",
      "befehl": "ms-settings:personalization-lockscreen",
      "start": "ms-settings:personalization-lockscreen",
      "kurz": "Sperrbildschirm",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Sperrbildschirm'. URI: ms-settings:personalization-lockscreen",
      "destruktiv": false
    },
    {
      "kategorie": "win11",
      "befehl": "ms-settings:personalization-fonts",
      "start": "ms-settings:personalization-fonts",
      "kurz": "Schriftarten",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Schriftarten'. URI: ms-settings:personalization-fonts",
      "destruktiv": false
    },
    {
      "kategorie": "win11",
      "befehl": "ms-settings:personalization-touchkeyboard",
      "start": "ms-settings:personalization-touchkeyboard",
      "kurz": "Touch‑Tastatur",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Touch‑Tastatur'. URI: ms-settings:personalization-touchkeyboard",
      "destruktiv": false
    },
    {
      "kategorie": "win11",
      "befehl": "ms-settings:personalization-devices",
      "start": "ms-settings:personalization-devices",
      "kurz": "Geräte",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Geräte'. URI: ms-settings:personalization-devices",
      "destruktiv": false
    },
    {
      "kategorie": "win11",
      "befehl": "ms-settings:windowsupdate-restartoptions",
      "start": "ms-settings:windowsupdate-restartoptions",
      "kurz": "Neustartoptionen",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Neustartoptionen'. URI: ms-settings:windowsupdate-restartoptions",
      "destruktiv": false
    },
    {
      "kategorie": "win11",
      "befehl": "ms-settings:windowsupdate-history",
      "start": "ms-settings:windowsupdate-history",
      "kurz": "Update‑Historie",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Update‑Historie'. URI: ms-settings:windowsupdate-history",
      "destruktiv": false
    },
    {
      "kategorie": "win11",
      "befehl": "ms-settings:windowsupdate-options",
      "start": "ms-settings:windowsupdate-options",
      "kurz": "Update‑Optionen",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Update‑Optionen'. URI: ms-settings:windowsupdate-options",
      "destruktiv": false
    },
    {
      "kategorie": "win11",
      "befehl": "ms-settings:bluetooth-devices",
      "start": "ms-settings:bluetooth-devices",
      "kurz": "Bluetooth Geräte",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Bluetooth Geräte'. URI: ms-settings:bluetooth-devices",
      "destruktiv": false
    },
    {
      "kategorie": "win11",
      "befehl": "ms-settings:network-ethernet",
      "start": "ms-settings:network-ethernet",
      "kurz": "Ethernet",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Ethernet'. URI: ms-settings:network-ethernet",
      "destruktiv": false
    },
    {
      "kategorie": "win11",
      "befehl": "ms-settings:network-wifi",
      "start": "ms-settings:network-wifi",
      "kurz": "WLAN",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'WLAN'. URI: ms-settings:network-wifi",
      "destruktiv": false
    },
    {
      "kategorie": "win11",
      "befehl": "ms-settings:network-vpn",
      "start": "ms-settings:network-vpn",
      "kurz": "VPN",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'VPN'. URI: ms-settings:network-vpn",
      "destruktiv": false
    },
    {
      "kategorie": "win11",
      "befehl": "ms-settings:network-mobilehotspot",
      "start": "ms-settings:network-mobilehotspot",
      "kurz": "Hotspot",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Hotspot'. URI: ms-settings:network-mobilehotspot",
      "destruktiv": false
    },
    {
      "kategorie": "win11",
      "befehl": "ms-settings:network-proxy",
      "start": "ms-settings:network-proxy",
      "kurz": "Proxy",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Proxy'. URI: ms-settings:network-proxy",
      "destruktiv": false
    },
    {
      "kategorie": "win11",
      "befehl": "ms-settings:apps-volume",
      "start": "ms-settings:apps-volume",
      "kurz": "App‑Lautstärke",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'App‑Lautstärke'. URI: ms-settings:apps-volume",
      "destruktiv": false
    },
    {
      "kategorie": "win11",
      "befehl": "ms-settings:apps-advanced-appsettings",
      "start": "ms-settings:apps-advanced-appsettings",
      "kurz": "Erweiterte App‑Einstellungen",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Erweiterte App‑Einstellungen'. URI: ms-settings:apps-advanced-appsettings",
      "destruktiv": false
    },
    {
      "kategorie": "win11",
      "befehl": "ms-settings:system-sound",
      "start": "ms-settings:system-sound",
      "kurz": "Sound",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Sound'. URI: ms-settings:system-sound",
      "destruktiv": false
    },
    {
      "kategorie": "win11",
      "befehl": "ms-settings:system-notifications",
      "start": "ms-settings:system-notifications",
      "kurz": "Benachrichtigungen",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Benachrichtigungen'. URI: ms-settings:system-notifications",
      "destruktiv": false
    },
    {
      "kategorie": "win11",
      "befehl": "ms-settings:system-storage",
      "start": "ms-settings:system-storage",
      "kurz": "Speicher",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Speicher'. URI: ms-settings:system-storage",
      "destruktiv": false
    },
    {
      "kategorie": "win11",
      "befehl": "ms-settings:system-battery",
      "start": "ms-settings:system-battery",
      "kurz": "Akku",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Akku'. URI: ms-settings:system-battery",
      "destruktiv": false
    },
    {
      "kategorie": "deep",
      "befehl": "shell:::{BB06C0E4-D293-4f75-8A90-CB05B6477EEE}",
      "start": "shell:::{BB06C0E4-D293-4f75-8A90-CB05B6477EEE}",
      "kurz": "Systeminfo",
      "lang": "Oeffnet den Shell-Namespace 'Systeminfo' ueber die CLSID. Aufruf: explorer.exe shell:::{BB06C0E4-D293-4f75-8A90-CB05B6477EEE}",
      "destruktiv": false
    },
    {
      "kategorie": "deep",
      "befehl": "shell:::{D20A3E47-8B2F-4F85-9BB5-DBF9A1C3D1C3}",
      "start": "shell:::{D20A3E47-8B2F-4F85-9BB5-DBF9A1C3D1C3}",
      "kurz": "Verwaltung",
      "lang": "Oeffnet den Shell-Namespace 'Verwaltung' ueber die CLSID. Aufruf: explorer.exe shell:::{D20A3E47-8B2F-4F85-9BB5-DBF9A1C3D1C3}",
      "destruktiv": false
    },
    {
      "kategorie": "deep",
      "befehl": "shell:::{ED7BA470-8E54-465E-825C-99712043E01C}",
      "start": "shell:::{ED7BA470-8E54-465E-825C-99712043E01C}",
      "kurz": "GodMode",
      "lang": "Oeffnet den Shell-Namespace 'GodMode' ueber die CLSID. Aufruf: explorer.exe shell:::{ED7BA470-8E54-465E-825C-99712043E01C}",
      "destruktiv": false
    },
    {
      "kategorie": "deep",
      "befehl": "shell:::{F02C1A0D-BE21-4350-88B0-7367FC96EF3C}",
      "start": "shell:::{F02C1A0D-BE21-4350-88B0-7367FC96EF3C}",
      "kurz": "Netzwerk",
      "lang": "Oeffnet den Shell-Namespace 'Netzwerk' ueber die CLSID. Aufruf: explorer.exe shell:::{F02C1A0D-BE21-4350-88B0-7367FC96EF3C}",
      "destruktiv": false
    },
    {
      "kategorie": "deep",
      "befehl": "shell:::{645FF040-5081-101B-9F08-00AA002F954E}",
      "start": "shell:::{645FF040-5081-101B-9F08-00AA002F954E}",
      "kurz": "Papierkorb",
      "lang": "Oeffnet den Shell-Namespace 'Papierkorb' ueber die CLSID. Aufruf: explorer.exe shell:::{645FF040-5081-101B-9F08-00AA002F954E}",
      "destruktiv": false
    },
    {
      "kategorie": "deep",
      "befehl": "shell:::{20D04FE0-3AEA-1069-A2D8-08002B30309D}",
      "start": "shell:::{20D04FE0-3AEA-1069-A2D8-08002B30309D}",
      "kurz": "Dieser PC",
      "lang": "Oeffnet den Shell-Namespace 'Dieser PC' ueber die CLSID. Aufruf: explorer.exe shell:::{20D04FE0-3AEA-1069-A2D8-08002B30309D}",
      "destruktiv": false
    },
    {
      "kategorie": "deep",
      "befehl": "shell:::{1F4DE370-D627-11D1-BA4F-00A0C91EEDBA}",
      "start": "shell:::{1F4DE370-D627-11D1-BA4F-00A0C91EEDBA}",
      "kurz": "Systemsteuerung",
      "lang": "Oeffnet den Shell-Namespace 'Systemsteuerung' ueber die CLSID. Aufruf: explorer.exe shell:::{1F4DE370-D627-11D1-BA4F-00A0C91EEDBA}",
      "destruktiv": false
    },
    {
      "kategorie": "deep",
      "befehl": "shell:::{E9950154-C418-419e-A90A-20C5287AE24B}",
      "start": "shell:::{E9950154-C418-419e-A90A-20C5287AE24B}",
      "kurz": "Sicherheit",
      "lang": "Oeffnet den Shell-Namespace 'Sicherheit' ueber die CLSID. Aufruf: explorer.exe shell:::{E9950154-C418-419e-A90A-20C5287AE24B}",
      "destruktiv": false
    },
    {
      "kategorie": "deep",
      "befehl": "shell:::{A3C414DC-1D3A-4B3B-9C1E-5A1E2F1F1F1F}",
      "start": "shell:::{A3C414DC-1D3A-4B3B-9C1E-5A1E2F1F1F1F}",
      "kurz": "Geräte",
      "lang": "Oeffnet den Shell-Namespace 'Geräte' ueber die CLSID. Aufruf: explorer.exe shell:::{A3C414DC-1D3A-4B3B-9C1E-5A1E2F1F1F1F}",
      "destruktiv": false
    },
    {
      "kategorie": "deep",
      "befehl": "shell:::{D4480E6F-9D0C-4f1b-8C9C-0E7E5F2A1A1A}",
      "start": "shell:::{D4480E6F-9D0C-4f1b-8C9C-0E7E5F2A1A1A}",
      "kurz": "Speicher",
      "lang": "Oeffnet den Shell-Namespace 'Speicher' ueber die CLSID. Aufruf: explorer.exe shell:::{D4480E6F-9D0C-4f1b-8C9C-0E7E5F2A1A1A}",
      "destruktiv": false
    },
    {
      "kategorie": "deep",
      "befehl": "shell:::{F1D6F7C4-3F3A-4f1e-8C9C-0E7E5F2A1A1A}",
      "start": "shell:::{F1D6F7C4-3F3A-4f1e-8C9C-0E7E5F2A1A1A}",
      "kurz": "Energie",
      "lang": "Oeffnet den Shell-Namespace 'Energie' ueber die CLSID. Aufruf: explorer.exe shell:::{F1D6F7C4-3F3A-4f1e-8C9C-0E7E5F2A1A1A}",
      "destruktiv": false
    },
    {
      "kategorie": "deep",
      "befehl": "shell:::{D9EF8727-CAC2-4e6f-8C9C-0E7E5F2A1A1A}",
      "start": "shell:::{D9EF8727-CAC2-4e6f-8C9C-0E7E5F2A1A1A}",
      "kurz": "Netzwerkprofile",
      "lang": "Oeffnet den Shell-Namespace 'Netzwerkprofile' ueber die CLSID. Aufruf: explorer.exe shell:::{D9EF8727-CAC2-4e6f-8C9C-0E7E5F2A1A1A}",
      "destruktiv": false
    },
    {
      "kategorie": "deep",
      "befehl": "shell:::{A8A91A66-3A7D-4424-8D27-5E3C3B0C1C1C}",
      "start": "shell:::{A8A91A66-3A7D-4424-8D27-5E3C3B0C1C1C}",
      "kurz": "Geräteinstallation",
      "lang": "Oeffnet den Shell-Namespace 'Geräteinstallation' ueber die CLSID. Aufruf: explorer.exe shell:::{A8A91A66-3A7D-4424-8D27-5E3C3B0C1C1C}",
      "destruktiv": false
    },
    {
      "kategorie": "deep",
      "befehl": "shell:::{B4FB3F98-C1EA-428d-A78A-D1F5659CBA93}",
      "start": "shell:::{B4FB3F98-C1EA-428d-A78A-D1F5659CBA93}",
      "kurz": "Heimnetzgruppe",
      "lang": "Oeffnet den Shell-Namespace 'Heimnetzgruppe' ueber die CLSID. Aufruf: explorer.exe shell:::{B4FB3F98-C1EA-428d-A78A-D1F5659CBA93}",
      "destruktiv": false
    },
    {
      "kategorie": "deep",
      "befehl": "shell:::{7A9D1F5B-4E5F-4f1e-8C9C-0E7E5F2A1A1A}",
      "start": "shell:::{7A9D1F5B-4E5F-4f1e-8C9C-0E7E5F2A1A1A}",
      "kurz": "Speicherdiagnose",
      "lang": "Oeffnet den Shell-Namespace 'Speicherdiagnose' ueber die CLSID. Aufruf: explorer.exe shell:::{7A9D1F5B-4E5F-4f1e-8C9C-0E7E5F2A1A1A}",
      "destruktiv": false
    },
    {
      "kategorie": "deep",
      "befehl": "msinfo32",
      "start": "msinfo32",
      "kurz": "Systeminformationen",
      "lang": "Startet 'Systeminformationen' als Windows-Befehl. Aufruf: msinfo32",
      "destruktiv": false
    },
    {
      "kategorie": "deep",
      "befehl": "dxdiag",
      "start": "dxdiag",
      "kurz": "DirectX Diagnose",
      "lang": "Startet 'DirectX Diagnose' als Windows-Befehl. Aufruf: dxdiag",
      "destruktiv": false
    },
    {
      "kategorie": "deep",
      "befehl": "winsat formal",
      "start": "winsat formal",
      "kurz": "Windows Leistungsindex",
      "lang": "Startet 'Windows Leistungsindex' als Windows-Befehl. Aufruf: winsat formal",
      "destruktiv": false
    },
    {
      "kategorie": "deep",
      "befehl": "cleanmgr",
      "start": "cleanmgr",
      "kurz": "Datenträgerbereinigung",
      "lang": "Startet 'Datenträgerbereinigung' als Windows-Befehl. Aufruf: cleanmgr",
      "destruktiv": false
    },
    {
      "kategorie": "deep",
      "befehl": "systempropertiesadvanced",
      "start": "systempropertiesadvanced",
      "kurz": "Erweiterte Systemeigenschaften",
      "lang": "Startet 'Erweiterte Systemeigenschaften' als Windows-Befehl. Aufruf: systempropertiesadvanced",
      "destruktiv": false
    },
    {
      "kategorie": "deep",
      "befehl": "systempropertiescomputername",
      "start": "systempropertiescomputername",
      "kurz": "Computername",
      "lang": "Startet 'Computername' als Windows-Befehl. Aufruf: systempropertiescomputername",
      "destruktiv": false
    },
    {
      "kategorie": "deep",
      "befehl": "systempropertieshardware",
      "start": "systempropertieshardware",
      "kurz": "Hardware",
      "lang": "Startet 'Hardware' als Windows-Befehl. Aufruf: systempropertieshardware",
      "destruktiv": false
    },
    {
      "kategorie": "deep",
      "befehl": "systempropertiesremote",
      "start": "systempropertiesremote",
      "kurz": "Remote",
      "lang": "Startet 'Remote' als Windows-Befehl. Aufruf: systempropertiesremote",
      "destruktiv": false
    },
    {
      "kategorie": "deep",
      "befehl": "systempropertiesprotection",
      "start": "systempropertiesprotection",
      "kurz": "Systemschutz",
      "lang": "Startet 'Systemschutz' als Windows-Befehl. Aufruf: systempropertiesprotection",
      "destruktiv": false
    },
    {
      "kategorie": "deep",
      "befehl": "systempropertiesperformance",
      "start": "systempropertiesperformance",
      "kurz": "Leistung",
      "lang": "Startet 'Leistung' als Windows-Befehl. Aufruf: systempropertiesperformance",
      "destruktiv": false
    },
    {
      "kategorie": "versteckt",
      "befehl": "systemreset",
      "start": "systemreset",
      "kurz": "Windows zurücksetzen",
      "lang": "Achtung: Dieser Befehl kann das System aendern oder Daten loeschen (Windows zurücksetzen). Aufruf nur nach Bestaetigung: systemreset",
      "destruktiv": true
    },
    {
      "kategorie": "versteckt",
      "befehl": "systemreset -cleanpc",
      "start": "systemreset -cleanpc",
      "kurz": "Neuinstallation",
      "lang": "Achtung: Dieser Befehl kann das System aendern oder Daten loeschen (Neuinstallation). Aufruf nur nach Bestaetigung: systemreset -cleanpc",
      "destruktiv": true
    },
    {
      "kategorie": "versteckt",
      "befehl": "reagentc /info",
      "start": "reagentc /info",
      "kurz": "Wiederherstellungsstatus",
      "lang": "Startet 'Wiederherstellungsstatus' als Windows-Befehl. Aufruf: reagentc /info",
      "destruktiv": false
    },
    {
      "kategorie": "versteckt",
      "befehl": "reagentc /enable",
      "start": "reagentc /enable",
      "kurz": "Wiederherstellung aktivieren",
      "lang": "Startet 'Wiederherstellung aktivieren' als Windows-Befehl. Aufruf: reagentc /enable",
      "destruktiv": false
    },
    {
      "kategorie": "versteckt",
      "befehl": "reagentc /disable",
      "start": "reagentc /disable",
      "kurz": "Wiederherstellung deaktivieren",
      "lang": "Achtung: Dieser Befehl kann das System aendern oder Daten loeschen (Wiederherstellung deaktivieren). Aufruf nur nach Bestaetigung: reagentc /disable",
      "destruktiv": true
    },
    {
      "kategorie": "versteckt",
      "befehl": "shutdown /r /o",
      "start": "shutdown /r /o",
      "kurz": "Erweiterte Startoptionen",
      "lang": "Achtung: Dieser Befehl kann das System aendern oder Daten loeschen (Erweiterte Startoptionen). Aufruf nur nach Bestaetigung: shutdown /r /o",
      "destruktiv": true
    },
    {
      "kategorie": "versteckt",
      "befehl": "bcdedit",
      "start": "bcdedit",
      "kurz": "Boot-Konfiguration",
      "lang": "Achtung: Dieser Befehl kann das System aendern oder Daten loeschen (Boot-Konfiguration). Aufruf nur nach Bestaetigung: bcdedit",
      "destruktiv": true
    },
    {
      "kategorie": "versteckt",
      "befehl": "bootsect",
      "start": "bootsect",
      "kurz": "Bootsektor",
      "lang": "Achtung: Dieser Befehl kann das System aendern oder Daten loeschen (Bootsektor). Aufruf nur nach Bestaetigung: bootsect",
      "destruktiv": true
    },
    {
      "kategorie": "versteckt",
      "befehl": "bcdboot",
      "start": "bcdboot",
      "kurz": "Bootdateien",
      "lang": "Achtung: Dieser Befehl kann das System aendern oder Daten loeschen (Bootdateien). Aufruf nur nach Bestaetigung: bcdboot",
      "destruktiv": true
    },
    {
      "kategorie": "versteckt",
      "befehl": "sfc /scannow",
      "start": "sfc /scannow",
      "kurz": "Systemdateiprüfung",
      "lang": "Startet 'Systemdateiprüfung' als Windows-Befehl. Aufruf: sfc /scannow",
      "destruktiv": false
    },
    {
      "kategorie": "versteckt",
      "befehl": "dism /online /cleanup-image /restorehealth",
      "start": "dism /online /cleanup-image /restorehealth",
      "kurz": "Systemreparatur",
      "lang": "Startet 'Systemreparatur' als Windows-Befehl. Aufruf: dism /online /cleanup-image /restorehealth",
      "destruktiv": false
    },
    {
      "kategorie": "versteckt",
      "befehl": "dism /online /cleanup-image /scanhealth",
      "start": "dism /online /cleanup-image /scanhealth",
      "kurz": "Scan",
      "lang": "Startet 'Scan' als Windows-Befehl. Aufruf: dism /online /cleanup-image /scanhealth",
      "destruktiv": false
    },
    {
      "kategorie": "versteckt",
      "befehl": "dism /online /cleanup-image /checkhealth",
      "start": "dism /online /cleanup-image /checkhealth",
      "kurz": "Check",
      "lang": "Startet 'Check' als Windows-Befehl. Aufruf: dism /online /cleanup-image /checkhealth",
      "destruktiv": false
    },
    {
      "kategorie": "versteckt",
      "befehl": "dism /online /cleanup-image /startcomponentcleanup",
      "start": "dism /online /cleanup-image /startcomponentcleanup",
      "kurz": "Komponentenbereinigung",
      "lang": "Startet 'Komponentenbereinigung' als Windows-Befehl. Aufruf: dism /online /cleanup-image /startcomponentcleanup",
      "destruktiv": false
    },
    {
      "kategorie": "versteckt",
      "befehl": "dism /online /enable-feature",
      "start": "dism /online /enable-feature",
      "kurz": "Feature aktivieren",
      "lang": "Startet 'Feature aktivieren' als Windows-Befehl. Aufruf: dism /online /enable-feature",
      "destruktiv": false
    },
    {
      "kategorie": "versteckt",
      "befehl": "dism /online /disable-feature",
      "start": "dism /online /disable-feature",
      "kurz": "Feature deaktivieren",
      "lang": "Achtung: Dieser Befehl kann das System aendern oder Daten loeschen (Feature deaktivieren). Aufruf nur nach Bestaetigung: dism /online /disable-feature",
      "destruktiv": true
    },
    {
      "kategorie": "versteckt",
      "befehl": "dism /online /get-features",
      "start": "dism /online /get-features",
      "kurz": "Featureliste",
      "lang": "Startet 'Featureliste' als Windows-Befehl. Aufruf: dism /online /get-features",
      "destruktiv": false
    },
    {
      "kategorie": "versteckt",
      "befehl": "dism /online /get-packages",
      "start": "dism /online /get-packages",
      "kurz": "Paketliste",
      "lang": "Startet 'Paketliste' als Windows-Befehl. Aufruf: dism /online /get-packages",
      "destruktiv": false
    },
    {
      "kategorie": "versteckt",
      "befehl": "dism /online /remove-package",
      "start": "dism /online /remove-package",
      "kurz": "Paket entfernen",
      "lang": "Achtung: Dieser Befehl kann das System aendern oder Daten loeschen (Paket entfernen). Aufruf nur nach Bestaetigung: dism /online /remove-package",
      "destruktiv": true
    },
    {
      "kategorie": "versteckt",
      "befehl": "dism /online /add-package",
      "start": "dism /online /add-package",
      "kurz": "Paket hinzufügen",
      "lang": "Startet 'Paket hinzufügen' als Windows-Befehl. Aufruf: dism /online /add-package",
      "destruktiv": false
    },
    {
      "kategorie": "versteckt",
      "befehl": "dism /online /get-drivers",
      "start": "dism /online /get-drivers",
      "kurz": "Treiberliste",
      "lang": "Startet 'Treiberliste' als Windows-Befehl. Aufruf: dism /online /get-drivers",
      "destruktiv": false
    },
    {
      "kategorie": "versteckt",
      "befehl": "dism /online /get-intl",
      "start": "dism /online /get-intl",
      "kurz": "Sprachinfo",
      "lang": "Startet 'Sprachinfo' als Windows-Befehl. Aufruf: dism /online /get-intl",
      "destruktiv": false
    },
    {
      "kategorie": "versteckt",
      "befehl": "dism /online /set-intl",
      "start": "dism /online /set-intl",
      "kurz": "Sprache setzen",
      "lang": "Startet 'Sprache setzen' als Windows-Befehl. Aufruf: dism /online /set-intl",
      "destruktiv": false
    },
    {
      "kategorie": "versteckt",
      "befehl": "dism /online /cleanup-image",
      "start": "dism /online /cleanup-image",
      "kurz": "Cleanup",
      "lang": "Startet 'Cleanup' als Windows-Befehl. Aufruf: dism /online /cleanup-image",
      "destruktiv": false
    },
    {
      "kategorie": "versteckt",
      "befehl": "control admintools",
      "start": "control admintools",
      "kurz": "Verwaltung",
      "lang": "Startet ein Systemsteuerungsfenster (Verwaltung). Aufruf: control admintools",
      "destruktiv": false
    },
    {
      "kategorie": "versteckt",
      "befehl": "control color",
      "start": "control color",
      "kurz": "Farbverwaltung",
      "lang": "Startet ein Systemsteuerungsfenster (Farbverwaltung). Aufruf: control color",
      "destruktiv": false
    },
    {
      "kategorie": "versteckt",
      "befehl": "control folders",
      "start": "control folders",
      "kurz": "Ordneroptionen",
      "lang": "Startet ein Systemsteuerungsfenster (Ordneroptionen). Aufruf: control folders",
      "destruktiv": false
    },
    {
      "kategorie": "versteckt",
      "befehl": "control gamecontrollers",
      "start": "control gamecontrollers",
      "kurz": "Gamecontroller",
      "lang": "Startet ein Systemsteuerungsfenster (Gamecontroller). Aufruf: control gamecontrollers",
      "destruktiv": false
    },
    {
      "kategorie": "versteckt",
      "befehl": "control irprops.cpl",
      "start": "control irprops.cpl",
      "kurz": "Infrarot",
      "lang": "Startet ein Systemsteuerungsfenster (Infrarot). Aufruf: control irprops.cpl",
      "destruktiv": false
    },
    {
      "kategorie": "versteckt",
      "befehl": "control telephon.cpl",
      "start": "control telephon.cpl",
      "kurz": "Telefonie",
      "lang": "Startet ein Systemsteuerungsfenster (Telefonie). Aufruf: control telephon.cpl",
      "destruktiv": false
    },
    {
      "kategorie": "versteckt",
      "befehl": "control tabletpc.cpl",
      "start": "control tabletpc.cpl",
      "kurz": "Tablet PC",
      "lang": "Startet ein Systemsteuerungsfenster (Tablet PC). Aufruf: control tabletpc.cpl",
      "destruktiv": false
    },
    {
      "kategorie": "versteckt",
      "befehl": "control access.cpl",
      "start": "control access.cpl",
      "kurz": "Eingabehilfen",
      "lang": "Startet ein Systemsteuerungsfenster (Eingabehilfen). Aufruf: control access.cpl",
      "destruktiv": false
    },
    {
      "kategorie": "versteckt",
      "befehl": "control nusrmgr.cpl",
      "start": "control nusrmgr.cpl",
      "kurz": "Benutzerkonten (alt)",
      "lang": "Startet ein Systemsteuerungsfenster (Benutzerkonten (alt)). Aufruf: control nusrmgr.cpl",
      "destruktiv": false
    },
    {
      "kategorie": "versteckt",
      "befehl": "control odbccp32.cpl",
      "start": "control odbccp32.cpl",
      "kurz": "ODBC",
      "lang": "Startet ein Systemsteuerungsfenster (ODBC). Aufruf: control odbccp32.cpl",
      "destruktiv": false
    },
    {
      "kategorie": "versteckt",
      "befehl": "control srchadmin.dll",
      "start": "control srchadmin.dll",
      "kurz": "Suche",
      "lang": "Startet ein Systemsteuerungsfenster (Suche). Aufruf: control srchadmin.dll",
      "destruktiv": false
    },
    {
      "kategorie": "versteckt",
      "befehl": "control storprop.dll",
      "start": "control storprop.dll",
      "kurz": "Speicher",
      "lang": "Startet ein Systemsteuerungsfenster (Speicher). Aufruf: control storprop.dll",
      "destruktiv": false
    },
    {
      "kategorie": "versteckt",
      "befehl": "control themecpl.dll",
      "start": "control themecpl.dll",
      "kurz": "Themes",
      "lang": "Startet ein Systemsteuerungsfenster (Themes). Aufruf: control themecpl.dll",
      "destruktiv": false
    },
    {
      "kategorie": "veraltet",
      "befehl": "ms-settings:homegroup",
      "start": "ms-settings:homegroup",
      "kurz": "Heimnetzgruppe (entfernt)",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Heimnetzgruppe (entfernt)'. URI: ms-settings:homegroup",
      "destruktiv": false
    },
    {
      "kategorie": "veraltet",
      "befehl": "ms-settings:quietmoments",
      "start": "ms-settings:quietmoments",
      "kurz": "Ruhezeiten (entfernt)",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Ruhezeiten (entfernt)'. URI: ms-settings:quietmoments",
      "destruktiv": false
    },
    {
      "kategorie": "veraltet",
      "befehl": "ms-settings:workplace",
      "start": "ms-settings:workplace",
      "kurz": "Arbeitsplatzbeitritt (entfernt)",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Arbeitsplatzbeitritt (entfernt)'. URI: ms-settings:workplace",
      "destruktiv": false
    },
    {
      "kategorie": "veraltet",
      "befehl": "ms-settings:sync",
      "start": "ms-settings:sync",
      "kurz": "Synchronisierung (Legacy)",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Synchronisierung (Legacy)'. URI: ms-settings:sync",
      "destruktiv": false
    },
    {
      "kategorie": "veraltet",
      "befehl": "ms-settings:windowsupdate-action",
      "start": "ms-settings:windowsupdate-action",
      "kurz": "Update-Aktionen (Legacy)",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Update-Aktionen (Legacy)'. URI: ms-settings:windowsupdate-action",
      "destruktiv": false
    },
    {
      "kategorie": "veraltet",
      "befehl": "ms-settings:windowsupdate-restartoptions",
      "start": "ms-settings:windowsupdate-restartoptions",
      "kurz": "Neustartoptionen (Legacy)",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Neustartoptionen (Legacy)'. URI: ms-settings:windowsupdate-restartoptions",
      "destruktiv": false
    },
    {
      "kategorie": "veraltet",
      "befehl": "ms-settings:windowsupdate-history",
      "start": "ms-settings:windowsupdate-history",
      "kurz": "Update-Historie (Legacy)",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Update-Historie (Legacy)'. URI: ms-settings:windowsupdate-history",
      "destruktiv": false
    },
    {
      "kategorie": "veraltet",
      "befehl": "ms-settings:windowsupdate-options",
      "start": "ms-settings:windowsupdate-options",
      "kurz": "Update-Optionen (Legacy)",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Update-Optionen (Legacy)'. URI: ms-settings:windowsupdate-options",
      "destruktiv": false
    },
    {
      "kategorie": "veraltet",
      "befehl": "ms-settings:privacy-feedback",
      "start": "ms-settings:privacy-feedback",
      "kurz": "Feedback (Legacy)",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Feedback (Legacy)'. URI: ms-settings:privacy-feedback",
      "destruktiv": false
    },
    {
      "kategorie": "veraltet",
      "befehl": "ms-settings:privacy-backgroundapps",
      "start": "ms-settings:privacy-backgroundapps",
      "kurz": "Hintergrund-Apps (Legacy)",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Hintergrund-Apps (Legacy)'. URI: ms-settings:privacy-backgroundapps",
      "destruktiv": false
    },
    {
      "kategorie": "veraltet",
      "befehl": "ms-settings:privacy-appdiagnostics",
      "start": "ms-settings:privacy-appdiagnostics",
      "kurz": "App-Diagnose (Legacy)",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'App-Diagnose (Legacy)'. URI: ms-settings:privacy-appdiagnostics",
      "destruktiv": false
    },
    {
      "kategorie": "veraltet",
      "befehl": "ms-settings:privacy-activityhistory",
      "start": "ms-settings:privacy-activityhistory",
      "kurz": "Aktivitätsverlauf (Legacy)",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Aktivitätsverlauf (Legacy)'. URI: ms-settings:privacy-activityhistory",
      "destruktiv": false
    },
    {
      "kategorie": "veraltet",
      "befehl": "ms-settings:gaming-gamedvr",
      "start": "ms-settings:gaming-gamedvr",
      "kurz": "Game DVR (entfernt)",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Game DVR (entfernt)'. URI: ms-settings:gaming-gamedvr",
      "destruktiv": false
    },
    {
      "kategorie": "veraltet",
      "befehl": "ms-settings:gaming-broadcasting",
      "start": "ms-settings:gaming-broadcasting",
      "kurz": "Broadcasting (entfernt)",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Broadcasting (entfernt)'. URI: ms-settings:gaming-broadcasting",
      "destruktiv": false
    },
    {
      "kategorie": "veraltet",
      "befehl": "ms-settings:mobile-devices",
      "start": "ms-settings:mobile-devices",
      "kurz": "Mobile Geräte (Legacy)",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Mobile Geräte (Legacy)'. URI: ms-settings:mobile-devices",
      "destruktiv": false
    },
    {
      "kategorie": "veraltet",
      "befehl": "ms-settings:mobile-devices-addphone",
      "start": "ms-settings:mobile-devices-addphone",
      "kurz": "Telefon hinzufügen (Legacy)",
      "lang": "Oeffnet die Windows-Einstellungen auf der Seite 'Telefon hinzufügen (Legacy)'. URI: ms-settings:mobile-devices-addphone",
      "destruktiv": false
    },
    {
      "kategorie": "veraltet",
      "befehl": "control homegroup",
      "start": "control homegroup",
      "kurz": "Heimnetzgruppe (entfernt)",
      "lang": "Startet ein Systemsteuerungsfenster (Heimnetzgruppe (entfernt)). Aufruf: control homegroup",
      "destruktiv": false
    },
    {
      "kategorie": "veraltet",
      "befehl": "control wscui.cpl",
      "start": "control wscui.cpl",
      "kurz": "Sicherheitscenter (Legacy)",
      "lang": "Startet ein Systemsteuerungsfenster (Sicherheitscenter (Legacy)). Aufruf: control wscui.cpl",
      "destruktiv": false
    },
    {
      "kategorie": "veraltet",
      "befehl": "control nusrmgr.cpl",
      "start": "control nusrmgr.cpl",
      "kurz": "Benutzerkonten (XP/7)",
      "lang": "Startet ein Systemsteuerungsfenster (Benutzerkonten (XP/7)). Aufruf: control nusrmgr.cpl",
      "destruktiv": false
    },
    {
      "kategorie": "veraltet",
      "befehl": "control telephon.cpl",
      "start": "control telephon.cpl",
      "kurz": "Telefonie (Legacy)",
      "lang": "Startet ein Systemsteuerungsfenster (Telefonie (Legacy)). Aufruf: control telephon.cpl",
      "destruktiv": false
    },
    {
      "kategorie": "veraltet",
      "befehl": "control tabletpc.cpl",
      "start": "control tabletpc.cpl",
      "kurz": "Tablet PC Einstellungen (Legacy)",
      "lang": "Startet ein Systemsteuerungsfenster (Tablet PC Einstellungen (Legacy)). Aufruf: control tabletpc.cpl",
      "destruktiv": false
    },
    {
      "kategorie": "veraltet",
      "befehl": "control irprops.cpl",
      "start": "control irprops.cpl",
      "kurz": "Infrarot (Legacy)",
      "lang": "Startet ein Systemsteuerungsfenster (Infrarot (Legacy)). Aufruf: control irprops.cpl",
      "destruktiv": false
    },
    {
      "kategorie": "veraltet",
      "befehl": "control gamecontrollers",
      "start": "control gamecontrollers",
      "kurz": "Gamecontroller (Legacy)",
      "lang": "Startet ein Systemsteuerungsfenster (Gamecontroller (Legacy)). Aufruf: control gamecontrollers",
      "destruktiv": false
    },
    {
      "kategorie": "veraltet",
      "befehl": "control srchadmin.dll",
      "start": "control srchadmin.dll",
      "kurz": "Sucheinstellungen (Legacy)",
      "lang": "Startet ein Systemsteuerungsfenster (Sucheinstellungen (Legacy)). Aufruf: control srchadmin.dll",
      "destruktiv": false
    },
    {
      "kategorie": "veraltet",
      "befehl": "control storprop.dll",
      "start": "control storprop.dll",
      "kurz": "Speicherverwaltung (Legacy)",
      "lang": "Startet ein Systemsteuerungsfenster (Speicherverwaltung (Legacy)). Aufruf: control storprop.dll",
      "destruktiv": false
    },
    {
      "kategorie": "veraltet",
      "befehl": "control themecpl.dll",
      "start": "control themecpl.dll",
      "kurz": "Themes (Legacy)",
      "lang": "Startet ein Systemsteuerungsfenster (Themes (Legacy)). Aufruf: control themecpl.dll",
      "destruktiv": false
    },
    {
      "kategorie": "veraltet",
      "befehl": "explorer.exe shell:HomeGroup",
      "start": "explorer.exe shell:HomeGroup",
      "kurz": "Heimnetzgruppe (entfernt)",
      "lang": "Startet den Explorer mit einem bekannten Ordner oder einer URI (Heimnetzgruppe (entfernt)). Aufruf: explorer.exe shell:HomeGroup",
      "destruktiv": false
    },
    {
      "kategorie": "veraltet",
      "befehl": "explorer.exe shell:Libraries",
      "start": "explorer.exe shell:Libraries",
      "kurz": "Bibliotheken (Legacy)",
      "lang": "Startet den Explorer mit einem bekannten Ordner oder einer URI (Bibliotheken (Legacy)). Aufruf: explorer.exe shell:Libraries",
      "destruktiv": false
    },
    {
      "kategorie": "veraltet",
      "befehl": "explorer.exe shell:AppsFolder",
      "start": "explorer.exe shell:AppsFolder",
      "kurz": "Apps (Legacy Verhalten)",
      "lang": "Startet den Explorer mit einem bekannten Ordner oder einer URI (Apps (Legacy Verhalten)). Aufruf: explorer.exe shell:AppsFolder",
      "destruktiv": false
    },
    {
      "kategorie": "veraltet",
      "befehl": "rundll32.exe shell32.dll,SHHelpShortcuts_RunDLL",
      "start": "rundll32.exe shell32.dll,SHHelpShortcuts_RunDLL",
      "kurz": "Hilfe (Legacy)",
      "lang": "Ruft eine System-DLL auf und oeffnet 'Hilfe (Legacy)'. Aufruf: rundll32.exe shell32.dll,SHHelpShortcuts_RunDLL",
      "destruktiv": false
    },
    {
      "kategorie": "veraltet",
      "befehl": "rundll32.exe shell32.dll,Control_RunDLL hotplug.dll",
      "start": "rundll32.exe shell32.dll,Control_RunDLL hotplug.dll",
      "kurz": "Hardware sicher entfernen (Legacy)",
      "lang": "Ruft eine System-DLL auf und oeffnet 'Hardware sicher entfernen (Legacy)'. Aufruf: rundll32.exe shell32.dll,Control_RunDLL hotplug.dll",
      "destruktiv": false
    },
    {
      "kategorie": "veraltet",
      "befehl": "rundll32.exe shell32.dll,Control_RunDLL access.cpl",
      "start": "rundll32.exe shell32.dll,Control_RunDLL access.cpl",
      "kurz": "Eingabehilfen (Legacy)",
      "lang": "Ruft eine System-DLL auf und oeffnet 'Eingabehilfen (Legacy)'. Aufruf: rundll32.exe shell32.dll,Control_RunDLL access.cpl",
      "destruktiv": false
    },
    {
      "kategorie": "veraltet",
      "befehl": "rundll32.exe shell32.dll,Control_RunDLL joy.cpl",
      "start": "rundll32.exe shell32.dll,Control_RunDLL joy.cpl",
      "kurz": "Joystick (Legacy)",
      "lang": "Ruft eine System-DLL auf und oeffnet 'Joystick (Legacy)'. Aufruf: rundll32.exe shell32.dll,Control_RunDLL joy.cpl",
      "destruktiv": false
    }
  ]
}
""")
