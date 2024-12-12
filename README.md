# DealsHunter

This project is built during my python stack internship @ Infosys Springboard

This branch is maintained by [VarshiniShreeV](https://github.com/VarshiniShreeV)

### Dependencies:
1. Python (version: 3.13.0 or above)
2. Python IDE (Visual Studio Code / PyCharm / IDLE / Eclipse)
3. Libraries : Streamlit, Beatiful Soup, Selenium 

## Milestone 1
A website "DealsHunter" is built using streamlit in python, which scrapes the data from the website DealsHeaven[https://dealsheaven.in/] using beautifulsoup and requests libraries.

In the folder Milestone 1 -> Run app.py:
```
streamlit run app.py
```

![Screenshot 2024-11-17 194413](https://github.com/user-attachments/assets/fa5cb83a-9db3-493b-bce6-cc627e67b08e)


### Milestone 1 Enhancement
A status bar is added and the UI is modified for visual appeal. Also, help section is provided.

In the folder Milestone 1 -> Run milestone_1.py:
```
streamlit run milestone_1.py
```

![enhance](https://github.com/user-attachments/assets/d3af01d7-b3a2-440e-b18b-9185e3cfc8f9)

![image](https://github.com/user-attachments/assets/9b957204-dd4a-49b2-bccc-320fda9611a4)


## Milestone 2

## DealsHunter
The DealsHunter website is enhanced further for better user experience and filtering by category is integrated. The products are displayed with their respective images and other details.

In the folder Milestone 2 -> Run milestone_2_t1.py:
```
streamlit run milestone_2_t1.py
```

![8](https://github.com/user-attachments/assets/d934d2bf-13ed-47bf-b496-dd1ca2c581d0)
![9](https://github.com/user-attachments/assets/5dd1fa7e-dc4f-46d0-b562-bdb0e264cb6d)

## Public Library
Using Selenium, we scrape the states and their respective libraries information from the [Public Libraries website](https://publiclibraries.com/state/). Using sqlite3, we store the scraped data in 2 tables, which are related to each other by having common state id. Using selenium, the scraped information of libraries for s specific chosen state is displayed.

In the folder Milestone 2 -> Run milestone_2_t2.py:
```
streamlit run milestone_2_t2.py
```

### States Table (2 fields: state_id, state_name)
![L 2](https://github.com/user-attachments/assets/91555d0c-505a-4949-8f51-d8732651f382)

### Libraries Table (7 fields : id, state_id, city, library, address, zip, phone)
![L 3](https://github.com/user-attachments/assets/bec22b5a-3078-44e4-9ae6-a246241392a1)

### Schema of the 2 tables in the Data Base libraries_data.db
![L 4](https://github.com/user-attachments/assets/27197aa4-9c59-4fff-8422-60614acbe3e6)

### Relation between 2 tables (States (Strong Entity) -> Libraries (Weak Entity)
![L 5](https://github.com/user-attachments/assets/869fd5e3-b199-47a1-9bd6-31127117379b)

### GUI using Streamlit
![L 1](https://github.com/user-attachments/assets/bb9e0d2c-182a-4952-bd05-455fe197b0c8)
![L 9](https://github.com/user-attachments/assets/f2fd34ea-de9c-4321-b729-f6dd71fab40f)
![L 7](https://github.com/user-attachments/assets/21d10826-60ce-44b1-92b7-ea1396d4e612)


## Milestone 3
Using selenium, we scrape the job cards from the [Behance Job Listings](https://www.behance.net/joblist), up until the pages scrolled (here, default 10). Then, a gui is built using streamlit, where a dynamic search bar (which helps you search easier by providing pre-existing options in a drop down), is implemented and the corresponding job listings are displayed as cards.
So, the scraper file must be executed before ui file, since it scrapes and stores the data.

In the folder milestone 3 ->
Run the scraper file:
```
python scraper.py
```
Then run the ui file:
```
streamlit run ui.py
```

### GUI : Displaying all the scraped data initially
![3 1](https://github.com/user-attachments/assets/71334e3b-36e3-4f53-88f1-767977ea6ce5)
-
### Dynamic Search Assistance
![3 2](https://github.com/user-attachments/assets/e345bb3a-5114-4b4a-bc47-5597e67d08d6)
-
### Fetched Results
![3 3](https://github.com/user-attachments/assets/9b1d3fc4-1aad-4894-bbd1-bdebcb2c5fac)





