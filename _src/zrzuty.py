# Testy + zrzuty: wszystkie podstrony PL i EN, 6 rozmiarów (telefony: Android UA, DPR 2.625)
# python _src/zrzuty.py all [base_url]
import sys, pathlib, json
from playwright.sync_api import sync_playwright
EXE = r'C:/Users/Admin/AppData/Local/ms-playwright/chromium_headless_shell-1228/chrome-headless-shell-win64/chrome-headless-shell.exe'
root = pathlib.Path(__file__).resolve().parent.parent
base = sys.argv[2] if len(sys.argv) > 2 and sys.argv[2] != '_' else None
out = root / ('_zrzuty_live' if base else '_zrzuty'); out.mkdir(exist_ok=True)
pages = ['index', 'o-nas', 'oferta', 'oferta-energia', 'oferta-inwestycje', 'oferta-hurt', 'partnerzy', 'aktualnosci', 'kariera', 'kontakt']
only = sys.argv[1].split(',') if len(sys.argv) > 1 and sys.argv[1] != 'all' else pages
langs = sys.argv[3].split(',') if len(sys.argv) > 3 else ['pl', 'en']
PH = [(360, 640), (390, 844), (412, 915)]
PC = [(1280, 720), (1440, 900), (1920, 1080)]
UA = 'Mozilla/5.0 (Linux; Android 14; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Mobile Safari/537.36'
CHECK = r'''() => {
  const iw=innerWidth, ih=innerHeight;
  const hero=document.querySelector('.hero');
  const h1=document.querySelector('h1');const rg=document.createRange();rg.selectNodeContents(h1);const hr=rg.getBoundingClientRect();
  const skip=e=>e.closest('.nav')||e.closest('svg')||e.closest('.mob')||e.closest('.hero-ph')||e.closest('.phead-ph')||e.classList.contains('hero')||e.classList.contains('phead');
  const over=[...document.querySelectorAll('body *')].filter(e=>{if(skip(e))return false;const r=e.getBoundingClientRect();return r.width&&(r.right>iw+1||r.left<-1)}).map(e=>e.tagName+'.'+e.className).slice(0,5);
  const marg=iw<1000?[...document.querySelectorAll('main p, main h1, main h2, main h3, main li, main label, main .btn, footer p, footer li')].filter(e=>{if(!e.offsetParent)return false;const r=e.getBoundingClientRect();return r.width&&(r.left<15.5||r.right>iw-15.5)}).map(e=>e.tagName+'.'+e.className+':'+Math.round(e.getBoundingClientRect().left)).slice(0,5):[];
  const navs=[...document.querySelectorAll('.nav>ul>li')].filter(a=>a.offsetParent&&getComputedStyle(document.querySelector('.nav')).position!=='fixed');
  const navRow=navs.every(a=>Math.abs(a.getBoundingClientRect().top-navs[0].getBoundingClientRect().top)<14);
  const ph=document.querySelector('.hero-ph,.phead-ph');
  const imgs=[...document.images].filter(i=>!i.complete||!i.naturalWidth).map(i=>i.currentSrc||i.src);
  const kbtn=document.querySelector('.nav-k .btn');const kb=kbtn&&getComputedStyle(document.querySelector('.nav')).position!=='fixed'?kbtn.getBoundingClientRect():null;
  return {sw:document.documentElement.scrollWidth, iw, ih,
    heroBottom: hero?Math.round(hero.getBoundingClientRect().bottom):null,
    ctaBottom: document.querySelector('#heroCta')?Math.round(document.querySelector('#heroCta').getBoundingClientRect().bottom):null,
    foto: ph?Math.round(ph.getBoundingClientRect().width)+'x'+Math.round(ph.getBoundingClientRect().height):null,
    h1ok: hr.right<=iw+0.5 && hr.left>=0, navRow, over, marg, badImg:imgs,
    kontaktBtn: kb?(kb.right<=iw && kb.bottom<=ih):null,
    fonts:document.fonts.check('600 20px "Plus Jakarta Sans"')&&document.fonts.check('400 16px "IBM Plex Sans"')}}'''
bad = 0
with sync_playwright() as p:
    br = p.chromium.launch(executable_path=EXE)
    for lang in langs:
        for name in only:
            url = (base + name + '.html' if base else root.joinpath(name + '.html').as_uri()) + ('?lang=en' if lang == 'en' else '')
            for w, h in PH + PC:
                mobile = w < 1000
                ctx = br.new_context(viewport={'width': w, 'height': h}, device_scale_factor=2.625 if mobile else 1,
                                     user_agent=UA if mobile else None, is_mobile=mobile, has_touch=mobile)
                pg = ctx.new_page()
                errs = []
                pg.on('console', lambda m: errs.append(m.text) if m.type == 'error' else None)
                pg.on('pageerror', lambda e: errs.append(str(e)))
                pg.goto(url, wait_until='networkidle')
                pg.evaluate("document.querySelectorAll('img').forEach(i=>i.loading='eager')")
                pg.evaluate("async()=>{for(let y=0;y<document.body.scrollHeight;y+=600){scrollTo(0,y);await new Promise(r=>setTimeout(r,25))}scrollTo(0,0)}")
                pg.wait_for_timeout(700)
                r = pg.evaluate(CHECK)
                prob = []
                if r['sw'] > w: prob.append('OVERFLOW')
                if r['over']: prob.append('over')
                if r['marg']: prob.append('marg')
                if not r['h1ok']: prob.append('h1')
                if r['badImg']: prob.append('img')
                if not r['fonts']: prob.append('fonts')
                if not r['navRow']: prob.append('nav2rows')
                if r['kontaktBtn'] is False: prob.append('kontaktBtn')
                if name == 'index' and abs(r['heroBottom'] - h) > 1: prob.append('heroBottom')
                if errs: prob.append('ERR')
                if prob: bad += 1
                print(lang, name, w, h, 'OK' if not prob else 'PROBLEM ' + ','.join(prob), json.dumps(r, ensure_ascii=False) if prob else f"hero={r['heroBottom']} cta={r['ctaBottom']} foto={r['foto']}", errs[:2], flush=True)
                tag = f'{name}_{lang}_{w}x{h}'
                pg.screenshot(path=str(out / f'{tag}_ekran1.png'))
                if (w, h) in [(390, 844), (1440, 900)]:
                    pg.add_style_tag(content='.mob{display:none!important}.top{position:relative!important}')
                    pg.screenshot(path=str(out / f'{tag}_full.png'), full_page=True)
                    pg.evaluate("document.querySelectorAll('style').forEach(x=>{if(x.textContent.includes('.mob{display:none'))x.remove()})")
                if name == 'index' and (w, h) == (390, 844) and lang == 'pl':
                    pg.click('#burger'); pg.wait_for_timeout(300)
                    pg.click('.sub-t'); pg.wait_for_timeout(200)
                    pg.screenshot(path=str(out / '390_menu.png'))
                    pg.click('#burger')
                    pg.evaluate("scrollTo(0,1600)"); pg.wait_for_timeout(500)
                    print('  pasek widac:', pg.evaluate("document.getElementById('mob').classList.contains('widac')"))
                    pg.screenshot(path=str(out / '390_pasek.png'))
                if name == 'index' and (w, h) == (1440, 900) and lang == 'pl':
                    pg.hover('.has-sub>a'); pg.wait_for_timeout(300)
                    pg.screenshot(path=str(out / '1440_dropdown.png'))
                    pg.click('.lang button[data-l=en]'); pg.wait_for_timeout(300)
                    print('  EN alt:', pg.evaluate("document.querySelector('.hero-ph img').alt"))
                if name == 'kontakt' and (w, h) == (1440, 900) and lang == 'pl':
                    pg.click('#form button'); pg.wait_for_timeout(400)
                    pg.screenshot(path=str(out / '1440_kontakt_form.png'))
                ctx.close()
    br.close()
print('PROBLEMOW:', bad)
