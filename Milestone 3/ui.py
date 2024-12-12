import streamlit as st
import pandas as pd

st.set_page_config(page_title="Behance Job Listings", page_icon="💼")
st.markdown("""
    <style>
        .header {
            font-size: 50px;
            font-weight: bold;
            color: #333;
            text-align: center;
            margin-top: -25px;
        }
        .card {
            border-radius: 10px;
            padding: 10px;
            margin: 10px;
            background-color: #0E1117;
            border: 2px solid #ccc; 
            transition: transform 0.3s, box-shadow 0.3s ease-in-out;
            height: 180px;
            width: 220px; 
            display: flex;
            flex-direction: column;
            overflow: hidden;
        }
        .card:hover {
            transform: scale(1.05) translateY(-5px);
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
            border-color: #d42626;  
        }
        .card h4 {
            font-size: 20px;
            margin-top: -10px;
            color: #edc542;  
            text-align: center;
            margin-bottom: -10px;
            overflow: hidden;
            text-overflow: ellipsis;
            white-space: nowrap;
        }
        .card p {
            color: #cdd199;
            margin-bottom: 8px;
            font-size: 14px;
            overflow: hidden;
            text-overflow: ellipsis;
            white-space: nowrap;
        }
        .stSelectbox>div>div>input {
            font-size: 16px;
            padding: 8px;
        }
        .stSelectbox>div>div>div {
            font-size: 16px;
        }
        .stTextInput input {
            font-size: 16px;
        }
    </style>
    """, unsafe_allow_html=True)

filename = "jobs.csv"
try:
    # Load the CSV file
    data = pd.read_csv(filename)
    st.markdown("<p class='header'>JOBS</p>", unsafe_allow_html=True)

    unique_companies = data["Company"].dropna().unique()

    # Dynamic search with dropdown
    search_query = st.selectbox(
        "Search by Organizations",
        options=["All"] + sorted(unique_companies), 
        help="Type or select an organization",
    )

    # Filter based on user selection
    if search_query != "Start typing a company name...":
        if search_query == "All":
                filtered_data = data  # Display all data if "All" is selected
        else:
            filtered_data = data[data["Company"].str.contains(search_query, case=False, na=False)]

        # Display job cards 
        if not filtered_data.empty:
            st.write(f"#### Job Listings for '{search_query}'")
            
            # Display 3 cards per row
            col_count = 3 
            cols = st.columns(col_count)

            for i, (index, row) in enumerate(filtered_data.iterrows()):
                with cols[i % col_count]:  
                    st.markdown(
                        f"""
                        <div class="card">
                            <h4> 🏬 {row['Company']}</h4>
                            <p> 🪪 {row['Job Title']}</p>
                            <p class="description"> ❓ {row['Description']}</p>
                            <p> 🗓️ {row['Time Posted']}</p>
                            <p> 📍 {row['Location']}</p>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
        else:
            st.warning("No job listings found for the selected company.")
    else:
        st.info("Please select or type a company to see job listings.")

except FileNotFoundError:
    st.error(f"Error: The file `{filename}` was not found. Please ensure it exists.")
