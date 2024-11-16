import requests
from bs4 import BeautifulSoup
import csv
import streamlit as st

base_url = "https://dealsheaven.in/?page="

st.write("# Deals Scraper")
st.write("Enter the range of pages you would like to scrape")

start_page = st.text_input("Starting Page", "0")  
end_page = st.text_input("Ending Page", "0")    

try:
    start = int(start_page)
    end = int(end_page)
    
    if start <= 0 or end <= 0:
        st.error("Page numbers must be greater than zero.")
    elif start > end:
        st.error("Starting page must be less than or equal to ending page.")
    elif end > 1703 :
        st.error("The DealsHeaven Website has only 1703 Pages!")
    else:
        # Start scraping process
        with open("product_deals.csv", mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Title", "Image", "Price", "Discount", "Special Price", "Link", "Rating"])

            for current_page in range(start, end + 1):  
                st.write(f"Scraping page {current_page}...")
                url = base_url + str(current_page)
                response = requests.get(url)

                # Check if the HTTP request was successful
                if response.status_code != 200:
                    st.warning(f"Failed to retrieve page {current_page}. Skipping...")
                    continue

                soup = BeautifulSoup(response.text, 'html.parser')
                all_items = soup.find_all("div", class_="product-item-detail")

                if not all_items:
                    st.warning(f"No products found on page {current_page}. Stopping scraper.")
                    break

                for item in all_items:
                    product = {}

                    # Extract product's Discount
                    discount = item.find("div", class_="discount")
                    product['Discount'] = discount.text.strip() if discount else "N/A"

                    # Extract product's Link
                    link = item.find("a", href=True)
                    product['Link'] = link['href'] if link else "N/A"

                    # Extract product's Image Link
                    image = item.find("img", src=True)
                    product['Image'] = image['data-src'] if image else "N/A"

                    details_inner = item.find("div", class_="deatls-inner")
                    
                    # Extract product's Title
                    title = details_inner.find("h3", title=True) if details_inner else None
                    product['Title'] = title['title'].replace("[Apply coupon] ", "").replace('"', '') if title else "N/A"

                    # Extract product's Original Price
                    price = details_inner.find("p", class_="price") if details_inner else None
                    product['Price'] = f"₹{price.text.strip().replace(',', '')}" if price else "N/A"

                    # Extract product's Special Price ( Price after dicount on Original Price )
                    s_price = details_inner.find("p", class_="spacail-price") if details_inner else None
                    product['Special Price'] = f"₹{s_price.text.strip().replace(',', '')}" if s_price else "N/A"

                    # Extract product's Ratings
                    rating = details_inner.find("div", class_="star-point") if details_inner else None
                    if rating:
                        style_width = rating.find("div", class_="star") if rating else None
                        if style_width:
                            percent = style_width.find("span", style=True) if style_width else None
                            if percent:
                                style = percent['style']
                                width_percentage = int(style.split(":")[1].replace('%', '').strip())
                                stars = round((width_percentage / 100) * 5, 1)
                                product['Rating'] = stars
                            else:
                                product['Rating'] = "N/A"
                        else:
                            product['Rating'] = "N/A"
                    else:
                        product['Rating'] = "N/A"

                    # Dynamically write into a csv file
                    writer.writerow([product.get('Title', 'N/A'), f'=HYPERLINK("{product.get("Image", "N/A")}","Image")', product.get('Price', 'N/A'), product.get('Discount', 'N/A'), product.get('Special Price', 'N/A'), f'= HYPERLINK("{product.get("Link", "N/A")}","Link")', product.get('Rating', 'N/A')])

        st.write("Data scraping and saving completed.") # Displays in the UI

except ValueError:
    st.error("Please enter valid integers for the starting and ending page.")