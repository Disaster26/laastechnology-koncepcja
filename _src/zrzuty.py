import sys, pathlib, json
from playwright.sync_api import sync_playwright
EXE = r'C:/Users/Admin/AppData/Local/ms-playwright/chromium_headless_shell-1228/chrome-headless-shell-win64/chrome-headless-shell.exe'
root = pathlib.Path(__file__).resolve().parent.parent
out = root / '_zrzuty'; out.mkdir(exist_ok=True)
pages = ['index', 'o-nas', 'oferta', 'oferta-hurt', 'oferta-inwestycje', 'oferta-energia', 'partnerzy', 'aktualnosci', 'kariera', 'kontakt']
only = sys.argv[1].split(',') if len(sys.argv) > 1 and sys.argv[1] != 'all' else pages
sizes = [(390, 844), (1440, 900)]
extra = [(360, 640), (412, 915), (1280, 720), (1024, 768)]
CHECK = r'''() => {
  const hero=document.querySelector('.hero');
  const h1=document.querySelector('h1');const rg=document.createRange();rg.selectNodeContents(h1);
  const over=[...document.querySelectorAll('body *')].filter(e=>{if(e.closest('.nav')||e.closest('svg')||e.closest('.mob'))return false;const r=e.getBoundingClientRect();return r.width&&(r.right>innerWidth+1||r.left<-1)}).map(e=>e.tagName+'.'+e.className).slice(0,5);
  const navs=[...document.querySelectorAll('.nav>ul>li')].filter(a=>a.offsetParent&&getComputedStyle(document.querySelector('.nav')).position!=='fixed');
  const navRow=navs.every(a=>Math.abs(a.getBoundingClientRect().top-navs[0].getBoundingClientRect().top)<14);
  const ph=document.querySelector('.hero-ph');
  return {sw:document.documentElement.scrollWidth, iw:innerWidth, ih:innerHeight,
    heroBottom: hero?Math.round(hero.getBoundingClientRect().bottom):null,
    ctaBottom: document.querySelector('#heroCta')?Math.round(document.querySelector('#heroCta').getBoundingClientRect().bottom):null,
    fotoH: ph?Math.round(ph.getBoundingClientRect().height):null,
    h1r:Math.round(rg.getBoundingClientRect().right), navRow, over,
    fonts:document.fonts.check('700 20px Archivo')&&document.fonts.check('400 16px "IBM Plex Sans"')}}'''
with sync_playwright() as p:
    br = p.chromium.launch(executable_path=EXE)
    for name in only:
        url = root.joinpath(name + '.html').as_uri()
        for w, h in sizes + (extra if name == 'index' else []):
            pg = br.new_page(viewport={'width': w, 'height': h}, device_scale_factor=1)
            errs = []
            pg.on('console', lambda m: errs.append(m.text) if m.type == 'error' else None)
            pg.on('pageerror', lambda e: errs.append(str(e)))
            pg.goto(url, wait_until='networkidle')
            pg.evaluate("document.querySelectorAll('img').forEach(i=>i.loading='eager')")
            pg.evaluate("async()=>{for(let y=0;y<document.body.scrollHeight;y+=600){scrollTo(0,y);await new Promise(r=>setTimeout(r,30))}scrollTo(0,0)}")
            pg.wait_for_timeout(1200)
            r = pg.evaluate(CHECK)
            print(name, w, h, json.dumps(r, ensure_ascii=False), 'ERR' if errs else '', errs[:3])
            tag = f'{name}_{w}x{h}'
            pg.screenshot(path=str(out / f'{tag}_ekran1.png'))
            if (w, h) in sizes:
                pg.add_style_tag(content='.mob{display:none!important}.top{position:relative!important}')
                pg.screenshot(path=str(out / f'{tag}_full.png'), full_page=True)
            if name == 'index' and w == 390:
                pg.evaluate("document.querySelectorAll('style').forEach(x=>{if(x.textContent.includes('.mob{display:none'))x.remove()})")
                pg.click('#burger'); pg.wait_for_timeout(300)
                pg.click('.sub-t'); pg.wait_for_timeout(200)
                pg.screenshot(path=str(out / '390_menu.png'))
                pg.click('#burger')
                pg.click('.lang button[data-l=en]'); pg.wait_for_timeout(300)
                pg.evaluate("scrollTo(0,0)")
                print('EN', json.dumps(pg.evaluate(CHECK)))
                pg.screenshot(path=str(out / 'index_390_EN_ekran1.png'))
                pg.evaluate("scrollTo(0,1400)"); pg.wait_for_timeout(500)
                pg.screenshot(path=str(out / '390_pasek.png'))
            if name == 'index' and w == 1440:
                pg.click('.lang button[data-l=en]'); pg.wait_for_timeout(300)
                pg.add_style_tag(content='.top{position:relative!important}')
                pg.screenshot(path=str(out / 'index_1440_EN_full.png'), full_page=True)
                pg.click('.lang button[data-l=pl]')
                pg.hover('.has-sub>a'); pg.wait_for_timeout(300)
                pg.screenshot(path=str(out / '1440_dropdown.png'))
            if name == 'kontakt' and w == 1440:
                pg.click('#form button'); pg.wait_for_timeout(400)
                pg.screenshot(path=str(out / '1440_kontakt_form.png'))
            pg.close()
    br.close()
