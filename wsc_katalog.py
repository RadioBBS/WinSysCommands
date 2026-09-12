"""
WinSysCommands – Zeigt Windows-Systembefehle und 20 Befehlskategorien in Tabellen mit Kurz- und Langbeschreibung und startet den gewaehlten Eintrag.

Projekt:     WinSysCommands
Modul:       wsc_katalog.py
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
Version 1.0.0 – 2026-09-12 – Katalogzugriff fuer Systembefehle und 20 Kategorien.

Aufruf / Nutzung
----------------
Wird importiert, nicht als Programm gestartet.
"""

from __future__ import annotations

from dataclasses import dataclass

import project_meta as meta
from wsc_daten import KATALOG
from wsc_system import system_abschnitte, system_eintraege


@dataclass(frozen=True)
class Kategorie:
    """Eine Registerkarte im Katalog."""

    id: str
    tab: str
    titel: str


@dataclass(frozen=True)
class Eintrag:
    """Ein aufrufbarer Befehl mit Kurz- und Langtext."""

    kategorie: str
    befehl: str
    start: str
    kurz: str
    lang: str
    destruktiv: bool
    abschnitt: str = ""
    abschnitt_titel: str = ""


def _als_eintrag(roh: dict[str, object]) -> Eintrag:
    """Wandelt ein Katalogdict in einen Eintrag."""
    return Eintrag(
        kategorie=str(roh["kategorie"]),
        befehl=str(roh["befehl"]),
        start=str(roh.get("start") or roh["befehl"]),
        kurz=str(roh["kurz"]),
        lang=str(roh["lang"]),
        destruktiv=bool(roh.get("destruktiv", False)),
        abschnitt=str(roh.get("abschnitt") or ""),
        abschnitt_titel=str(roh.get("abschnitt_titel") or ""),
    )


def kategorien() -> list[Kategorie]:
    """Liefert Systembefehle plus die 20 Kategorie-Registerkarten.

    Rueckgabe
    ---------
    Liste, erstes Element ist immer die Systembefehle-Karte.

    Fehlerfaelle
    ------------
    Keine.

    Beispiel
    --------
    >>> kategorien()[0].id == meta.SYSTEM_KAT
    True
    """
    erste = Kategorie(meta.SYSTEM_KAT, "System", "System Commands")
    kurz = {
        "ms-settings": "Settings",
        "control": "control",
        "explorer": "Explorer",
    }
    weitere = [
        Kategorie(str(item["id"]), kurz.get(str(item["id"]), str(item["tab"])), str(item["titel"]))
        for item in KATALOG["kategorien"]
    ]
    return [erste, *weitere]


_ALLE: list[Eintrag] | None = None


def alle_eintraege() -> list[Eintrag]:
    """Liefert Systembefehle und alle Kategorieeintraege."""
    global _ALLE
    if _ALLE is None:
        roh = list(system_eintraege())
        roh.extend(KATALOG["eintraege"])
        _ALLE = [_als_eintrag(item) for item in roh]
    return _ALLE


def eintraege_von(kat_id: str, suche: str = "") -> list[Eintrag]:
    """Filtert Eintraege einer Kategorie, optional per Suchtext.

    Parameter
    ---------
    kat_id:
        Interne Kategorien-ID.
    suche:
        Freitext gegen Befehl und Kurzbeschreibung.

    Rueckgabe
    ---------
    Trefferliste in Katalogreihenfolge.

    Fehlerfaelle
    ------------
    Keine.

    Beispiel
    --------
    >>> len(eintraege_von(meta.SYSTEM_KAT)) > 0
    True
    """
    nadel = suche.strip().casefold()
    treffer: list[Eintrag] = []
    for eintrag in alle_eintraege():
        if eintrag.kategorie != kat_id:
            continue
        if nadel and nadel not in eintrag.befehl.casefold() and nadel not in eintrag.kurz.casefold():
            continue
        treffer.append(eintrag)
    return treffer


def finde_kategorie(name: str) -> Kategorie | None:
    """Findet eine Kategorie per ID oder Tab-Beschriftung."""
    nadel = name.strip().casefold()
    if not nadel or nadel in {"systembefehle", "system commands", "system"}:
        return kategorien()[0]
    for kat in kategorien():
        if kat.id.casefold() == nadel or kat.tab.casefold() == nadel:
            return kat
        if kat.titel.casefold() == nadel:
            return kat
    return None


def finde_eintrag(befehl: str, kat_id: str = "") -> Eintrag | None:
    """Findet den ersten Eintrag mit gleichem Befehls- oder Starttext."""
    nadel = befehl.strip().casefold()
    for eintrag in alle_eintraege():
        if kat_id and eintrag.kategorie != kat_id:
            continue
        if eintrag.befehl.casefold() == nadel or eintrag.start.casefold() == nadel:
            return eintrag
    return None


def abschnitte_von(kat_id: str) -> list[tuple[str, str]]:
    """Liefert sichtbare Abschnitte; Systembefehle haben mehrere Tabellen."""
    if kat_id == meta.SYSTEM_KAT:
        return system_abschnitte()
    kat = finde_kategorie(kat_id)
    titel = kat.titel if kat else kat_id
    return [("", titel)]
