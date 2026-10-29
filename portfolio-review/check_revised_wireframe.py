from pathlib import Path
import sys, json
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'.portfolio-tools'))
from playwright.sync_api import sync_playwright
from PIL import Image
OUT=ROOT/'누니드_브랜딩_포트폴리오'
stem='브랜딩 포폴 프로세스 와이어프레임'
with sync_playwright() as p:
    browser=p.chromium.launch(executable_path='C:/Program Files/Google/Chrome/Application/chrome.exe',headless=True)
    page=browser.new_page(viewport={'width':1920,'height':1144},device_scale_factor=1)
    errors=[]
    page.on('pageerror',lambda e:errors.append(str(e)))
    page.goto((OUT/(stem+'.html')).as_uri())
    page.evaluate('document.fonts.ready')
    for i in range(22):
        page.locator('.slide').nth(i).screenshot(path=str(OUT/'미리보기'/(stem+f'_{i+1:02}.png')))
    page.screenshot(path=str(OUT/'미리보기'/'와이어프레임_세로전체.png'),full_page=True)
    page.pdf(path=str(OUT/(stem+'.pdf')),prefer_css_page_size=True,print_background=True)
    from pypdf import PdfReader
    pdf=PdfReader(OUT/(stem+'.pdf'))
    assert len(pdf.pages)==25, len(pdf.pages)
    assert all(abs(float(p.mediabox.width)-1440)<1 and abs(float(p.mediabox.height)-810)<1 for p in pdf.pages)
    checks=[]
    for width in [1500,850,390]:
        page.set_viewport_size({'width':width,'height':1000})
        page.wait_for_timeout(100)
        checks.append({'width':width,'scrollWidth':page.evaluate('document.documentElement.scrollWidth')})
    assert not errors,errors
    assert all(c['scrollWidth']<=c['width'] for c in checks),checks
    (OUT/'와이어프레임_수정검증.json').write_text(json.dumps({'browser_errors':errors,'widths':checks},indent=2),encoding='utf-8')
    browser.close()
im=Image.open(OUT/'미리보기'/'와이어프레임_세로전체.png').convert('RGB')
im.thumbnail((1440,40000))
im.save(OUT/(stem+'_전체보기.jpg'),quality=85)
print(checks)
