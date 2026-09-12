"""
WinSysCommands – Zeigt Windows-Systembefehle und 20 Befehlskategorien in Tabellen mit Kurz- und Langbeschreibung und startet den gewaehlten Eintrag.

Projekt:     WinSysCommands
Modul:       wsc_gui.py
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
Version 1.0.0 – 2026-09-12 – Tabellen mit Aufruflinks, 3x7-Kategorien, scharfe Calibri.
Version 1.0.0 – 2026-09-12 – Eigenes Fenstericon; GitHub-Invertocat als Repo-Link.
Version 1.0.0 – 2026-09-13 – Python-Powered-Logo als Hinweis auf die Programmiersprache.

Aufruf / Nutzung
----------------
Wird von winsyscommands.py gestartet, nicht direkt:

    python winsyscommands.py
"""

from __future__ import annotations

import ctypes
import os
import tkinter as tk
import webbrowser
from tkinter import font as tkfont
from tkinter import messagebox, ttk

import project_meta as meta
from wsc_icons import GITHUB_MARK, PYTHON_POWERED, lade_png, setze_fenstericon
from wsc_katalog import Eintrag, Kategorie, eintraege_von, finde_kategorie, kategorien
from wsc_launch import starte_eintrag
from wsc_system import system_abschnitte

PROCESS_PER_MONITOR_DPI_AWARE = 2
DPI_AWARENESS_CONTEXT_PER_MONITOR_AWARE_V2 = -4


def aktiviere_dpi() -> None:
    """Schaltet Per-Monitor-DPI ein, damit Windows die Oberflaeche nicht weich skaliert.

    Rueckgabe
    ---------
    None.

    Fehlerfaelle
    ------------
    Fehlende DLL-Funktionen werden ignoriert; die GUI startet dann mit Systemstandard.

    Beispiel
    --------
    >>> aktiviere_dpi() is None
    True
    """
    if os.name != "nt":
        return
    try:
        kontext = ctypes.c_void_p(DPI_AWARENESS_CONTEXT_PER_MONITOR_AWARE_V2)
        ctypes.windll.user32.SetThreadDpiAwarenessContext(kontext)
        return
    except (AttributeError, OSError):
        pass
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(PROCESS_PER_MONITOR_DPI_AWARE)
    except (AttributeError, OSError):
        try:
            ctypes.windll.user32.SetProcessDPIAware()
        except (AttributeError, OSError):
            return


def setze_tk_skalierung(root: tk.Misc) -> None:
    """Setzt die Tk-Punktgroesse auf die echte Monitor-DPI.

    Parameter
    ---------
    root:
        Bereits erzeugtes Tk-Fenster.

    Rueckgabe
    ---------
    None.

    Fehlerfaelle
    ------------
    Ohne GetDpiForWindow bleibt die Tk-Vorgabe.

    Beispiel
    --------
    >>> isinstance(setze_tk_skalierung, object)
    True
    """
    if os.name != "nt":
        return
    root.update_idletasks()
    try:
        dpi = int(ctypes.windll.user32.GetDpiForWindow(root.winfo_id()))
    except (AttributeError, OSError, ValueError):
        return
    if dpi < 96:
        dpi = 96
    root.tk.call("tk", "scaling", dpi / 72)


def _schrift(groesse: int, *stil: str) -> tuple[str, int] | tuple[str, int, str]:
    """Baut ein Calibri-Tupel in der gewuenschten Groesse.

    Parameter
    ---------
    groesse:
        Punktgroesse.
    stil:
        Optionale Tk-Stile wie bold oder underline.

    Rueckgabe
    ---------
    Schrift-Tupel fuer Label, Button und Text.

    Fehlerfaelle
    ------------
    Keine.

    Beispiel
    --------
    >>> _schrift(11)[0]
    'Calibri'
    """
    if stil:
        return (meta.SCHRIFT_FAMILIE, groesse, " ".join(stil))
    return (meta.SCHRIFT_FAMILIE, groesse)


class CommandApp(tk.Tk):
    """Hauptfenster im Stil einer Befehlsliste mit Registerkarten."""

    def __init__(self, start_kat: str = "") -> None:
        super().__init__()
        setze_tk_skalierung(self)
        self._setze_schriften()
        self.title(f"{meta.WINDOW_TITLE} {meta.VERSION}")
        self.minsize(meta.WINDOW_MIN_W, meta.WINDOW_MIN_H)
        self.geometry("1400x800")
        self.configure(bg=meta.HINTERGRUND)
        self._fenstericon = setze_fenstericon(self)
        self._github_mark = None
        self._python_logo = None
        self._suche = tk.StringVar(value="")
        self._status = tk.StringVar(value="")
        self._gewaehlt: Eintrag | None = None
        self._tab_frames: dict[str, TabSeite] = {}
        self._tab_knoepfe: dict[str, tk.Label] = {}
        self._aktiv_id = kategorien()[0].id
        self._baue_menu()
        self._baue_kopf()
        self._baue_karten()
        ttk.Label(self, textvariable=self._status, anchor="w").pack(
            side=tk.BOTTOM, fill=tk.X, padx=8, pady=(0, 6)
        )
        self._inhalt = tk.Frame(self, bg=meta.HINTERGRUND)
        self._inhalt.pack(fill=tk.BOTH, expand=True, padx=8, pady=(0, 4))
        for kat in kategorien():
            seite = TabSeite(self._inhalt, kat, self)
            self._tab_frames[kat.id] = seite
        self._suche.trace_add("write", lambda *_args: self._filter_aktuell())
        if start_kat:
            self._oeffne_kategorie(start_kat)
        self.after(50, self._tab_gewechselt)

    def _setze_schriften(self) -> None:
        """Setzt Calibri fuer Standard-, Text- und Menueschriften.

        Rueckgabe
        ---------
        None.

        Fehlerfaelle
        ------------
        Unbekannte Tk-Schriftnamen werden uebergangen.

        Beispiel
        --------
        >>> CommandApp._setze_schriften.__name__
        '_setze_schriften'
        """
        for name in ("TkDefaultFont", "TkTextFont", "TkMenuFont", "TkHeadingFont"):
            try:
                tkfont.nametofont(name).configure(
                    family=meta.SCHRIFT_FAMILIE, size=meta.SCHRIFT_GROESSE
                )
            except tk.TclError:
                continue
        stil = ttk.Style(self)
        stil.configure(".", font=_schrift(meta.SCHRIFT_GROESSE))

    def _baue_menu(self) -> None:
        """Datei, Bearbeiten, Ansicht und Hilfe analog zur Store-App."""
        menue = tk.Menu(self)
        datei = tk.Menu(menue, tearoff=0)
        datei.add_command(label="Beenden", command=self.destroy)
        menue.add_cascade(label="Datei", menu=datei)
        bearbeiten = tk.Menu(menue, tearoff=0)
        bearbeiten.add_command(label="Befehl kopieren", command=self.kopiere_befehl)
        bearbeiten.add_command(label="Suche fokussieren", command=lambda: self._suchfeld.focus_set())
        menue.add_cascade(label="Bearbeiten", menu=bearbeiten)
        ansicht = tk.Menu(menue, tearoff=0)
        ansicht.add_command(label="Naechste Kategorie", command=self._naechste_karte)
        menue.add_cascade(label="Ansicht", menu=ansicht)
        hilfe = tk.Menu(menue, tearoff=0)
        hilfe.add_command(label="Info", command=self._info)
        hilfe.add_command(label="GitHub-Repository", command=self._oeffne_github)
        hilfe.add_command(label="Python-Website", command=self._oeffne_python)
        menue.add_cascade(label="Hilfe", menu=hilfe)
        self.config(menu=menue)

    def _baue_kopf(self) -> None:
        """Suchzeile ueber den Registerkarten."""
        kopf = tk.Frame(self, bg=meta.HINTERGRUND)
        kopf.pack(fill=tk.X, padx=12, pady=(8, 4))
        tk.Label(
            kopf,
            text="Suche:",
            bg=meta.HINTERGRUND,
            font=_schrift(meta.SCHRIFT_GROESSE),
        ).pack(side=tk.LEFT)
        self._suchfeld = ttk.Entry(kopf, textvariable=self._suche, width=40)
        self._suchfeld.pack(side=tk.LEFT, padx=8)
        ttk.Button(kopf, text="Starten", command=self.starten_gewaehlt).pack(side=tk.RIGHT)
        ttk.Button(kopf, text="Kopieren", command=self.kopiere_befehl).pack(side=tk.RIGHT, padx=6)
        self._baue_github_mark(kopf)
        self._baue_python_logo(kopf)

    def _baue_github_mark(self, kopf: tk.Frame) -> None:
        """Setzt das unveraenderte Invertocat als Link zum Repository.

        GitHub erlaubt die Marke als Schaltflaeche zum eigenen Projekt, nicht
        als Produkticon. Deshalb liegt das Bild in der Kopfzeile und oeffnet
        nur GITHUB_URL.

        Parameter
        ---------
        kopf:
            Rahmen der Suchzeile.

        Rueckgabe
        ---------
        None.

        Fehlerfaelle
        ------------
        Fehlende Datei: die Kopfzeile bleibt ohne Mark-Bild.

        Beispiel
        --------
        >>> CommandApp._baue_github_mark.__name__
        '_baue_github_mark'
        """
        self._github_mark = lade_png(GITHUB_MARK, kantenlaenge=24)
        if self._github_mark is None:
            return
        knopf = tk.Label(
            kopf,
            image=self._github_mark,
            bg=meta.HINTERGRUND,
            cursor="hand2",
        )
        knopf.pack(side=tk.RIGHT, padx=(0, 8))
        knopf.bind("<Button-1>", lambda _e: self._oeffne_github())
        knopf.bind("<Enter>", lambda _e: self._status.set("GitHub-Repository oeffnen"))

    def _baue_python_logo(self, kopf: tk.Frame) -> None:
        """Setzt das unveraenderte Python-Powered-Logo als Sprachhinweis.

        Die PSF erlaubt das unveraenderte Logo ohne vorherige Freigabe, um
        anzuzeigen, dass Software in der Programmiersprache Python geschrieben
        ist. Es ist nicht das Fenstericon.

        Parameter
        ---------
        kopf:
            Rahmen der Suchzeile.

        Rueckgabe
        ---------
        None.

        Fehlerfaelle
        ------------
        Fehlende Datei: die Kopfzeile bleibt ohne Python-Logo.

        Beispiel
        --------
        >>> CommandApp._baue_python_logo.__name__
        '_baue_python_logo'
        """
        self._python_logo = lade_png(PYTHON_POWERED)
        if self._python_logo is None:
            return
        rahmen = tk.Frame(kopf, bg=meta.HINTERGRUND)
        rahmen.pack(side=tk.RIGHT, padx=(0, 8))
        knopf = tk.Label(
            rahmen,
            image=self._python_logo,
            bg=meta.HINTERGRUND,
            cursor="hand2",
        )
        knopf.pack(side=tk.LEFT)
        tm = tk.Label(
            rahmen,
            text="™",
            bg=meta.HINTERGRUND,
            cursor="hand2",
            font=_schrift(8),
        )
        tm.pack(side=tk.LEFT, anchor="n")
        for teil in (knopf, tm, rahmen):
            teil.bind("<Button-1>", lambda _e: self._oeffne_python())
            teil.bind(
                "<Enter>",
                lambda _e: self._status.set(
                    "Geschrieben in der Programmiersprache Python (python.org)"
                ),
            )

    def _oeffne_python(self) -> None:
        """Oeffnet die Python-Website im Standardbrowser.

        Rueckgabe
        ---------
        None.

        Fehlerfaelle
        ------------
        Wenn der Browser nicht startet, erscheint ein Dialog mit der Adresse.

        Beispiel
        --------
        >>> CommandApp._oeffne_python.__name__
        '_oeffne_python'
        """
        geoffnet = webbrowser.open(meta.PYTHON_URL)
        if not geoffnet:
            messagebox.showerror(
                meta.PROJEKT,
                f"Python-Website konnte nicht geoeffnet werden. Adresse: {meta.PYTHON_URL}",
            )
            return
        self._status.set(meta.PYTHON_URL)

    def _oeffne_github(self) -> None:
        """Oeffnet die Projektseite auf GitHub im Standardbrowser.

        Rueckgabe
        ---------
        None.

        Fehlerfaelle
        ------------
        Wenn der Browser nicht startet, erscheint ein Dialog mit der Adresse.

        Beispiel
        --------
        >>> CommandApp._oeffne_github.__name__
        '_oeffne_github'
        """
        geoffnet = webbrowser.open(meta.GITHUB_URL)
        if not geoffnet:
            messagebox.showerror(
                meta.PROJEKT,
                f"Repository konnte nicht geoeffnet werden. Adresse: {meta.GITHUB_URL}",
            )
            return
        self._status.set(meta.GITHUB_URL)

    def _baue_karten(self) -> None:
        """Zeichnet 21 Kategorien als 3 x 7 Knöpfe über die Fensterbreite."""
        huelle = tk.Frame(self, bg=meta.HINTERGRUND)
        huelle.pack(fill=tk.X, padx=8, pady=(0, 4))
        leiste = tk.Frame(huelle, bg=meta.HINTERGRUND)
        spalten = 7
        for idx, kat in enumerate(kategorien()):
            knopf = tk.Label(
                leiste,
                text=kat.tab,
                font=_schrift(meta.SCHRIFT_KNOPF),
                relief=tk.GROOVE,
                bd=1,
                padx=4,
                pady=6,
                bg="#f3f3f3",
                cursor="hand2",
            )
            knopf.bind("<Button-1>", lambda _e, kid=kat.id: self._waehle_karte(kid))
            knopf.grid(
                row=idx // spalten,
                column=idx % spalten,
                sticky="nsew",
                padx=3,
                pady=3,
            )
            self._tab_knoepfe[kat.id] = knopf
        for col in range(spalten):
            leiste.columnconfigure(col, weight=1, uniform="kat")
        leiste.update_idletasks()
        hoehe = max(leiste.winfo_reqheight(), 90)
        self._karten_huelle = huelle
        self._karten_leiste = leiste
        huelle.configure(height=hoehe)
        huelle.pack_propagate(False)
        leiste.place(x=0, y=0, relwidth=1.0, height=hoehe)
        self.bind("<Configure>", self._karten_anpassen)
        self.after_idle(self._karten_anpassen)

    def _karten_anpassen(self, event: tk.Event | None = None) -> None:
        """Haelt die 3x7-Leiste auf der Clientbreite, damit alle sieben Spalten sichtbar sind.

        Parameter
        ---------
        event:
            Configure-Ereignis oder None beim ersten Layout.

        Rueckgabe
        ---------
        None.

        Fehlerfaelle
        ------------
        Keine.

        Beispiel
        --------
        >>> CommandApp._karten_anpassen.__name__
        '_karten_anpassen'
        """
        if event is not None and event.widget is not self:
            return
        if not hasattr(self, "_karten_huelle"):
            return
        breite = self.winfo_width() - 20
        if breite < 200:
            return
        self._karten_huelle.configure(width=breite)

    def aktuelle_kategorie(self) -> str:
        """ID der sichtbaren Registerkarte."""
        return self._aktiv_id

    def _waehle_karte(self, kat_id: str) -> None:
        """Wechselt die sichtbare Kategorie."""
        self._aktiv_id = kat_id
        self._tab_gewechselt()

    def _tab_gewechselt(self, _event: object | None = None) -> None:
        """Zeichnet die aktive Tabelle nach einem Tabwechsel neu."""
        for kid, knopf in self._tab_knoepfe.items():
            if kid == self._aktiv_id:
                knopf.configure(bg="#cce4f7", relief=tk.SUNKEN)
            else:
                knopf.configure(bg="#f3f3f3", relief=tk.GROOVE)
        for kid, seite in self._tab_frames.items():
            if kid == self._aktiv_id:
                seite.pack(fill=tk.BOTH, expand=True)
            else:
                seite.pack_forget()
        seite = self._tab_frames[self.aktuelle_kategorie()]
        seite.fuellen(self._suche.get())
        self._setze_status(seite.anzahl)

    def _filter_aktuell(self) -> None:
        """Wendet den Suchtext auf die offene Karte an."""
        seite = self._tab_frames[self.aktuelle_kategorie()]
        seite.fuellen(self._suche.get())
        self._setze_status(seite.anzahl)

    def _setze_status(self, anzahl: int) -> None:
        """Aktualisiert die Statuszeile."""
        kat = next(item for item in kategorien() if item.id == self.aktuelle_kategorie())
        self._status.set(f"{kat.titel}: {anzahl} Eintraege")

    def zeige_eintrag(self, eintrag: Eintrag, *, starten: bool) -> None:
        """Fuellt die rechte Spalte und startet optional den Link."""
        self._gewaehlt = eintrag
        seite = self._tab_frames[eintrag.kategorie]
        seite.zeige_detail(eintrag)
        if starten:
            self.starten_gewaehlt()

    def starten_gewaehlt(self) -> None:
        """Startet den in der Detailspalte gezeigten Befehl."""
        if self._gewaehlt is None:
            messagebox.showinfo(meta.PROJEKT, "Bitte zuerst einen Befehl in der Tabelle anwaehlen.")
            return
        code = starte_eintrag(
            self._gewaehlt,
            nachfragen=lambda text: messagebox.askyesno(meta.PROJEKT, text),
        )
        if code != 0:
            messagebox.showerror(meta.PROJEKT, "Start fehlgeschlagen. Details stehen auf stderr.")

    def kopiere_befehl(self) -> None:
        """Kopiert die Startzeile in die Zwischenablage."""
        if self._gewaehlt is None:
            return
        self.clipboard_clear()
        self.clipboard_append(self._gewaehlt.start)
        self._status.set(f"Kopiert: {self._gewaehlt.start}")

    def _oeffne_kategorie(self, name: str) -> None:
        """Waehlt die Registerkarte per ID oder Tabnamen."""
        kat = finde_kategorie(name)
        if kat is not None:
            self._aktiv_id = kat.id

    def _naechste_karte(self) -> None:
        """Blaettert zur naechsten Registerkarte."""
        karten = kategorien()
        idx = next(i for i, kat in enumerate(karten) if kat.id == self._aktiv_id)
        self._waehle_karte(karten[(idx + 1) % len(karten)].id)

    def _info(self) -> None:
        """Zeigt Version und Zweck."""
        messagebox.showinfo(
            meta.PROJEKT,
            f"{meta.PROJEKT} {meta.VERSION} ({meta.STAND})\n\n{meta.BESCHREIBUNG}",
        )


class TabSeite(tk.Frame):
    """Eine Kategorie: Tabelle links, Langbeschreibung im rechten Drittel."""

    def __init__(self, parent: tk.Frame, kat: Kategorie, app: CommandApp) -> None:
        super().__init__(parent, bg=meta.HINTERGRUND)
        self.kat = kat
        self.app = app
        self.anzahl = 0
        paned = ttk.Panedwindow(self, orient=tk.HORIZONTAL)
        paned.pack(fill=tk.BOTH, expand=True)
        links = tk.Frame(paned, bg=meta.HINTERGRUND)
        rechts = tk.Frame(paned, bg=meta.DETAIL_HG, width=380)
        paned.add(links, weight=2)
        paned.add(rechts, weight=1)
        self._canvas = tk.Canvas(links, bg=meta.HINTERGRUND, highlightthickness=0)
        scroll = ttk.Scrollbar(links, orient=tk.VERTICAL, command=self._canvas.yview)
        self._innen = tk.Frame(self._canvas, bg=meta.HINTERGRUND)
        self._innen.bind(
            "<Configure>",
            lambda _e: self._canvas.configure(scrollregion=self._canvas.bbox("all")),
        )
        self._fenster = self._canvas.create_window((0, 0), window=self._innen, anchor="nw")
        self._canvas.configure(yscrollcommand=scroll.set)
        self._canvas.bind("<Configure>", self._breite_anpassen)
        self._canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self._canvas.bind("<Enter>", lambda _e: self._canvas.bind_all("<MouseWheel>", self._rad))
        self._canvas.bind("<Leave>", lambda _e: self._canvas.unbind_all("<MouseWheel>"))
        self._detail = tk.Text(
            rechts,
            wrap=tk.WORD,
            bg=meta.DETAIL_HG,
            relief=tk.FLAT,
            padx=12,
            pady=12,
            font=_schrift(meta.SCHRIFT_KOPF),
        )
        self._detail.pack(fill=tk.BOTH, expand=True)
        self._detail.insert("1.0", "Einen Befehl in der Tabelle anwaehlen.")
        self._detail.configure(state=tk.DISABLED)

    def _breite_anpassen(self, event: tk.Event) -> None:
        """Haelt die Innentabelle auf Canvas-Breite."""
        self._canvas.itemconfigure(self._fenster, width=event.width)

    def _rad(self, event: tk.Event) -> None:
        """Mausrad fuer die Befehlsliste."""
        self._canvas.yview_scroll(int(-event.delta / 120), "units")

    def fuellen(self, suche: str) -> None:
        """Baut die HTML-aehnlichen Tabellen der Kategorie neu."""
        for kind in self._innen.winfo_children():
            kind.destroy()
        eintraege = eintraege_von(self.kat.id, suche)
        self.anzahl = len(eintraege)
        tk.Label(
            self._innen,
            text=self.kat.titel,
            font=_schrift(meta.SCHRIFT_TITEL, "bold"),
            bg=meta.HINTERGRUND,
            anchor="w",
        ).pack(fill=tk.X, padx=16, pady=(16, 4))
        ttk.Separator(self._innen, orient=tk.HORIZONTAL).pack(fill=tk.X, padx=16, pady=(0, 12))
        if self.kat.id == meta.SYSTEM_KAT:
            self._system_tabellen(eintraege)
        else:
            self._eine_tabelle(self.kat.titel, eintraege)

    def _system_tabellen(self, eintraege: list[Eintrag]) -> None:
        """Mehrere Untertabellen wie control.exe und *.cpl in der Store-App."""
        by_abs: dict[str, list[Eintrag]] = {}
        for item in eintraege:
            by_abs.setdefault(item.abschnitt, []).append(item)
        for abs_id, titel in system_abschnitte():
            gruppe = by_abs.get(abs_id, [])
            if gruppe:
                self._eine_tabelle(titel, gruppe)

    def _eine_tabelle(self, titel: str, zeilen: list[Eintrag]) -> None:
        """Zwei Spalten: Aufruflink links, Kurzbeschreibung rechts."""
        kasten = tk.Frame(self._innen, bg=meta.HINTERGRUND)
        kasten.pack(fill=tk.X, padx=16, pady=(0, 16))
        tk.Label(
            kasten,
            text=titel,
            font=_schrift(meta.SCHRIFT_KOPF, "bold"),
            bg=meta.HINTERGRUND,
            anchor="w",
        ).pack(fill=tk.X, pady=(0, 6))
        tabelle = tk.Frame(kasten, bg=meta.TABELLEN_RAND, bd=1)
        tabelle.pack(fill=tk.X)
        for idx, eintrag in enumerate(zeilen):
            farbe = "#ffffff" if idx % 2 == 0 else "#fafafa"
            zeile = tk.Frame(tabelle, bg=farbe)
            zeile.pack(fill=tk.X, padx=1, pady=1)
            zeile.columnconfigure(0, weight=2, minsize=240)
            zeile.columnconfigure(1, weight=3, minsize=260)
            link = tk.Label(
                zeile,
                text=eintrag.befehl,
                fg=meta.LINK_FARBE,
                bg=farbe,
                cursor="hand2",
                font=_schrift(meta.SCHRIFT_GROESSE, "underline"),
                anchor="w",
                padx=8,
                pady=4,
            )
            link.grid(row=0, column=0, sticky="nsew")
            kurz = tk.Label(
                zeile,
                text=eintrag.kurz,
                bg=farbe,
                font=_schrift(meta.SCHRIFT_GROESSE),
                anchor="w",
                padx=8,
                pady=4,
            )
            kurz.grid(row=0, column=1, sticky="nsew")
            link.bind("<Button-1>", lambda _e, item=eintrag: self.app.zeige_eintrag(item, starten=True))
            kurz.bind("<Button-1>", lambda _e, item=eintrag: self.app.zeige_eintrag(item, starten=False))

    def zeige_detail(self, eintrag: Eintrag) -> None:
        """Schreibt die Langbeschreibung in das rechte Drittel."""
        self._detail.configure(state=tk.NORMAL)
        self._detail.delete("1.0", tk.END)
        warn = "\n\nAchtung: destruktiver Befehl, Start nur nach Bestaetigung." if eintrag.destruktiv else ""
        text = (
            f"{eintrag.befehl}\n\n"
            f"{eintrag.kurz}\n\n"
            f"{eintrag.lang}\n\n"
            f"Startzeile:\n{eintrag.start}{warn}"
        )
        self._detail.insert("1.0", text)
        self._detail.configure(state=tk.DISABLED)


def starte_gui(start_kat: str = "") -> int:
    """Oeffnet das Hauptfenster und blockiert bis zum Schliessen.

    Rueckgabe
    ---------
    0 nach normalem Fensterende.
    """
    aktiviere_dpi()
    app = CommandApp(start_kat=start_kat)
    app.mainloop()
    return 0
