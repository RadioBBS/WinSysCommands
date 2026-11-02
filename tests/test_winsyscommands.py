"""
WinSysCommands – Zeigt Windows-Systembefehle und 20 Befehlskategorien in Tabellen mit Kurz- und Langbeschreibung und startet den gewaehlten Eintrag.

Projekt:     WinSysCommands
Modul:       tests/test_winsyscommands.py
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
Version 1.0.0 – 2026-09-12 – Erste Testfassung.
Version 1.0.0 – 2026-09-12 – Prueft Fenstericon und GitHub-Marke getrennt.
Version 1.0.0 – 2026-09-13 – Prueft Python-Powered-Logo und PYTHON_URL.
Version 1.0.1 – 2026-11-02 – Startausgabe und Python 3.11 nach Styleguide 2.1.0.

Aufruf / Nutzung
----------------
  python -m unittest tests.test_winsyscommands
"""

from __future__ import annotations

import os
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import project_meta as meta  # noqa: E402
from winsyscommands import BEISPIELE, main  # noqa: E402
from wsc_katalog import alle_eintraege, eintraege_von, finde_kategorie, kategorien  # noqa: E402
from wsc_launch import baue_argv, ist_konsole  # noqa: E402

PFLICHTFELDER = (
    "Projekt",
    "Modul",
    "Version",
    "Stand",
    "Abhaengig",
    "Bezug",
    "Lizenz",
    "Upstream",
    "Erstellt mit",
    "Autor",
)
KOPF_DATEIEN = (
    meta.SKRIPT,
    "wsc_gui.py",
    "wsc_icons.py",
    "wsc_katalog.py",
    "wsc_daten.py",
    "wsc_system.py",
    "wsc_launch.py",
    "project_meta.py",
    "PROJECT.yaml",
    "pyproject.toml",
    "requirements.txt",
    "README.md",
    "CHANGELOG.md",
    "LICENSE",
    "CITATION.cff",
    ".gitignore",
    ".gitattributes",
    "tests/__init__.py",
    "tests/test_winsyscommands.py",
    ".github/workflows/ci.yml",
    "assets/README.md",
)


def yaml_value(text: str, key: str) -> str:
    """Liest einen einzeiligen YAML-Schluessel."""
    for line in text.splitlines():
        if line.startswith("#") or ":" not in line:
            continue
        left, right = line.split(":", 1)
        if left.strip() == key:
            return right.strip().strip('"').strip("'")
    return ""


def toml_value(text: str, key: str) -> str:
    """Liest einen einzeiligen TOML-Schluessel im [project]-Block grob."""
    in_project = False
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("["):
            in_project = stripped == "[project]"
            continue
        if in_project and stripped.startswith(f"{key} "):
            return stripped.split("=", 1)[1].strip().strip('"').strip("'")
    return ""


def run_cli(extra: list[str]) -> subprocess.CompletedProcess[str]:
    """Startet winsyscommands.py als Kindprozess."""
    return subprocess.run(
        [sys.executable, str(ROOT / meta.SKRIPT), *extra],
        capture_output=True,
        text=True,
        check=False,
        cwd=str(ROOT),
        encoding="utf-8",
        errors="replace",
    )


class MetaTests(unittest.TestCase):
    """Abgleich PROJECT.yaml / pyproject.toml / Dateikoepfe."""

    def test_versions_match(self) -> None:
        """Eine Versionsnummer in YAML, TOML, Meta und CITATION."""
        yaml_text = (ROOT / "PROJECT.yaml").read_text(encoding="utf-8")
        toml_text = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
        cff = (ROOT / "CITATION.cff").read_text(encoding="utf-8")
        self.assertEqual(yaml_value(yaml_text, "version"), meta.VERSION)
        self.assertEqual(toml_value(toml_text, "version"), meta.VERSION)
        self.assertEqual(yaml_value(cff, "version"), meta.VERSION)
        self.assertEqual(yaml_value(yaml_text, "stand"), meta.STAND)
        self.assertEqual(yaml_value(yaml_text, "description"), meta.BESCHREIBUNG)

    def test_headers_present(self) -> None:
        """Pflichtfelder in allen Projektdateien."""
        for rel in KOPF_DATEIEN:
            text = (ROOT / rel).read_text(encoding="utf-8")
            for field in PFLICHTFELDER:
                self.assertIn(field, text, f"{rel} ohne Feld {field}")
            self.assertIn(meta.VERSION, text)
            self.assertIn(meta.STAND, text)
            self.assertIn(meta.BESCHREIBUNG, text)

    def test_no_literal_user_path(self) -> None:
        """Keine fest verdrahteten Profilpfade in den Quellen."""
        needle = os.environ.get("USERPROFILE", "___none___")
        for rel in KOPF_DATEIEN:
            text = (ROOT / rel).read_text(encoding="utf-8")
            self.assertNotIn(needle, text, f"{rel} enthaelt USERPROFILE-Literal")


class CliTests(unittest.TestCase):
    """--help/--version ohne Fachlauf."""

    def test_help(self) -> None:
        """Hilfe nennt Zweck, Version und dieselben Beispiele wie README."""
        proc = run_cli(["--help"])
        self.assertEqual(proc.returncode, 0)
        self.assertIn(meta.BESCHREIBUNG, proc.stdout)
        self.assertIn(meta.VERSION, proc.stdout)
        for beispiel in BEISPIELE:
            self.assertIn(beispiel, proc.stdout)
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        for beispiel in BEISPIELE:
            self.assertIn(beispiel, readme)

    def test_version(self) -> None:
        """--version gibt Nummer, Datum und Zweck aus."""
        proc = run_cli(["--version"])
        self.assertEqual(proc.returncode, 0)
        self.assertIn(meta.VERSION, proc.stdout)
        self.assertIn(meta.STAND, proc.stdout)
        self.assertIn(meta.BESCHREIBUNG, proc.stdout)

    def test_unknown_option(self) -> None:
        """Unbekannte Option: FEHLER und Exit 2."""
        proc = run_cli(["--gibt-es-nicht"])
        self.assertEqual(proc.returncode, 2)
        self.assertIn("FEHLER:", proc.stderr)
        self.assertIn("--help", proc.stderr)

    def test_unknown_kategorie_list(self) -> None:
        """Unbekannte Kategorie beim Listen: Exit 2."""
        proc = run_cli(["--list", "--kategorie", "gibt-es-nicht"])
        self.assertEqual(proc.returncode, 2)
        self.assertIn("FEHLER:", proc.stderr)

    def test_main_version(self) -> None:
        """main() mit --version ohne Kindprozess."""
        self.assertEqual(main(["--version"]), 0)

    def test_list_system(self) -> None:
        """--list gibt Systembefehle aus, ohne GUI."""
        proc = run_cli(["--list", "--kategorie", "Systembefehle"])
        self.assertEqual(proc.returncode, 0)
        self.assertIn("Control.exe", proc.stdout)
        self.assertIn("appwiz.cpl", proc.stdout)


class KatalogTests(unittest.TestCase):
    """21 Karten, Eintraege und Startzeilen."""

    def test_einundzwanzig_kategorien(self) -> None:
        """Systembefehle plus 20 Gruppen."""
        karten = kategorien()
        self.assertEqual(len(karten), 21)
        self.assertEqual(karten[0].id, meta.SYSTEM_KAT)
        self.assertTrue(len(eintraege_von(meta.SYSTEM_KAT)) >= 40)
        for kat in karten:
            self.assertGreater(len(eintraege_von(kat.id)), 0, kat.id)

    def test_suche_shell_desktop(self) -> None:
        """shell:Desktop liegt in der shell-Karte."""
        treffer = eintraege_von("shell", "Desktop")
        self.assertTrue(any(item.befehl == "shell:Desktop" for item in treffer))

    def test_finde_kategorie_alias(self) -> None:
        """Tabname und ID treffen dieselbe Karte."""
        self.assertEqual(finde_kategorie("shell:").id, "shell")
        self.assertEqual(finde_kategorie("GodMode").id, "godmode")

    def test_destruktiv_markiert(self) -> None:
        """Bekannte Risiko-Befehle sind markiert."""
        namen = {item.befehl.casefold() for item in alle_eintraege() if item.destruktiv}
        self.assertTrue(any("shutdown" in name for name in namen))
        self.assertTrue(any("diskpart" in name for name in namen))

    def test_argv_shell_und_settings(self) -> None:
        """Startzeilen werden abgebildet, ohne Prozesse zu starten."""
        self.assertEqual(baue_argv("shell:Desktop")[0], "explorer.exe")
        self.assertEqual(baue_argv("ms-settings:display"), ["startfile", "ms-settings:display"])
        self.assertTrue(ist_konsole("ipconfig"))
        ps = baue_argv("powershell: Get-VM")
        self.assertEqual(ps[0], "powershell.exe")
        self.assertIn("Get-VM", ps)

    def test_argv_mmc_und_temp(self) -> None:
        """MMC geht an die Shell, shell:Temp auf den echten Temp-Ordner."""
        self.assertEqual(baue_argv("services.msc"), ["startfile", "services.msc"])
        self.assertEqual(baue_argv("mmc devmgmt.msc"), ["startfile", "devmgmt.msc"])
        self.assertEqual(baue_argv("appwiz.cpl"), ["startfile", "appwiz.cpl"])
        temp_argv = baue_argv("shell:Temp")
        self.assertEqual(temp_argv[0], "startfile")
        self.assertTrue(temp_argv[1])
        env_temp = os.environ.get("TEMP") or os.environ.get("TMP")
        if env_temp:
            self.assertEqual(temp_argv[1], env_temp)


class IconTests(unittest.TestCase):
    """Fenstericon, GitHub-Marke und Python-Logo getrennt halten."""

    def test_github_url(self) -> None:
        """Repo-Link zeigt auf GitHub, nicht auf ein lokales Literal."""
        self.assertTrue(meta.GITHUB_URL.startswith("https://github.com/"))
        self.assertIn(meta.PROJEKT, meta.GITHUB_URL)

    def test_python_url(self) -> None:
        """Python-Link zeigt auf python.org."""
        self.assertEqual(meta.PYTHON_URL, "https://www.python.org/")

    def test_icon_dateien(self) -> None:
        """PNG-Magic, eigenes App-Icon ungleich den Marken-Dateien."""
        app = ROOT / "assets" / "app-icon.png"
        mark = ROOT / "assets" / "github-mark.png"
        python = ROOT / "assets" / "python-powered.png"
        png = b"\x89PNG\r\n\x1a\n"
        self.assertEqual(app.read_bytes()[:8], png)
        self.assertEqual(mark.read_bytes()[:8], png)
        self.assertEqual(python.read_bytes()[:8], png)
        self.assertNotEqual(app.read_bytes(), mark.read_bytes())
        self.assertNotEqual(app.read_bytes(), python.read_bytes())

    def test_fenstericon_nicht_fremdmarke(self) -> None:
        """Die GUI setzt iconphoto nur mit dem eigenen App-Icon."""
        gui = (ROOT / "wsc_gui.py").read_text(encoding="utf-8")
        icons = (ROOT / "wsc_icons.py").read_text(encoding="utf-8")
        self.assertIn("setze_fenstericon", gui)
        self.assertIn('APP_ICON = ASSETS / "app-icon.png"', icons)
        self.assertIn('GITHUB_MARK = ASSETS / "github-mark.png"', icons)
        self.assertIn('PYTHON_POWERED = ASSETS / "python-powered.png"', icons)
        self.assertIn("lade_png(APP_ICON)", icons)
        self.assertNotIn("iconphoto(True, self._github_mark)", gui)
        self.assertNotIn("iconphoto(True, self._python_logo)", gui)


class TabellenTests(unittest.TestCase):
    """GitHub-Tabellen in der Doku spaltenweise ausgerichtet."""

    def test_readme_tabelle_ausgerichtet(self) -> None:
        """Pipes untereinander in der Parameter-Tabelle."""
        zeilen = [
            line
            for line in (ROOT / "README.md").read_text(encoding="utf-8").splitlines()
            if line.startswith("| Name")
            or line.startswith("| -----------")
            or line.startswith("| --")
        ]
        self.assertGreaterEqual(len(zeilen), 3)
        laengen = {len(line) for line in zeilen}
        self.assertEqual(len(laengen), 1, zeilen)
