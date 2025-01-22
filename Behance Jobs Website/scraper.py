from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import csv
import time

# Input handling
inputs = input("Enter category, subcategory, job title separated by commas: ")
selected_category, selected_subcategory, job_title = inputs.split(',')

print("Selected Category:", selected_category)
print("Selected Subcategory:", selected_subcategory)
print("Job Title:", job_title)

def scraper():
    chrome_options = Options()
    chrome_options.add_argument("--start-fullscreen")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        if selected_subcategory:
            subcategory = selected_subcategory.lower().replace(" & ", "-").replace("/", "-").replace(" ", "-").strip()
            url = f"https://www.behance.net/joblist?category={subcategory}"
        elif selected_category.lower() == "all":
            url = "https://www.behance.net/joblist"
        else:
            url = f"https://www.behance.net/joblist?tracking_source=nav20&category={selected_category.lower().replace(' ', '-')}"
        
        print("Generated URL:", url)
        driver.get(url)
        time.sleep(3)  # Allow page to load

        scroll_limit = 20
        scroll_count = 0
        job_found = False
        data = []
        specific_job_data = []

        while scroll_count < scroll_limit:
            job_cards = driver.find_elements(By.CLASS_NAME, "JobCard-jobCard-mzZ")
            print(f"Number of job cards found so far: {len(job_cards)}")

            for index, card in enumerate(job_cards):
                try:
                    company = card.find_element(By.CLASS_NAME, "JobCard-company-GQS").text
                    title = card.find_element(By.CLASS_NAME, "JobCard-jobTitle-LS4").text
                    description = card.find_element(By.CLASS_NAME, "JobCard-jobDescription-SYp").text
                    time_posted = card.find_element(By.CLASS_NAME, "JobCard-time-Cvz").text
                    location = card.find_element(By.CLASS_NAME, "JobCard-jobLocation-sjd").text
                    image_element = card.find_element(By.CLASS_NAME, 'JobLogo-logoButton-aes').find_element(By.TAG_NAME, 'img')
                    image_url = image_element.get_attribute('src')
                    job_link = card.find_element(By.TAG_NAME, "a").get_attribute("href")

                    # Append data to list
                    data.append([company, title, description, time_posted, location, image_url, job_link])

                    # Check if the current job title matches the desired job title
                    if title.lower() == job_title.lower() and not job_found:
                        print(f"Found the job: {title}")
                        job_found = True

                        try:
                            card.click()
                            time.sleep(4)  # Allow job details to load
                            specific_job_data.append([company, title, description, time_posted, location, image_url, job_link])
                        except Exception as e:
                            print("Could not click on the job card:", e)
                except Exception as e:
                    print(f"Error extracting job details for card {index + 1}: {e}")

            if job_found:
                break

            driver.execute_script("window.scrollBy(0, 1000);")
            scroll_count += 1
            time.sleep(2)  # Allow content to load

        # Save all jobs data to jobs.csv
        if data:
            with open("jobs.csv", mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(["Company", "Job Title", "Description", "Time Posted", "Location", "Image URL", "Job Link"])
                writer.writerows(data)
            print("All jobs data saved to jobs.csv")

        # Save specific job data to card.csv
        if specific_job_data:
            with open("card.csv", mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(["Company", "Job Title", "Description", "Time Posted", "Location", "Image URL", "Job Link"])
                writer.writerows(specific_job_data)
            print("Specific job data saved to card.csv")
        else:
            print("No specific job data found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

scraper()
