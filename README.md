# DealsHunter
This project is built during my Python stack internship @ **Infosys Springboard**

## Project Description

The **DealHunter** project aims to scrape product details from the e-commerce website [Deals Heaven](https://dealsheaven.in/). The objective of the project is to automate the process of retrieving product information such as titles, prices, discounts, and special prices, saving time and effort for users who wish to track deals from the site.

---

### Milestone 1

In **Milestone 1**, the primary goal is to scrape the following details for each product:

- **Product Title**: The name or title of the product.
- **Product Price**: The current price of the product.

This data will be extracted from the website and saved into a **CSV** file for future analysis and use.

---

### Milestone 2

In **Milestone 2**, the focus expands to scrape additional product details, which include:

- **Special Price**: The discounted price of the product, if available.
- **Discount**: The discount percentage or value for the product, if applicable.

These additional details will be appended to the data from Milestone 1, enhancing the information saved into the **CSV** file.

---

## Technologies Used

- **Python**: The programming language used to write the scraper.
- **BeautifulSoup**: A Python library used to parse the HTML content of web pages.
- **Requests**: A Python library used to send HTTP requests and fetch web pages.

---
## Running the Script

Clone the repository:

``` bash
git clone https://github.com/yourusername/DealHunter.git
```
Navigate to the project folder:

```bash
cd DealHunter
```
Run the scraper:

```bash
python main.py
```

The product details (title, price, discount, and special price) will be saved into a CSV file named product_deals.csv.

---

## Acknowledgments

- Infosys Springboard for the internship opportunity.
- Deals Heaven for providing the e-commerce data source.
