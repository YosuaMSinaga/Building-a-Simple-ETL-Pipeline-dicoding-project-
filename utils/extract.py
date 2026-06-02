import requests
from bs4 import BeautifulSoup
from datetime import datetime

def scrape_collection_data(base_url):
    products = []
    for page in range(1, 51):
        if page == 1:
            url = base_url
        else:
            url = f"{base_url}/page{page}"
        
        print(f"Scraping: {url}")
        
        try:
            response = requests.get(url, timeout=10)
            if response.status_code != 200:
                print(f"Selesai di halaman {page}")
                break
            
            soup = BeautifulSoup(response.text, "html.parser")
            cards = soup.find_all("div", class_="collection-card")
            
            if not cards: break

            for card in cards:
                try:
                    title = card.find("h3").get_text(strip=True) if card.find("h3") else "N/A"
                    price = card.find("span", class_="price").get_text(strip=True) if card.find("span", class_="price") else "0"
                    details = card.find_all("p")
                    
                    products.append({
                        "Title": title,
                        "Price": price,
                        "Rating": details[0].get_text(strip=True) if len(details) > 0 else "0",
                        "Colors": details[1].get_text(strip=True) if len(details) > 1 else "0",
                        "Size": details[2].get_text(strip=True) if len(details) > 2 else "N/A",
                        "Gender": details[3].get_text(strip=True) if len(details) > 3 else "N/A",
                        "timestamp": datetime.now()
                    })
                except: continue
        except Exception as e:
            print(f"Error pada halaman {page}: {e}")
            break
            
    return products