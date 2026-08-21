import os
import time
import hashlib
import urllib.request
from playwright.sync_api import sync_playwright

def get_image_hash(filepath):
    with open(filepath, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()

def main():
    base_dir = r"C:\Users\SBS\pjy\로고"
    output_dir = os.path.join(base_dir, "output")
    os.makedirs(output_dir, exist_ok=True)
    
    flow_md_path = os.path.join(output_dir, "flow.md")
    
    print("=== DEDUPLICATION & UNIQUE REFERENCE COLLECTION ===")
    
    # Queries to gather diverse pin candidates
    queries = [
        "https://www.pinterest.com/search/pins/?q=ND%20monogram%20logo%20serif",
        "https://www.pinterest.com/search/pins/?q=ND%20initials%20logo%20design%20minimalist",
        "https://www.pinterest.com/search/pins/?q=N%20D%20lettermark%20logo%20black%20white",
        "https://www.pinterest.com/search/pins/?q=ND%20interlocking%20logo%20brand"
    ]
    
    candidate_urls = []
    seen_urls = set()
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1280, "height": 960})
        page = context.new_page()
        
        for q in queries:
            print(f"Searching: {q}")
            page.goto(q, wait_until="domcontentloaded")
            try:
                page.wait_for_selector('img[src*="i.pinimg.com"]', timeout=15000)
            except Exception:
                pass
            time.sleep(2.5)
            
            pins = page.locator('img[src*="/236x/"], img[src*="/474x/"]')
            count = pins.count()
            print(f"Found {count} pins for query.")
            
            for i in range(count):
                src = pins.nth(i).get_attribute("src") or ""
                alt = pins.nth(i).get_attribute("alt") or ""
                
                # Filter out profile icons / low res avatars
                if "/60x60/" in src or "/75x75/" in src:
                    continue
                    
                # Clean URL stem to avoid duplicates
                stem = src.split("/")[-1]
                if stem not in seen_urls:
                    seen_urls.add(stem)
                    candidate_urls.append((src, alt))
                    
        browser.close()
        
    print(f"\nTotal unique pin candidates found: {len(candidate_urls)}")
    
    # Download 5 unique images
    downloaded_hashes = set()
    unique_saved = []
    
    idx = 1
    for src, alt in candidate_urls:
        if idx > 5:
            break
            
        high_res_src = src.replace("/236x/", "/736x/").replace("/474x/", "/736x/")
        filename = f"similar_logo_{idx}.jpg"
        temp_path = os.path.join(output_dir, f"temp_{idx}.jpg")
        final_path = os.path.join(output_dir, filename)
        
        req = urllib.request.Request(high_res_src, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        try:
            with urllib.request.urlopen(req) as response, open(temp_path, 'wb') as out_file:
                out_file.write(response.read())
                
            file_hash = get_image_hash(temp_path)
            if file_hash in downloaded_hashes:
                print(f"Skipping duplicate image content for candidate {src}")
                os.remove(temp_path)
                continue
                
            downloaded_hashes.add(file_hash)
            if os.path.exists(final_path):
                os.remove(final_path)
            os.rename(temp_path, final_path)
            print(f"[SUCCESS {idx}/5] Saved distinct image: {filename} (Hash: {file_hash[:8]})")
            unique_saved.append((filename, alt, high_res_src))
            idx += 1
        except Exception as e:
            print(f"Failed to download {high_res_src}: {e}")
            if os.path.exists(temp_path):
                os.remove(temp_path)

    print(f"\nSuccessfully downloaded {len(unique_saved)} completely unique images!")
    
    # Now generate distinct prompts for all 5 images
    prompts = {
        "similar_logo_1.jpg": (
            "Minimalist luxury monogram logo featuring intertwined letters 'N' and 'D', "
            "designed in a classic serif style with elegant thin and thick contrast strokes, "
            "solid flat black line art on a pure white background (#FFFFFF), ultra-clean vector graphic, "
            "balanced negative space, no drop shadows, no gradients, no 3D effects, clean beauty brand identity."
        ),
        "similar_logo_2.jpg": (
            "Refined typography monogram combining uppercase 'N' and 'D' in a delicate serif font, "
            "vertical alignment with subtle arc curves, monochrome black graphic mark isolated on a stark white backdrop (#FFFFFF), "
            "flat 2D vector style, high visual contrast, elegant cosmetics logo, no textures, no mockups."
        ),
        "similar_logo_3.jpg": (
            "Modern geometric serif monogram design for initials 'N' and 'D', "
            "bold vertical stems with sharp serif feet and flowing curve loops, "
            "solid black emblem centered on a clean white background (#FFFFFF), "
            "2D flat vector aesthetic, crisp lines, luxury skincare brand identity, no gradients, no 3D rendering."
        ),
        "similar_logo_4.jpg": (
            "Clean aesthetic lettermark logo combining letters 'N' and 'D' into a single emblem, "
            "minimalist serif typography with sleek stroke balance, solid black line art on pure white (#FFFFFF), "
            "flat graphic design, timeless elegance, high contrast ratio, no background texture, no shadows."
        ),
        "similar_logo_5.jpg": (
            "Sophisticated beauty brand monogram featuring overlapping initials 'N' and 'D', "
            "crafted with ultra-thin serif accents and graceful curved outlines, "
            "flat black vector icon on a pure white backdrop (#FFFFFF), minimal 2D layout, "
            "effortless elegance, no gradients, no drop shadows, no 3D mockups."
        )
    }
    
    flow_content = []
    for item in unique_saved:
        fname = item[0]
        prompt = prompts.get(fname, prompts["similar_logo_1.jpg"])
        flow_content.append(f"# {fname}\n\n{prompt}")
        
    with open(flow_md_path, "w", encoding="utf-8") as f:
        f.write("\n\n".join(flow_content) + "\n")
        
    print(f"[COMPLETE] Rewrote {flow_md_path} with 5 distinct English Flow prompts.")

if __name__ == "__main__":
    main()
