import streamlit as st
import pandas as pd
import subprocess
import time


st.set_page_config(page_title="Behance Job Listings", page_icon="💼", layout="wide")

st.markdown("""
    <style>
        /* Header Styling */
        .header {
            font-size: 48px;
            font-weight: bold;
            text-align: center;
            margin-top: -25px;
            padding-bottom: 20px;
        }

        /* Card Container Styling */
        .card {
            border-radius: 12px;
            padding: 15px;
            margin: 15px;
            border: 2px solid #ccc; 
            transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
            height: auto; /* Adjust height based on content */
            width: 100%; /* Full width on smaller screens */
            max-width: 300px; /* Restrict maximum width */
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            overflow: hidden;
            box-sizing: border-box;
        }

        /* Card Hover Effect */
        .card:hover {
            transform: scale(1.05) translateY(-5px);
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
            border-color: #d42626;
        }

        /* Image Styling */
        .card img {
            width: 100%;
            height: 150px; /* Adjust height for a better ratio */
            object-fit: cover;
            border-radius: 12px;
            margin-bottom: 15px;
        }

        /* Card Title Styling */
        .card h4 {
            font-size: 22px;
            text-align: center;
            margin: 0;
            overflow: hidden;
            text-overflow: ellipsis;
            white-space: nowrap;
        }

        /* Card Description Styling */
        .card p {
            margin: 5px 0;
            font-size: 14px;
            overflow: hidden;
            text-overflow: ellipsis;
            white-space: nowrap;
        }
        
        /* Link */
        .card a {
            display: inline-block;
            margin-top: 5px;
            color: #007bff;
            text-decoration: none;
            font-size: 14px;
        }

        /* Input Fields Styling (Select and Text Inputs) */
        .stSelectbox>div>div>input {
            font-size: 16px;
            padding: 10px;
            border-radius: 8px;

            border: 1px solid #ccc;
            transition: border 0.3s ease;
        }

        .stSelectbox>div>div>div {
            font-size: 16px;
        }

        .stTextInput input {
            font-size: 16px;
        }
        .sidebar{
            font-size: 14px;
            padding: 8px;
            width: 150px;
        }

        /* Sidebar Visibility in Streamlit */
        .css-1d391kg {  
            visibility: visible !important;
        }

        /* Media Queries for Responsiveness */

        /* Adjust card layout on smaller screens */
        @media (max-width: 768px) {
            .card {
                width: 100%;
                margin: 10px 0;
            }
        }

        /* Further adjustments for very small screens */
        @media (max-width: 480px) {
            .header {
                font-size: 40px;
            }
            .card {
                width: 100%;
                margin: 10px;
            }
        }
    </style>
    """, unsafe_allow_html=True)

# Theme CSS
light_theme = """
    body {
        background-color: #f9f9f9;
        color: #333;
    }
    .header {
        color: #333;
    }
    .card {
        background-color: #ffffff;
        border: 2px solid #ccc;
    }
    .card h4 {
        color: #333;
    }
    .card p {
        color: #555;
    }
"""
dark_theme = """
    body {
        background-color: #0E1117;
        color: #ffffff;
    }
    .header {
        color: #ffffff;
    }
    .card {
        background-color: #1c1f26;
        border: 2px solid #444;
    }
    .card h4 {
        color: #edc542;
    }
    .card p {
        color: #cdd199;
    }
"""

# Sidebar theme selector
st.sidebar.title("JOBS💼")
st.sidebar.subheader("From\nBehance Job Listings")
selected_theme = st.sidebar.radio("Choose a theme:", ("Light", "Dark"))

if selected_theme == "Light":
    theme_css = light_theme
else:
    theme_css = dark_theme

st.markdown(f"<style>{theme_css}</style>", unsafe_allow_html=True)

categories = {
    "All" : [],
    "POPULAR": [
        "Logo Design",
        "Branding Services",
        "Social Media Design",
        "Website Design",
        "Illustrations",
        "Packaging Design",
        "Landing Page Design",
        "UI/UX Design",
        "Architecture & Interior Design",
    ],
    "GRAPHIC DESIGN": [
        "Logo Design",
        "Stationery Design",
        "Fonts & Typography",
        "Branding Services",
        "Book Design",
        "Packaging Design",
        "Album Cover Design",
        "Signage Design",
        "Invitation Design",
        "T-Shirt & Merchandise",
        "Flyer & Brochure Design",
        "Poster Design",
        "Identity Design",
        "Brand Guidelines",
    ],
    "WEB & APP DESIGN": [
        "Website Design",
        "App Design",
        "UI/UX Design",
        "Landing Page Design",
        "Icon Design",
    ],
    "DRAWING & ILLUSTRATION": [
        "Illustrations",
        "Portraits",
        "Comics & Character Design",
        "Fashion Design",
        "Pattern Design",
        "Storyboards",
        "Tattoo Design",
        "NFT Art",
        "3D Illustration",
        "Children's Illustration",
    ],
    "MARKETING DESIGN": [
        "Social Media Design",
        "Presentation Design",
        "Infographic Design",
        "Resume Design",
        "Copywriting",
    ],
    "PHOTOGRAPHY & EDITING": [
        "Product Photography",
        "Landscape Photography",
        "Image Editing & Retouching",
        "Portrait Photography",
    ],
    "ARCHITECTURE & INTERIOR DESIGN": [
        "Architecture & Interior Design",
        "Landscape Design",
    ],
    "PRODUCT & GAME DESIGN": [
        "Industrial Design",
        "Graphics for Streamers",
        "Game Design",
    ],
    "CAREER & LEARNING": [
        "Creative Tool Coaching",
        "Mentorship & Career Advice",
    ],
    "3D": [
        "Modeling Projects",
        "Architecture Renderings",
    ],
    "AUDIO & MUSIC": [
        "Music Composition & Production",
        "Sound Design",
    ],
    "ANIMATION & MOTION GRAPHICS": [
        "Animated Gifs",
        "Logo Animation",
        "Motion Graphics",
    ],
    "VIDEO PRODUCTION & EDITING": [
        "Video Production & Editing",
        "Explainer Videos",
        "Short Video Ads",
    ],
}

def display_categories():

    if categories:
        category_names = list(categories.keys())
        selected_category = st.sidebar.radio("Choose a Category", category_names)

        if selected_category:
            subcategories = categories[selected_category]
            selected_subcategory = st.sidebar.radio(
                f"Subcategories under '{selected_category}'", subcategories
            )
            return selected_category, selected_subcategory
    else:
        st.sidebar.write("No categories found.")
        return None, None
    
selected_category, selected_subcategory = display_categories()

names = ["Graphic Designer", "Motion graphic Designer", "Copywriter","Content Creator","Ads Specialist","Menu Editor", "Visual Designer", "UX Writer ", "Retoucher", "UI/UX Designer", "UI Designer", "Product Designer", "Videographer", "3D Designer", "Senior Graphic Designer", "UI/UX Developer", "Logo Designer", "Graphic Design Intern", "Creative Designer", "Senior Product Designer", "Designer", "Visual Identity Designer", "Market Designer", "Arch. Project Manager", "Video Editor", "Brand Graphic Designer", "Art Director", "UI/UX Intern", "3D Visulaizer", "Interior Designer", "2D Artist Leader", "Social Media Designer" ]
job_title = st.selectbox(" ", options=[" "]+sorted(names), help="Search for a specific Job!",
                         )

def scrape():
   with st.spinner("Scraping in progress... This may take a while."):
        try:
            # Running the scraper.py script using subprocess, since circular import might be encountered if we use importing (job_title) is passed from the UI to scraper function
            result = subprocess.run(["python", "scraper.py"], input= f"{selected_category},{selected_subcategory},{job_title}", capture_output=True, text=True, check=True)
            if result.returncode == 0:
                st.success("Scraping completed successfully!")
            else:
                st.error(f"Scraping failed: {result.stderr}")
        except Exception as e:
                st.error(f"An error occurred: {e}") 

cols = st.columns([1,1])

if cols[0].button("Scrape", key="General_Scrape"):
    scrape()

if cols[1].button("Show", key= "Specific_Data"):
    try:
        file = "card.csv"
        specific_data = pd.read_csv(file)
        if specific_data.empty:
            st.write("The specified job is not found")
        else:
            col_count = 5
            cols = st.columns(col_count)
            for i, (index, row) in enumerate(specific_data.iterrows()):
                with cols[i % col_count]:  
                    st.markdown(
                        f"""
                        <div class="card">
                            <img src="{row['Image URL']}" alt="Job Image"</img>
                            <h4> 🏬 {row['Company']}</h4>
                            <p> 🪪 {row['Job Title']}</p>
                            <p class="description"> ❓ {row['Description']}</p>
                            <p> 🗓️ {row['Time Posted']}</p>
                            <p> 📍 {row['Location']}</p>
                            <a href="{row['Job Link']}" target="_blank">View Job</a>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
    except FileNotFoundError:
        st.write("Oops!!The specified job is not found")
        
    
try:
    
    # Scraping
    if st.sidebar.button("Scrape", key="Category_scraper"):
        scrape()
    
    filename = "jobs.csv"    # Stores all the job cards displayed in the screen
    data = pd.read_csv(filename)

    unique_companies = data["Company"].dropna().unique()

    # Dynamic search with dropdown
    search_query = st.selectbox(
        "Search by Organizations",
        options=["All"] + sorted(unique_companies), 
        help="Type or select an organization",
    )
    if search_query != "Start typing a company name...":
        if search_query == "All":
                filtered_data = data  
        else:
            filtered_data = data[data["Company"].str.contains(search_query, case=False, na=False)]

        # Displaying job cards
        if not filtered_data.empty:
            st.write(f"#### Job Listings for '{search_query}'")
            col_count = 5
            cols = st.columns(col_count)
            for i, (index, row) in enumerate(filtered_data.iterrows()):
                with cols[i % col_count]:  
                    st.markdown(
                        f"""
                        <div class="card">
                            <img src="{row['Image URL']}" alt="Job Image"</img>
                            <h4> 🏬 {row['Company']}</h4>
                            <p> 🪪 {row['Job Title']}</p>
                            <p class="description"> ❓ {row['Description']}</p>
                            <p> 🗓️ {row['Time Posted']}</p>
                            <p> 📍 {row['Location']}</p>
                            <a href="{row['Job Link']}" target="_blank">View Job</a>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
        else:
            st.warning("No job listings found for the selected company.")
    else:
        st.info("Please select or type a company to see job listings.")
    
except FileNotFoundError:
    st.error("No jobs are scraped yet.")
