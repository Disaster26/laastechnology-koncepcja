import re,json,sys,urllib.request,os
UA={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36'}
out=json.load(open('pexels_res.json',encoding='utf-8')) if os.path.exists('pexels_res.json') else {}
for q in sys.argv[1:]:
    import subprocess
    h=subprocess.run(['curl','-s','-A',UA['User-Agent'],'https://www.pexels.com/search/'+q.replace(' ','%20')+'/'],capture_output=True).stdout.decode('utf-8')
    m=re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>',h,re.S)
    import time; time.sleep(9)
    if not m:
        print('FAIL',q,len(h)); continue
    d=json.loads(m.group(1))
    res=[]
    def walk(o):
        if isinstance(o,dict):
            a=o.get('attributes')
            if isinstance(a,dict) and 'alt' in a and 'image' in a:
                res.append({'id':a.get('id'),'alt':a.get('alt'),'w':a.get('width'),'h':a.get('height'),'user':(a.get('user') or {}).get('first_name','')+' '+((a.get('user') or {}).get('last_name') or ''),'slug':a.get('slug'),'img':a['image'].get('download_link') if isinstance(a['image'],dict) else None})
            for v in o.values(): walk(v)
        elif isinstance(o,list):
            for v in o: walk(v)
    walk(d)
    out[q]=res[:14]
    for r in res[:14]: print(q,'|',r['id'],r['w'],r['h'],r['user'],'|',r['alt'])
json.dump(out,open('pexels_res.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
