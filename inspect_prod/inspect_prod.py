from bs4 import BeautifulSoup
import requests
import time

url = "https://www.yesstyle.com/en/celimax-the-vita-a-retinal-shot-tightening-booster-15ml/info.html/pid.1130946339"
html = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}).text
soup = BeautifulSoup(html, "html.parser")

print("Starting data ingestion...")
max_retries = 5
retries = 0
delay = 1
while retries < max_retries:
    try:
        # Product details
        h1_elem = soup.select_one(".productDetailPage_productUpper-heading__IKsLu h1")
        if h1_elem:
            # Get all text nodes that are direct children of <h1> (not inside <a>)
            title = ''.join(t for t in h1_elem.contents if t.name is None).strip()
        else:
            title = None
        #title = soup.select_one(".productDetailPage_productUpper-heading__IKsLu h1").get_text(strip=True)
        brand = soup.select_one(".productDetailPage_productUpper-heading__IKsLu h1 a").get_text(strip=True)
        current_price = soup.select_one(".productDetailPage_priceContainer__8AIXw span").get_text(strip=True)
        original_price = soup.select_one(".productDetailPage_listPrice__VPPgw").get_text(strip=True)
        #original_price_elem = soup.select_one(".productDetailPage_listPrice__VPPgw")
        #original_price = original_price_elem.get_text(strip=True) if original_price_elem else None
        # original_price = soup.select_one(".productDetailPage_unitPrice__s2XgI").get_text(strip=True)
        rating = soup.select_one(".productDetailPage_ratingRow__VNeGN").get_text(strip=True)
        #num_reviews = soup.select_one(".customerreviews_chartRow__Wz8ZS p").get_text(strip=True)

        # Review samples
        reviews = [r.get_text(strip=True) for r in soup.select(".customerreviews_reviewCard__4V1EE")]
        break

    except requests.exceptions.RequestException as e:
            print(f"Error scraping data: {e}. Retrying in {delay} seconds...")
            time.sleep(delay)
            retries += 1
            delay *= 2
scraping_line = [
     f"title is {title}",
     f"brand is {brand}",
     f"current_price is {current_price}",
     f"original_price is {original_price}",
     f"rating is {rating}",
]
#print(title, brand, current_price, original_price, rating, num_reviews)
for line in scraping_line:
     print(line)
print(reviews[:3])  # first 3 reviews

