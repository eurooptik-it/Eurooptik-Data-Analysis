# scraper.py
import undetected_chromedriver as uc
from bs4 import BeautifulSoup

def scrape_smartbuy(product_query: str) -> dict:
    details = {
        "Color": "N/A",
        "Gender": "N/A",
        "Shape": "N/A",
        "Price": "N/A",
        "Error": None
    }
    
    driver = None  
    try:
        options = uc.ChromeOptions()
        options.add_argument("--headless") 
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        driver = uc.Chrome(options=options, use_subprocess=True)

        search_url = f"https://www.smartbuyglasses.com/search?q={product_query.replace(' ', '+')}"
        driver.get(search_url)

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        
        product_link_element = soup.select_one("a.product-block__image-link")

        if not product_link_element:
            details["Error"] = "Product not found on site"
            return details

        product_url = "https://www.smartbuyglasses.com" + product_link_element['href']
        driver.get(product_url)
        
        product_soup = BeautifulSoup(driver.page_source, 'html.parser')
        spec_items = product_soup.select("div.pro-technical-specification-item")

        for item in spec_items:
            title_element = item.select_one("div.title-wrapper")
            info_element = item.select_one(".specification-info")
            if title_element and info_element:
                title = title_element.get_text(strip=True).replace(':', '')
                info = info_element.get_text(strip=True)
                if title == "Frame Color": details["Color"] = info
                elif title == "Gender": details["Gender"] = info
                elif title == "Frame Shape": details["Shape"] = info

        price_element = product_soup.select_one("span.product-price-info-display")
        if price_element:
            details["Price"] = price_element.get_text(strip=True)

    except Exception as e:
        details["Error"] = f"An error occurred: {e}"
    finally:
        if driver:
            driver.quit()
            
    return details