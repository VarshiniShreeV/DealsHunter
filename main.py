import requests
from bs4 import BeautifulSoup
import csv

base_url = "https://dealsheaven.in/?page="

with open("product_deals.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Price", "Discount", "Special Price"])  
    
    current_page = 1  # Starting with page 1

    while True:
        print(f"Scraping page {current_page}...")
        url = base_url + str(current_page)
        response = requests.get(url)
        
        # Checking whether HTTP request is successful
        if response.status_code != 200:                                  
            print(f"Failed to retrieve page {current_page}. Skipping...")
            current_page += 1
            continue
        
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all product items
        all_items = soup.find_all("div", class_="product-item-detail")
        
        if not all_items: 
            print(f"No products found on page {current_page}. Stopping scraper.")
            break  # Stop scraping when no products are found

        for item in all_items:
            product = {}

            # Extracting discount 
            discount = item.find("div", class_="discount")
            if discount:
                product['Discount'] = discount.text.strip()
            else:
                product['Discount'] = "N/A"
            
            # Extracting product's title
            details_inner = item.find("div", class_="deatls-inner")
            if details_inner:
                title = details_inner.find("h3", title=True)
                if title:
                    product['Title'] = title['title'].replace("[Apply coupon] ", "").replace('"', '')
                else:
                    product['Title'] = "N/A"
            else:
                product['Title'] = "N/A"

            # Extracting product's price 
            price = details_inner.find("p", class_="price") if details_inner else None
            if price:
                product['Price'] = f"₹{price.text.strip().replace(',', '')}"  # Adding ₹ symbol
            else:
                product['Price'] = "N/A"
            
            # Extracting special price 
            s_price = details_inner.find("p", class_="spacail-price") if details_inner else None
            if s_price:
                product['Special Price'] = f"₹{s_price.text.strip().replace(',', '')}"  # Adding ₹ symbol
            else:
                product['Special Price'] = "N/A"
            
            # Dynamically writing into csv file
            writer.writerow([product.get('Title', 'N/A'), product.get('Price', 'N/A'), product.get('Discount', 'N/A'), product.get('Special Price', 'N/A')])

        current_page +=1            

print("Data scraping and saving completed.")