from pathlib import Path
import sys,json
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'.portfolio-tools'))
from playwright.sync_api import sync_playwright
from pypdf import PdfReader
from PIL import Image,ImageDraw
OUT=ROOT/'누니드_브랜딩_포트폴리오'
PRE=OUT/'미리보기'
PRE.mkdir(exist_ok=True)
results=[]
with sync_playwright() as p:
    browser=p.chromium.launch(executable_path='C:/Program Files/Google/Chrome/Application/chrome.exe',headless=True)
    page=browser.new_page(viewport={'width':1660,'height':1120},device_scale_factor=1)
    errors=[]
    page.on('pageerror',lambda err:errors.append(str(err)))
    for path in sorted(OUT.glob('*.html')):
        page.goto(path.as_uri(),wait_until='load')
        page.evaluate('document.fonts.ready')
        count=page.locator('.slide').count()
        assert count==22
        bounds=page.evaluate('''()=>[...document.querySelectorAll('.slide')].map((s,i)=>{const foot=s.querySelector('.foot').getBoundingClientRect();const content=[...s.querySelectorAll('.body h3,.body p,.body article,.phone,.browser,.closing,.coverbottom,.guidebottom,.conceptdetails,.flowinsight')].map(x=>x.getBoundingClientRect());return {page:i+1,bottom:Math.max(...content.map(r=>r.bottom))-s.getBoundingClientRect().top,limit:foot.top-s.getBoundingClientRect().top}})''')
        page.locator('.toolbar').evaluate("el=>el.style.visibility='hidden'")
        for i in range(22):
            page.locator('.slide').nth(i).screenshot(path=str(PRE/(path.stem+f'_{i+1:02}.png')))
        page.locator('.toolbar').evaluate("el=>el.style.visibility='visible'")
        page.select_option('select','page-14')
        page.wait_for_function('Math.abs(document.querySelector("#page-14").getBoundingClientRect().top)<100',timeout=10000)
        page.pdf(path=str(OUT/(path.stem+'.pdf')),prefer_css_page_size=True,print_background=True,display_header_footer=False)
        pdf=PdfReader(OUT/(path.stem+'.pdf'))
        assert len(pdf.pages)==22, len(pdf.pages)
        page.set_viewport_size({'width':390,'height':844})
        page.wait_for_timeout(100)
        assert page.evaluate('document.documentElement.scrollWidth <= innerWidth+1')
        page.set_viewport_size({'width':1660,'height':1120})
        results.append({'file':path.name,'pages':count,'pdf_pages':len(pdf.pages),'content_bounds':bounds})
    browser.close()
assert not errors,errors
(OUT/'검증.json').write_text(json.dumps({'results':results,'browser_errors':errors},ensure_ascii=False,indent=2),encoding='utf-8')
for title in [p.stem for p in OUT.glob('*.html')]:
    sheet=Image.new('RGB',(1600,1800),'#deded8')
    for i in range(22):
        im=Image.open(PRE/(title+f'_{i+1:02}.png'));im.thumbnail((390,244));x=(i%4)*400;y=(i//4)*300;sheet.paste(im,(x,y));ImageDraw.Draw(sheet).text((x+12,y+252),f'{i+1:02}',fill='black')
    sheet.save(OUT/(title+'_전체보기.jpg'))
print(json.dumps({'pages_per_version':22,'pdfs':2,'browser_errors':errors,'overlap_candidates':[{ 'file':r['file'],'pages':[b for b in r['content_bounds'] if b['bottom']>b['limit']-8]} for r in results]},ensure_ascii=True))
