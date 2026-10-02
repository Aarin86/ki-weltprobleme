#!/usr/bin/env python3
"""Woechentlicher KI-Beitrag fuer ki-weltprobleme (laeuft in GitHub Actions).

Laeuft taeglich, schreibt aber nur, wenn der letzte Beitrag 6+ Tage her ist.
Verpasste Laeufe werden so am Folgetag nachgeholt.
Das Modell liefert JSON (Datei, Titel, Text); das Skript haengt den Abschnitt selbst an,
damit Format und Beitragszeile immer stimmen und nichts Bestehendes veraendert wird.
"""
import json
import os
import pathlib
import subprocess
import sys
import time
import urllib.request

API = "https://api.deepseek.com"
MODELL_ID = os.environ.get("MODELL_ID", "deepseek-flash")
MODELL_NAME = os.environ.get("MODELL_NAME", "DeepSeek V4.1-Flash")
KEY = os.environ.get("DEEPSEEK_API_KEY", "")
ERZWINGEN = os.environ.get("ERZWINGEN", "false") == "true"
MIN_TAGE = 6
THEMEN = pathlib.Path("themen")


def git(*args):
    return subprocess.run(["git", *args], check=True, capture_output=True, text=True).stdout.strip()


def anfrage(pfad, daten=None):
    req = urllib.request.Request(
        API + pfad,
        data=json.dumps(daten).encode() if daten else None,
        headers={"Authorization": f"Bearer {KEY}", "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=600) as r:
        return json.load(r)


def ausgabe(name, wert):
    if "GITHUB_OUTPUT" in os.environ:
        with open(os.environ["GITHUB_OUTPUT"], "a") as f:
            f.write(f"{name}={wert}\n")


def main():
    ausgabe("neu", "nein")
    if not KEY:
        sys.exit("FEHLER: Secret DEEPSEEK_API_KEY fehlt.")

    letzter = git("log", "-1", "--format=%ct", "--grep=^Beitrag ", "--", "themen")
    if letzter and not ERZWINGEN:
        alter = (time.time() - int(letzter)) / 86400
        if alter < MIN_TAGE:
            print(f"Übersprungen: letzter Beitrag vor {alter:.1f} Tagen.")
            return

    modelle = [m["id"] for m in anfrage("/models").get("data", [])]
    if MODELL_ID not in modelle:
        sys.exit(f"FEHLER: Modell {MODELL_ID} nicht verfügbar. Vorhanden: {modelle}")

    dateien = sorted(p for p in THEMEN.glob("*.md") if not p.stem.endswith("_en"))
    inhalt = "\n\n".join(f"===== {p.name} =====\n{p.read_text()}" for p in dateien)
    heute = time.strftime("%Y-%m-%d")

    system = (
        "Du schreibst EINEN neuen Beitrag für das öffentliche Repository ki-weltprobleme "
        "(KI-Ansätze zu Weltproblemen). Regeln: "
        "(1) Wähle genau eine der vorhandenen Themendateien. Bevorzuge Themen mit wenigen "
        "Beiträgen und wiederhole keine Gedanken, die dort schon stehen. "
        "(2) 300 bis 600 Wörter, konkret, mit mindestens drei umsetzbaren Maßnahmen "
        "(fett nummeriert wie **1. ...**) und einem Absatz **Was unsicher ist.** "
        "(3) Keine erfundenen Zahlen oder Quellen; bei unsicheren Zahlen schreibe "
        "'Größenordnung unklar'. "
        "(4) Korrektes Deutsch mit echten Umlauten (ä ö ü ß), nicht ae/oe/ue/ss. "
        "(5) Antworte ausschließlich mit JSON: "
        '{"datei": "<dateiname.md>", "titel": "<Überschrift ohne #>", '
        '"text": "<Markdown-Text ohne Überschrift und ohne Beitragszeile>"}'
    )
    nachricht = f"Vorhandene Themendateien und ihr Inhalt:\n\n{inhalt}"
    namen = {p.name: p for p in dateien}

    fehler = ""
    for versuch in range(3):
        antwort = anfrage("/chat/completions", {
            "model": MODELL_ID,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": nachricht + fehler},
            ],
            "response_format": {"type": "json_object"},
            "max_tokens": 8000,
        })
        try:
            b = json.loads(antwort["choices"][0]["message"]["content"])
            datei, titel, text = b["datei"].strip(), b["titel"].strip().lstrip("# "), b["text"].strip()
        except (KeyError, ValueError, AttributeError) as e:
            fehler = f"\n\nDeine letzte Antwort war kein gültiges JSON ({e}). Bitte nur JSON."
            continue
        woerter = len(text.split())
        if datei not in namen:
            fehler = f"\n\nDie Datei {datei} gibt es nicht. Wähle eine aus der Liste."
        elif not 250 <= woerter <= 700:
            fehler = f"\n\nDein Text hatte {woerter} Wörter. Gefordert sind 300 bis 600."
        elif not titel or "\n" in titel:
            fehler = "\n\nDer Titel fehlt oder ist mehrzeilig."
        else:
            pfad = namen[datei]
            alt = pfad.read_text().rstrip("\n")
            pfad.write_text(f"{alt}\n\n## {titel}\n\nBeitrag: {MODELL_NAME}, {heute}\n\n{text}\n")
            print(f"Ergänzt: {pfad} ({woerter} Wörter) — {titel}")
            ausgabe("neu", "ja")
            ausgabe("datei", datei)
            return
        print(f"Versuch {versuch + 1} verworfen:{fehler}")
    sys.exit("FEHLER: kein gültiger Beitrag nach 3 Versuchen.")


if __name__ == "__main__":
    main()
