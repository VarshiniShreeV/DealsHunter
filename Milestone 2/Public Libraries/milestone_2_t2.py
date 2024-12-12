# Public Library Scraping

import sqlite3
import streamlit as st
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager 
import time

st.set_page_config(layout="wide")
st.title("Library Near You")

db_name = "libraries_data.db"

if "selected_state" not in st.session_state:
    st.session_state.selected_state = None
if "viewing_details" not in st.session_state:
    st.session_state.viewing_details = False

def scraper():
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    # Create tables for states and libraries if they don't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS states (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        state_name TEXT UNIQUE
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS libraries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        state_id INTEGER,
        city TEXT,
        library TEXT,
        address TEXT,
        zip TEXT,
        phone TEXT,
        FOREIGN KEY (state_id) REFERENCES states (id)
    )
    ''')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))  # Automatically handles the driver
    driver.maximize_window()

    url = "https://publiclibraries.com/state/"
    driver.get(url)

    # Scrape states
    states = driver.find_elements(By.CSS_SELECTOR, "a[href*='/state/']")
    state_links = [state.get_attribute("href") for state in states]

    for state_link in state_links:
        driver.get(state_link)
        state_name = driver.find_element(By.TAG_NAME, "h1").text.replace(" Public Libraries", "")
        print(f"Scraping data for {state_name}...")

        # Insert state into States Table
        cursor.execute('''
        INSERT OR IGNORE INTO states (state_name)
        VALUES (?)
        ''', (state_name,))
        connection.commit()
        
        state_id = cursor.execute('''SELECT id FROM states WHERE state_name = ?''', (state_name,)).fetchone()[0]

        # Scrape libraries data of respective states
        rows = driver.find_elements(By.CSS_SELECTOR, "#libraries tbody tr")
        for row in rows:
            columns = row.find_elements(By.TAG_NAME, "td")
            if len(columns) == 5:  # Ensure valid row structure
                city = columns[0].text
                library = columns[1].text
                address = columns[2].text
                zip_code = columns[3].text
                phone = columns[4].text

                # Insert library data into the libraries table
                cursor.execute('''
                INSERT INTO libraries (state_id, city, library, address, zip, phone)
                VALUES (?, ?, ?, ?, ?, ?)
                ''', (state_id, city, library, address, zip_code, phone))

        connection.commit() 
        time.sleep(2)  

    driver.quit()
    connection.close()

scraper()

connection = sqlite3.connect(db_name)
state_names = [row[0] for row in connection.execute("SELECT state_name FROM states").fetchall()]

if not st.session_state.viewing_details:  
    state = st.selectbox("Choose a State", ["Select"] + state_names) # Only show if view details not visisble

    if state != "Select":
        st.session_state.selected_state = state  # Update session state
        if st.button("Scrape Libraries"):  
            st.session_state.viewing_details = True  

else:
    selected_state = st.session_state.selected_state
    st.title(f"Libraries in {selected_state}")

    query = '''
    SELECT libraries.city, libraries.library, libraries.address, libraries.zip, libraries.phone
    FROM libraries
    JOIN states ON libraries.state_id = states.id
    WHERE states.state_name = ?
    '''
    result = pd.read_sql_query(query, connection, params=(selected_state,))

    if result.empty:
        st.write(f"No libraries found for {selected_state}.")
    else:
        st.dataframe(result, use_container_width=True)

    # Redirect to main page
    if st.button("Back to State Selection"):
        st.session_state.viewing_details = False  # Reset the flag to go back to dropdown

connection.close()
