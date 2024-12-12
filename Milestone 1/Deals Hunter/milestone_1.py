import requests
from bs4 import BeautifulSoup
import csv
import streamlit as st
import pandas as pd
import time

# Base URL
BASE_URL = "https://dealsheaven.in/?page="

# CSV File Name
CSV_FILENAME = "product_deals.csv"

# Streamlit App Configuration
st.set_page_config(page_title="Deals Hunter", page_icon=":moneybag:")

st.title("**Deals Hunter**")
st.write("*Your Ultimate Deals Finder!*")

# Store Selector
stores = st.selectbox(
    "Select Store to Filter:",
    ("All Stores", "Flipkart", "Amazon", "Paytm", "FoodPanda", "FreeCharge", "Paytm Mall"),
)

# Page Range Inputs
st.write("Enter the range of pages you would like to scrape:")
start_page = st.number_input("Starting Page", min_value=1, max_value=1703, value=1)
end_page = st.number_input("Ending Page", min_value=1, max_value=1703, value=1)

# Validate Page Range
if start_page > end_page:
    st.error("Starting page must be less than or equal to ending page.")
else:
    # Start Scraping Button
    if st.button("Start Scraping"):
        # Initialize Progress Bar
        progress_bar = st.progress(0)
        scraped_data = []  # Collect data rows

        for current_page in range(start_page, end_page + 1):
            url = BASE_URL + str(current_page)
            response = requests.get(url)

            # HTTP Error Handling
            if response.status_code != 200:
                st.warning(f"Failed to retrieve page {current_page}. Skipping...")
                continue

            soup = BeautifulSoup(response.text, "html.parser")
            all_items = soup.find_all("div", class_="product-item-detail")

            if not all_items:
                st.warning(f"No products found on page {current_page}. Stopping scraper.")
                break

            # Extract Details for Each Item
            for item in all_items:
                product = {
                    "Title": "N/A",
                    "Image": "N/A",
                    "Price": "N/A",
                    "Discount": "N/A",
                    "Special Price": "N/A",
                    "Link": "N/A",
                    "Rating": "N/A",
                    "Store": "N/A",
                }

                # Extract Details
                discount = item.find("div", class_="discount")
                product["Discount"] = discount.text.strip() if discount else "N/A"

                link = item.find("a", href=True)
                product["Link"] = link["href"] if link else "N/A"

                image = item.find("img", src=True)
                product["Image"] = image["data-src"] if image else "N/A"

                details_inner = item.find("div", class_="deatls-inner")
                title = details_inner.find("h3", title=True) if details_inner else None
                product["Title"] = (
                    title["title"].replace("[Apply coupon] ", "").replace('"', "")
                    if title
                    else "N/A"
                )

                price = details_inner.find("p", class_="price") if details_inner else None
                product["Price"] = f"₹{price.text.strip().replace(',', '')}" if price else "N/A"

                s_price = (
                    details_inner.find("p", class_="spacail-price")
                    if details_inner
                    else None
                )
                product["Special Price"] = (
                    f"₹{s_price.text.strip().replace(',', '')}" if s_price else "N/A"
                )

                rating = (
                    details_inner.find("div", class_="star-point")
                    if details_inner
                    else None
                )
                if rating:
                    style_width = rating.find("div", class_="star")
                    percent = style_width.find("span", style=True) if style_width else None
                    if percent:
                        style = percent["style"]
                        width_percentage = int(style.split(":")[1].replace("%", "").strip())
                        stars = round((width_percentage / 100) * 5, 1)
                        product["Rating"] = stars
                    else:
                        product["Rating"] = "N/A"

                store = (
                    details_inner.find("div", class_="esite-logo") 
                    if details_inner 
                    else None)
                if store:
                    img_tag = store.find("img", alt=True)
                    product["Store"] = img_tag["alt"].strip() if img_tag and "alt" in img_tag.attrs else "N/A"
                else:
                    product["Store"] = "N/A"

                # Add Product to Data
                scraped_data.append(product)

            # Update Progress Bar
            progress = (current_page - start_page + 1) / (end_page - start_page + 1)
            progress_bar.progress(progress)

            # Rate Limiting
            time.sleep(1)

        # Write to CSV
        if scraped_data:
            df = pd.DataFrame(scraped_data)
            df.to_csv(CSV_FILENAME, index=False, encoding="utf-8")
            st.success("Data scraping and saving completed.")
            st.write(df)

            
# Help Section
with st.expander("Help"):
    st.write(
        """
        **How to Use Deals Hunter:**
        1. Enter the range of pages to scrape (between 1 and 1703).
        2. Click 'Start Scraping' to fetch product deals.
        3. The scraped data is displayed.
        4. To download the scraped data as a csv file, click the download button on the top right above the displayed scraped data section.
        """
    )
    