# -*- coding: utf-8 -*-
# Generator stron wizualizacji LAAS Technology (PL + EN przez data-en)
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

SYMBOLS = '''<svg width="0" height="0" style="position:absolute" aria-hidden="true">
  <symbol id="mark" viewBox="0 0 40 40"><rect x="1.5" y="1.5" width="37" height="37" fill="none" stroke="currentColor" stroke-width="3"/><path d="M1.5 38.5V20H20v18.5z" fill="var(--acc)"/><path d="M20 1.5v18.5h18.5" fill="none" stroke="currentColor" stroke-width="3"/></symbol>
  <symbol id="i-arr" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" d="M5 12h13M13 6l6 6-6 6"/></symbol>
  <symbol id="i-mail" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-width="1.9" stroke-linejoin="round" d="M3.5 5.5h17v13h-17zM3.8 6l8.2 7 8.2-7"/></symbol>
  <symbol id="i-pin" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-width="1.9" d="M12 21s-6.5-6.2-6.5-11.2a6.5 6.5 0 0 1 13 0C18.5 14.8 12 21 12 21Z"/><circle cx="12" cy="9.8" r="2.3" fill="none" stroke="currentColor" stroke-width="1.9"/></symbol>
  <symbol id="i-down" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" d="M6 9l6 6 6-6"/></symbol>
  <symbol id="i-user" viewBox="0 0 24 24"><circle cx="12" cy="8" r="4" fill="none" stroke="currentColor" stroke-width="1.9"/><path d="M4 21c1-4.4 4.2-6.5 8-6.5s7 2.1 8 6.5" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round"/></symbol>
</svg>'''

OFERTA = [
    ('oferta-hurt.html', 'Sprzedaż hurtowa', 'Wholesale'),
    ('oferta-inwestycje.html', 'Dostawy dla inwestycji', 'Supplies for projects'),
    ('oferta-energia.html', 'Energooszczędność i smart home', 'Energy saving and smart home'),
]
NAV = [
    ('index.html', 'Strona główna', 'Home'),
    ('o-nas.html', 'O nas', 'About us'),
    ('oferta.html', 'Oferta', 'Products and services'),
    ('partnerzy.html', 'Partnerzy', 'Partners'),
    ('aktualnosci.html', 'Aktualności', 'News'),
    ('kariera.html', 'Kariera', 'Careers'),
]

def logo(cls='brand'):
    return f'<a class="{cls}" href="index.html" aria-label="LAAS Technology - strona główna"><svg class="mark" aria-hidden="true"><use href="#mark"/></svg><span class="wm"><b>LAAS</b><span>Technology</span></span></a>'

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
      {T('p', 'Sprzedaż hurtowa elektrycznych artykułów użytku domowego.', 'Wholesale of electrical household appliances.')}
      <p class="foot-slog">Innowacje | Oszczędności | Efektywność</p>
    </div>
    <div><h2 data-en="Menu">Menu</h2><ul>{menu}</ul></div>
    <div><h2 data-en="Products and services">Oferta</h2><ul>{of}</ul></div>
    <div class="foot-d"><h2 data-en="Company details">Dane firmy</h2>
      <p>LAAS Technology Sp. z o.o.<br>ul. Jesienna 27<br>05-502 Bobrowiec</p>
      <p>NIP 1231593199<br>REGON 543411286<br>KRS 0001208967</p>
      <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
    </div>
  </div>
  <div class="wrap foot-b">
    <span>&copy; 2026 LAAS Technology Sp. z o.o.</span>
    {T('a', 'Polityka prywatności', 'Privacy policy', 'href="#"')}
    <span class="foot-w"><span data-en="Working draft - design and build:">Wizualizacja robocza - wykonanie:</span> <a href="https://wylinka.pl" target="_blank" rel="noopener">Wylinka</a></span>
  </div>
</footer>'''

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
<meta name="theme-color" content="#FFFFFF">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 40 40'%3E%3Crect width='40' height='40' fill='%231B1E21'/%3E%3Cpath d='M6 34V20h14v14z' fill='%23FFC20E'/%3E%3Cpath d='M20 6v14h14' fill='none' stroke='%23fff' stroke-width='3'/%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@500;600;700;800&family=IBM+Plex+Sans:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css?v={V}">
<script>try{{if((new URLSearchParams(location.search).get('lang')||localStorage.getItem('laas-lang'))==='en')document.documentElement.classList.add('is-en')}}catch(e){{}}</script>
</head>
<body>
<!-- Wizualizacja robocza (koncepcja) strony LAAS Technology Sp. z o.o. Treści ogólne do potwierdzenia z klientem; nie podajemy niesprawdzonych liczb, marek ani referencji. -->
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

def phead(crumb_pl, crumb_en, h1_pl, h1_en, lead_pl, lead_en, img=None, alt=''):
    ph = f'<figure class="phead-ph"><img src="img/{img}" alt="{e(alt)}" width="1600" height="1067"></figure>' if img else ''
    return f'''<section class="phead{' phead-img' if img else ''}">
  <div class="wrap">
    <p class="crumb"><a href="index.html" data-en="Home">Strona główna</a><span aria-hidden="true">/</span>{T('span', crumb_pl, crumb_en)}</p>
    <div class="phead-g">
      {T('h1', h1_pl, h1_en)}
      {T('p', lead_pl, lead_en, 'class="lead"')}
    </div>
  </div>
  {ph}
</section>'''

def cta(h_pl='Porozmawiajmy o współpracy', h_en="Let's talk about working together",
        p_pl='Napisz, jakich produktów szukasz, w jakich ilościach i na kiedy. Odpowiemy z propozycją oferty.',
        p_en='Tell us what products you need, in what quantities and by when. We will reply with a proposal.'):
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

# ---------------------------------------------------------------- STRONA GŁÓWNA
tiles = [
    ('oferta-hurt.html', 'hurt.jpg', 'Magazyn z regałami pełnymi kartonów z towarem',
     'Sprzedaż hurtowa', 'Wholesale',
     'Elektryczne artykuły użytku domowego dla sklepów, hurtowni i dystrybutorów. Stały asortyment, warunki ustalane indywidualnie.',
     'Electrical household appliances for retailers, wholesalers and distributors. A steady range and individually agreed terms.'),
    ('oferta-inwestycje.html', 'inwestycje.jpg', 'Nowoczesna kuchnia z płytą indukcyjną w zabudowie',
     'Dostawy dla inwestycji', 'Supplies for projects',
     'Kompletujemy urządzenia dla mieszkań, biur i obiektów na wynajem. Jedna oferta i jeden harmonogram dostaw dla całej inwestycji.',
     'We put together appliances for apartments, offices and rental properties. One quote and one delivery schedule for the whole project.'),
    ('oferta-energia.html', 'energia.jpg', 'Inteligentne gniazdko, żarówki i czujniki na jasnym tle',
     'Energooszczędność i smart home', 'Energy saving and smart home',
     'Urządzenia, które zużywają mniej energii i pozwalają sterować domem z telefonu: od sprzętu AGD po gniazdka i czujniki.',
     'Devices that use less energy and let you control your home from a phone: from household appliances to smart plugs and sensors.'),
]
tiles_html = ''.join(f'''<article class="tile">
  <a href="{h}" class="tile-ph"><img src="img/{img}" alt="{e(alt)}" width="1600" height="1067" loading="lazy"></a>
  {T('h3', f'<a href="{h}">{tp}</a>', f'<a href="{h}">{te}</a>')}
  {T('p', pp, pe)}
  <a class="more" href="{h}"><span data-en="Details">Szczegóły</span>{ARR}</a>
</article>''' for h, img, alt, tp, te, pp, pe in tiles)

pillars = [
    ('Innowacje', 'Innovation',
     'Śledzimy, co nowego pojawia się w urządzeniach domowych, i wprowadzamy do oferty produkty, które realnie ułatwiają codzienne życie: sterowanie z aplikacji, automatyczne programy, nowe technologie grzania i chłodzenia.',
     'We follow what is new in home appliances and add products that make everyday life genuinely easier: app control, automatic programmes, new heating and cooling technologies.'),
    ('Oszczędności', 'Savings',
     'Przy doborze produktów patrzymy na koszt użytkowania, nie tylko na cenę zakupu. Wysoka klasa energetyczna i niskie zużycie wody to mniejsze rachunki dla końcowego użytkownika.',
     'When selecting products we look at the cost of use, not just the purchase price. A high energy class and low water use mean lower bills for the end user.'),
    ('Efektywność', 'Efficiency',
     'Krótka droga od zapytania do dostawy. Jeden opiekun prowadzi zamówienie od początku do końca, a ustalenia potwierdzamy na piśmie.',
     'A short path from enquiry to delivery. One account manager handles the order from start to finish, and every arrangement is confirmed in writing.'),
]
pillars_html = ''.join(f'<div class="pil">{T("h3", a, b)}{T("p", c, d)}</div>' for a, b, c, d in pillars)

steps = [
    ('Zapytanie.', 'Enquiry.', 'Opisujesz, czego potrzebujesz: asortyment, ilości, termin i miejsce dostawy.', 'You describe what you need: product range, quantities, date and delivery address.'),
    ('Oferta.', 'Quote.', 'Przygotowujemy propozycję produktów i warunków handlowych, w razie potrzeby z zamiennikami.', 'We prepare a product proposal and trading terms, with alternatives where useful.'),
    ('Dostawa.', 'Delivery.', 'Ustalamy harmonogram i pilnujemy, żeby towar dotarł kompletny i na czas.', 'We agree a schedule and make sure the goods arrive complete and on time.'),
    ('Opieka po sprzedaży.', 'After-sales care.', 'Ten sam opiekun pomaga przy reklamacjach, uzupełnieniach i kolejnych zamówieniach.', 'The same account manager helps with complaints, top-ups and repeat orders.'),
]
steps_html = ''.join(f'<li><span class="st">{T("b", a, b)} {T("span", c, d)}</span></li>' for a, b, c, d in steps)

news = [
    ('2025-12-02', '2 grudnia 2025', '2 December 2025',
     'LAAS Technology w Krajowym Rejestrze Sądowym', 'LAAS Technology entered in the National Court Register',
     'Spółka została wpisana do KRS pod numerem 0001208967. Siedziba mieści się w Bobrowcu pod Piasecznem, przy ul. Jesiennej 27.',
     'The company was entered in the National Court Register under number 0001208967. Its registered office is in Bobrowiec near Piaseczno, at ul. Jesienna 27.'),
    ('2026', '2026', '2026',
     'Uruchamiamy stronę internetową', 'Our website goes live',
     'Nowa strona w wersji polskiej i angielskiej: oferta, informacje dla partnerów i bezpośredni kontakt z opiekunem projektu.',
     'A new website in Polish and English: our range, information for partners and direct contact with a project manager.'),
]
def news_html(items):
    return ''.join(f'''<article class="news-i">
  <time datetime="{dt}" data-en="{e(de)}">{dp}</time>
  {T('h3', tp, te)}
  {T('p', pp, pe)}
</article>''' for dt, dp, de, tp, te, pp, pe in items)

logos = ''.join('<li data-en="Brand logo">Logo marki</li>' for _ in range(6))

home = f'''<section class="hero">
  <div class="hero-txt">
    <p class="hero-loc"><svg aria-hidden="true"><use href="#i-pin"/></svg><span data-en="Wholesale - Bobrowiec near Piaseczno">Hurtownia - Bobrowiec k. Piaseczna</span></p>
    {T('h1', 'Elektryczne artykuły użytku domowego w&nbsp;hurcie', 'Electrical household appliances, wholesale')}
    {T('p', 'Dostarczamy sklepom, dystrybutorom i firmom realizującym inwestycje sprzęt, który oszczędza energię i czas. Ofertę i warunki ustalamy z każdym klientem indywidualnie.', 'We supply retailers, distributors and property developers with equipment that saves energy and time. The range and terms are agreed individually with each client.', 'class="lead"')}
    <div class="hero-cta" id="heroCta">
      <a class="btn" href="oferta.html"><span data-en="See our range">Zobacz ofertę</span>{ARR}</a>
      <a class="btn btn-o" href="kontakt.html" data-en="Contact">Kontakt</a>
    </div>
    <p class="hero-slog">Innowacje <i>|</i> Oszczędności <i>|</i> Efektywność</p>
  </div>
  <figure class="hero-ph">
    <picture>
      <source media="(max-width:999px)" srcset="img/hero-m.jpg">
      <img src="img/hero.jpg" alt="Jasna kuchnia z piekarnikami i płytą indukcyjną w zabudowie" width="1800" height="1201" fetchpriority="high">
    </picture>
  </figure>
</section>

<section class="sec" id="oferta">
  <div class="wrap">
    <div class="sec-h">
      {T('h2', 'Oferta', 'What we offer')}
      {T('p', 'Trzy obszary, w których możemy pomóc. Każdy z nich prowadzi ten sam opiekun - bez przekazywania sprawy między działami.', 'Three areas where we can help. Each is handled by the same account manager, with no passing between departments.')}
    </div>
    <div class="tiles">{tiles_html}</div>
  </div>
</section>

<section class="sec sec-g">
  <div class="wrap pils">
    <div class="pils-h">
      {T('h2', 'Innowacje, oszczędności, efektywność', 'Innovation, savings, efficiency')}
      {T('p', 'Te trzy słowa podpisujemy pod każdą wiadomością, bo według nich dobieramy produkty i prowadzimy współpracę.', 'We sign every message with these three words, because they guide how we choose products and work with clients.')}
      <figure class="pils-ph"><img src="img/wlacznik.jpg" alt="Inteligentny włącznik światła na ścianie sypialni" width="1400" height="934" loading="lazy"></figure>
    </div>
    <div class="pils-l">{pillars_html}</div>
  </div>
</section>

<section class="sec">
  <div class="wrap split">
    <figure class="split-ph"><img src="img/magazyn.jpg" alt="Wysokie stosy kartonów w hali magazynowej" width="1600" height="1200" loading="lazy"></figure>
    <div class="split-t">
      {T('h2', 'Jak wygląda współpraca', 'How we work together')}
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
      {T('h2', 'Marki i producenci', 'Brands and manufacturers')}
      <a class="more" href="partnerzy.html"><span data-en="All partners">Wszyscy partnerzy</span>{ARR}</a>
    </div>
    <ul class="logos">{logos}</ul>
    {T('p', 'Miejsce na logotypy marek, które dystrybuujemy - uzupełnimy je razem z Państwem.', 'Space for the logos of the brands we distribute - to be filled in together with you.', 'class="note"')}
  </div>
</section>

{cta()}'''
page('index.html', 'LAAS Technology - hurtowa sprzedaż elektrycznych artykułów użytku domowego',
     'LAAS Technology - wholesale of electrical household appliances',
     'LAAS Technology Sp. z o.o., Bobrowiec k. Piaseczna: sprzedaż hurtowa elektrycznych artykułów użytku domowego, dostawy dla inwestycji, urządzenia energooszczędne.', home)

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
    ('Konkretnie', 'To the point', 'Odpowiadamy na zapytania z ceną, dostępnością i terminem. Jeśli czegoś nie możemy dostarczyć, mówimy to od razu.', 'We answer enquiries with price, availability and lead time. If we cannot supply something, we say so straight away.'),
    ('Jeden opiekun', 'One point of contact', 'Każdą współpracę prowadzi jedna osoba, która zna historię zamówień i potrzeby klienta.', 'Each account is handled by one person who knows the order history and the client’s needs.'),
    ('Koszt w całym okresie używania', 'Total cost of ownership', 'Doradzamy produkty, które opłacają się nie tylko przy zakupie, ale i przez lata pracy u użytkownika.', 'We recommend products that pay off not only at purchase but over years of use.'),
]
values_html = ''.join(f'<div class="pil">{T("h3", a, b)}{T("p", c, d)}</div>' for a, b, c, d in values)
onas = f'''{phead('O nas', 'About us', 'O nas', 'About us',
 'LAAS Technology to spółka z Bobrowca pod Piasecznem, która zajmuje się sprzedażą hurtową elektrycznych artykułów użytku domowego.',
 'LAAS Technology is a company based in Bobrowiec near Piaseczno, specialising in the wholesale of electrical household appliances.')}
<section class="sec">
  <div class="wrap split">
    <div class="split-t">
      {T('h2', 'Kim jesteśmy', 'Who we are')}
      {T('p', 'Jesteśmy młodą firmą - spółka została wpisana do Krajowego Rejestru Sądowego w grudniu 2025 roku. Dobieramy produkty, przygotowujemy oferty i koordynujemy dostawy elektrycznych artykułów użytku domowego dla firm.', 'We are a young company, entered in the National Court Register in December 2025. We select products, prepare quotes and coordinate deliveries of electrical household appliances for businesses.')}
      {T('p', 'Za każdym zamówieniem stoi konkretna osoba: opiekun projektu, który prowadzi współpracę od pierwszego zapytania do dostawy i dalej, przy kolejnych zamówieniach.', 'Behind every order there is a real person: a project manager who handles the relationship from the first enquiry through delivery and on to repeat orders.')}
    </div>
    <figure class="split-ph"><img src="img/drobne.jpg" alt="Czajnik i ekspres do kawy na blacie kuchennym" width="1400" height="934" loading="lazy"></figure>
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
page('o-nas.html', 'O nas - LAAS Technology', 'About us - LAAS Technology', 'Poznaj LAAS Technology Sp. z o.o. z Bobrowca k. Piaseczna.', onas)

# ---------------------------------------------------------------- OFERTA
rows = [
    ('oferta-hurt.html', 'hurt.jpg', 'Magazyn z regałami pełnymi towaru', 'Sprzedaż hurtowa', 'Wholesale',
     'Dla sklepów stacjonarnych i internetowych, hurtowni oraz dystrybutorów, którzy szukają stałego dostawcy elektrycznych artykułów użytku domowego.',
     'For high-street and online shops, wholesalers and distributors looking for a steady supplier of electrical household appliances.',
     [('Duże AGD - wolnostojące i do zabudowy', 'Large appliances - freestanding and built-in'), ('Drobne AGD do kuchni i domu', 'Small kitchen and home appliances'), ('Warunki ustalane indywidualnie', 'Individually agreed terms')]),
    ('oferta-inwestycje.html', 'inwestycje.jpg', 'Kuchnia w zabudowie z płytą indukcyjną', 'Dostawy dla inwestycji', 'Supplies for projects',
     'Dla deweloperów, wykonawców, firm wykończeniowych i zarządców obiektów na wynajem, którzy wyposażają wiele lokali naraz.',
     'For developers, contractors, fit-out companies and rental property managers equipping many units at once.',
     [('Kompletacja urządzeń na całą inwestycję', 'Appliance packages for the whole project'), ('Harmonogram dostaw zgodny z budową', 'Delivery schedule aligned with construction'), ('Jeden opiekun projektu', 'One project manager')]),
    ('oferta-energia.html', 'energia.jpg', 'Inteligentne urządzenia domowe na jasnym tle', 'Energooszczędność i smart home', 'Energy saving and smart home',
     'Urządzenia o niskim zużyciu energii i rozwiązania inteligentnego domu, które pomagają ograniczyć rachunki i wygodnie sterować sprzętem.',
     'Low-energy appliances and smart home solutions that help reduce bills and make equipment easy to control.',
     [('Sprzęt o wysokiej klasie energetycznej', 'High energy-class appliances'), ('Inteligentne gniazdka, czujniki i oświetlenie', 'Smart plugs, sensors and lighting'), ('Pomoc w doborze rozwiązań', 'Help choosing the right solution')]),
]
def ul(items): return '<ul class="ticks">' + ''.join(f'<li data-en="{e(b)}">{a}</li>' for a, b in items) + '</ul>'
rows_html = ''.join(f'''<article class="row">
  <a class="row-ph" href="{h}"><img src="img/{img}" alt="{e(alt)}" width="1600" height="1067" loading="lazy"></a>
  <div class="row-t">
    {T('h2', f'<a href="{h}">{tp}</a>', f'<a href="{h}">{te}</a>')}
    {T('p', pp, pe)}
    {ul(li)}
    <a class="more" href="{h}"><span data-en="Details">Szczegóły</span>{ARR}</a>
  </div>
</article>''' for h, img, alt, tp, te, pp, pe, li in rows)
oferta = f'''{phead('Oferta', 'Products and services', 'Oferta', 'Products and services',
 'Sprzedajemy hurtowo elektryczne artykuły użytku domowego i kompletujemy dostawy dla inwestycji. Zakres i warunki dopasowujemy do odbiorcy.',
 'We sell electrical household appliances wholesale and put together supplies for building projects. The range and terms are tailored to each client.')}
<section class="sec sec-tight"><div class="wrap rows">{rows_html}</div></section>
{cta('Nie widzisz tego, czego szukasz?', 'Can’t see what you’re looking for?', 'Napisz, jakiego produktu potrzebujesz. Sprawdzimy dostępność i przygotujemy ofertę.', 'Tell us which product you need. We will check availability and prepare a quote.')}'''
page('oferta.html', 'Oferta - LAAS Technology', 'Products and services - LAAS Technology', 'Oferta LAAS Technology: sprzedaż hurtowa, dostawy dla inwestycji, energooszczędność i smart home.', oferta)

def subpage(fname, crumb_pl, crumb_en, h1p, h1e, lp, le, img, alt, blocks, extra=''):
    b = ''
    for hp, he, pp, pe, li in blocks:
        b += f'<div class="blk">{T("h2", hp, he)}{T("p", pp, pe)}{ul(li) if li else ""}</div>'
    others = ''.join(f'<li><a href="{h}" data-en="{e(se)}">{sp}</a></li>' for h, sp, se in OFERTA if h != fname)
    body = f'''{phead(crumb_pl, crumb_en, h1p, h1e, lp, le, img, alt)}
<section class="sec">
  <div class="wrap det">
    <div class="det-m">{b}{extra}</div>
    <aside class="det-a">
      {T('h2', 'Pozostała oferta', 'Other services')}
      <ul>{others}</ul>
      <div class="det-k">
        {T('p', 'Masz pytanie o ten zakres oferty?', 'Questions about this service?')}
        <p class="person-n">Marcin Ostrowski</p>
        <p class="person-r">Project Manager</p>
        <a href="mailto:{EMAIL}">{EMAIL}</a>
      </div>
    </aside>
  </div>
</section>
{cta()}'''
    return body

hurt = subpage('oferta-hurt.html', 'Sprzedaż hurtowa', 'Wholesale', 'Sprzedaż hurtowa', 'Wholesale',
  'Elektryczne artykuły użytku domowego dla sklepów, hurtowni i dystrybutorów - z jednym opiekunem i warunkami dopasowanymi do skali zamówień.',
  'Electrical household appliances for retailers, wholesalers and distributors - with one account manager and terms matched to your order volume.',
  'hurt.jpg', 'Pracownicy magazynu przy regałach z towarem',
  [('Asortyment', 'Product range', 'Oferta obejmuje urządzenia do kuchni i całego domu. Poniżej przykładowy zakres - docelowo uzupełnimy go o aktualne kategorie i marki.', 'The range covers appliances for the kitchen and the whole home. Below is an example scope, to be completed with current categories and brands.',
    [('Duże AGD: lodówki, pralki, zmywarki, piekarniki, płyty grzewcze', 'Large appliances: fridges, washing machines, dishwashers, ovens, hobs'), ('Drobne AGD: czajniki, ekspresy, roboty kuchenne, odkurzacze', 'Small appliances: kettles, coffee machines, food processors, vacuum cleaners'), ('Urządzenia do pielęgnacji i higieny', 'Personal care appliances'), ('Akcesoria i części eksploatacyjne', 'Accessories and consumables')]),
   ('Dla kogo', 'Who it is for', 'Współpracę kierujemy do firm, które kupują regularnie lub w większych ilościach: sklepów stacjonarnych i internetowych, hurtowni regionalnych oraz dystrybutorów.', 'We work with businesses that buy regularly or in larger volumes: high-street and online shops, regional wholesalers and distributors.', None),
   ('Warunki współpracy', 'Terms of cooperation', 'Ceny, minimalne zamówienia i terminy dostaw ustalamy indywidualnie, w zależności od wielkości i regularności zamówień. Każdą ofertę potwierdzamy na piśmie.', 'Prices, minimum order quantities and delivery times are agreed individually, depending on order size and frequency. Every quote is confirmed in writing.', None)])
page('oferta-hurt.html', 'Sprzedaż hurtowa - LAAS Technology', 'Wholesale - LAAS Technology', 'Hurtowa sprzedaż elektrycznych artykułów użytku domowego - LAAS Technology.', hurt)

inw = subpage('oferta-inwestycje.html', 'Dostawy dla inwestycji', 'Supplies for projects', 'Dostawy dla inwestycji', 'Supplies for projects',
  'Wyposażamy w urządzenia całe inwestycje: mieszkania, biura, apartamenty na wynajem. Jedna oferta, jeden harmonogram, jeden opiekun projektu.',
  'We equip entire projects with appliances: apartments, offices, rental units. One quote, one schedule, one project manager.',
  'inwestycje.jpg', 'Kuchnia w zabudowie z płytą indukcyjną i okapem',
  [('Co obejmuje', 'What it covers', 'Przygotowujemy zestawienie urządzeń dla wszystkich lokali w inwestycji i pilnujemy, żeby dostawy pasowały do etapów prac.', 'We prepare an appliance schedule for every unit in the project and make sure deliveries fit the stages of work.',
    [('Dobór urządzeń do standardu wykończenia', 'Selecting appliances to match the fit-out standard'), ('Zestawienie ilościowe i oferta dla całej inwestycji', 'Bill of quantities and a quote for the whole project'), ('Harmonogram dostaw dopasowany do budowy', 'Delivery schedule matched to construction'), ('Uzupełnienia i wymiany po odbiorach', 'Top-ups and replacements after handover')]),
   ('Dla kogo', 'Who it is for', 'Dla deweloperów, generalnych wykonawców, firm wykończeniowych, zarządców najmu krótkoterminowego i obiektów hotelowych.', 'For developers, general contractors, fit-out companies, short-term rental managers and hotels.', None),
   ('Jak pracujemy', 'How we work', 'Projekt prowadzi jeden opiekun - Project Manager, który zna zestawienie, terminy i ustalenia z budowy. Nie trzeba niczego tłumaczyć kilku osobom.', 'The project is run by one Project Manager who knows the schedule, the dates and the site arrangements. No need to explain things to several people.', None)])
page('oferta-inwestycje.html', 'Dostawy dla inwestycji - LAAS Technology', 'Supplies for projects - LAAS Technology', 'Kompletacja i dostawy urządzeń AGD dla inwestycji - LAAS Technology.', inw)

en_ = subpage('oferta-energia.html', 'Energooszczędność i smart home', 'Energy saving and smart home', 'Energooszczędność i smart home', 'Energy saving and smart home',
  'Urządzenia, które zużywają mniej energii, i rozwiązania inteligentnego domu. Pomagamy dobrać sprzęt, który obniża koszty użytkowania.',
  'Appliances that use less energy, and smart home solutions. We help choose equipment that lowers running costs.',
  'smart.jpg', 'Smartfon i urządzenia inteligentnego domu',
  [('Co obejmuje', 'What it covers', 'Łączymy klasyczne AGD z rozwiązaniami, które pozwalają mierzyć i ograniczać zużycie energii.', 'We combine traditional appliances with solutions that let you measure and reduce energy use.',
    [('AGD o wysokiej klasie energetycznej', 'High energy-class appliances'), ('Inteligentne gniazdka z pomiarem zużycia', 'Smart plugs with energy monitoring'), ('Czujniki, włączniki i oświetlenie sterowane z aplikacji', 'App-controlled sensors, switches and lighting'), ('Urządzenia z programami oszczędzania wody i energii', 'Appliances with water and energy saving programmes')]),
   ('Dlaczego to ważne', 'Why it matters', 'Urządzenie pracuje w domu wiele lat. Różnica w zużyciu energii między modelami przekłada się na rachunki przez cały ten czas - warto ją uwzględnić już przy zakupie.', 'An appliance works in a home for many years. The difference in energy use between models shows up in the bills for that whole time, so it is worth considering at purchase.', None),
   ('Pomoc w doborze', 'Help with selection', 'Podpowiemy, które rozwiązania mają sens w danym projekcie lub w ofercie sklepu, i przygotujemy zestawienie z porównaniem.', 'We will advise which solutions make sense for a given project or shop range, and prepare a comparison.', None)])
page('oferta-energia.html', 'Energooszczędność i smart home - LAAS Technology', 'Energy saving and smart home - LAAS Technology', 'Urządzenia energooszczędne i smart home - LAAS Technology.', en_)

# ---------------------------------------------------------------- PARTNERZY
logos8 = ''.join('<li data-en="Brand logo">Logo marki</li>' for _ in range(8))
partn = f'''{phead('Partnerzy', 'Partners', 'Partnerzy', 'Partners',
 'Budujemy współpracę z producentami i dostawcami elektrycznych artykułów użytku domowego oraz z firmami, które je sprzedają i montują.',
 'We build relationships with manufacturers and suppliers of electrical household appliances, and with the companies that sell and install them.', 'partnerzy.jpg', 'Ekspozycja urządzeń kuchennych w sklepie')}
<section class="sec">
  <div class="wrap">
    <div class="sec-h">
      {T('h2', 'Marki w ofercie', 'Brands we carry')}
      {T('p', 'Miejsce na logotypy marek, które dystrybuujemy - uzupełnimy je razem z Państwem.', 'Space for the logos of the brands we distribute - to be filled in together with you.')}
    </div>
    <ul class="logos logos-8">{logos8}</ul>
  </div>
</section>
<section class="sec sec-g">
  <div class="wrap two">
    <div class="blk">
      {T('h2', 'Dla producentów i dostawców', 'For manufacturers and suppliers')}
      {T('p', 'Szukasz dystrybutora dla swoich urządzeń w Polsce? Porozmawiajmy o warunkach i o tym, do jakich odbiorców możemy dotrzeć z Twoją ofertą.', 'Looking for a distributor for your appliances in Poland? Let’s talk about terms and the customers we can reach with your products.')}
    </div>
    <div class="blk">
      {T('h2', 'Dla odbiorców', 'For buyers')}
      {T('p', 'Sklepy, hurtownie i firmy realizujące inwestycje zapraszamy do stałej współpracy. Przygotujemy ofertę dopasowaną do skali i rodzaju zamówień.', 'We invite shops, wholesalers and project companies to work with us on a regular basis. We will prepare an offer suited to the size and type of your orders.')}
    </div>
  </div>
</section>
{cta('Zostań partnerem', 'Become a partner', 'Napisz kilka słów o swojej firmie i ofercie. Odpowiemy z propozycją dalszych kroków.', 'Write a few words about your company and products. We will reply with suggested next steps.')}'''
page('partnerzy.html', 'Partnerzy - LAAS Technology', 'Partners - LAAS Technology', 'Partnerzy LAAS Technology - producenci, dostawcy i odbiorcy.', partn)

# ---------------------------------------------------------------- AKTUALNOŚCI
akt = f'''{phead('Aktualności', 'News', 'Aktualności', 'News',
 'Informacje o firmie, zmianach w ofercie i nowych markach.', 'Company news, changes to our range and new brands.')}
<section class="sec sec-tight">
  <div class="wrap">
    <div class="news news-l">{news_html(list(reversed(news)))}</div>
    {T('p', 'Tu pojawią się kolejne wpisy, np. o nowych markach w ofercie lub zmianach w asortymencie.', 'More posts will appear here, for example about new brands or changes to our range.', 'class="note"')}
  </div>
</section>
{cta()}'''
page('aktualnosci.html', 'Aktualności - LAAS Technology', 'News - LAAS Technology', 'Aktualności LAAS Technology.', akt)

# ---------------------------------------------------------------- KARIERA
kar = f'''{phead('Kariera', 'Careers', 'Kariera', 'Careers',
 'Rozwijamy firmę i chętnie poznajemy ludzi, którzy chcą rozwijać się razem z nami - w handlu, obsłudze klienta i logistyce.',
 'We are growing and keen to meet people who want to grow with us - in sales, customer service and logistics.')}
<section class="sec">
  <div class="wrap split">
    <div class="split-t">
      {T('h2', 'Aktualne ogłoszenia', 'Current openings')}
      {T('p', 'Ogłoszenia rekrutacyjne będą publikowane w tym miejscu, z opisem stanowiska, zakresem obowiązków i sposobem aplikowania.', 'Job postings will be published here, with a description of the role, responsibilities and how to apply.')}
      {T('h2', 'Aplikacja spontaniczna', 'Speculative applications')}
      {T('p', f'Nie widzisz ogłoszenia dla siebie? Wyślij CV na adres <a href="mailto:{EMAIL}">{EMAIL}</a> z dopiskiem „Kariera” i krótką informacją, czym chcesz się zajmować.', f'Don’t see a role for you? Send your CV to <a href="mailto:{EMAIL}">{EMAIL}</a> with “Careers” in the subject and a short note about what you would like to do.')}
      {T('p', 'Do CV dołącz zgodę na przetwarzanie danych osobowych w celu rekrutacji.', 'Please include consent to the processing of your personal data for recruitment purposes.', 'class="note"')}
    </div>
    <figure class="split-ph split-ph-t"><img src="img/kariera.jpg" alt="Kartony z towarem na regale magazynowym" width="1100" height="1650" loading="lazy"></figure>
  </div>
</section>'''
page('kariera.html', 'Kariera - LAAS Technology', 'Careers - LAAS Technology', 'Praca w LAAS Technology.', kar)

# ---------------------------------------------------------------- KONTAKT
kon = f'''{phead('Kontakt', 'Contact', 'Kontakt', 'Contact',
 'Napisz, czego potrzebujesz - odpowiemy z propozycją oferty. Możesz skorzystać z formularza albo napisać bezpośrednio do opiekuna.',
 'Tell us what you need and we will reply with a proposal. Use the form or write directly to your account manager.')}
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
          <option data-en="Wholesale">Sprzedaż hurtowa</option>
          <option data-en="Supplies for projects">Dostawy dla inwestycji</option>
          <option data-en="Energy saving and smart home">Energooszczędność i smart home</option>
          <option data-en="Partnership">Współpraca partnerska</option>
          <option data-en="Other">Inne</option>
        </select>
      </label>
      <label><span data-en="Message">Wiadomość</span><textarea name="w" rows="5" placeholder="Asortyment, ilości, termin i miejsce dostawy" data-en-ph="Products, quantities, date and delivery address"></textarea></label>
      <label class="chk"><input type="checkbox" name="z"><span data-en="I consent to the processing of my data in order to respond to this enquiry.">Wyrażam zgodę na przetwarzanie moich danych w celu odpowiedzi na zapytanie.</span></label>
      <button class="btn" type="submit"><span data-en="Send enquiry">Wyślij zapytanie</span>{ARR}</button>
      <p class="form-msg" id="formMsg" hidden data-en="This is a working draft of the website - the form does not send messages yet.">To wizualizacja robocza strony - formularz jeszcze nie wysyła wiadomości.</p>
    </form>
  </div>
</section>'''
page('kontakt.html', 'Kontakt - LAAS Technology', 'Contact - LAAS Technology', 'Kontakt z LAAS Technology Sp. z o.o., Bobrowiec k. Piaseczna.', kon, mob=False)

print('ok', V)
