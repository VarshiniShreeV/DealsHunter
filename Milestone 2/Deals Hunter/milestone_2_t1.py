import requests
from bs4 import BeautifulSoup
import csv
import streamlit as st
import pandas as pd
import time

# Base URL
BASE_URL = "https://dealsheaven.in/?page="

# CSV File Name
csv_filename = "product_deals.csv"

st.set_page_config(page_title="Deals Hunter", page_icon=":moneybag:")

st.title("**Deals Hunter**")
st.write("*Your Ultimate Deals Finder!*")

with st.container():
    input_cols = st.columns([2, 2, 3, 4, 4])
    stores = input_cols[2].selectbox(
        "Select Store",
        ("All Stores", "Flipkart", "Amazon", "Paytm", "FoodPanda", "FreeCharge", "Paytm Mall"),
    )
    categories = input_cols[3].selectbox("Choose Category", ("All categories", "Automotive", "Baby Care & Toys", "Bags, Wallets & Luggage", "Beauty & Personal Care", "Books & Stationery", "Cameras & Camera Accessories", "Clothing Fashion & Apparels", "Computers, Laptops & Accessories", "Electronics","Food, Entertainment & Services", "Footwears", "Freebies", "Grocery", "Headphone, Speakers & Soundbar", "Home Decor & Furnishing", "Home Entertainment: LED, LCD TV", "Home Kitchen Appliances", "Mobiles & Mobile Accessories", "Musical Instruments", "Others", "Pets", "Recharge", "Software Games", "Sports, Fitness, Outdoor & Health", "Travel Bus & Flight", "Vouchers & Gift Card", "Webhosting & Domain Services"),)

    start_page = input_cols[0].number_input("Start", min_value=1, max_value=1703)
    end_page = input_cols[1].number_input("End", min_value=1, max_value=1703)

    if start_page > end_page:
        st.error("Starting page must be less than or equal to ending page.")
    else:
        input_cols[4].write("\n" * 5)
        input_cols[4].write("\n" * 3)
        if input_cols[4].button("Fetch Deals", key="scrape"):
            progress_bar = st.progress(0)
            scraped_data = []  
            with open(csv_filename, mode="w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["Title", "Image", "Price", "Discount", "Special Price", "Link", "Rating","Store"])

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
                    
                    # Extract Product Details
                    for item in all_items:
                        product = {}

                        discount = item.find("div", class_="discount")
                        product['Discount'] = discount.text.strip() if discount else "N/A"

                        link = item.find("a", href=True)
                        product['Link'] = link['href'] if link else "N/A"

                        image = item.find("img", src=True)
                        product['Image'] = image['data-src'] if image else "N/A"

                        details_inner = item.find("div", class_="deatls-inner")

                        title = details_inner.find("h3", title=True) if details_inner else None
                        product['Title'] = title['title'].replace("[Apply coupon] ", "").replace('"', '') if title else "N/A"

                        price = details_inner.find("p", class_="price") if details_inner else None
                        product['Price'] = f"₹{price.text.strip().replace(',', '')}" if price else "N/A"

                        s_price = details_inner.find("p", class_="spacail-price") if details_inner else None
                        product['Special Price'] = f"₹{s_price.text.strip().replace(',', '')}" if s_price else "N/A"

                        rating = details_inner.find("div", class_="star-point") if details_inner else None
                        product['Rating'] = "N/A"
                        if rating:
                            style_width = rating.find("div", class_="star")
                            if style_width:
                                percent = style_width.find("span", style=True)
                                if percent:
                                    width_percentage = int(percent['style'].split(":")[1].replace('%', '').strip())
                                    stars = round((width_percentage / 100) * 5, 1)
                                    product['Rating'] = stars

                        store = details_inner.find("div", class_="esite-logo") if details_inner else None
                        if store:
                            img_tag = store.find("img", alt=True)
                            product["Store"] = img_tag["alt"].strip() if img_tag and "alt" in img_tag.attrs else "N/A"
                        else:
                            product["Store"] = "N/A"

                        scraped_data.append(product)

                        writer.writerow([product.get('Title', 'N/A'), product.get("Image", "N/A"), product.get('Price', 'N/A'), product.get('Discount', 'N/A'), product.get('Special Price', 'N/A'), product.get("Link", "N/A"), product.get('Rating', 'N/A'), product.get('Store', 'N/A')])

                    progress = (current_page - start_page + 1) / (end_page - start_page + 1)
                    progress_bar.progress(progress)

                    time.sleep(1)
                    
                    output = pd.read_csv(csv_filename)
                    print(type(output))
                    
                    try:
                        if stores != 'All Stores':
                            filtered_output = output[output['Store']==stores]
                        else:
                            filtered_output = output
                    except Exception as e:
                        print("OOPS! An error occured")
                    
                    with st.container():
                        num_products = len(filtered_output)
                        cols = st.columns(5)  # Aligning 5 columns for each row

                        for i in range(0, num_products, 5):  
                            row_products = filtered_output.iloc[i:i+5]
                            
                            for j, product in enumerate(row_products.itertuples(), 1):  
                                if (product.Title != 'N/A' and
                                    product.Image != 'N/A' and
                                    product.Price != 'N/A' and
                                    product.Discount != 'N/A' and
                                    product.Rating != 'N/A' and
                                    product.Link != 'N/A'):
                                    with cols[j - 1]:  
                                        image_url = product.Image
                                        if isinstance(image_url, str) and image_url.startswith('http'):
                                            st.image(image_url, use_container_width=True)
                                        else:
                                            st.image('https://via.placeholder.com/200', use_container_width=True)

                                        st.write(f"**{product.Title}**")
                                        st.write(f"Price: {product.Price}")
                                        st.write(f"Discount: {product.Discount}")
                                        st.write(f"Rating: {product.Rating}")
                                        st.write(f"[Link]({product.Link})")
                        

with st.container():                      
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
            
    with st.expander("Contact"):
        st.write(
        """
        **How to reach us?**
        Mail at varshinishreevelumani@gmail.com
        """
    )
