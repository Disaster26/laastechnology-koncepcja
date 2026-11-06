# -*- coding: utf-8 -*-
# Generator stron wizualizacji LAAS Technology (PL + EN przez data-en)
# v2 (04.11.2026): kolorystyka i grafiki wg materiałów od prezesa (nocne miasto, granat + błękit/fiolet)
import html, pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
V = 1  # cache-bust
import sys
if len(sys.argv) > 1: V = sys.argv[1]

def e(s): return html.escape(s, quote=True)

def T(tag, pl, en, attrs=''):
    a = (' ' + attrs) if attrs else ''
    return f'<{tag}{a} data-en="{e(en)}">{pl}</{tag}>'

EMAIL = 'marcin.ostrowski@laastechnology.pl'
ARR = '<svg class="ic" aria-hidden="true"><use href="#i-arr"/></svg>'

# grafiki od klienta, WebP w kilku szerokościach: nazwa -> (szerokości, w, h)
IMG = {
    'laas-miasto': ([480, 720, 916], 916, 569),
    'laas-miasto-m': ([480, 700], 700, 554),
    'laas-budynki': ([480, 700], 700, 485),
    'laas-swiatlo': ([480, 746], 746, 520),
    'laas-razem': ([480, 720, 1156], 1156, 495),
    'laas-razem-m': ([480, 750], 750, 495),
    'laas-rozmowa': ([480, 720, 820], 820, 959),
    'laas-hurt': ([480, 960, 1400], 1600, 1067),
}
def srcset(name):
    ws = IMG[name][0]
    return ', '.join(f'img/{name}-{w}.webp {w}w' for w in ws)
def pic(name, alt_pl, alt_en, sizes, lazy=True, attrs=''):
    ws, w, h = IMG[name]
    ld = ' loading="lazy" decoding="async"' if lazy else ' fetchpriority="high"'
    a = (' ' + attrs) if attrs else ''
    return f'<img src="img/{name}-{ws[-1]}.webp" srcset="{srcset(name)}" sizes="{sizes}" alt="{e(alt_pl)}" data-en-alt="{e(alt_en)}" width="{w}" height="{h}"{ld}{a}>'

ALT = {
    'miasto': ('Nocne miasto z podświetlonymi budynkami połączonymi liniami światła - grafika LAAS Technology',
               'Night city with illuminated buildings connected by lines of light - LAAS Technology graphic'),
    'budynki': ('Budynki i ulice nocą połączone siecią świetlnych punktów',
                'Buildings and streets at night linked by a network of light points'),
    'swiatlo': ('Wieżowce i latarnia uliczna nocą, połączone siecią świetlnych punktów',
                'Skyscrapers and a street lamp at night, linked by a network of light points'),
    'razem': ('Uścisk dłoni człowieka i cyfrowej dłoni z punktów światła na tle nocnego miasta',
              'A handshake between a human hand and a digital hand made of light points, against a night city'),
    'rozmowa': ('Dwoje ludzi rozmawia w biurze na tle oświetlonego nocą miasta',
                'Two people talking in an office against a city lit up at night'),
    'hurt': ('Magazyn z regałami pełnymi kartonów z towarem', 'Warehouse with shelves full of boxed goods'),
}

SYMBOLS = '''<svg width="0" height="0" style="position:absolute" aria-hidden="true">
  <symbol id="i-arr" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" d="M5 12h13M13 6l6 6-6 6"/></symbol>
  <symbol id="i-mail" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-width="1.9" stroke-linejoin="round" d="M3.5 5.5h17v13h-17zM3.8 6l8.2 7 8.2-7"/></symbol>
  <symbol id="i-pin" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-width="1.9" d="M12 21s-6.5-6.2-6.5-11.2a6.5 6.5 0 0 1 13 0C18.5 14.8 12 21 12 21Z"/><circle cx="12" cy="9.8" r="2.3" fill="none" stroke="currentColor" stroke-width="1.9"/></symbol>
  <symbol id="i-down" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" d="M6 9l6 6 6-6"/></symbol>
  <symbol id="i-user" viewBox="0 0 24 24"><circle cx="12" cy="8" r="4" fill="none" stroke="currentColor" stroke-width="1.9"/><path d="M4 21c1-4.4 4.2-6.5 8-6.5s7 2.1 8 6.5" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/></symbol>
</svg>'''

OFERTA = [
    ('oferta-energia.html', 'Inteligentne oświetlenie', 'Smart lighting'),
    ('oferta-inwestycje.html', 'Budynki i inwestycje', 'Buildings and projects'),
    ('oferta-hurt.html', 'Sprzedaż hurtowa', 'Wholesale'),
]
NAV = [
    ('index.html', 'Strona główna', 'Home'),
    ('o-nas.html', 'O nas', 'About us'),
    ('oferta.html', 'Oferta', 'Solutions'),
    ('partnerzy.html', 'Partnerzy', 'Partners'),
    ('aktualnosci.html', 'Aktualności', 'News'),
    ('kariera.html', 'Kariera', 'Careers'),
]

def logo(cls='brand'):
    return f'<a class="{cls}" href="index.html" aria-label="LAAS Technology - strona główna"><span class="wm"><b>LAAS</b><span>Technology</span></span></a>'

def header(active):
    items = []
    for href, pl, en in NAV:
        cur = ' aria-current="page"' if href == active or (href == 'oferta.html' and active.startswith('oferta')) else ''
        if href == 'oferta.html':
            sub = ''.join(f'<li><a href="{h}"{" aria-current=\"page\"" if h == active else ""} data-en="{e(se)}">{sp}</a></li>' for h, sp, se in OFERTA)
            items.append(f'<li class="has-sub"><a href="{href}"{cur} data-en="{e(en)}">{pl}</a><button class="sub-t" type="button" aria-label="Rozwiń ofertę" data-en-al="Expand"><svg aria-hidden="true"><use href="#i-down"/></svg></button><ul class="sub">{sub}</ul></li>')
        else:
            items.append(f'<li><a href="{href}"{cur} data-en="{e(en)}">{pl}</a></li>')
    kcur = ' aria-current="page"' if active == 'kontakt.html' else ''
    items.append(f'<li class="nav-k"><a class="btn btn-s" href="kontakt.html"{kcur} data-en="Contact">Kontakt</a></li>')
    return f'''<div class="topbar"><div class="wrap topbar-in">
  <span><svg aria-hidden="true"><use href="#i-pin"/></svg>ul. Jesienna 27, 05-502 Bobrowiec</span>
  <a href="mailto:{EMAIL}"><svg aria-hidden="true"><use href="#i-mail"/></svg>{EMAIL}</a>
</div></div>
<header class="top" id="top">
  <div class="wrap top-in">
    {logo()}
    <nav class="nav" id="nav" aria-label="Menu główne"><ul>{''.join(items)}</ul></nav>
    <div class="lang" role="group" aria-label="Język / Language"><button type="button" data-l="pl" aria-pressed="true">PL</button><button type="button" data-l="en" aria-pressed="false">EN</button></div>
    <button class="burger" id="burger" type="button" aria-label="Otwórz menu" aria-expanded="false" aria-controls="nav"><span></span><span></span><span></span></button>
  </div>
</header>'''

def footer():
    menu = ''.join(f'<li><a href="{h}" data-en="{e(en)}">{pl}</a></li>' for h, pl, en in NAV[1:]) + '<li><a href="kontakt.html" data-en="Contact">Kontakt</a></li>'
    of = ''.join(f'<li><a href="{h}" data-en="{e(en)}">{pl}</a></li>' for h, pl, en in OFERTA)
    return f'''<footer class="foot">
  <div class="wrap foot-in">
    <div class="foot-a">
      {logo('brand brand-w')}
      {T('p', 'Inteligentne zarządzanie oświetleniem. Rozwiązania szyte na miarę ludzi, przestrzeni i potrzeb.', 'Smart lighting management. Solutions tailored to people, spaces and needs.')}
      <p class="foot-slog">Innowacje | Oszczędności | Efektywność</p>
    </div>
    <div><h2 data-en="Menu">Menu</h2><ul>{menu}</ul></div>
    <div><h2 data-en="Solutions">Oferta</h2><ul>{of}</ul></div>
    <div class="foot-d"><h2 data-en="Company details">Dane firmy</h2>
      <p>LAAS Technology Sp. z o.o.<br>ul. Jesienna 27<br>05-502 Bobrowiec</p>
      <p>NIP 1231593199<br>REGON 543411286<br>KRS 0001208967</p>
      <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
    </div>
  </div>
  <div class="wrap foot-b">
    <span>&copy; 2026 LAAS Technology Sp. z o.o.</span>
    {T('a', 'Polityka prywatności', 'Privacy policy', 'href="#"')}
    <span class="foot-w"><span data-en="Working draft">Wizualizacja robocza</span> · <a class="wylinka-badge" href="https://wylinka.pl/?utm_source=laastechnology.pl&amp;utm_medium=stopka&amp;utm_campaign=wykonanie" rel="noopener" title="Strona wykonana przez Wylinka"><svg viewBox="0 0 64 64" aria-hidden="true" focusable="false" fill="currentColor"><path d="M9.8 22.8l-1.2-7.9 2.2-3.7 15.5 4.6-.5 1.5-7.2 5.5 4.7 15.6 5-15.6 7 0 4.1 12.7-4.2-.9-2.6 1.8-.8-2.2-5.3 15.6-4.3 0 .4 .2-2.1 2.8-1.3-1.1 1.1-1.4-3.1 .2-.1-1.7 2.2-.1-5.7-16.5-4.8 .6-.8 3.1 0 .5-.3 .5 .8 2.2-1.6 .5-.4-1.3-.8 1.6-1.5-.8 .8-1.6-1.4 .6-.6-1.6 2.3-.8 .2-.4 1.3-4.8 5.9-.8-2.4-6.9zM15.2 13.7l-.1-.4-.4 .8-.1 .8 .1 1 .1 .4 .3 .7 .3-.9 .1-.7 0-.8z"/><path class="wy-pod" d="M37.1 49.8l-4.5-13.3 2.6-1.8 4.2 .9 .9 2.8 3-9.7 0-.5 .1-.8 3.2-8.4 .5-1 .6-1 .9-1.1 1.3-1 1.1-.7 1.4-.5 1.4-.3 .7 0 .9 0 1.2 .3 1.4 .6 .8 .5 .7 .7 .6 .7 .5 .9 .3 .9 .1 .9 0 .8-.2 .9-.5 .9-.5 .6-.7 .5-.7 .3-.1-.1 0-.1 .5-.5 .3-.7 .2-.5 0-.6-.1-.6-.3-.7-.4-.5-.4-.4-.5-.3-.6-.3-.7 0-.7 .1-.6 .1-.5 .4-.5 .5-.3 .5-.2 .7-.1 1.5-1.4 5.1-.8 3.3-.3 .7-.5 .7-6 17.5 1.9 .1-.1 1.7-3.1-.2 1.1 1.4-1.3 1.1-2.1-2.8 .4-.2z"/><path class="wy-old" d="M40.8 50l.4-.2-4.1 0-4.2-12.5 2.5-1.7 4.3 .9 .6 1.9 .6-1.6 0-.3 2.4-7.8 0-.5 .1-.8 3.2-8.4 .4-.8 .6-.9 .9-1.2 .9-.9 1.3-.8 1.4-.6 1.2-.3 1.4-.1 1.3 .1 .6 .2 .8 .3 1.1 .6 .9 .7 .7 .9 .5 .9 .3 .9 .1 1.1-.1 .9-.3 .9-.4 .7-.6 .7-.6 .4-.6 .2-.1-.1 0-.1 .5-.5 .3-.7 .2-.5 0-.5-.1-.6-.2-.6-.3-.5-.4-.5-.5-.3-.6-.3-.7-.1-.6 0-.6 .1-.6 .3-.6 .5-.3 .4-.2 .5-.1 .5-.1 1.5-1.4 5.1-.8 3.3-.3 .7-.5 .7-6 17.5 1.9 .1-.1 1.7-3.1-.2 1.1 1.4-1.3 1.1zM49.6 17.1l.6 1.7-1.5 1.9 .4 .4 1.8-2.1-.7-2.1zM48.1 28.3l.5 1.8-1.7 1.8 .4 .4 1.9-2-.6-2.2zM37.9 41.7l1.7-1.5-.4-.4-1.7 1.4zM42.6 38.7l-1.5 2.8 1.1 2-1.3 2.6 .5 .2 1.5-2.8-1.1-2 1.4-2.5z"/></svg><span data-en="design: &lt;b&gt;Wylinka&lt;/b&gt;">wykonanie: <b>Wylinka</b></span></a></span>
  </div>
</footer>'''

FAV = "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 40 40'%3E%3Cdefs%3E%3ClinearGradient id='g' x1='0' x2='1'%3E%3Cstop offset='0' stop-color='%233D8BFF'/%3E%3Cstop offset='1' stop-color='%238C7CFF'/%3E%3C/linearGradient%3E%3C/defs%3E%3Crect width='40' height='40' rx='8' fill='%23050B1C'/%3E%3Cpath d='M12 9v20h16' fill='none' stroke='url(%23g)' stroke-width='4.5' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E"

def page(fname, title_pl, title_en, desc, body, mob=True):
    mobbar = '' if not mob else '<div class="mob" id="mob"><a class="btn" href="kontakt.html" data-en="Send an enquiry">Wyślij zapytanie</a></div>'
    doc = f'''<!doctype html>
<html lang="pl" data-title-pl="{e(title_pl)}" data-title-en="{e(title_en)}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="robots" content="noindex, nofollow">
<title>{e(title_pl)}</title>
<meta name="description" content="{e(desc)}">
<meta name="theme-color" content="#050B1C">
<meta name="color-scheme" content="dark">
<link rel="icon" href="{FAV}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700&family=IBM+Plex+Sans:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css?v={V}">
<script>try{{if((new URLSearchParams(location.search).get('lang')||localStorage.getItem('laas-lang'))==='en')document.documentElement.classList.add('is-en')}}catch(e){{}}</script>
</head>
<body>
<!-- Wizualizacja robocza (koncepcja) strony LAAS Technology Sp. z o.o. Kolorystyka i grafiki wg materiałów przesłanych przez klienta. Treści do potwierdzenia z klientem; nie podajemy niesprawdzonych liczb, marek ani referencji. -->
{SYMBOLS}
{header(fname)}
<main id="main">
{body}
</main>
{footer()}
{mobbar}
<script src="app.js?v={V}"></script>
</body>
</html>
'''
    (ROOT / fname).write_text(doc, encoding='utf-8')

def phead(crumb_pl, crumb_en, h1_pl, h1_en, lead_pl, lead_en, img=None, alt=None, mimg=None, pos=None):
    if img:
        a_pl, a_en = alt
        src_m = f'<source media="(max-width:999px)" srcset="{srcset(mimg)}" sizes="100vw">' if mimg else ''
        st = f' style="--pos:{pos}"' if pos else ''
        ph = f'<figure class="phead-ph"{st}><picture>{src_m}{pic(img, a_pl, a_en, "(max-width:999px) 100vw, 62vw", lazy=False)}</picture></figure>'
        return f'''<section class="phead phead-img">
  {ph}
  <div class="wrap phead-w">
    <p class="crumb"><a href="index.html" data-en="Home">Strona główna</a><span aria-hidden="true">/</span>{T('span', crumb_pl, crumb_en)}</p>
    <div class="phead-g">
      {T('h1', h1_pl, h1_en)}
      {T('p', lead_pl, lead_en, 'class="lead"')}
    </div>
  </div>
</section>'''
    return f'''<section class="phead">
  <div class="wrap">
    <p class="crumb"><a href="index.html" data-en="Home">Strona główna</a><span aria-hidden="true">/</span>{T('span', crumb_pl, crumb_en)}</p>
    <div class="phead-g">
      {T('h1', h1_pl, h1_en)}
      {T('p', lead_pl, lead_en, 'class="lead"')}
    </div>
  </div>
</section>'''

CTA_P_PL = 'Każdy projekt zaczyna się od rozmowy. Opowiedz nam o swoich potrzebach, a wspólnie znajdziemy najlepsze rozwiązanie.'
CTA_P_EN = 'Every project starts with a conversation. Tell us what you need and together we will find the best solution.'
def cta(h_pl='Porozmawiajmy o Twoim projekcie', h_en="Let's talk about your project", p_pl=CTA_P_PL, p_en=CTA_P_EN):
    return f'''<section class="cta">
  <div class="wrap cta-in">
    <div>
      {T('h2', h_pl, h_en)}
      {T('p', p_pl, p_en)}
    </div>
    <div class="person">
      <svg class="person-i" aria-hidden="true"><use href="#i-user"/></svg>
      <div>
        <p class="person-n">Marcin Ostrowski</p>
        <p class="person-r">Project Manager</p>
        <a href="mailto:{EMAIL}">{EMAIL}</a>
      </div>
    </div>
    <a class="btn" href="kontakt.html"><span data-en="Contact form">Formularz kontaktowy</span>{ARR}</a>
  </div>
</section>'''

def todo(pl, en):
    return T('p', pl, en, 'class="todo"')

# ---------------------------------------------------------------- STRONA GŁÓWNA
tiles = [
    ('oferta-energia.html', 'laas-swiatlo', 'swiatlo',
     'Inteligentne oświetlenie', 'Smart lighting',
     'Systemy, które dopasowują światło do ludzi, przestrzeni i potrzeb - z czujnikami, automatyką i analizą danych o zużyciu energii.',
     'Systems that adapt light to people, spaces and needs - with sensors, automation and analysis of energy use.'),
    ('oferta-inwestycje.html', 'laas-budynki', 'budynki',
     'Budynki i inwestycje', 'Buildings and projects',
     'Rozwiązania dla obiektów i całych inwestycji: dobór systemu, integracja z instalacjami budynku i jeden opiekun projektu.',
     'Solutions for buildings and whole projects: system selection, integration with building installations and one project manager.'),
    ('oferta-hurt.html', 'laas-hurt', 'hurt',
     'Sprzedaż hurtowa', 'Wholesale',
     'Elektryczne artykuły i urządzenia dla sklepów, hurtowni i dystrybutorów. Warunki ustalane indywidualnie.',
     'Electrical products and appliances for retailers, wholesalers and distributors. Individually agreed terms.'),
]
tiles_html = ''.join(f'''<article class="tile">
  <a href="{h}" class="tile-ph" tabindex="-1" aria-hidden="true">{pic(img, *ALT[ak], "(max-width:999px) 100vw, 400px")}</a>
  {T('h3', f'<a href="{h}">{tp}</a>', f'<a href="{h}">{te}</a>')}
  {T('p', pp, pe)}
  <a class="more" href="{h}"><span data-en="Details">Szczegóły</span>{ARR}</a>
</article>''' for h, img, ak, tp, te, pp, pe in tiles)

pillars = [
    ('Innowacje', 'Innovation',
     'Łączymy nowoczesne technologie, algorytmy i sztuczną inteligencję. Dane z czujników pokazują, jak naprawdę używana jest przestrzeń, a system dopasowuje do tego światło.',
     'We combine modern technology, algorithms and artificial intelligence. Sensor data shows how a space is really used, and the system adjusts the light to match.'),
    ('Oszczędności', 'Savings',
     'Światło tam, gdzie jest potrzebne, i wtedy, kiedy jest potrzebne. Optymalizacja zużycia energii to niższe koszty utrzymania obiektu przez cały okres pracy instalacji.',
     'Light where it is needed, when it is needed. Optimised energy use means lower running costs for the whole life of the installation.'),
    ('Efektywność', 'Efficiency',
     'Krótka droga od rozmowy do wdrożenia. Jeden opiekun prowadzi projekt od początku do końca, a ustalenia potwierdzamy na piśmie.',
     'A short path from first conversation to deployment. One project manager runs the project from start to finish, and every arrangement is confirmed in writing.'),
]
pillars_html = ''.join(f'<div class="pil">{T("h3", a, b)}{T("p", c, d)}</div>' for a, b, c, d in pillars)

steps = [
    ('Rozmowa.', 'Conversation.', 'Opowiadasz o obiekcie i potrzebach: jaka to przestrzeń, jak jest używana i czego od niej oczekujesz.', 'You tell us about the site and your needs: what kind of space it is, how it is used and what you expect from it.'),
    ('Pomysł.', 'Idea.', 'Proponujemy rozwiązanie dopasowane do miejsca i ludzi - jak garnitur szyty na miarę, a nie z wieszaka.', 'We propose a solution that fits the place and its people - tailored, not off the peg.'),
    ('Rozwiązanie.', 'Solution.', 'Ustalamy zakres i harmonogram, a opiekun projektu pilnuje wdrożenia do końca.', 'We agree the scope and schedule, and the project manager sees the deployment through.'),
    ('Opieka.', 'Support.', 'Ten sam opiekun zostaje z Tobą po uruchomieniu - przy zmianach, rozbudowie i kolejnych obiektach.', 'The same project manager stays with you after launch - for changes, extensions and further sites.'),
]
steps_html = ''.join(f'<li><span class="st">{T("b", a, b)} {T("span", c, d)}</span></li>' for a, b, c, d in steps)

news = [
    ('2025-12-02', '2 grudnia 2025', '2 December 2025',
     'LAAS Technology w Krajowym Rejestrze Sądowym', 'LAAS Technology entered in the National Court Register',
     'Spółka została wpisana do KRS pod numerem 0001208967. Siedziba mieści się w Bobrowcu pod Piasecznem, przy ul. Jesiennej 27.',
     'The company was entered in the National Court Register under number 0001208967. Its registered office is in Bobrowiec near Piaseczno, at ul. Jesienna 27.'),
    ('2026', '2026', '2026',
     'Uruchamiamy stronę internetową', 'Our website goes live',
     'Nowa strona w wersji polskiej i angielskiej: nasze rozwiązania, informacje dla partnerów i bezpośredni kontakt z opiekunem projektu.',
     'A new website in Polish and English: our solutions, information for partners and direct contact with a project manager.'),
]
def news_html(items):
    return ''.join(f'''<article class="news-i">
  <time datetime="{dt}" data-en="{e(de)}">{dp}</time>
  {T('h3', tp, te)}
  {T('p', pp, pe)}
</article>''' for dt, dp, de, tp, te, pp, pe in items)

logos = ''.join('<li data-en="Partner logo">Logo partnera</li>' for _ in range(6))

home = f'''<section class="hero">
  <div class="hero-txt">
    <p class="hero-loc"><svg aria-hidden="true"><use href="#i-pin"/></svg><span>Bobrowiec k. Piaseczna</span></p>
    {T('h1', 'Inteligentne zarządzanie oświetleniem', 'Smart lighting management')}
    {T('p', 'Jesteśmy „krawcami” światła. Łączymy nowoczesne technologie, algorytmy i sztuczną inteligencję, aby dopasować oświetlenie do ludzi, przestrzeni i potrzeb.', 'We are tailors of light. We combine modern technology, algorithms and artificial intelligence to fit lighting to people, spaces and needs.', 'class="lead"')}
    <div class="hero-cta" id="heroCta">
      <a class="btn" href="oferta.html"><span data-en="Our solutions">Poznaj rozwiązania</span>{ARR}</a>
      <a class="btn btn-o" href="kontakt.html" data-en="Contact">Kontakt</a>
    </div>
    <p class="hero-slog">Innowacje <i>|</i> Oszczędności <i>|</i> Efektywność</p>
  </div>
  <figure class="hero-ph">
    <picture>
      <source media="(max-width:999px)" srcset="{srcset('laas-miasto-m')}" sizes="100vw">
      {pic('laas-miasto', *ALT['miasto'], '(max-width:999px) 100vw, 56vw', lazy=False)}
    </picture>
  </figure>
</section>

<section class="sec" id="oferta">
  <div class="wrap">
    <div class="sec-h">
      {T('h2', 'Rozwiązania szyte na miarę', 'Tailor-made solutions')}
      {T('p', 'Trzy obszary, w których możemy pomóc. Każdy z nich prowadzi ten sam opiekun - bez przekazywania sprawy między działami.', 'Three areas where we can help. Each is handled by the same project manager, with no passing between departments.')}
    </div>
    <div class="tiles">{tiles_html}</div>
  </div>
</section>

<section class="sec sec-g">
  <div class="wrap pils">
    <div class="pils-h">
      {T('h2', 'Innowacje, oszczędności, efektywność', 'Innovation, savings, efficiency')}
      {T('p', 'Te trzy słowa podpisujemy pod każdą wiadomością, bo według nich projektujemy rozwiązania i prowadzimy współpracę.', 'We sign every message with these three words, because they guide how we design solutions and work with clients.')}
      <figure class="pils-ph">{pic('laas-razem-m', *ALT['razem'], '(max-width:999px) 100vw, 520px')}</figure>
    </div>
    <div class="pils-l">{pillars_html}</div>
  </div>
</section>

<section class="sec">
  <div class="wrap split">
    <figure class="split-ph split-ph-t">{pic('laas-rozmowa', *ALT['rozmowa'], '(max-width:999px) 100vw, 600px')}</figure>
    <div class="split-t">
      {T('h2', 'Każdy projekt zaczyna się od rozmowy', 'Every project starts with a conversation')}
      <ul class="steps">{steps_html}</ul>
      <a class="more" href="o-nas.html"><span data-en="More about us">Więcej o nas</span>{ARR}</a>
    </div>
  </div>
</section>

<section class="sec sec-t">
  <div class="wrap">
    <div class="sec-h sec-h-row">
      {T('h2', 'Aktualności', 'News')}
      <a class="more" href="aktualnosci.html"><span data-en="All news">Wszystkie wpisy</span>{ARR}</a>
    </div>
    <div class="news">{news_html(news)}</div>
  </div>
</section>

<section class="sec sec-t">
  <div class="wrap">
    <div class="sec-h sec-h-row">
      {T('h2', 'Partnerzy technologiczni', 'Technology partners')}
      <a class="more" href="partnerzy.html"><span data-en="All partners">Wszyscy partnerzy</span>{ARR}</a>
    </div>
    <ul class="logos">{logos}</ul>
    {todo('Do uzupełnienia: logotypy partnerów i producentów, z którymi współpracujemy.', 'To be completed: logos of the partners and manufacturers we work with.')}
  </div>
</section>

{cta('Porozmawiajmy o inteligentnym oświetleniu', "Let's talk about smart lighting")}'''
page('index.html', 'LAAS Technology - inteligentne zarządzanie oświetleniem',
     'LAAS Technology - smart lighting management',
     'LAAS Technology Sp. z o.o., Bobrowiec k. Piaseczna: inteligentne zarządzanie oświetleniem, rozwiązania dla budynków i inwestycji, sprzedaż hurtowa.', home)

# ---------------------------------------------------------------- O NAS
reg = [
    ('Nazwa', 'Name', 'LAAS Technology Sp. z o.o.'),
    ('Siedziba', 'Registered office', 'ul. Jesienna 27, 05-502 Bobrowiec, gm. Piaseczno'),
    ('NIP', 'Tax ID (NIP)', '1231593199'),
    ('REGON', 'REGON', '543411286'),
    ('KRS', 'KRS number', '0001208967'),
    ('Wpis do KRS', 'Entered in KRS', '<span data-en="2 December 2025">2 grudnia 2025</span>'),
    ('Sąd rejestrowy', 'Registry court', '<span data-en="District Court for the Capital City of Warsaw, 14th Commercial Division of the National Court Register">Sąd Rejonowy dla m.st. Warszawy, XIV Wydział Gospodarczy KRS</span>'),
    ('Przeważająca działalność', 'Main activity', '<span data-en="Wholesale of electrical household appliances (PKD 46.43.Z)">Sprzedaż hurtowa elektrycznych artykułów użytku domowego (PKD 46.43.Z)</span>'),
]
reg_html = ''.join(f'<div class="reg-r">{T("dt", a, b)}<dd>{c}</dd></div>' for a, b, c in reg)
values = [
    ('Na miarę', 'Made to measure', 'Nie sprzedajemy gotowca z katalogu. Każde rozwiązanie zaczynamy od poznania miejsca, ludzi i sposobu, w jaki korzystają z przestrzeni.', 'We do not sell an off-the-shelf package. Every solution starts with getting to know the place, the people and how they use the space.'),
    ('Jeden opiekun', 'One point of contact', 'Każdą współpracę prowadzi jedna osoba, która zna historię projektu i potrzeby klienta.', 'Each project is handled by one person who knows its history and the client’s needs.'),
    ('Koszt w całym okresie pracy', 'Total cost of ownership', 'Doradzamy rozwiązania, które opłacają się nie tylko przy zakupie, ale przez lata pracy instalacji.', 'We recommend solutions that pay off not only at purchase but over years of operation.'),
]
values_html = ''.join(f'<div class="pil">{T("h3", a, b)}{T("p", c, d)}</div>' for a, b, c, d in values)
onas = f'''{phead('O nas', 'About us', 'O nas', 'About us',
 'LAAS Technology to spółka z Bobrowca pod Piasecznem. Tworzymy inteligentne systemy, które dopasowują oświetlenie do ludzi, przestrzeni i potrzeb.',
 'LAAS Technology is a company based in Bobrowiec near Piaseczno. We create smart systems that adapt lighting to people, spaces and needs.')}
<section class="sec">
  <div class="wrap split">
    <div class="split-t">
      {T('h2', 'Kim jesteśmy', 'Who we are')}
      {T('p', 'Jesteśmy młodą firmą - spółka została wpisana do Krajowego Rejestru Sądowego w grudniu 2025 roku. Mówimy o sobie, że jesteśmy „krawcami” światła: zamiast gotowych zestawów szyjemy rozwiązania na miarę konkretnego miejsca.', 'We are a young company, entered in the National Court Register in December 2025. We call ourselves tailors of light: instead of ready-made kits, we tailor solutions to a specific place.')}
      {T('p', 'Za każdym projektem stoi konkretna osoba: opiekun projektu, który prowadzi współpracę od pierwszej rozmowy do wdrożenia i dalej.', 'Behind every project there is a real person: a project manager who handles the relationship from the first conversation through deployment and beyond.')}
      {todo('Do uzupełnienia: krótka historia firmy, zespół i przykładowe realizacje.', 'To be completed: a short company history, the team and example projects.')}
    </div>
    <figure class="split-ph">{pic('laas-swiatlo', *ALT['swiatlo'], '(max-width:999px) 100vw, 600px')}</figure>
  </div>
</section>
<section class="sec sec-g">
  <div class="wrap pils">
    <div class="pils-h">
      {T('h2', 'Czym się kierujemy', 'What guides us')}
      {T('p', 'Nasze hasło to innowacje, oszczędności i efektywność. W praktyce oznacza to trzy proste zasady.', 'Our motto is innovation, savings and efficiency. In practice it comes down to three simple rules.')}
    </div>
    <div class="pils-l">{values_html}</div>
  </div>
</section>
<section class="sec">
  <div class="wrap reg-w">
    {T('h2', 'Dane rejestrowe', 'Company registration details')}
    <dl class="reg">{reg_html}</dl>
  </div>
</section>
{cta()}'''
page('o-nas.html', 'O nas - LAAS Technology', 'About us - LAAS Technology', 'Poznaj LAAS Technology Sp. z o.o. z Bobrowca k. Piaseczna - inteligentne zarządzanie oświetleniem.', onas)

# ---------------------------------------------------------------- OFERTA
rows = [
    ('oferta-energia.html', 'laas-swiatlo', 'swiatlo', 'Inteligentne oświetlenie', 'Smart lighting',
     'Systemy inteligentnego zarządzania oświetleniem, które zwiększają efektywność, obniżają koszty i tworzą komfortowe, bezpieczne przestrzenie.',
     'Smart lighting management systems that increase efficiency, lower costs and create comfortable, safe spaces.',
     [('Sterowanie światłem dopasowane do ludzi i przestrzeni', 'Lighting control adapted to people and spaces'), ('Czujniki, automatyka i integracje IoT', 'Sensors, automation and IoT integrations'), ('Optymalizacja zużycia energii', 'Energy use optimisation')]),
    ('oferta-inwestycje.html', 'laas-budynki', 'budynki', 'Budynki i inwestycje', 'Buildings and projects',
     'Dla inwestorów, deweloperów, wykonawców i zarządców obiektów, którzy chcą od początku zaplanować oświetlenie jako system, a nie zbiór lamp.',
     'For investors, developers, contractors and facility managers who want to plan lighting as a system from the start, not as a set of lamps.',
     [('Dobór rozwiązania do obiektu', 'Choosing the right solution for the building'), ('Integracja z instalacjami budynku', 'Integration with building installations'), ('Jeden opiekun projektu', 'One project manager')]),
    ('oferta-hurt.html', 'laas-hurt', 'hurt', 'Sprzedaż hurtowa', 'Wholesale',
     'Dla sklepów stacjonarnych i internetowych, hurtowni oraz dystrybutorów, którzy szukają stałego dostawcy elektrycznych artykułów i urządzeń.',
     'For high-street and online shops, wholesalers and distributors looking for a steady supplier of electrical products and appliances.',
     [('Stały asortyment', 'A steady product range'), ('Warunki ustalane indywidualnie', 'Individually agreed terms'), ('Dostawy zgodne z harmonogramem', 'Deliveries on schedule')]),
]
def ul(items): return '<ul class="ticks">' + ''.join(f'<li data-en="{e(b)}">{a}</li>' for a, b in items) + '</ul>'
rows_html = ''.join(f'''<article class="row">
  <a class="row-ph" href="{h}" tabindex="-1" aria-hidden="true">{pic(img, *ALT[ak], "(max-width:999px) 100vw, 640px")}</a>
  <div class="row-t">
    {T('h2', f'<a href="{h}">{tp}</a>', f'<a href="{h}">{te}</a>')}
    {T('p', pp, pe)}
    {ul(li)}
    <a class="more" href="{h}"><span data-en="Details">Szczegóły</span>{ARR}</a>
  </div>
</article>''' for h, img, ak, tp, te, pp, pe, li in rows)
oferta = f'''{phead('Oferta', 'Solutions', 'Inteligentne rozwiązania dla lepszego jutra', 'Smart solutions for a better tomorrow',
 'Dostarczamy kompleksowe systemy inteligentnego zarządzania oświetleniem, które zwiększają efektywność, obniżają koszty i tworzą komfortowe, bezpieczne przestrzenie.',
 'We deliver complete smart lighting management systems that increase efficiency, lower costs and create comfortable, safe spaces.',
 'laas-miasto', ALT['miasto'], 'laas-miasto-m', '45% 55%')}
<section class="sec sec-tight"><div class="wrap rows">{rows_html}</div></section>
{cta('Nie wiesz, od czego zacząć?', 'Not sure where to start?', 'Opisz obiekt i to, co chcesz osiągnąć. Zaproponujemy rozwiązanie i kolejne kroki.', 'Describe the site and what you want to achieve. We will propose a solution and the next steps.')}'''
page('oferta.html', 'Oferta - LAAS Technology', 'Solutions - LAAS Technology', 'Oferta LAAS Technology: inteligentne oświetlenie, rozwiązania dla budynków i inwestycji, sprzedaż hurtowa.', oferta)

def subpage(fname, crumb_pl, crumb_en, h1p, h1e, lp, le, img, ak, blocks, mimg=None, pos=None, extra=''):
    b = ''
    for hp, he, pp, pe, li in blocks:
        b += f'<div class="blk">{T("h2", hp, he)}{T("p", pp, pe)}{ul(li) if li else ""}</div>'
    others = ''.join(f'<li><a href="{h}" data-en="{e(se)}">{sp}</a></li>' for h, sp, se in OFERTA if h != fname)
    body = f'''{phead(crumb_pl, crumb_en, h1p, h1e, lp, le, img, ALT[ak], mimg, pos)}
<section class="sec">
  <div class="wrap det">
    <div class="det-m">{b}{extra}</div>
    <aside class="det-a">
      {T('h2', 'Pozostała oferta', 'Other solutions')}
      <ul>{others}</ul>
      <div class="det-k">
        {T('p', 'Masz pytanie o ten zakres oferty?', 'Questions about this area?')}
        <p class="person-n">Marcin Ostrowski</p>
        <p class="person-r">Project Manager</p>
        <a href="mailto:{EMAIL}">{EMAIL}</a>
      </div>
    </aside>
  </div>
</section>
{cta()}'''
    return body

en_ = subpage('oferta-energia.html', 'Inteligentne oświetlenie', 'Smart lighting', 'Inteligentne zarządzanie oświetleniem', 'Smart lighting management',
  'Światło, które dopasowuje się do ludzi, przestrzeni i pory dnia. Łączymy czujniki, automatykę i analizę danych, żeby oświetlenie zużywało mniej energii i lepiej służyło użytkownikom.',
  'Light that adapts to people, spaces and the time of day. We combine sensors, automation and data analysis so lighting uses less energy and serves its users better.',
  'laas-swiatlo', 'swiatlo',
  [('Co obejmuje', 'What it covers', 'System łączy oprawy, czujniki i oprogramowanie w jedną całość, którą można monitorować i zmieniać bez wymiany całej instalacji.', 'The system brings luminaires, sensors and software together into one whole that can be monitored and adjusted without replacing the installation.',
    [('Sterowanie oświetleniem dopasowane do ludzi, przestrzeni i pory dnia', 'Lighting control adapted to people, spaces and time of day'), ('Algorytmy i analiza danych w czasie rzeczywistym', 'Algorithms and real-time data analysis'), ('Integracja z czujnikami, systemami i urządzeniami IoT', 'Integration with sensors, systems and IoT devices'), ('Niezawodność, ochrona danych i pełna kontrola systemu', 'Reliability, data protection and full control of the system')]),
   ('Dlaczego to ważne', 'Why it matters', 'Oświetlenie pracuje codziennie przez wiele lat. Światło dopasowane do faktycznego użycia przestrzeni to niższe zużycie energii i koszty, a przy tym większy komfort i bezpieczeństwo.', 'Lighting works every day for many years. Light matched to how a space is actually used means lower energy use and costs, along with greater comfort and safety.', None),
   ('Rozwiązanie szyte na miarę', 'A tailored solution', 'Każdy obiekt jest inny. Zaczynamy od rozmowy i poznania potrzeb, a potem proponujemy rozwiązanie dopasowane do miejsca - a nie odwrotnie.', 'Every site is different. We start with a conversation and an understanding of your needs, then propose a solution that fits the place - not the other way round.', None)],
  extra=todo('Do uzupełnienia: konkretne produkty i technologie, z których korzystamy, oraz przykładowe wdrożenia.', 'To be completed: the specific products and technologies we use, and example deployments.'))
page('oferta-energia.html', 'Inteligentne oświetlenie - LAAS Technology', 'Smart lighting - LAAS Technology', 'Inteligentne zarządzanie oświetleniem - LAAS Technology.', en_)

inw = subpage('oferta-inwestycje.html', 'Budynki i inwestycje', 'Buildings and projects', 'Budynki i inwestycje', 'Buildings and projects',
  'Oświetlenie zaplanowane jako system dla całego obiektu lub inwestycji. Jedna propozycja, jeden harmonogram, jeden opiekun projektu.',
  'Lighting planned as a system for a whole building or project. One proposal, one schedule, one project manager.',
  'laas-budynki', 'budynki',
  [('Co obejmuje', 'What it covers', 'Przygotowujemy rozwiązanie dla całego obiektu i pilnujemy, żeby wdrożenie pasowało do etapów prac.', 'We prepare a solution for the whole building and make sure deployment fits the stages of work.',
    [('Analiza potrzeb i sposobu użytkowania obiektu', 'Analysis of needs and how the building is used'), ('Dobór systemu sterowania i urządzeń', 'Selection of control system and devices'), ('Integracja z istniejącymi instalacjami budynku', 'Integration with existing building installations'), ('Harmonogram wdrożenia dopasowany do budowy', 'Deployment schedule matched to construction')]),
   ('Dla kogo', 'Who it is for', 'Dla inwestorów, deweloperów, generalnych wykonawców i zarządców obiektów - wszędzie tam, gdzie oświetlenie ma pracować wydajnie przez lata.', 'For investors, developers, general contractors and facility managers - wherever lighting needs to work efficiently for years.', None),
   ('Jak pracujemy', 'How we work', 'Projekt prowadzi jeden opiekun - Project Manager, który zna zakres, terminy i ustalenia z budowy. Nie trzeba niczego tłumaczyć kilku osobom.', 'The project is run by one Project Manager who knows the scope, the dates and the site arrangements. No need to explain things to several people.', None)],
  extra=todo('Do uzupełnienia: rodzaje obiektów, w których pracujemy, i przykładowe realizacje.', 'To be completed: the types of buildings we work on and example projects.'))
page('oferta-inwestycje.html', 'Budynki i inwestycje - LAAS Technology', 'Buildings and projects - LAAS Technology', 'Inteligentne oświetlenie dla budynków i inwestycji - LAAS Technology.', inw)

hurt = subpage('oferta-hurt.html', 'Sprzedaż hurtowa', 'Wholesale', 'Sprzedaż hurtowa', 'Wholesale',
  'Elektryczne artykuły i urządzenia dla sklepów, hurtowni i dystrybutorów - z jednym opiekunem i warunkami dopasowanymi do skali zamówień.',
  'Electrical products and appliances for retailers, wholesalers and distributors - with one account manager and terms matched to your order volume.',
  'laas-hurt', 'hurt',
  [('Asortyment', 'Product range', 'Prowadzimy sprzedaż hurtową elektrycznych artykułów użytku domowego. Aktualne kategorie i marki uzupełnimy razem z Państwem.', 'We sell electrical household products wholesale. Current categories and brands will be filled in together with you.', None),
   ('Dla kogo', 'Who it is for', 'Współpracę kierujemy do firm, które kupują regularnie lub w większych ilościach: sklepów stacjonarnych i internetowych, hurtowni regionalnych oraz dystrybutorów.', 'We work with businesses that buy regularly or in larger volumes: high-street and online shops, regional wholesalers and distributors.', None),
   ('Warunki współpracy', 'Terms of cooperation', 'Ceny, minimalne zamówienia i terminy dostaw ustalamy indywidualnie, w zależności od wielkości i regularności zamówień. Każdą ofertę potwierdzamy na piśmie.', 'Prices, minimum order quantities and delivery times are agreed individually, depending on order size and frequency. Every quote is confirmed in writing.', None)],
  pos='50% 50%',
  extra=todo('Do uzupełnienia: kategorie produktów i marki w ofercie hurtowej.', 'To be completed: product categories and brands in the wholesale range.'))
page('oferta-hurt.html', 'Sprzedaż hurtowa - LAAS Technology', 'Wholesale - LAAS Technology', 'Sprzedaż hurtowa - LAAS Technology.', hurt)

# ---------------------------------------------------------------- PARTNERZY
logos8 = ''.join('<li data-en="Partner logo">Logo partnera</li>' for _ in range(8))
partn = f'''{phead('Partnerzy', 'Partners', 'Razem tworzymy lepszy świat', 'Together we create a better world',
 'Współpracujemy z liderami technologii, aby dostarczać inteligentne rozwiązania dla ludzi, przestrzeni i przyszłości.',
 'We work with technology leaders to deliver smart solutions for people, spaces and the future.', 'laas-razem', ALT['razem'], 'laas-razem-m', '30% 50%')}
<section class="sec">
  <div class="wrap">
    <div class="sec-h">
      {T('h2', 'Partnerzy technologiczni', 'Technology partners')}
      {T('p', 'Producenci i dostawcy technologii, z którymi tworzymy nasze rozwiązania.', 'The manufacturers and technology suppliers we build our solutions with.')}
    </div>
    <ul class="logos logos-8">{logos8}</ul>
    {todo('Do uzupełnienia: logotypy i nazwy partnerów - uzupełnimy je razem z Państwem.', 'To be completed: partner logos and names - to be filled in together with you.')}
  </div>
</section>
<section class="sec sec-g">
  <div class="wrap two">
    <div class="blk">
      {T('h2', 'Dla producentów i dostawców technologii', 'For manufacturers and technology suppliers')}
      {T('p', 'Rozwijasz oprawy, czujniki lub oprogramowanie do sterowania oświetleniem? Porozmawiajmy o tym, jak możemy wspólnie dotrzeć z nimi do obiektów i inwestycji.', 'Do you develop luminaires, sensors or lighting control software? Let’s talk about how we can bring them to buildings and projects together.')}
    </div>
    <div class="blk">
      {T('h2', 'Dla wykonawców i odbiorców', 'For contractors and buyers')}
      {T('p', 'Firmy wykonawcze, sklepy i hurtownie zapraszamy do stałej współpracy. Przygotujemy propozycję dopasowaną do skali i rodzaju projektów.', 'We invite contractors, shops and wholesalers to work with us on a regular basis. We will prepare a proposal suited to the size and type of your projects.')}
    </div>
  </div>
</section>
{cta('Zostań partnerem', 'Become a partner', 'Napisz kilka słów o swojej firmie i ofercie. Odpowiemy z propozycją dalszych kroków.', 'Write a few words about your company and products. We will reply with suggested next steps.')}'''
page('partnerzy.html', 'Partnerzy - LAAS Technology', 'Partners - LAAS Technology', 'Partnerzy LAAS Technology - razem tworzymy lepszy świat.', partn)

# ---------------------------------------------------------------- AKTUALNOŚCI
akt = f'''{phead('Aktualności', 'News', 'Aktualności', 'News',
 'Informacje o firmie, nowych rozwiązaniach i realizacjach.', 'Company news, new solutions and projects.')}
<section class="sec sec-tight">
  <div class="wrap">
    <div class="news news-l">{news_html(list(reversed(news)))}</div>
    {T('p', 'Tu pojawią się kolejne wpisy, np. o nowych wdrożeniach lub partnerach.', 'More posts will appear here, for example about new deployments or partners.', 'class="note"')}
  </div>
</section>
{cta()}'''
page('aktualnosci.html', 'Aktualności - LAAS Technology', 'News - LAAS Technology', 'Aktualności LAAS Technology.', akt)

# ---------------------------------------------------------------- KARIERA
kar = f'''{phead('Kariera', 'Careers', 'Kariera', 'Careers',
 'Rozwijamy firmę i chętnie poznajemy ludzi, którzy chcą razem z nami tworzyć inteligentne rozwiązania - w technologii, projektach i obsłudze klienta.',
 'We are growing and keen to meet people who want to build smart solutions with us - in technology, projects and customer service.')}
<section class="sec">
  <div class="wrap split">
    <div class="split-t">
      {T('h2', 'Aktualne ogłoszenia', 'Current openings')}
      {T('p', 'Ogłoszenia rekrutacyjne będą publikowane w tym miejscu, z opisem stanowiska, zakresem obowiązków i sposobem aplikowania.', 'Job postings will be published here, with a description of the role, responsibilities and how to apply.')}
      {T('h2', 'Aplikacja spontaniczna', 'Speculative applications')}
      {T('p', f'Nie widzisz ogłoszenia dla siebie? Wyślij CV na adres <a href="mailto:{EMAIL}">{EMAIL}</a> z dopiskiem „Kariera” i krótką informacją, czym chcesz się zajmować.', f'Don’t see a role for you? Send your CV to <a href="mailto:{EMAIL}">{EMAIL}</a> with “Careers” in the subject and a short note about what you would like to do.')}
      {T('p', 'Do CV dołącz zgodę na przetwarzanie danych osobowych w celu rekrutacji.', 'Please include consent to the processing of your personal data for recruitment purposes.', 'class="note"')}
    </div>
    <figure class="split-ph">{pic('laas-razem-m', *ALT['razem'], '(max-width:999px) 100vw, 600px')}</figure>
  </div>
</section>'''
page('kariera.html', 'Kariera - LAAS Technology', 'Careers - LAAS Technology', 'Praca w LAAS Technology.', kar)

# ---------------------------------------------------------------- KONTAKT
kon = f'''{phead('Kontakt', 'Contact', 'Porozmawiajmy', "Let's talk",
 'Każdy projekt zaczyna się od rozmowy. Napisz przez formularz albo bezpośrednio do opiekuna projektu - odpowiemy z propozycją.',
 'Every project starts with a conversation. Use the form or write directly to the project manager - we will reply with a proposal.',
 'laas-rozmowa', ALT['rozmowa'], None, '50% 30%')}
<section class="sec sec-tight" id="kontakt">
  <div class="wrap kon">
    <div class="kon-d">
      <div class="kon-b">
        {T('h2', 'Osoba kontaktowa', 'Contact person')}
        <p class="person-n">Marcin Ostrowski</p>
        <p class="person-r">Project Manager</p>
        <p><a class="kon-mail" href="mailto:{EMAIL}"><svg aria-hidden="true"><use href="#i-mail"/></svg>{EMAIL}</a></p>
      </div>
      <div class="kon-b">
        {T('h2', 'Siedziba', 'Registered office')}
        <p>LAAS Technology Sp. z o.o.<br>ul. Jesienna 27<br>05-502 Bobrowiec</p>
        <p><a class="more" href="https://www.openstreetmap.org/search?query=Jesienna%2027%2C%20Bobrowiec" target="_blank" rel="noopener"><span data-en="Show on map">Pokaż na mapie</span>{ARR}</a></p>
      </div>
      <div class="kon-b">
        {T('h2', 'Dane rejestrowe', 'Registration details')}
        <p>NIP 1231593199<br>REGON 543411286<br>KRS 0001208967</p>
      </div>
    </div>
    <form class="form" id="form" novalidate>
      {T('h2', 'Formularz kontaktowy', 'Contact form')}
      <div class="f-g">
        <label><span data-en="Full name">Imię i nazwisko</span><input type="text" name="n" autocomplete="name"></label>
        <label><span data-en="Company">Firma</span><input type="text" name="f" autocomplete="organization"></label>
        <label><span data-en="E-mail">E-mail</span><input type="email" name="e" autocomplete="email"></label>
        <label><span data-en="Phone">Telefon</span><input type="tel" name="t" autocomplete="tel"></label>
      </div>
      <label><span data-en="Subject">Temat</span>
        <select name="s">
          <option data-en="Smart lighting">Inteligentne oświetlenie</option>
          <option data-en="Buildings and projects">Budynki i inwestycje</option>
          <option data-en="Wholesale">Sprzedaż hurtowa</option>
          <option data-en="Partnership">Współpraca partnerska</option>
          <option data-en="Other">Inne</option>
        </select>
      </label>
      <label><span data-en="Message">Wiadomość</span><textarea name="w" rows="5" placeholder="Jaki obiekt, czego potrzebujesz, w jakim terminie" data-en-ph="What kind of site, what you need, by when"></textarea></label>
      <label class="chk"><input type="checkbox" name="z"><span data-en="I consent to the processing of my data in order to respond to this enquiry.">Wyrażam zgodę na przetwarzanie moich danych w celu odpowiedzi na zapytanie.</span></label>
      <button class="btn" type="submit"><span data-en="Send enquiry">Wyślij zapytanie</span>{ARR}</button>
      <p class="form-msg" id="formMsg" hidden data-en="This is a working draft of the website - the form does not send messages yet.">To wizualizacja robocza strony - formularz jeszcze nie wysyła wiadomości.</p>
    </form>
  </div>
</section>'''
page('kontakt.html', 'Kontakt - LAAS Technology', 'Contact - LAAS Technology', 'Kontakt z LAAS Technology Sp. z o.o., Bobrowiec k. Piaseczna.', kon, mob=False)

print('ok', V)
