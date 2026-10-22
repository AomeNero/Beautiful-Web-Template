"""Generate 3-view screenshots for Wedding-Events template using Playwright."""
import os
from PIL import Image
from playwright.sync_api import sync_playwright

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(PROJECT_ROOT, "templates", "Wedding-Events")
HTML_FILE = os.path.join(TEMPLATE_DIR, "Wedding-Events.html")
SCREENSHOT_DIR = os.path.join(PROJECT_ROOT, "assets", "screenshots")
WEBP_DIR = os.path.join(SCREENSHOT_DIR, "webp")

os.makedirs(SCREENSHOT_DIR, exist_ok=True)
os.makedirs(WEBP_DIR, exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1440, "height": 900})
    page.goto(f"file:///{os.path.abspath(HTML_FILE).replace(chr(92), '/')}", wait_until="domcontentloaded")
    page.wait_for_timeout(3000)

    full_height = page.evaluate("document.documentElement.scrollHeight")
    print(f"Full page height: {full_height}px")

    # Resize viewport to full page height so clips work
    page.set_viewport_size({"width": 1440, "height": full_height})
    page.wait_for_timeout(1000)

    third = full_height // 3

    shots = [
        ("Wedding-Events-01.png", 0, third),
        ("Wedding-Events-02.png", third, third * 2),
        ("Wedding-Events-03.png", third * 2, full_height),
    ]

    for name, top, bottom in shots:
        clip = {"x": 0, "y": top, "width": 1440, "height": bottom - top}
        path = os.path.join(SCREENSHOT_DIR, name)
        page.screenshot(path=path, clip=clip, type="png")
        print(f"Saved: {path}")

        webp_path = os.path.join(WEBP_DIR, name.replace(".png", ".webp"))
        img = Image.open(path)
        img.save(webp_path, "WEBP", quality=85)
        print(f"Saved: {webp_path}")

    browser.close()

print("Done!")
