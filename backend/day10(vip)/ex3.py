import time
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize Selenium WebDriver (Make sure to have ChromeDriver or appropriate driver installed)
driver = webdriver.Chrome()  # You may need to specify the path to the ChromeDriver
url = "https://www.jiosaavn.com/artist/s.-p.-balasubrahmanyam-songs/Ix5AC5h7LSg_"
driver.get(url)

# Select All Languages
time.sleep(3)  # Wait for the page to load
select_languages = driver.find_element(By.XPATH, '//*[@id="lang-select"]/div')  # Modify XPATH as needed
select_languages.click()
time.sleep(1)

# Select all languages (assuming it's a button click)
all_languages = driver.find_element(By.XPATH, '//*[text()="Select All"]')  # Modify XPATH as needed
all_languages.click()
time.sleep(1)

# Load more songs
while True:
    try:
        load_more_button = driver.find_element(By.XPATH, '//*[text()="Load More"]')
        load_more_button.click()
        time.sleep(2)  # Wait for more songs to load
    except:
        break  # Exit the loop if the button is not found

# Get the page source after loading all songs
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Find all song links in the "Popular" category
song_links = [a['href'] for a in soup.find_all('a', class_='song-name')]

# Initialize a count for songs under "Aditya Music"
aditya_music_count = 0


# Function to extract copyright information
def get_copyright_info(song_url):
    driver.get(song_url)
    time.sleep(2)  # Wait for the song page to load
    song_soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Locate copyright information
    copyright_info = song_soup.find(text=re.compile(r'^\(P\)|℗', re.IGNORECASE))
    if copyright_info and "Aditya Music" in copyright_info:
        return True
    return False


# Scrape each song page
for link in song_links:
    if get_copyright_info(link):
        aditya_music_count += 1

# Print the total count of songs under "Aditya Music"
print(aditya_music_count)  # Output the count as an integer

# Clean up
driver.quit()
