"""
WinSysCommands – Zeigt Windows-Systembefehle und 20 Befehlskategorien in Tabellen mit Kurz- und Langbeschreibung und startet den gewaehlten Eintrag.

Projekt:     WinSysCommands
Modul:       wsc_launch.py
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
Version 1.0.0 – 2026-09-12 – MMC per ShellExecute, shell:Temp auf %TEMP%.

Aufruf / Nutzung
----------------
Wird importiert, nicht als Programm gestartet.
"""

from __future__ import annotations

import os
import shlex
import shutil
import subprocess
import sys
from collections.abc import Callable

from wsc_katalog import Eintrag

CREATE_NEW_CONSOLE = 0x00000010

KONSOLE_KOEPFE = frozenset(
    {
        "bcdboot",
        "bcdedit",
        "bootsect",
        "chkdsk",
        "defrag",
        "diskpart",
        "diskperf",
        "dism",
        "format",
        "fsutil",
        "ipconfig",
        "logoff",
        "mountvol",
        "net",
        "netsh",
        "netstat",
        "pathping",
        "ping",
        "powercfg",
        "psinfo",
        "pskill",
        "pslist",
        "psloggedon",
        "psexec",
        "psservice",
        "query",
        "qwinsta",
        "reagentc",
        "reg",
        "rwinsta",
        "scp",
        "sfc",
        "sftp",
        "shutdown",
        "ssh",
        "systemreset",
        "tracert",
        "tscon",
        "tsdiscon",
        "vssadmin",
        "wbadmin",
        "winrm",
        "winrs",
        "winsat",
        "wmic",
    }
)


def erstes_wort(start: str) -> str:
    """Liefert das erste Token ohne Dateiendung, kleingeschrieben."""
    teile = shlex.split(start.strip(), posix=False)
    if not teile:
        return ""
    name = os.path.basename(teile[0]).casefold()
    if name.endswith(".exe") or name.endswith(".cmd") or name.endswith(".bat"):
        name = name.rsplit(".", 1)[0]
    return name


def ist_konsole(start: str) -> bool:
    """True, wenn der Befehl in einer neuen Konsole laufen soll."""
    low = start.strip().casefold()
    if low.startswith("powershell:"):
        return True
    return erstes_wort(start) in KONSOLE_KOEPFE


def _temp_ordner() -> str:
    """Liefert den Windows-Temp-Ordner aus der Umgebung.

    Rueckgabe
    ---------
    Pfad aus TEMP oder TMP, sonst leer.

    Fehlerfaelle
    ------------
    Keine.

    Beispiel
    --------
    >>> isinstance(_temp_ordner(), str)
    True
    """
    return os.environ.get("TEMP") or os.environ.get("TMP") or ""


def _mmc_datei(text: str) -> str | None:
    """Extrahiert die .msc-Datei aus einer Startzeile, sonst None.

    Parameter
    ---------
    text:
        Katalog-Startzeile.

    Rueckgabe
    ---------
    Snap-In-Dateiname oder None.

    Fehlerfaelle
    ------------
    Keine.

    Beispiel
    --------
    >>> _mmc_datei("mmc services.msc")
    'services.msc'
    """
    teile = shlex.split(text.strip(), posix=False)
    if not teile:
        return None
    erstes = teile[0]
    if erstes.casefold().endswith(".msc"):
        return erstes
    if erstes.casefold() in {"mmc", "mmc.exe"} and len(teile) >= 2:
        return teile[1]
    return None


def baue_argv(start: str) -> list[str]:
    """Baut die Argumentliste ohne den Prozess zu starten.

    Parameter
    ---------
    start:
        Startzeile aus dem Katalog.

    Rueckgabe
    ---------
    Argumentliste fuer subprocess oder os.startfile-Markierung als eine URI.

    Fehlerfaelle
    ------------
    ValueError, wenn die Startzeile leer ist.

    Beispiel
    --------
    >>> baue_argv("shell:Desktop")[0]
    'explorer.exe'
    """
    text = start.strip()
    if not text:
        raise ValueError("leere Startzeile")
    low = text.casefold()
    if low.startswith("powershell:"):
        cmd = text.split(":", 1)[1].strip()
        return ["powershell.exe", "-NoExit", "-Command", cmd]
    if low.startswith("ms-settings:"):
        return ["startfile", text]
    if low.startswith("shell:"):
        return _argv_shell(text)
    msc = _mmc_datei(text)
    if msc:
        return ["startfile", msc]
    if low.endswith(".cpl"):
        return ["startfile", text]
    if ist_konsole(text):
        return ["cmd.exe", "/k", text]
    return shlex.split(text, posix=False)


def _argv_shell(text: str) -> list[str]:
    """Mappt shell:-Namen; Temp ist kein Known-Folder und braucht %TEMP%.

    Parameter
    ---------
    text:
        Zeile beginnend mit shell:

    Rueckgabe
    ---------
    explorer- oder startfile-Argumente.

    Fehlerfaelle
    ------------
    ValueError, wenn Temp ohne Umgebungsvariable bleibt.

    Beispiel
    --------
    >>> baue_argv("shell:Desktop")
    ['explorer.exe', 'shell:Desktop']
    """
    low = text.strip().casefold()
    if low in {"shell:temp", "shell:tmp"}:
        temp = _temp_ordner()
        if not temp:
            raise ValueError("TEMP-Ordner ist nicht gesetzt")
        return ["startfile", temp]
    return ["explorer.exe", text]


def _startfile(ziel: str) -> None:
    """Oeffnet eine URI, ein Snap-In oder einen Ordner mit der Windows-Shell.

    ShellExecute zeigt bei MMC-Konsolen die UAC-Abfrage; Popen wuerde mit
    Fehler 193 (.msc ist keine EXE) oder 740 (fehlende Rechte) scheitern.

    Parameter
    ---------
    ziel:
        Datei, Ordner oder URI.

    Rueckgabe
    ---------
    None.

    Fehlerfaelle
    ------------
    OSError, wenn weder die Datei noch ein gleichnamiges .exe oeffnet.

    Beispiel
    --------
    >>> _startfile  # doctest: +SKIP
    """
    try:
        os.startfile(ziel)  # noqa: S606 – bewusst Shell-Open fuer MMC und Ordner
        return
    except OSError:
        if ziel.casefold().endswith(".msc"):
            ersatz = ziel[:-4] + ".exe"
            os.startfile(ersatz)  # noqa: S606
            return
        raise


def starte_eintrag(
    eintrag: Eintrag,
    *,
    ja: bool = False,
    nachfragen: Callable[[str], bool] | None = None,
) -> int:
    """Startet einen Katalogeintrag.

    Parameter
    ---------
    eintrag:
        Ausgewaehlter Befehl.
    ja:
        Ueberspringt die Rueckfrage bei destruktiven Befehlen.
    nachfragen:
        Optionaler Dialog; Standard ist Konsole ja/nein.

    Rueckgabe
    ---------
    0 bei Start, 1 bei Fehler oder Abbruch.

    Fehlerfaelle
    ------------
    OSError beim Prozessstart wird als Exit 1 gemeldet.

    Beispiel
    --------
    >>> starte_eintrag  # doctest: +SKIP
    """
    if os.name != "nt":
        sys.stderr.write("FEHLER: Starten ist nur unter Windows vorgesehen. Hinweis: --help\n")
        return 1
    if eintrag.destruktiv and not ja:
        frage = (
            f"Der Befehl kann das System aendern:\n{eintrag.start}\n"
            "Wirklich starten?"
        )
        ok = nachfragen(frage) if nachfragen else _konsole_ja(frage)
        if not ok:
            sys.stderr.write("FEHLER: Start abgebrochen.\n")
            return 1
    try:
        argv = baue_argv(eintrag.start)
    except ValueError as exc:
        sys.stderr.write(f"FEHLER: {exc}. Hinweis: --help\n")
        return 1
    try:
        _ausfuehren(argv)
    except OSError as exc:
        sys.stderr.write(f"FEHLER: Start fehlgeschlagen: {exc}. Pruefen Sie, ob das Werkzeug existiert.\n")
        return 1
    return 0


def _ausfuehren(argv: list[str]) -> None:
    """Startet argv; startfile-URIs gehen an die Windows-Shell."""
    if argv[0] == "startfile":
        _startfile(argv[1])
        return
    flags = 0
    if argv[0].casefold() in {"cmd.exe", "powershell.exe"}:
        flags = CREATE_NEW_CONSOLE
    subprocess.Popen(argv, creationflags=flags, close_fds=False)


def _konsole_ja(frage: str) -> bool:
    """Liest eine Bestaetigung von stdin."""
    sys.stderr.write(frage + " [j/N]: ")
    sys.stderr.flush()
    try:
        antwort = input().strip().casefold()
    except EOFError:
        return False
    return antwort in {"j", "ja", "y", "yes"}


def pruefe_windows_werkzeuge() -> str | None:
    """Prueft explorer.exe vor dem Fachlauf; --help braucht das nicht.

    Rueckgabe
    ---------
    None wenn vorhanden, sonst ein deutscher Fehlertext.
    """
    if os.name != "nt":
        return "Dieses Programm startet Systembefehle nur unter Windows."
    if shutil.which("explorer.exe") is None:
        return (
            "explorer.exe wurde nicht gefunden. Unter Windows gehoert Explorer "
            "zum System; eine Neuinstallation ist nicht per pip moeglich."
        )
    return None
