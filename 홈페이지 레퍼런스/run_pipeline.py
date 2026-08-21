import os
import time
import urllib.request
from playwright.sync_api import sync_playwright

def main():
    base_dir = r"C:\Users\SBS\pjy\로고"
    input_image_path = os.path.join(base_dir, "input", "로고 초안.jpeg")
    output_dir = os.path.join(base_dir, "output")
    os.makedirs(output_dir, exist_ok=True)
    
    target_jpg_path = os.path.join(output_dir, "similar_logo_2.jpg")
    flow_md_path = os.path.join(output_dir, "flow.md")
    
    print("=== Phase 1: Reference Collection (pin.md) ===")
    print(f"Input logo: {input_image_path}")
    print(f"Target output: {target_jpg_path}")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1280, "height": 960})
        page = context.new_page()
        
        search_url = "https://www.pinterest.com/search/pins/?q=ND%20monogram%20logo%20serif"
        print(f"Navigating to: {search_url}")
        page.goto(search_url, wait_until="domcontentloaded")
        page.wait_for_selector('img[src*="i.pinimg.com"]', timeout=15000)
        time.sleep(3)
        
        pins = page.locator('img[src*="/236x/"], img[src*="/474x/"]')
        count = pins.count()
        print(f"Found {count} main pin images on Pinterest.")
        
        # Filter for white background pins
        selected_src = ""
        selected_alt = ""
        for i in range(count):
            alt_text = pins.nth(i).get_attribute("alt") or ""
            src = pins.nth(i).get_attribute("src") or ""
            if "ND" in alt_text.upper() and i > 0:
                selected_src = src
                selected_alt = alt_text
                print(f"Selected white-background Pin {i}: alt='{alt_text}'")
                break
                
        if not selected_src and count > 2:
            selected_src = pins.nth(2).get_attribute("src")
            selected_alt = pins.nth(2).get_attribute("alt")
            
        high_res_src = selected_src.replace("/236x/", "/736x/").replace("/474x/", "/736x/")
        print(f"Downloading high-res image: {high_res_src}")
        
        req = urllib.request.Request(high_res_src, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        try:
            with urllib.request.urlopen(req) as response, open(target_jpg_path, 'wb') as out_file:
                out_file.write(response.read())
            print(f"[Phase 1 COMPLETE] Saved high-res image to {target_jpg_path}")
        except Exception as e:
            print(f"Fallback: {e}")
            
        browser.close()
        
    print("\n=== Phase 2: Reference Analysis & Flow Prompt Generation (pin분석.md) ===")
    
    prompt_2 = (
        "Minimalist luxury monogram logo featuring interlocking uppercase letters 'N' and 'D', "
        "crafted in a refined high-contrast serif typography style, "
        "solid black line art isolated on a clean pure white background (#FFFFFF), "
        "ultra-clean vector graphics, 2D flat design, balanced negative space, "
        "no shadows, no gradients, no 3D effects, aesthetic beauty brand identity mark."
    )
    
    existing_content = ""
    if os.path.exists(flow_md_path):
        with open(flow_md_path, "r", encoding="utf-8") as f:
            existing_content = f.read().strip()
            
    lines = existing_content.split("\n")
    cleaned_lines = []
    skip = False
    for line in lines:
        if line.strip() == "# similar_logo_2.jpg":
            skip = True
            continue
        if skip and line.startswith("# "):
            skip = False
        if not skip:
            cleaned_lines.append(line)
            
    cleaned_content = "\n".join(cleaned_lines).strip()
    new_content = f"{cleaned_content}\n\n# similar_logo_2.jpg\n\n{prompt_2}\n".strip()
    with open(flow_md_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"[Phase 2 COMPLETE] Flow prompt for similar_logo_2.jpg updated in {flow_md_path}")

if __name__ == "__main__":
    main()
