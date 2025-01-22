# **Scraping Projects**

This repository showcases a collection of Python-based scraping projects developed during my Python stack internship at Infosys Springboard. The projects demonstrate the power of automation, dynamic user interfaces, and data extraction from web sources, providing practical solutions for real-world problems.  


---

## **Overview**

### **1. Deals Hunter**
- A web scraping application built using **Streamlit** and **BeautifulSoup** to extract deals from [DealsHeaven](https://dealsheaven.in/).  
- Provides an intuitive user interface with status tracking, enhanced visuals, and a help section for user assistance.  
- Includes category filtering and dynamic display of deal information such as product details, images, and prices.  

### **2. Libraries Near You**
- Scrapes library data from [Public Libraries](https://publiclibraries.com/state/) using **Selenium**.  
- Data is stored in an **SQLite database** with two relational tables:  
  - **States:** Contains state IDs and names.  
  - **Libraries:** Stores library details, including city, address, zip, and phone, linked to the respective state ID.  
- The GUI, built with **Streamlit**, allows users to select a state and view its libraries dynamically.  

### **3. Behance Job Listings Scraper**
- Automates job scraping from [Behance Jobs](https://www.behance.net/joblist) using **Selenium**.  
- Displays job cards with company details, descriptions, and categories.  
- Implements a **dynamic search bar** with suggestions for filtering job listings based on organizations.  
- Enhanced user experience with **light and dark themes** and a sidebar for category selection.

---

## **Key Features**

- **Web Scraping:**  
  Extracts data from diverse web sources using **BeautifulSoup** and **Selenium**.  
- **Data Storage:**  
  Stores structured data in **SQLite** databases for efficient querying and manipulation.  
- **Interactive GUIs:**  
  Dynamic and responsive user interfaces built with **Streamlit** for intuitive navigation.  
- **Theming:**  
  Light and dark theme options for better visual customization.  
- **Automation:**  
  Seamless integration with automation tools for scraping processes.

---

## **Installation Guide**

1. Ensure Python (version 3.8 or above) is installed on your system.  
2. Clone this repository:
   ```bash
   git clone https://github.com/VarshiniShreeV/ScrapingProjects.git
   ```
3. Navigate to the project directory:  
   ```bash
   cd ScrapingProjects
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## **How to Run the Applications**

### **Deals Hunter**
1. Navigate to the respective folder.  
2. Run the main application file:  
   ```bash
   streamlit run ui.py
   ```

### **Public Libraries Data**
1. Run the library scraper to populate the database:  
   ```bash
   streamlit run ui.py
   ```

### **Behance Job Listings Scraper**
1. Run the main UI file (scraper and filters integrated):  
   ```bash
   streamlit run ui.py
   ```

---

## **Screenshots**

### DealsHunter UI  
![DealsHunter UI](https://github.com/user-attachments/assets/d3af01d7-b3a2-440e-b18b-9185e3cfc8f9)  

### Public Libraries Data Viewer  
![Library Viewer](https://github.com/user-attachments/assets/bb9e0d2c-182a-4952-bd05-455fe197b0c8)  

### Behance Job Listings Viewer  
![Behance Viewer](https://github.com/user-attachments/assets/6ec4b6a8-52e5-4ae4-97cc-69cc037f6b33)  

---

## [Demo Video](https://drive.google.com/file/d/1Z6UufS6qM9LyfkB-ifjfQ1M_ItDDnr8L/view?pli=1)
