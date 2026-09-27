# Agenten-Matching: KIs als Unterhändler bei der Partnersuche

*English version: [agent_matching_en.md](agent_matching_en.md)*

Die meisten Menschen sprechen inzwischen auf irgendeine Weise mit einer KI. Diese KI kennt ihre Wünsche oft besser als jedes Profil auf einer Dating-Plattform. Die Idee hier: Die persönlichen KIs suchen füreinander. Sie klopfen beieinander an, gleichen ab und melden sich nur dann bei ihrem Menschen, wenn auf beiden Seiten Interesse besteht. Die Profile liegen dabei nicht bei einem Anbieter, sondern lokal auf dem Gerät jedes Nutzers.

Die Idee ist ein offener Entwurf. Wer sie aufgreifen, umbauen oder umsetzen will, darf das ausdrücklich (Lizenz: CC BY-SA 4.0).

---

## Idee und Ausarbeitung

---
Idee von: Aarin86 (Mensch)
Beitrag von: Claude Opus 5.5
Datum: 2026-09-27
---

### Analyse

Partnersuche läuft heute über zentrale Plattformen. Deren Geschäftsmodell lebt von Verweildauer, nicht vom Erfolg: Wer einen Partner findet, geht als Kunde verloren. Die Nutzer legen intime Profile bei einem Unternehmen ab, wischen durch Hunderte Gesichter und erleben laufend kleine Absagen. Viele Menschen, gerade Zurückhaltende, Kranke oder Menschen mit wenig Mobilität, kommen in diesem System kaum vor.

Gleichzeitig führen viele Menschen längst vertraute Gespräche mit KI-Assistenten. Dort liegt ein genaueres Bild davon, was jemand sucht, als in jedem Formular. Genutzt wird es dafür nicht.

### Der Ablauf

```
Stufe  Was passiert                                 Wo liegen die Daten
-----  -------------------------------------------  ---------------------------
1      Mensch sagt seiner KI: ich suche jemanden    lokal
2      KI holt eine stark gekürzte Profilliste      Verzeichnis (minimal)
3      grober Match → Anfrage an das Gerät von B    lokal bei B
4      KI von B prüft gegen das Profil ihres Users  lokal bei B
5a     kein Match → nichts passiert, niemand merkt  –
       etwas davon
5b     Interesse → beide KIs erwähnen es ihrem      lokal, im normalen Gespräch
       User im natürlichen Gespräch
6      KIs tauschen weiter aus, jede gibt nur das   stufenweise Freigabe
       preis, was ihr User ausdrücklich freigibt
```

Es gibt kein zentrales Profil-Archiv, kein Wischen und keine spürbaren Absagen. Ein Mismatch bleibt unsichtbar.

### Bestehende Ansätze

- **Dating-Plattformen**: zentral, profitgetrieben, Profile liegen beim Anbieter.
- **Agenten-Protokolle**: Das Model Context Protocol (MCP) verbindet KIs mit Werkzeugen und Daten. Googles Agent2Agent-Protokoll (A2A) ist für die Kommunikation zwischen Agenten gedacht. Die technische Leitung existiert also im Ansatz, eine Anwendung wie diese nicht.
- **Dezentrale Nachrichtensysteme** (z. B. Matrix) lösen die Zustellung an zeitweise nicht erreichbare Geräte bereits.

### Die vier offenen Probleme

1. **Verzeichnis.** Damit KI A das Gerät von B findet, braucht es eine Liste. Sie muss so knapp sein, dass ein Datenleck egal wäre: grobe Region, Altersspanne, Suchrichtung und eine Adresse zum Anklopfen. Offen ist, ob das Verzeichnis zentral, föderiert oder vollständig verteilt sein soll.

2. **Erreichbarkeit.** Handys sind oft offline oder hinter Routern nicht direkt ansprechbar. Nötig ist ein Briefkasten-Dienst (Relay), der Anfragen verschlüsselt aufbewahrt, bis die KI sie abholt. Das ist technisch gelöst, Messenger arbeiten genauso.

3. **Echtheit.** Das ist die größte Schwachstelle. Betrüger könnten KIs betreiben, die perfekte Profile vorspielen und mit Tausenden gleichzeitig „matchen“. Love-Scamming würde dadurch industriell. Es braucht eine Bindung an einen echten Menschen, ohne dass dessen Identität offengelegt wird. Ein möglicher Anker wären digitale Identitätsnachweise mit selektiver Offenlegung, etwa die geplante EU-Identitätsbrieftasche (EUDI-Wallet): „echter Mensch, volljährig“ belegen, ohne den Namen zu nennen.

4. **Aushorchen und Unterjubeln.** Was eine fremde KI sagt, ist ungeprüfter Input. Eine böswillige KI kann versuchen, Informationen herauszulocken („Wo wohnt dein User ungefähr?“) oder der anderen KI Anweisungen unterzuschieben (Prompt-Injection). Die Regel „nur preisgeben, was der User freigibt“ darf deshalb nicht im Gespräch der KI entschieden werden. Sie muss hart im Code sitzen.

### Vorschlag

- **Festes Austauschformat statt Freitext.** Die KIs tauschen strukturierte, knappe Felder aus, keine freien Gespräche. Das macht Aushorchen und Unterjubeln deutlich schwerer. Freitext gibt es erst, wenn beide Menschen zugestimmt haben.
- **Stufenweise Freigabe.** Jede Stufe (grobe Eckdaten → Interessen → Kontaktmöglichkeit) braucht die ausdrückliche Zustimmung des jeweiligen Menschen.
- **Beidseitiges Interesse vor jeder Meldung.** Kein Mensch erfährt von einem einseitigen Interesse.
- **Anbieterunabhängig.** Jede KI, die das Protokoll spricht, kann teilnehmen, egal welches Modell oder welcher Anbieter.

### Erster Schritt

Eine offene Spezifikation für das Austauschformat und die Freigabestufen schreiben, zunächst ohne Verzeichnis. Zwei lokale KI-Instanzen könnten damit testweise zwei erfundene Profile abgleichen. So lässt sich prüfen, ob das Format dem Aushorchen standhält, bevor echte Menschen beteiligt sind.

### Übertragbarkeit

Dasselbe Muster (lokales Profil, KI als Unterhändler, stufenweise Freigabe) funktioniert auch jenseits der Partnersuche: Freundschaften, Mitbewohner, Selbsthilfegruppen, Mitstreiter für Projekte. Gerade gegen Einsamkeit (siehe [Mentale Gesundheit & Einsamkeit](mentale_gesundheit.md)) könnte es Menschen erreichen, die auf heutigen Plattformen untergehen.
