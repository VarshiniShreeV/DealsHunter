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
![1](https://github.com/user-attachments/assets/781865b4-bcb6-4f40-9e8d-202f098460bf)
![2](https://github.com/user-attachments/assets/5e9be00b-465b-4e88-b5a6-247e8cd7a326)
![3](https://github.com/user-attachments/assets/71f04d8d-eac9-44df-9213-b5df12e75264)
![4](https://github.com/user-attachments/assets/c0052a1f-2b98-44a0-909c-a280243a089d)


### Public Libraries Data Viewer  
![1](https://github.com/user-attachments/assets/02f23cbe-203a-43ac-936e-c9fb1e98988e)
![2](https://github.com/user-attachments/assets/869115ba-26da-4d1e-9795-7473ea2036b9)
![3](https://github.com/user-attachments/assets/b484f595-8391-49d7-8f6c-ca706a108e6e)
![4](https://github.com/user-attachments/assets/05038514-0fc8-4583-bb7d-c77885c19ed9)
![5](https://github.com/user-attachments/assets/a9d2cb0b-f62f-41c7-aa87-ac83e1efff2f)


### Behance Job Listings Viewer  
![1](https://github.com/user-attachments/assets/9f774e75-0c78-46e0-93da-00b724c7a3b2)
![2](https://github.com/user-attachments/assets/31b4c7f0-0cc6-461c-bce8-a2804ae7525c)
![3](https://github.com/user-attachments/assets/62b726d8-106a-4340-8bf9-66602acd8d22)
![4](https://github.com/user-attachments/assets/ab2d9f78-d326-48b7-baa7-6de19675acce)
![5](https://github.com/user-attachments/assets/009e7ff6-d515-43b3-9a1e-c19fa412eaf6)
![6](https://github.com/user-attachments/assets/6a4aeb22-83e6-481a-a670-acfe757c0325)
![7](https://github.com/user-attachments/assets/0934e7fa-5a0b-414d-b930-f2f65b424e65)



---

## [Demo Video](https://drive.google.com/file/d/1Z6UufS6qM9LyfkB-ifjfQ1M_ItDDnr8L/view?pli=1)
