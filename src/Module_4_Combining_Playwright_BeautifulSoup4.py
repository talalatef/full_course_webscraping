from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

def scrape_dynamic_site():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto('https://waya.media/arabi/')
        
        # Wait for dynamic content
        page.wait_for_selector('.dynamic-content')
        
        # Get HTML after JavaScript execution
        html = page.content()
        
        # Parse with BeautifulSoup
        soup = BeautifulSoup(html, 'lxml')
        
        # Extract data
        items = soup.find_all('div', class_='item')
        data = []
        for item in items:
            title = item.find('h2').text.strip()
            price = item.find('span', class_='price').text.strip()
            data.append({'title': title, 'price': price})
        
        browser.close()
        return data

results = scrape_dynamic_site()
print(results)