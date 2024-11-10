import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

# Initialize the Chrome WebDriver
options = Options()
options.add_argument('--headless')  # Run headless for faster scraping
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)


def load_songs(url):
    driver.get(url)

    # Select all languages
    try:
        select_all_languages = driver.find_element(By.XPATH,
                                                   "//div[@class='language-select']//span[contains(text(), 'All Languages')]")
        select_all_languages.click()
    except Exception as e:
        print(f"Error selecting languages: {e}")

    # Scroll and load more songs
    while True:
        try:
            load_more_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Load more')]")
            load_more_button.click()
            time.sleep(3)  # Wait for more songs to load
        except Exception:
            break  # Exit loop if the button is not found


def scrape_song_pages():
    song_links = []
    songs = driver.find_elements(By.XPATH, "//div[@class='songs-list']//a[@class='link']")

    for song in songs:
        song_links.append(song.get_attribute('href'))

    return song_links


def get_copyright_info(song_url):
    driver.get(song_url)
    time.sleep(2)  # Wait for the page to load

    # Parse the song page
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Locate copyright information
    copyright_info = soup.find('div', class_='copyright')
    if copyright_info:
        return copyright_info.text.strip()
    return ""


def count_aditya_music(songs):
    count = 0
    for song in songs:
        copyright_info = get_copyright_info(song)
        # Check if "Aditya Music" is in the copyright information
        if re.search(r'\bAditya Music\b', copyright_info, re.IGNORECASE):
            count += 1
    return count


# Main execution
url = "https://www.jiosaavn.com/artist/s.-p.-balasubrahmanyam-songs/Ix5AC5h7LSg_"
load_songs(url)
song_links = scrape_song_pages()
aditya_music_count = count_aditya_music(song_links)

# Print the total count of songs under "Aditya Music"
print(f"Total number of songs with 'Aditya Music' copyright: {aditya_music_count}")

# Close the browser
driver.quit()
