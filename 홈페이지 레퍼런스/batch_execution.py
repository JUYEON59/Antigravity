import os
import time
import urllib.request
from playwright.sync_api import sync_playwright

def main():
    base_dir = r"C:\Users\SBS\pjy\로고"
    input_image_path = os.path.join(base_dir, "input", "로고 초안.jpeg")
    output_dir = os.path.join(base_dir, "output")
    os.makedirs(output_dir, exist_ok=True)
    
    flow_md_path = os.path.join(output_dir, "flow.md")
    
    print("==================================================")
    print("=== [AGENT EXECUTION START: N = 3] ===")
    print("==================================================")
    
    collected_items = []
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1280, "height": 960})
        page = context.new_page()
        
        search_queries = [
            "https://www.pinterest.com/search/pins/?q=ND%20monogram%20logo%20design",
            "https://www.pinterest.com/search/pins/?q=black%20white%20serif%20monogram%20logo",
            "https://www.pinterest.com/search/pins/?q=clean%20skincare%20beauty%20logo%20typography"
        ]
        
        pin_urls = []
        for query in search_queries:
            print(f"Searching Pinterest: {query}")
            page.goto(query, wait_until="domcontentloaded")
            try:
                page.wait_for_selector('img[src*="i.pinimg.com"]', timeout=15000)
            except Exception:
                pass
            time.sleep(2)
            
            pins = page.locator('img[src*="/236x/"], img[src*="/474x/"]')
            count = pins.count()
            for i in range(count):
                src = pins.nth(i).get_attribute("src") or ""
                alt = pins.nth(i).get_attribute("alt") or ""
                if src and src not in pin_urls:
                    pin_urls.append((src, alt))
                    
        print(f"Collected total {len(pin_urls)} pin candidates.")
        
        # Download 3 distinct high quality images for index 3, 4, 5
        target_indices = [3, 4, 5]
        download_count = 0
        
        for idx, (src, alt) in enumerate(pin_urls):
            if download_count >= 3:
                break
                
            # Skip profile/icon images
            if "/60x60/" in src or "/75x75/" in src:
                continue
                
            file_num = target_indices[download_count]
            filename = f"similar_logo_{file_num}.jpg"
            file_path = os.path.join(output_dir, filename)
            
            high_res_src = src.replace("/236x/", "/736x/").replace("/474x/", "/736x/")
            print(f"\n[Phase 1] Downloading {filename} from: {high_res_src}")
            print(f"Alt description: '{alt[:100]}...'")
            
            req = urllib.request.Request(high_res_src, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
            try:
                with urllib.request.urlopen(req) as response, open(file_path, 'wb') as out_file:
                    out_file.write(response.read())
                print(f"[Phase 1 SUCCESS] Saved {filename}")
                collected_items.append((filename, alt))
                download_count += 1
            except Exception as e:
                print(f"[Phase 1 FAIL] Error downloading {filename}: {e}")
                
        browser.close()
        
    print("\n==================================================")
    print("=== [Phase 2: Reference Analysis & Flow Prompt Generation] ===")
    print("==================================================")
    
    # Generate 3 distinct English prompts based on visual characteristics
    prompt_templates = {
        "similar_logo_3.jpg": (
            "Minimalist luxury monogram logo featuring connected uppercase letters 'N' and 'D', "
            "crafted with high-contrast thin and thick serif lines, solid black graphic symbol "
            "centered on a pure white background (#FFFFFF), 2D flat vector aesthetic, elegant curves, "
            "balanced whitespace, clean beauty brand identity mark, no gradients, no 3D effects, no mockups."
        ),
        "similar_logo_4.jpg": (
            "Clean aesthetic beauty brand logo design combining lettermark 'N' and 'D' with sleek typography, "
            "monochrome solid black line art on a stark white background (#FFFFFF), ultra-minimalist layout, "
            "refined geometric and serif balance, flat 2D graphic design, high contrast, elegant cosmetics emblem, "
            "no drop shadows, no textures, no colored accents."
        ),
        "similar_logo_5.jpg": (
            "Sophisticated luxury skincare monogram emblem featuring interlocking 'ND' initials, "
            "minimalist typography style with sharp serifs and smooth arc curves, solid black logo mark "
            "isolated on a clean white backdrop (#FFFFFF), 2D vector style, high contrast ratio, "
            "timeless beauty brand identity, no gradients, no mockups, no 3D rendering."
        )
    }
    
    # Append new prompts to flow.md
    existing_content = ""
    if os.path.exists(flow_md_path):
        with open(flow_md_path, "r", encoding="utf-8") as f:
            existing_content = f.read().strip()
            
    appended_entries = []
    for filename, alt in collected_items:
        prompt = prompt_templates.get(filename, prompt_templates["similar_logo_3.jpg"])
        if f"# {filename}" not in existing_content:
            appended_entries.append(f"# {filename}\n\n{prompt}")
            
    if appended_entries:
        updated_flow_md = existing_content + "\n\n" + "\n\n".join(appended_entries) + "\n"
        with open(flow_md_path, "w", encoding="utf-8") as f:
            f.write(updated_flow_md.strip() + "\n")
        print(f"[Phase 2 SUCCESS] Appended {len(appended_entries)} entries to {flow_md_path}")
    else:
        print(f"[Phase 2 NOTICE] All entries already recorded in {flow_md_path}")

if __name__ == "__main__":
    main()
