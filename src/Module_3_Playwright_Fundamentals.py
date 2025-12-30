from playwright.sync_api import sync_playwright

def interact_with_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto('https://google.com')
        
        # Wait for the search input to be visible
        page.wait_for_selector('textarea[name="q"], input[name="q"]', state='visible')
        
        # Click elements
        # page.click('button#composeButton')
        
        # Fill forms - Google uses name="q" for search input
        page.fill('textarea[name="q"], input[name="q"]', 'playwright')
        
        # Press keys
        page.press('textarea[name="q"], input[name="q"]', 'Enter')
        
        # Wait for search results to load
        page.wait_for_load_state('networkidle')
        
        # Screenshot
        page.screenshot(path='screenshot.png')
        
        browser.close()

interact_with_page()