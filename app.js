(function(){
  var d=document,root=d.documentElement;
  // menu
  var b=d.getElementById('burger'),n=d.getElementById('nav');
  function setMenu(o){n.classList.toggle('open',o);d.body.classList.toggle('menu-open',o);b.setAttribute('aria-expanded',o?'true':'false');b.setAttribute('aria-label',o?(L==='en'?'Close menu':'Zamknij menu'):(L==='en'?'Open menu':'Otwórz menu'))}
  b.addEventListener('click',function(){setMenu(!n.classList.contains('open'))});
  d.addEventListener('keydown',function(e){if(e.key==='Escape')setMenu(false)});
  d.querySelectorAll('.sub-t').forEach(function(t){t.addEventListener('click',function(){t.parentNode.classList.toggle('open')})});

  // język PL / EN
  var L='pl';
  try{L=new URLSearchParams(location.search).get('lang')||localStorage.getItem('laas-lang')||'pl'}catch(e){}
  if(L!=='en')L='pl';
  function apply(l){
    L=l;
    d.querySelectorAll('[data-en]').forEach(function(el){
      if(!el.hasAttribute('data-pl'))el.setAttribute('data-pl',el.innerHTML);
      el.innerHTML=l==='en'?el.getAttribute('data-en'):el.getAttribute('data-pl');
    });
    d.querySelectorAll('[data-en-ph]').forEach(function(el){
      if(!el.hasAttribute('data-pl-ph'))el.setAttribute('data-pl-ph',el.placeholder);
      el.placeholder=l==='en'?el.getAttribute('data-en-ph'):el.getAttribute('data-pl-ph');
    });
    d.querySelectorAll('[data-en-al]').forEach(function(el){
      if(!el.hasAttribute('data-pl-al'))el.setAttribute('data-pl-al',el.getAttribute('aria-label'));
      el.setAttribute('aria-label',l==='en'?el.getAttribute('data-en-al'):el.getAttribute('data-pl-al'));
    });
    root.lang=l;root.classList.toggle('is-en',l==='en');
    d.title=root.getAttribute(l==='en'?'data-title-en':'data-title-pl');
    d.querySelectorAll('.lang button').forEach(function(x){x.setAttribute('aria-pressed',x.getAttribute('data-l')===l?'true':'false')});
    b.setAttribute('aria-label',l==='en'?'Open menu':'Otwórz menu');
  }
  d.querySelectorAll('.lang button').forEach(function(x){x.addEventListener('click',function(){
    var l=x.getAttribute('data-l');apply(l);try{localStorage.setItem('laas-lang',l)}catch(e){}
  })});
  if(L==='en')apply('en');

  // dolny pasek na telefonie: po przewinięciu za przyciski z pierwszego ekranu
  var mob=d.getElementById('mob'),anchor=d.getElementById('heroCta')||d.querySelector('.phead');
  if(mob&&anchor&&'IntersectionObserver' in window){
    var past=false,atCta=false,cta=d.querySelector('.cta');
    var upd=function(){mob.classList.toggle('widac',past&&!atCta)};
    new IntersectionObserver(function(e){past=!e[0].isIntersecting&&e[0].boundingClientRect.top<0;upd()}).observe(anchor);
    if(cta)new IntersectionObserver(function(e){atCta=e[0].isIntersecting;upd()}).observe(cta);
  }

  // formularz: makieta, nic nie wysyła
  var f=d.getElementById('form'),m=d.getElementById('formMsg');
  if(f)f.addEventListener('submit',function(e){e.preventDefault();m.hidden=false;m.scrollIntoView({block:'nearest',behavior:'smooth'})});
})();
