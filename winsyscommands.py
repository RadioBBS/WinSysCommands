"""
WinSysCommands – Zeigt Windows-Systembefehle und 20 Befehlskategorien in Tabellen mit Kurz- und Langbeschreibung und startet den gewaehlten Eintrag.

Projekt:     WinSysCommands
Modul:       winsyscommands.py
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
Version 1.0.0 – 2026-09-12 – GUI mit 21 Karten, Listen- und Startmodus.
Version 1.0.1 – 2026-11-02 – Startausgabe und Python 3.11 nach Styleguide 2.1.0.

Aufruf / Nutzung
----------------
    python winsyscommands.py
    python winsyscommands.py --kategorie shell:
    python winsyscommands.py --list
    python winsyscommands.py --starten "shell:Desktop"
    python winsyscommands.py --help
    python winsyscommands.py --version
"""

from __future__ import annotations

import os
import platform

import argparse
import sys

import project_meta as meta
from wsc_katalog import eintraege_von, finde_eintrag, finde_kategorie, kategorien
from wsc_launch import pruefe_windows_werkzeuge, starte_eintrag

BEISPIELE = [
    "python winsyscommands.py",
    "python winsyscommands.py --kategorie shell:",
    "python winsyscommands.py --list",
    'python winsyscommands.py --starten "shell:Desktop"',
    "python winsyscommands.py --help",
    "python winsyscommands.py --version",
]


class WscParser(argparse.ArgumentParser):
    """ArgumentParser mit FEHLER:-Prefix und Exit 2."""

    def error(self, message: str) -> None:
        sys.stderr.write(f"FEHLER: {message}  Hinweis: --help\n")
        self.exit(2)


def build_parser() -> WscParser:
    """Baut den Parser ohne Fachlauf.

    Rueckgabe
    ---------
    Parser mit deutschen Hilfetexten.

    Fehlerfaelle
    ------------
    Keine.

    Beispiel
    --------
    >>> "--help" in build_parser().format_help()
    True
    """
    parser = WscParser(
        prog=meta.SKRIPT,
        add_help=False,
        description=meta.BESCHREIBUNG,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Beispiele:\n  " + "\n  ".join(BEISPIELE),
    )
    parser.add_argument("-h", "--help", action="store_true", help="Hilfe ausgeben und beenden (Exit 0).")
    parser.add_argument("--version", action="store_true", help="Version, Datum und Zweck ausgeben.")
    parser.add_argument("-E", "--Ende", action="store_true", dest="ende", help="Am Ende auf Taste warten.")
    parser.add_argument(
        "--kategorie",
        default="",
        metavar="NAME",
        help="Registerkarte (ID oder Tabname). Standard: Systembefehle. Beispiel: --kategorie shell:",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="Katalog als Text ausgeben, keine GUI. Beispiel: --list --kategorie MMC",
    )
    parser.add_argument(
        "--starten",
        default="",
        metavar="BEFEHL",
        help="Einen Katalogbefehl ohne GUI starten. Beispiel: --starten shell:Desktop",
    )
    parser.add_argument(
        "--yes",
        action="store_true",
        help="Destruktive Starts ohne Rueckfrage. Beispiel: --yes --starten shutdown",
    )
    return parser


def print_help(parser: WscParser) -> None:
    """Gibt Zweck, Version, Parameter und Beispiele aus."""
    print(meta.BESCHREIBUNG)
    print(f"Version: {meta.VERSION}  Stand: {meta.STAND}")
    print()
    print(parser.format_help())
    print("Parameter:")
    print()
    print("| Name        | Typ  | Standard      | Beschreibung                      | Beispiel                 |")
    print("| ----------- | ---- | ------------- | --------------------------------- | ------------------------ |")
    print("| --kategorie | str  | Systembefehle | Registerkarte oeffnen oder listen | --kategorie shell:       |")
    print("| --list      | flag | aus           | Textkatalog ohne GUI              | --list                   |")
    print("| --starten   | str  | leer          | Befehl aus dem Katalog starten    | --starten shell:Desktop  |")
    print("| --yes       | flag | aus           | Keine Rueckfrage bei Risiko       | --yes --starten shutdown |")
    print("| --Ende / -E | flag | aus           | Wartet am Ende auf Taste          | --Ende                   |")
    print("| --help / -h | flag | aus           | Hilfe, kein Fachlauf              | --help                   |")
    print("| --version   | flag | aus           | Version und Zweck                 | --version                |")


def print_version() -> None:
    """Gibt Nummer, Datum und Ein-Satz-Zweck aus."""
    print(f"{meta.PROJEKT} {meta.VERSION} ({meta.STAND})")
    print(meta.BESCHREIBUNG)


def liste_ausgeben(kat_name: str) -> int:
    """Schreibt Befehlstabellen auf stdout."""
    if kat_name.strip():
        kat = finde_kategorie(kat_name)
        if kat is None:
            sys.stderr.write(f"FEHLER: Unbekannte Kategorie {kat_name!r}. Hinweis: --help\n")
            return 2
        karten = [kat]
    else:
        karten = kategorien()
    for kat in karten:
        print(f"# {kat.titel}")
        for eintrag in eintraege_von(kat.id):
            print(f"{eintrag.befehl}\t{eintrag.kurz}")
        print()
    return 0


def starten_cli(befehl: str, kat_name: str, ja: bool) -> int:
    """Startet einen Katalogeintrag ohne GUI."""
    fehl = pruefe_windows_werkzeuge()
    if fehl:
        sys.stderr.write(f"FEHLER: {fehl}\n")
        return 1
    kat_id = ""
    if kat_name.strip():
        kat = finde_kategorie(kat_name)
        if kat is None:
            sys.stderr.write(f"FEHLER: Unbekannte Kategorie {kat_name!r}. Hinweis: --help\n")
            return 2
        kat_id = kat.id
    eintrag = finde_eintrag(befehl, kat_id)
    if eintrag is None:
        sys.stderr.write(f"FEHLER: Befehl {befehl!r} steht nicht im Katalog. Hinweis: --list\n")
        return 2
    return starte_eintrag(eintrag, ja=ja)


def starte_gui(kat_name: str) -> int:
    """Prueft Windows und oeffnet die Oberflaeche."""
    fehl = pruefe_windows_werkzeuge()
    if fehl:
        sys.stderr.write(f"FEHLER: {fehl}\n")
        return 1
    if kat_name.strip() and finde_kategorie(kat_name) is None:
        sys.stderr.write(f"FEHLER: Unbekannte Kategorie {kat_name!r}. Hinweis: --help\n")
        return 2
    from wsc_gui import starte_gui as _gui

    return _gui(start_kat=kat_name)


def wait_ende() -> None:
    """Wartet auf Taste, wenn --Ende gesetzt ist."""
    print('Programmende: "Hit any Key or Enter"')
    try:
        input()
    except EOFError:
        return


def _ausgabe_ist_terminal() -> bool:
    """Meldet, ob stdout ein Terminal ist.

    Rückgabewert:
        True bei einem Terminal.

    Fehlerfälle:
        Eine fehlende isatty-Methode gilt als kein Terminal.

    Beispiel:
        _ausgabe_ist_terminal()
    """
    try:
        return bool(sys.stdout.isatty())
    except (AttributeError, ValueError):
        return False


def print_startup_banner() -> None:
    """Gibt Kurzname, Zweck und Version vor dem Fachlauf aus.

    Rückgabewert:
        None

    Fehlerfälle:
        Keine.

    Beispiel:
        print_startup_banner()
    """
    if sys.platform == "win32":
        os.system("")
    name = meta.PROJEKT
    zweck = meta.BESCHREIBUNG
    version = meta.VERSION
    stand = meta.STAND
    innen = f"  {name}  "
    linie = "═" * len(innen)
    farbe = "\033[96m" if _ausgabe_ist_terminal() else ""
    aus = "\033[0m" if farbe else ""
    print(f"{farbe}╔{linie}╗{aus}")
    print(f"{farbe}║{innen}║{aus}")
    print(f"{farbe}╚{linie}╝{aus}")
    print(zweck)
    print()
    print(f"Version {version}  |  {stand}")
    print()


def pruefe_plattform() -> None:
    """Beendet den Fachlauf, wenn das Betriebssystem nicht zugesagt ist.

    Rückgabewert:
        None auf einem zugesagten System.

    Fehlerfälle:
        SystemExit 1 auf anderen Systemen.

    Beispiel:
        pruefe_plattform()
    """
    system = platform.system()
    if system in {"Windows"}:
        return
    print(
        "FEHLER: Dieses Programm läuft unter Windows 11 "
        f"(erkannt: {system}).",
        file=sys.stderr,
    )
    raise SystemExit(1)

def main(argv: list[str] | None = None) -> int:
    """Programmeinstieg: Hilfe, Liste, Start oder GUI.

    Parameter
    ---------
    argv:
        Testargumente; None liest sys.argv.

    Rueckgabe
    ---------
    0 Erfolg, 1 Laufzeit, 2 Aufruf.

    Fehlerfaelle
    ------------
    Unbekannte Optionen enden mit Exit 2.

    Beispiel
    --------
    >>> main(["--version"]) in (0,)
    True
    """
    parser = build_parser()
    args = parser.parse_args(argv)
    code = 0
    try:
        if args.help:
            print_help(parser)
        elif args.version:
            print_version()
        else:
            print_startup_banner()
            pruefe_plattform()
            if args.starten:
                code = starten_cli(args.starten, args.kategorie, args.yes)
            elif args.list:
                code = liste_ausgeben(args.kategorie)
            else:
                code = starte_gui(args.kategorie)
    finally:
        if args.ende:
            wait_ende()
    return code


if __name__ == "__main__":
    sys.exit(main())
