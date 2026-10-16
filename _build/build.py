# -*- coding: utf-8 -*-
"""Erzeugt alle HTML-Seiten der Website aus gemeinsamen Bausteinen.
Aufruf:  python _build/build.py   (schreibt die .html-Dateien in den Projektordner)
Texte der Leistungen stehen in _build/content.py.
"""
import json, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content import SERVICES, HOME_FAQ

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FIRMA = "Autopflege Leichlingen"
TEL = "0177 / 780 41 46"
TEL_HREF = "tel:+491777804146"
MAIL = "autopflegeservice@online.de"
STRASSE = "Walter-Frese-Str. 16"
ORT = "42799 Leichlingen"
MAPS = "https://www.google.com/maps/dir/?api=1&destination=Walter-Frese-Str.+16,+42799+Leichlingen"

# Bilder und Kurzpunkte je Leistung
EXTRA = {
    "autoaufbereitung": dict(img="fahrzeug-komplett", img2="werkstatt", img_alt="Frisch aufbereitete dunkelblaue Limousine", img2_alt="Aufbereitung eines Fahrzeugs in der Werkstatt", pts=["Schonende Handwäsche statt Waschstraße", "Felgen, Lack, Scheiben und Innenraum", "Ideal vor Verkauf oder nach dem Winter"]),
    "innenraumreinigung": dict(img="innenraumreinigung", img2="lederpflege", img_alt="Polsterreinigung eines Autositzes mit Bürste und Schaum", img2_alt="Lederpflege eines Autositzes", pts=["Polster und Teppiche tiefengereinigt", "Leder gereinigt und gepflegt", "Tierhaare, Flecken und Gerüche"]),
    "lackpolitur": dict(img="lackpolitur", img2="lack-abperleffekt", img_alt="Maschinelle Lackpolitur auf einer schwarzen Motorhaube", img2_alt="Wasserperlen auf poliertem Lack", pts=["Waschkratzer und Hologramme entfernen", "Matte Stellen auffrischen", "Tiefer Glanz mit Versiegelung"]),
    "lackierung": dict(img="lackierung", img2="smart-repair", img_alt="Lackierer trägt Klarlack auf einen Kotflügel auf", img2_alt="Punktuelle Lackreparatur an einem Stoßfänger", pts=["Smart Repair für Kratzer und Steinschläge", "Teil- und Ganzlackierung", "Farbton am Fahrzeug abgestimmt"]),
    "unfallschadenabwicklung": dict(img="unfallschaden", img2="karosserie-reparatur", img_alt="Schadensaufnahme am Heck eines Unfallfahrzeugs", img2_alt="Karosseriearbeiten an einem Kotflügel", pts=["Ein Ansprechpartner für alles", "Abstimmung mit der Versicherung", "Reparatur und Lackierung im Haus"]),
    "gutachten": dict(img="gutachten", img2="gutachten-detail", img_alt="Schadensaufnahme mit Tablet an einem Unfallfahrzeug", img2_alt="Dokumentation eines Lackschadens an der Karosserie", pts=["Schaden fachgerecht dokumentiert", "Reparaturkosten und Wertminderung", "Grundlage für die Versicherung"]),
    "ersatzwagen": dict(img="ersatzwagen", img2="fahrzeuguebergabe", img_alt="Schlüsselübergabe für einen Ersatzwagen", img2_alt="Fahrzeugübergabe in der Werkstatt", pts=["Mobil während der Reparatur", "Übergabe direkt bei Abgabe", "Bei Unfallschäden mit der Versicherung abgestimmt"]),
    "leasingrueckgabe": dict(img="leasingrueckgabe", img2="fahrzeug-komplett", img_alt="Lackkontrolle mit Prüflampe vor der Leasingrückgabe", img2_alt="Aufbereitetes Fahrzeug in der Halle", pts=["Bestandsaufnahme am Fahrzeug", "Kratzer und Innenraum in Ordnung bringen", "Teure Nachberechnungen vermeiden"]),
}
for _s in SERVICES:
    _s.update(EXTRA[_s["slug"]])

ICO = {
    "phone": '<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2z"/></svg>',
    "mail": '<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/></svg>',
    "pin": '<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 21s7-6.2 7-11.5A7 7 0 0 0 5 9.5C5 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/></svg>',
    "clock": '<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
    "check": '<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>',
    "lock": '<svg class="ico" viewBox="0 0 24 24" aria-hidden="true"><rect x="5" y="11" width="14" height="9" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/></svg>',
}
ARROW = '<svg class="arrow" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 12h15M13 6l6 6-6 6"/></svg>'

# Eigene Piktogramme für die Vorteile (werden beim Einblenden gezeichnet)
PIC = {
    "hand": '<svg class="pic" viewBox="0 0 48 48" aria-hidden="true"><path d="M5 31v-5l4-2 4.500-7.500A3 3 0 0 1 16 15h16a3 3 0 0 1 2.500 1.500L39 24l4 2v5a2 2 0 0 1-2 2h-2"/><path d="M11 33H7a2 2 0 0 1-2-2"/><path d="M19 33h10"/><circle cx="15" cy="33" r="4"/><circle cx="33" cy="33" r="4"/><path d="M11 24h26"/><path class="ac" d="M40 4v8M36 8h8"/><path class="ac" d="M7 7v5M4.500 9.500h5"/></svg>',
    "price": '<svg class="pic" viewBox="0 0 48 48" aria-hidden="true"><path d="M11 5h17l9 9v27a2 2 0 0 1-2 2H11a2 2 0 0 1-2-2V7a2 2 0 0 1 2-2z"/><path d="M28 5v9h9"/><path d="M15 21h12M15 27h7"/><circle class="ac" cx="30" cy="34" r="7"/><path class="ac" d="M26.800 34l2.300 2.300 4.200-4.600"/></svg>',
    "spray": '<svg class="pic" viewBox="0 0 48 48" aria-hidden="true"><path d="M6 15h24v9H6z"/><path d="M30 17h6v5h-6"/><path d="M12 15V7h11v8"/><path d="M12 24l-3 16h9l3-16"/><path d="M24 24v5a3 3 0 0 1-3 3"/><path class="ac" d="M40 13l4-3M41 19.500h5M40 26l4 3"/></svg>',
    "date": '<svg class="pic" viewBox="0 0 48 48" aria-hidden="true"><rect x="6" y="9" width="36" height="33" rx="4"/><path d="M6 18h36M15 5v8M33 5v8"/><path class="ac" d="M16 29.500l5.500 5.500L32 24"/></svg>',
}

BENEFITS = [
    ("hand", "Handarbeit statt Waschstraße", "Jedes Fahrzeug wird von Hand bearbeitet – schonend für Lack und Material."),
    ("price", "Preis steht vorher fest", "Sie bekommen ein Angebot, bevor wir anfangen. Keine Überraschung bei der Abholung."),
    ("spray", "Aufbereitung & Lack aus einer Hand", "Reinigung, Politur und Lackierung – ohne mehrere Betriebe anzufahren."),
    ("date", "Fester Termin", "Abgabe und Abholung stimmen wir verbindlich mit Ihnen ab."),
]


# Kleine Symbole für den Leistungsumfang; Zuordnung über Stichwörter im Text
def _i(body):
    return '<svg viewBox="0 0 24 24" aria-hidden="true">' + body + '</svg>'


INC_ICON = {
    "drop": _i('<path d="M12 3c4 5 6 8 6 11a6 6 0 0 1-12 0c0-3 2-6 6-11z"/><path d="M9.5 14.5a2.500 2.500 0 0 0 2.500 2.500"/>'),
    "seat": _i('<path d="M7 4h4a2 2 0 0 1 2 2v7h4a2 2 0 0 1 2 2v2H9a2 2 0 0 1-2-2z"/><path d="M9 17v3M17 17v3"/>'),
    "sparkle": _i('<path d="M11 3l1.900 5.100L18 10l-5.100 1.900L11 17l-1.900-5.100L4 10l5.100-1.900z"/><path d="M19 15v5M16.500 17.500h5"/>'),
    "wheel": _i('<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="2.500"/><path d="M12 3v6.500M12 14.500V21M3 12h6.500M14.500 12H21"/>'),
    "glass": _i('<path d="M3.500 17l2.300-8.500A2 2 0 0 1 7.700 7h8.600a2 2 0 0 1 1.900 1.500L20.500 17z"/><path d="M9 14l2.500-3.500M13 14.500l1.500-2"/>'),
    "shield": _i('<path d="M12 3l7 3v5c0 4.500-3 8-7 10-4-2-7-5.500-7-10V6z"/><path d="M9 12l2 2 4-4"/>'),
    "spray": _i('<path d="M3 8h11v4H3z"/><path d="M14 9h3v2h-3M6 8V4h5v4M6 12l-1.500 8h4l1.500-8"/><path d="M20 7l1.500-1M20.500 10h2M20 13l1.500 1"/>'),
    "palette": _i('<path d="M12 3a9 9 0 1 0 0 18c1.500 0 2-1 2-2s-.500-2 1-2h2a4 4 0 0 0 4-4c0-4.500-4-8-9-8z"/><circle cx="8" cy="11" r="1"/><circle cx="11.500" cy="7.500" r="1"/><circle cx="16" cy="9" r="1"/>'),
    "clock": _i('<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>'),
    "doc": _i('<path d="M7 3h7l4 4v14H7z"/><path d="M14 3v4h4M10 12h5M10 16h3"/>'),
    "search": _i('<circle cx="10.500" cy="10.500" r="6.500"/><path d="M15.500 15.500L21 21"/>'),
    "target": _i('<circle cx="12" cy="12" r="8"/><circle cx="12" cy="12" r="3"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3"/>'),
    "wrench": _i('<path d="M15 4a4.500 4.500 0 0 0 5 6l-9.500 9.500a2.100 2.100 0 0 1-3-3L17 7z"/>'),
    "paw": _i('<circle cx="7" cy="9" r="1.800"/><circle cx="12" cy="6.500" r="1.800"/><circle cx="17" cy="9" r="1.800"/><path d="M12 12c-3 0-5 2.500-5 5a2.500 2.500 0 0 0 2.500 2.500c1 0 1.500-.500 2.500-.500s1.500.500 2.500.500A2.500 2.500 0 0 0 17 17c0-2.500-2-5-5-5z"/>'),
    "car": _i('<path d="M3 16v-3l2-1 2-4.500h10l2 4.500 2 1v3h-2M5 16H3M10 16h4"/><circle cx="7.500" cy="16" r="2"/><circle cx="16.500" cy="16" r="2"/>'),
    "check": _i('<path d="M5 12.500l4.500 4.500L19 7.500"/>'),
}
INC_RULES = [
    ("shield", ["versiegelung", "wachs", "lackpflege"]),
    ("sparkle", ["politur", "polier", "hologramm", "matte ", "finish", "angleichen"]),
    ("paw", ["tierhaare"]),
    ("wheel", ["felgen", "radk"]),
    ("glass", ["scheibe", "scheinwerfer"]),
    ("seat", ["saugen", "innenraum", "polster", "teppich", "armaturen", "kunststoff", "leder"]),
    ("palette", ["farbton"]),
    ("clock", ["aushärtung"]),
    ("doc", ["pflegehinweise"]),
    ("search", ["bestandsaufnahme", "besichtigung", "schadensaufnahme"]),
    ("doc", ["konditionen", "gutachten", "dokumentation", "versicherung", "reparaturkosten", "wertminderung"]),
    ("wrench", ["karosserie"]),
    ("wrench", ["motorraum"]),
    ("target", ["smart repair", "kratzer", "steinschl", "parkrempler", "lackabplatzer"]),
    ("spray", ["lackierung", "stoßfänger", "kotflügel", "spiegel", "schrammen"]),
    ("drop", ["wäsche", "lackreinigung", "flugrost"]),
    ("car", ["türfalze", "ersatzwagen", "übergabe", "rückgabe bei"]),
    ("clock", ["reservierung"]),
]


def inc_icon(text):
    t = text.lower()
    for key, words in INC_RULES:
        if any(w in t for w in words):
            return INC_ICON[key]
    return INC_ICON["check"]


# Zusätzliche Fragen, die auf jeder Leistungsseite ergänzt werden
MORE_FAQ = [
    ("Wie bekomme ich ein Angebot?", "Am schnellsten über das Formular auf dieser Seite oder per Anruf. Beschreiben Sie kurz Fahrzeug und Zustand – gern auch mit Fotos per E-Mail. Sie erhalten dann ein unverbindliches Angebot."),
    ("Brauche ich einen Termin?", "Ja, wir arbeiten nach Terminvereinbarung. So können wir uns ohne Zeitdruck um Ihr Fahrzeug kümmern."),
    ("Kann ich mehrere Leistungen kombinieren?", "Ja. Aufbereitung, Politur und Lackarbeiten lassen sich gut in einem Termin verbinden. Wir stimmen die Reihenfolge der Arbeiten für Sie ab."),
    ("Aus welchen Orten kommen Ihre Kunden?", "Unser Betrieb liegt in Leichlingen. Viele Kunden kommen auch aus Langenfeld, Leverkusen, Solingen und Burscheid."),
]
HOME_FAQ = HOME_FAQ + [
    ("Wie bekomme ich ein Angebot?", "Am schnellsten über das Formular oder per Anruf. Beschreiben Sie kurz Fahrzeug und Zustand – gern auch mit Fotos per E-Mail. Sie erhalten dann ein unverbindliches Angebot."),
    ("Kann ich mehrere Leistungen kombinieren?", "Ja. Aufbereitung, Politur und Lackarbeiten lassen sich gut in einem Termin verbinden. Wir stimmen die Reihenfolge der Arbeiten für Sie ab."),
    ("Reparieren Sie auch Kratzer und kleine Lackschäden?", "Ja. Oberflächliche Kratzer entfernen wir mit einer Politur. Tiefere Schäden beheben wir per Smart Repair oder Lackierung – alles im selben Betrieb."),
    ("Bekomme ich einen Ersatzwagen?", "Auf Wunsch ja – nach Verfügbarkeit. Sagen Sie bei der Terminvergabe Bescheid, dann reservieren wir einen Ersatzwagen für die Dauer der Arbeiten."),
    ("Aus welchen Orten kommen Ihre Kunden?", "Unser Betrieb liegt in Leichlingen. Viele Kunden kommen auch aus Langenfeld, Leverkusen, Solingen und Burscheid."),
]


# ---------------------------------------------------------------- Bausteine
def amp(t):
    return t.replace("&", "&amp;")


def img(name, alt, lazy=True):
    l = ' loading="lazy"' if lazy else ' fetchpriority="high"'
    return f'<img src="assets/img/{name}.webp" alt="{alt}"{l} width="1536" height="1024">'


def head(title, desc, page, extra=""):
    return f'''<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#07162d">
<meta name="format-detection" content="telephone=no">
<meta property="og:type" content="website">
<meta property="og:locale" content="de_DE">
<meta property="og:site_name" content="{FIRMA}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="assets/img/fahrzeug-komplett.webp">
<link rel="icon" type="image/png" href="assets/img/favicon.png">
<link rel="preload" href="assets/fonts/barlow-400.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fonts/barlow-700.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/css/style.css">
<script>document.documentElement.className='js';</script>
<!-- Google Ads / Google Tag: Tag-ID hier eintragen und Block aktivieren (Einwilligung beachten).
<script async src="https://www.googletagmanager.com/gtag/js?id=AW-XXXXXXXXXX"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','AW-XXXXXXXXXX');</script>
-->
{extra}</head>
<body data-page="{page}">
<a class="skip" href="#inhalt">Zum Inhalt springen</a>
'''


def header(page):
    def cur(p):
        return ' aria-current="page"' if p == page else ""
    subs = "".join(f'<li><a href="{s["slug"]}.html"{cur(s["slug"])}>{amp(s["nav"])}</a></li>' for s in SERVICES)
    return f'''<div class="topbar">
  <div class="container">
    <div class="topbar__left">
      <span>{ICO["pin"]}{STRASSE}, {ORT}</span>
      <span>{ICO["clock"]}Termine nach Vereinbarung</span>
    </div>
    <a href="mailto:{MAIL}" data-track="email_click">{ICO["mail"]}{MAIL}</a>
  </div>
</div>
<header class="header" id="header">
  <div class="container header__inner">
    <a class="brand" href="index.html" aria-label="{FIRMA} – Startseite">
      <img src="assets/img/emblem-light.png" alt="" width="680" height="357">
      <span class="brand__text"><strong>{FIRMA}</strong><small>Aufbereitung &amp; Lackierung</small></span>
    </a>
    <nav class="nav" id="nav" aria-label="Hauptnavigation">
      <ul>
        <li class="has-sub"><a href="leistungen.html"{cur("leistungen")}>Leistungen</a>
          <ul class="sub">{subs}</ul>
        </li>
        <li><a href="lackierung.html">Lackierung</a></li>
        <li><a href="ueber-uns.html"{cur("ueber-uns")}>Über uns</a></li>
        <li><a href="kontakt.html"{cur("kontakt")}>Kontakt &amp; Anfahrt</a></li>
      </ul>
    </nav>
    <div class="header__cta">
      <a class="header__phone" href="{TEL_HREF}" data-track="phone_click" aria-label="Anrufen: {TEL}">
        {ICO["phone"]}
        <span><small>Rufen Sie uns an</small><strong>{TEL}</strong></span>
      </a>
      <a class="btn btn--red" href="#anfrage">Angebot anfragen</a>
      <button class="burger" id="burger" aria-label="Menü öffnen" aria-expanded="false" aria-controls="nav"><span></span><span></span><span></span></button>
    </div>
  </div>
</header>
<main id="inhalt">
'''


def form(preselect="", title="Kostenloses Angebot anfordern", sub="In 1 Minute ausgefüllt – wir melden uns bei Ihnen.", flat=False, full=False, fid="anfrage"):
    opts = "".join(f'<option{" selected" if s["option"] == preselect else ""}>{amp(s["option"])}</option>' for s in SERVICES)
    more = ""
    if full:
        more = '''<label>E-Mail (optional)<input type="email" name="email" autocomplete="email" inputmode="email"></label>
    <label>Ihre Nachricht (optional)<textarea name="nachricht" rows="3" placeholder="Fahrzeug, Zustand, Wunschtermin …"></textarea></label>'''
    else:
        more = '<input type="hidden" name="email" value=""><input type="hidden" name="nachricht" value="">'
    return f'''<div class="formcard{" formcard--flat" if flat else ""}" id="{fid}">
  <h2 class="formcard__title">{title}</h2>
  <p class="formcard__sub">{sub}</p>
  <form class="form js-form" action="/api/send" method="post" novalidate>
    <label>Name *<input type="text" name="name" autocomplete="name" required></label>
    <label>Telefon *<input type="tel" name="telefon" autocomplete="tel" inputmode="tel" required></label>
    <label>Gewünschte Leistung
      <select name="leistung"><option value="">Bitte auswählen</option>{opts}<option>Sonstiges</option></select>
    </label>
    {more}
    <label class="form__hp" aria-hidden="true">Website<input type="text" name="website" tabindex="-1" autocomplete="off"></label>
    <label class="form__check"><input type="checkbox" name="datenschutz" required><span>Ich habe die <a href="datenschutz.html">Datenschutzerklärung</a> gelesen und stimme der Verarbeitung meiner Angaben zur Bearbeitung der Anfrage zu.</span></label>
    <p class="form__msg" role="status" aria-live="polite"></p>
    <button class="btn btn--red btn--block" type="submit">Anfrage senden {ARROW}</button>
    <p class="form__note">{ICO["lock"]}Kostenlos und unverbindlich</p>
  </form>
</div>'''


def hero(h1, lead, media, formhtml, crumbs=None, sub=False, flat=False):
    top = f'<p class="hero__place">{ICO["pin"]}{STRASSE} · {ORT}</p>'
    return f'''<section class="hero{" hero--sub" if sub else ""}{" hero--flat" if flat else ""}">
  <div class="hero__media" aria-hidden="true">{media}</div>
  <div class="container hero__inner">
    <div>
      {top}
      <h1>{h1}</h1>
      <p class="lead">{lead}</p>
      <div class="hero__btns">
        <a class="btn btn--red" href="{TEL_HREF}" data-track="phone_click">{ICO["phone"]}{TEL}</a>
        <a class="btn btn--white" href="#anfrage">Angebot anfragen {ARROW}</a>
      </div>
      <ul class="hero__facts">
        <li>{ICO["check"]}Angebot vor Arbeitsbeginn</li>
        <li>{ICO["check"]}Sorgfältige Handarbeit</li>
        <li>{ICO["check"]}Termin nach Absprache</li>
      </ul>
    </div>
    {formhtml}
  </div>
</section>'''


def benefits(inline=False):
    cards = "".join(f'''<li class="benefit rv" style="--d:{i * .09:.2f}s">
        {PIC[k]}
        <h3>{amp(t)}</h3>
        <p>{p}</p>
      </li>''' for i, (k, t, p) in enumerate(BENEFITS))
    if inline:
        return f'''<section class="sec">
  <div class="container">
    <div class="sec__head rv"><span class="kicker">Ihre Vorteile</span><h2>Darauf können Sie sich verlassen</h2></div>
    <ul class="benefits__grid benefits__grid--inline">{cards}</ul>
  </div>
</section>'''
    return f'''<section class="benefits" aria-label="Ihre Vorteile">
  <div class="container">
    <ul class="benefits__grid">{cards}</ul>
  </div>
</section>'''


def svc_cards(items=None):
    items = items or SERVICES
    out = '<div class="cards cards--5">' if len(items) > 8 else '<div class="cards">'
    for i, s in enumerate(items):
        pts = "".join(f"<li>{p}</li>" for p in s["pts"])
        out += f'''<a class="card rv" style="--d:{(i % 4) * .08:.2f}s" href="{s["slug"]}.html">
  <div class="card__img">{img(s["img"], s["img_alt"])}</div>
  <div class="card__body">
    <h3>{s["card"]}</h3>
    <ul>{pts}</ul>
    <span class="card__more">Zur Leistung {ARROW}</span>
  </div>
</a>'''
    return out + '</div>\n<p class="swipe">Wischen für weitere Leistungen →</p>'


def flow(cls="sec"):
    return f'''<section class="{cls}">
  <div class="container">
    <div class="sec__head rv">
      <span class="kicker">Ablauf</span>
      <h2>In vier Schritten zum gepflegten Fahrzeug</h2>
    </div>
    <ol class="flow js-in">
      <li class="rv"><h3>Anfrage senden</h3><p>Per Formular, Anruf oder E-Mail – so, wie es für Sie am einfachsten ist.</p></li>
      <li class="rv" style="--d:.12s"><h3>Angebot erhalten</h3><p>Wir besprechen den Zustand und nennen Ihnen Umfang und Preis.</p></li>
      <li class="rv" style="--d:.24s"><h3>Fahrzeug abgeben</h3><p>Zum vereinbarten Termin kümmern wir uns sorgfältig um Ihr Auto.</p></li>
      <li class="rv" style="--d:.36s"><h3>Abholen</h3><p>Sie nehmen Ihr Fahrzeug sauber und gepflegt wieder entgegen.</p></li>
    </ol>
  </div>
</section>'''


def faq(items):
    out = '<div class="faq">'
    for i, (q, a) in enumerate(items):
        out += f'<details{" open" if i == 0 else ""}><summary>{q}</summary><p>{a}</p></details>'
    return out + "</div>"


def contact_list():
    return f'''<ul class="contact__list">
  <li>{ICO["phone"]}<div><small>Telefon</small><a href="{TEL_HREF}" data-track="phone_click">{TEL}</a></div></li>
  <li>{ICO["mail"]}<div><small>E-Mail</small><a href="mailto:{MAIL}" data-track="email_click">{MAIL}</a></div></li>
  <li>{ICO["pin"]}<div><small>Adresse</small><a href="{MAPS}" target="_blank" rel="noopener">{STRASSE}, {ORT}</a></div></li>
  <li>{ICO["clock"]}<div><small>Termine</small><b>Nach Vereinbarung</b></div></li>
</ul>'''


def final(preselect="", fid="anfrage-unten"):
    return f'''<section class="final">
  {img("ruecklicht", "")}
  <div class="container">
    <div class="rv rv-l">
      <span class="kicker">Kontakt</span>
      <h2>Jetzt unverbindlich anfragen</h2>
      <p class="lead">Schildern Sie uns kurz, worum es geht. Wir melden uns mit einem Angebot und einem Terminvorschlag.</p>
      {contact_list()}
    </div>
    <div class="rv rv-r">{form(preselect=preselect, title="Ihre Anfrage", sub="Je genauer die Angaben, desto schneller das Angebot.", flat=True, full=True, fid=fid)}</div>
  </div>
</section>'''


def footer(bar_href="#anfrage"):
    l1 = "".join(f'<li><a href="{s["slug"]}.html">{s["card"]}</a></li>' for s in SERVICES)
    return f'''</main>
<footer class="footer">
  <div class="container footer__top">
    <div>
      <a class="footer__brand" href="index.html">
        <img src="assets/img/emblem.png" alt="" width="680" height="357" loading="lazy">
        <span><strong>{FIRMA}</strong><small>Aufbereitung &amp; Lackierung</small></span>
      </a>
      <p class="footer__about">Fahrzeugaufbereitung und Lackierung in Leichlingen – sorgfältig von Hand, mit Angebot vor Arbeitsbeginn.</p>
    </div>
    <div>
      <h4>Leistungen</h4>
      <ul>{l1}</ul>
    </div>
    <div>
      <h4>Betrieb</h4>
      <ul>
        <li><a href="leistungen.html">Alle Leistungen</a></li>
        <li><a href="ueber-uns.html">Über uns</a></li>
        <li><a href="kontakt.html">Kontakt &amp; Anfahrt</a></li>
        <li><a href="impressum.html">Impressum</a></li>
        <li><a href="datenschutz.html">Datenschutz</a></li>
      </ul>
    </div>
    <div>
      <h4>Kontakt</h4>
      <ul>
        <li>{STRASSE}<br>{ORT}</li>
        <li><a href="{TEL_HREF}" data-track="phone_click">{TEL}</a></li>
        <li><a href="mailto:{MAIL}" data-track="email_click">{MAIL}</a></li>
        <li>Termine nach Vereinbarung</li>
      </ul>
    </div>
  </div>
  <div class="footer__bottom">
    <div class="container">
      <span>© <span class="js-year">2026</span> {FIRMA}</span>
      <span><a href="impressum.html">Impressum</a><a href="datenschutz.html">Datenschutz</a></span>
    </div>
  </div>
</footer>
<div class="mobilebar">
  <a href="{TEL_HREF}" data-track="phone_click">{ICO["phone"]}Anrufen</a>
  <a href="{bar_href}">Angebot anfragen</a>
</div>
<script src="assets/js/main.js" defer></script>
</body>
</html>
'''


def write(name, html):
    with open(os.path.join(ROOT, name), "w", encoding="utf-8", newline="\n") as f:
        f.write(html)
    print("geschrieben:", name)


# ---------------------------------------------------------------- Startseite
def build_home():
    ld = json.dumps({
        "@context": "https://schema.org", "@type": "AutoBodyShop", "name": FIRMA,
        "description": "Fahrzeugaufbereitung und Lackierung in Leichlingen",
        "telephone": "+491777804146", "email": MAIL,
        "address": {"@type": "PostalAddress", "streetAddress": STRASSE, "postalCode": "42799", "addressLocality": "Leichlingen", "addressCountry": "DE"},
        "areaServed": ["Leichlingen", "Langenfeld", "Leverkusen", "Solingen", "Burscheid"],
    }, ensure_ascii=False, indent=1)
    extra = f'<link rel="preload" href="assets/img/hero-poster.webp" as="image">\n<script type="application/ld+json">\n{ld}\n</script>\n'
    h = head("Autoaufbereitung &amp; Lackierung in Leichlingen | Autopflege Leichlingen",
             "Autopflege Leichlingen: Autoaufbereitung, Lackierung, Unfallschadenabwicklung und Gutachten in 42799 Leichlingen – auf Wunsch mit Ersatzwagen. Jetzt kostenloses Angebot anfragen: 0177 / 780 41 46.",
             "home", extra)
    h += header("home")
    video = '<video id="heroVideo" autoplay muted loop playsinline preload="metadata" poster="assets/img/hero-poster.webp"><source src="assets/video/hero.mp4" type="video/mp4"></video>'
    h += hero("Autoaufbereitung &amp; Lackierung <em>in Leichlingen</em>",
              "Aufbereitung, Lackpolitur und Lackierung – dazu Gutachten, Unfallschadenabwicklung und Ersatzwagen. Alles aus einer Hand.",
              video, form())
    h += benefits()
    h += f'''
<section class="sec" id="leistungen">
  <div class="container">
    <div class="sec__head sec__head--row rv">
      <div>
        <span class="kicker">Leistungen</span>
        <h2>Was wir für Ihr Fahrzeug tun können</h2>
        <p>Wählen Sie die passende Leistung – oder schildern Sie uns den Zustand und wir empfehlen Ihnen, was sinnvoll ist.</p>
      </div>
      <a class="btn btn--line" href="leistungen.html">Alle Leistungen {ARROW}</a>
    </div>
    {svc_cards()}
  </div>
</section>

<section class="sec sec--navy">
  <div class="container two">
    <div class="photo rv rv-l">{img("lackierung", "Lackierer trägt Klarlack auf einen Kotflügel auf")}</div>
    <div class="rv rv-r">
      <span class="kicker">Lackierung &amp; Unfallschaden</span>
      <h2>Lackschäden beheben, ohne dass man es später sieht</h2>
      <p class="lead">Parkrempler, verkratzter Stoßfänger oder Steinschlag: Kleine Schäden reparieren wir punktuell, größere Flächen lackieren wir fachgerecht neu.</p>
      <ul class="checks">
        <li>Teil- und Ganzlackierung</li>
        <li>Punktuelle Reparatur kleiner Schäden</li>
        <li>Farbton direkt am Fahrzeug abgestimmt</li>
        <li>Gutachten und Unfallschadenabwicklung aus einer Hand</li>
      </ul>
      <div class="btns">
        <a class="btn btn--red" href="lackierung.html">Zur Lackierung {ARROW}</a>
        <a class="btn btn--white" href="unfallschadenabwicklung.html">Unfallschaden</a>
      </div>
    </div>
  </div>
</section>

<section class="sec sec--soft">
  <div class="container">
    <div class="sec__head sec__head--center rv">
      <span class="kicker">Der Unterschied</span>
      <h2>Waschstraße oder Aufbereitung von Hand?</h2>
      <p>Eine Waschstraße macht das Auto sauber. Eine Aufbereitung bringt es wieder in Form.</p>
    </div>
    <div class="versus">
      <div class="versus__col rv rv-l">
        <h3>Waschstraße</h3>
        <ul>
          <li>Bürsten können feine Kratzer im Lack hinterlassen</li>
          <li>Der Innenraum bleibt außen vor</li>
          <li>Türfalze, Felgenbetten und Radkästen bleiben schmutzig</li>
          <li>Kratzer und matte Stellen bleiben, wie sie sind</li>
          <li>Keine Beratung zum Zustand Ihres Fahrzeugs</li>
        </ul>
      </div>
      <div class="versus__col versus__col--us rv rv-r">
        <h3>{FIRMA}</h3>
        <ul>
          <li>Schonende Handwäsche mit passenden Pflegemitteln</li>
          <li>Innenraum gründlich gereinigt – Polster, Leder, Teppiche</li>
          <li>Auch die Stellen, an die keine Anlage herankommt</li>
          <li>Politur, Smart Repair und Lackierung im selben Betrieb</li>
          <li>Persönliche Einschätzung direkt am Fahrzeug</li>
        </ul>
      </div>
    </div>
  </div>
</section>

{flow()}

<section class="sec sec--soft">
  <div class="container two">
    <div class="rv rv-l">
      <span class="kicker">Über uns</span>
      <h2>Ihr Betrieb für Autopflege in Leichlingen</h2>
      <p class="lead">Bei uns landet Ihr Auto nicht in einer Warteschlange, sondern bei jemandem, der sich Zeit dafür nimmt.</p>
      <p>Wir schauen uns jedes Fahrzeug vorab an, besprechen mit Ihnen, was sinnvoll ist, und arbeiten dann Schritt für Schritt – vom Innenraum über den Lack bis zum letzten Detail.</p>
      <ul class="chips" aria-label="Einzugsgebiet"><li>Leichlingen</li><li>Langenfeld</li><li>Leverkusen</li><li>Solingen</li><li>Burscheid</li></ul>
      <div class="btns">
        <a class="btn btn--navy" href="ueber-uns.html">Mehr über uns {ARROW}</a>
        <a class="btn btn--line" href="kontakt.html">Anfahrt</a>
      </div>
    </div>
    <div class="photo rv rv-r">{img("werkstatt", "Aufbereitung eines Fahrzeugs in der Werkstatt")}</div>
  </div>
</section>

<section class="sec">
  <div class="container two two--top">
    <div class="rv">
      <span class="kicker">Häufige Fragen</span>
      <h2>Gut zu wissen, bevor Sie anfragen</h2>
      <p class="lead">Ihre Frage ist nicht dabei? Rufen Sie einfach an.</p>
      <div class="btns"><a class="btn btn--navy" href="{TEL_HREF}" data-track="phone_click">{ICO["phone"]}{TEL}</a></div>
    </div>
    <div class="rv" style="--d:.1s">{faq(HOME_FAQ)}</div>
  </div>
</section>

{final()}
'''
    h += footer()
    write("index.html", h)


# ---------------------------------------------------------------- Leistungsseiten
PICK = {"autoaufbereitung": ["innenraumreinigung", "lackpolitur", "lackierung", "leasingrueckgabe"],
        "innenraumreinigung": ["autoaufbereitung", "lackpolitur", "leasingrueckgabe", "lackierung"],
        "lackpolitur": ["lackierung", "autoaufbereitung", "innenraumreinigung", "leasingrueckgabe"],
        "lackierung": ["unfallschadenabwicklung", "lackpolitur", "gutachten", "leasingrueckgabe"],
        "unfallschadenabwicklung": ["gutachten", "ersatzwagen", "lackierung", "autoaufbereitung"],
        "gutachten": ["unfallschadenabwicklung", "ersatzwagen", "lackierung", "lackpolitur"],
        "ersatzwagen": ["unfallschadenabwicklung", "gutachten", "lackierung", "autoaufbereitung"],
        "leasingrueckgabe": ["lackierung", "lackpolitur", "innenraumreinigung", "autoaufbereitung"]}


def build_service(s):
    others = [o for p in PICK[s["slug"]] for o in SERVICES if o["slug"] == p]
    h = head(amp(s["title"]) + " | " + FIRMA, s["desc"], s["slug"], f'<link rel="preload" href="assets/img/{s["img"]}.webp" as="image">\n')
    h += header(s["slug"])
    h += hero(amp(s["h1"]).replace(" in Leichlingen", " <em>in Leichlingen</em>"), s["lead"], img(s["img"], "", lazy=False),
              form(preselect=s["option"], title="Angebot anfragen"),
              sub=True, flat=True)
    h += f'''
<section class="sec">
  <div class="container">
    <div class="sec__head rv">
      <span class="kicker">Leistungsumfang</span>
      <h2>Das gehört {"zum" if s["slug"] in ("ersatzwagen", "gutachten") else "zur"} {s["card"]}</h2>
    </div>
    <ul class="incl">{"".join(f'<li class="rv" style="--d:{(i % 3) * .08:.2f}s"><span class="incl__ico">{inc_icon(x)}</span>{x}</li>' for i, x in enumerate(s["inc"]))}</ul>
  </div>
</section>

<section class="sec sec--soft">
  <div class="container two">
    <div class="rv rv-l">
      <span class="kicker">{s["card"]}</span>
      <h2>{s["h2a"]}</h2>
      {"".join(f"<p>{p}</p>" for p in s["pa"])}
      <div class="btns">
        <a class="btn btn--red" href="#anfrage">Angebot anfragen {ARROW}</a>
        <a class="btn btn--line" href="{TEL_HREF}" data-track="phone_click">{ICO["phone"]}{TEL}</a>
      </div>
    </div>
    <div class="photo rv rv-r">{img(s["img2"], s["img2_alt"])}</div>
  </div>
</section>

{benefits(inline=True)}

{flow("sec sec--soft")}

<section class="sec">
  <div class="container two two--top">
    <div class="rv">
      <span class="kicker">Gut zu wissen</span>
      <h2>{s["h2b"]}</h2>
      {"".join(f'<p class="lead">{p}</p>' for p in s["pb"])}
      <div class="btns"><a class="btn btn--navy" href="#anfrage">Jetzt anfragen {ARROW}</a></div>
    </div>
    <div class="rv" style="--d:.1s">{faq(s["faq"] + [q for q in MORE_FAQ if q[0] not in [x[0] for x in s["faq"]]])}</div>
  </div>
</section>

<section class="sec sec--soft">
  <div class="container">
    <div class="sec__head sec__head--row rv">
      <div><span class="kicker">Passt dazu</span><h2>Weitere Leistungen</h2></div>
      <a class="btn btn--line" href="leistungen.html">Alle Leistungen {ARROW}</a>
    </div>
    {svc_cards(others)}
  </div>
</section>

{final(preselect=s["option"])}
'''
    h += footer()
    write(s["slug"] + ".html", h)


# ---------------------------------------------------------------- Übersicht, Über uns, Kontakt
def build_leistungen():
    h = head("Leistungen: Aufbereitung &amp; Lackierung in Leichlingen | " + FIRMA,
             "Alle Leistungen von Autopflege Leichlingen: Autoaufbereitung, Innenraumreinigung, Lackpolitur, Lackierung, Unfallschadenabwicklung, Gutachten, Ersatzwagen und Leasingrückgabe.", "leistungen")
    h += header("leistungen")
    h += hero("Unsere Leistungen <em>in Leichlingen</em>", "Aufbereitung und Lackierung aus einer Hand. Wählen Sie eine Leistung für mehr Details – oder fragen Sie direkt ein Angebot an.",
              img("lackpolitur", "", lazy=False), form(), sub=True)
    h += benefits()
    h += f'''
<section class="sec">
  <div class="container">
    <div class="sec__head rv"><span class="kicker">Übersicht</span><h2>Alle Leistungen im Überblick</h2></div>
    {svc_cards()}
  </div>
</section>
{flow("sec sec--soft")}
{final()}
'''
    h += footer()
    write("leistungen.html", h)


def build_about():
    h = head("Über uns | " + FIRMA + " – Aufbereitung &amp; Lackierung",
             "Autopflege Leichlingen: Ihr Betrieb für Fahrzeugaufbereitung und Lackierung in der Walter-Frese-Str. 16, 42799 Leichlingen. Lernen Sie uns kennen.", "ueber-uns")
    h += header("ueber-uns")
    h += hero("Über Autopflege Leichlingen", "Fahrzeugaufbereitung und Lackierung direkt vor Ort – persönlich, sorgfältig und mit festen Absprachen.",
              img("werkstatt", "", lazy=False), form(), sub=True)
    h += benefits()
    h += f'''
<section class="sec">
  <div class="container two">
    <div class="rv rv-l">
      <span class="kicker">Unser Betrieb</span>
      <h2>Zeit fürs Fahrzeug statt Fließband</h2>
      <p class="lead">Wir konzentrieren uns auf zwei Dinge: Fahrzeuge gründlich aufbereiten und Lackschäden sauber beheben.</p>
      <p>Bei uns landet Ihr Auto nicht in einer Warteschlange. Wir schauen uns jedes Fahrzeug vorab an, besprechen mit Ihnen, was sinnvoll ist, und nennen Ihnen den Preis, bevor wir anfangen.</p>
      <p>Weil Aufbereitung und Lackierung bei uns unter einem Dach stattfinden, müssen Sie für eine Politur, eine Kratzerreparatur und eine Innenreinigung nicht drei verschiedene Betriebe anfahren.</p>
      <ul class="chips" aria-label="Einzugsgebiet"><li>Leichlingen</li><li>Langenfeld</li><li>Leverkusen</li><li>Solingen</li><li>Burscheid</li></ul>
      <div class="btns">
        <a class="btn btn--red" href="#anfrage">Angebot anfragen {ARROW}</a>
        <a class="btn btn--line" href="leistungen.html">Unsere Leistungen</a>
      </div>
    </div>
    <div class="photo rv rv-r">{img("fahrzeug-komplett", "Aufbereitetes Fahrzeug in der Halle")}</div>
  </div>
</section>
{flow("sec sec--soft")}
{final()}
'''
    h += footer()
    write("ueber-uns.html", h)


def build_contact():
    h = head("Kontakt &amp; Anfahrt | " + FIRMA,
             "Kontakt zu Autopflege Leichlingen: Walter-Frese-Str. 16, 42799 Leichlingen, Telefon 0177 / 780 41 46. Jetzt Termin oder Angebot anfragen.", "kontakt")
    h += header("kontakt")
    h += hero("Kontakt &amp; Anfahrt", "Rufen Sie an oder schreiben Sie uns. Je genauer Sie Fahrzeug und Wunsch beschreiben, desto schneller können wir Ihnen ein Angebot machen.",
              img("fahrzeug-komplett", "", lazy=False), form(), sub=True)
    h += benefits()
    h += f'''
<section class="sec">
  <div class="container contact">
    <div class="rv rv-l">
      <span class="kicker">So erreichen Sie uns</span>
      <h2>{STRASSE}, {ORT}</h2>
      {contact_list()}
      <div class="btns"><a class="btn btn--navy" href="{MAPS}" target="_blank" rel="noopener">{ICO["pin"]}Route planen</a></div>
    </div>
    <div class="rv rv-r">
      <div class="map" id="map" data-src="https://www.google.com/maps?q=Walter-Frese-Str.+16,+42799+Leichlingen&amp;output=embed">
        <div>
          <p><b>{STRASSE}, {ORT}</b><br>Beim Laden der Karte werden Daten an Google übertragen.</p>
          <button class="btn btn--line" type="button" id="mapLoad">Karte anzeigen</button>
        </div>
      </div>
    </div>
  </div>
</section>
{final()}
'''
    h += footer()
    write("kontakt.html", h)


def build_simple():
    def plain(title, desc, page, body):
        h = head(title + " | " + FIRMA, desc, page, '<meta name="robots" content="noindex">\n')
        h += header(page)
        h += f'<section class="sec"><div class="container legal">\n{body}\n</div></section>\n'
        h += footer("kontakt.html#anfrage")
        write(page + ".html", h)

    plain("Vielen Dank für Ihre Anfrage", "Ihre Anfrage ist bei uns eingegangen.", "danke", f'''<h1>Vielen Dank für Ihre Anfrage</h1>
<p class="lead" style="margin-top:18px">Ihre Nachricht ist bei uns eingegangen. Wir melden uns schnellstmöglich bei Ihnen.</p>
<p>Wenn es eilt, erreichen Sie uns telefonisch unter <a href="{TEL_HREF}" data-track="phone_click"><b>{TEL}</b></a>.</p>
<div class="btns"><a class="btn btn--navy" href="index.html">Zur Startseite</a><a class="btn btn--line" href="leistungen.html">Leistungen ansehen</a></div>
<script>window.dataLayer=window.dataLayer||[];window.dataLayer.push({{event:'lead_form_success'}});</script>''')

    plain("Impressum", "Impressum von Autopflege Leichlingen – Christoph Widerynski e. K.", "impressum", f'''<h1>Impressum</h1>
<h2>Angaben gemäß § 5 DDG</h2>
<p>Christoph Widerynski e. K.<br>{FIRMA}<br>{STRASSE}<br>{ORT}</p>
<p>Inhaber: Christoph Widerynski</p>
<h2>Kontakt</h2>
<p>Telefon: <a href="{TEL_HREF}">{TEL}</a><br>E-Mail: <a href="mailto:{MAIL}">{MAIL}</a></p>
<h2>Registereintrag</h2>
<p class="todo">Eintragung im Handelsregister. Registergericht: [Amtsgericht eintragen] · Registernummer: HRA [Nummer eintragen]</p>
<h2>Umsatzsteuer-Identifikationsnummer</h2>
<p>Umsatzsteuer-Identifikationsnummer gemäß § 27a Umsatzsteuergesetz: DE256197693</p>
<h2>Verantwortlich für den Inhalt</h2>
<p>Christoph Widerynski, Anschrift wie oben</p>
<h2>Verbraucherstreitbeilegung</h2>
<p>Wir sind nicht bereit und nicht verpflichtet, an Streitbeilegungsverfahren vor einer Verbraucherschlichtungsstelle teilzunehmen.</p>
<h2>Haftung für Inhalte und Links</h2>
<p>Die Inhalte dieser Website wurden mit Sorgfalt erstellt. Für die Richtigkeit, Vollständigkeit und Aktualität können wir jedoch keine Gewähr übernehmen. Für Inhalte externer Websites, auf die wir verlinken, sind ausschließlich deren Betreiber verantwortlich.</p>
<h2>Bildnachweise</h2>
<p>Video und Fotos teilweise von Freepik (lizenziert). Einzelne Abbildungen wurden mit KI-Unterstützung erstellt und dienen der Veranschaulichung.</p>''')

    plain("Datenschutz", "Datenschutzerklärung von Autopflege Leichlingen.", "datenschutz", f'''<h1>Datenschutzerklärung</h1>
<p class="lead" style="margin-top:18px">Der Schutz Ihrer persönlichen Daten ist uns wichtig. Nachfolgend informieren wir Sie darüber, welche Daten beim Besuch dieser Website verarbeitet werden.</p>

<h2>1. Verantwortlicher</h2>
<p>Christoph Widerynski e. K.<br>{FIRMA}<br>{STRASSE}, {ORT}<br>Telefon: <a href="{TEL_HREF}">{TEL}</a><br>E-Mail: <a href="mailto:{MAIL}">{MAIL}</a></p>

<h2>2. Hosting durch Vercel</h2>
<p>Diese Website wird bei Vercel Inc., 440 N Barranca Ave #4133, Covina, CA 91723, USA gehostet. Beim Aufruf der Website verarbeitet Vercel technisch notwendige Daten, insbesondere Ihre IP-Adresse, Datum und Uhrzeit des Zugriffs, die aufgerufene Seite, den Referrer sowie Angaben zu Browser und Betriebssystem (Server-Logfiles). Diese Daten sind erforderlich, um die Website sicher und stabil auszuliefern.</p>
<p>Rechtsgrundlage ist unser berechtigtes Interesse an einer sicheren und funktionsfähigen Bereitstellung der Website (Art. 6 Abs. 1 lit. f DSGVO). Mit Vercel besteht ein Vertrag zur Auftragsverarbeitung (Art. 28 DSGVO). Vercel ist unter dem EU-U.S. Data Privacy Framework zertifiziert; die Übermittlung in die USA erfolgt auf Grundlage des Angemessenheitsbeschlusses der EU-Kommission (Art. 45 DSGVO) bzw. der EU-Standardvertragsklauseln. Weitere Informationen: <a href="https://vercel.com/legal/privacy-policy" target="_blank" rel="noopener">vercel.com/legal/privacy-policy</a>.</p>

<h2>3. Anfrageformular und E-Mail-Versand über Resend</h2>
<p>Wenn Sie uns über das Anfrageformular kontaktieren, verarbeiten wir die von Ihnen eingegebenen Daten (Name, Telefonnummer, optional E-Mail-Adresse, gewünschte Leistung und Ihre Nachricht), um Ihre Anfrage zu bearbeiten und Ihnen ein Angebot zu erstellen. Pflichtfelder sind als solche gekennzeichnet.</p>
<p>Die Anfrage wird uns per E-Mail über den Dienst Resend (Resend, Inc., 2261 Market Street #5039, San Francisco, CA 94114, USA) zugestellt. Resend verarbeitet die Daten in unserem Auftrag; die Verarbeitung erfolgt über Server in der EU (Region Irland). Mit Resend besteht ein Vertrag zur Auftragsverarbeitung. Soweit dennoch Daten in die USA übermittelt werden, erfolgt dies auf Grundlage der EU-Standardvertragsklauseln bzw. des EU-U.S. Data Privacy Framework.</p>
<p>Rechtsgrundlage ist Art. 6 Abs. 1 lit. b DSGVO (Durchführung vorvertraglicher Maßnahmen) sowie Ihre Einwilligung (Art. 6 Abs. 1 lit. a DSGVO), die Sie mit dem Setzen des Häkchens erteilen und jederzeit widerrufen können. Die Daten werden gelöscht, sobald Ihre Anfrage abschließend bearbeitet ist und keine gesetzlichen Aufbewahrungspflichten entgegenstehen.</p>

<h2>4. Kontakt per E-Mail oder Telefon</h2>
<p>Wenn Sie uns per E-Mail oder Telefon kontaktieren, verarbeiten wir Ihre Angaben ausschließlich zur Bearbeitung Ihres Anliegens (Art. 6 Abs. 1 lit. b DSGVO bzw. lit. f DSGVO). Die Daten werden gelöscht, sobald sie nicht mehr erforderlich sind, sofern keine gesetzlichen Aufbewahrungspflichten bestehen.</p>

<h2>5. Google Maps</h2>
<p>Auf der Kontaktseite können Sie eine Karte von Google Maps (Google Ireland Limited, Gordon House, Barrow Street, Dublin 4, Irland) laden. Die Karte wird erst geladen, wenn Sie auf „Karte anzeigen“ klicken. Erst dann werden Daten wie Ihre IP-Adresse an Google übertragen, ggf. auch in die USA. Rechtsgrundlage ist Ihre Einwilligung durch den Klick (Art. 6 Abs. 1 lit. a DSGVO). Weitere Informationen: <a href="https://policies.google.com/privacy" target="_blank" rel="noopener">policies.google.com/privacy</a>.</p>

<h2>6. Schriften, Bilder und Videos</h2>
<p>Schriftarten, Bilder und Videos werden direkt von unserem Hosting-Anbieter ausgeliefert. Es findet keine Verbindung zu Servern von Google Fonts oder anderen externen Schriftanbietern statt.</p>

<h2>7. Cookies und Analyse</h2>
<p>Diese Website setzt derzeit keine Cookies und verwendet keine Analyse- oder Werbe-Tracking-Dienste. Sollten wir künftig solche Dienste (z. B. Google Ads Conversion-Tracking) einsetzen, holen wir vorher Ihre Einwilligung ein und ergänzen diese Datenschutzerklärung.</p>

<h2>8. Ihre Rechte</h2>
<p>Sie haben jederzeit das Recht auf Auskunft (Art. 15 DSGVO), Berichtigung (Art. 16 DSGVO), Löschung (Art. 17 DSGVO), Einschränkung der Verarbeitung (Art. 18 DSGVO), Datenübertragbarkeit (Art. 20 DSGVO) sowie Widerspruch gegen die Verarbeitung (Art. 21 DSGVO). Eine erteilte Einwilligung können Sie jederzeit mit Wirkung für die Zukunft widerrufen (Art. 7 Abs. 3 DSGVO). Wenden Sie sich dazu einfach an die oben genannten Kontaktdaten.</p>

<h2>9. Beschwerderecht</h2>
<p>Sie haben das Recht, sich bei einer Datenschutz-Aufsichtsbehörde zu beschweren. Zuständig ist die Landesbeauftragte für Datenschutz und Informationsfreiheit Nordrhein-Westfalen, Kavalleriestraße 2–4, 40213 Düsseldorf, <a href="https://www.ldi.nrw.de" target="_blank" rel="noopener">www.ldi.nrw.de</a>.</p>

<h2>10. SSL-/TLS-Verschlüsselung</h2>
<p>Diese Website nutzt aus Sicherheitsgründen eine SSL- bzw. TLS-Verschlüsselung. Eine verschlüsselte Verbindung erkennen Sie an „https://“ in der Adresszeile Ihres Browsers.</p>

<p style="margin-top:32px;color:var(--muted)">Stand: Oktober 2026</p>''')

if __name__ == "__main__":
    build_home()
    for s in SERVICES:
        build_service(s)
    build_leistungen()
    build_about()
    build_contact()
    build_simple()
