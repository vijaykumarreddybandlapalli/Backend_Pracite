import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the WebDriver
driver = webdriver.Chrome()  # Or specify the path to your WebDriver
driver.get("https://www.jiosaavn.com/artist/s.-p.-balasubrahmanyam-songs/Ix5AC5h7LSg_")

# Wait for page to load
wait = WebDriverWait(driver, 10)

# Step 1: Select All Languages
try:
    # Find and click on the language filter
    language_filter = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.lang-select')))
    language_filter.click()

    # Select all languages in the dropdown
    select_all_option = wait.until(EC.element_to_be_clickable((By.XPATH, '//label[contains(text(), "Select All")]')))
    select_all_option.click()

    # Close the dropdown by clicking outside
    ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    time.sleep(2)
except Exception as e:
    print("Error selecting languages:", e)

# Step 2: Load All Songs in "Popular" Category
# Scroll and click "Load More" until all songs are loaded
while True:
    try:
        # Scroll to the bottom of the page
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

        # Find and click "Load More" button if present
        load_more_button = driver.find_element(By.XPATH, '//button[contains(text(), "Load more")]')
        load_more_button.click()
        time.sleep(2)
    except Exception:
        # No more "Load More" button; all songs are loaded
        break

# Step 3: Scrape Song URLs from Popular Category
song_elements = driver.find_elements(By.CSS_SELECTOR, 'a[href*="/song/"]')
song_urls = [song.get_attribute('href') for song in song_elements]

# Step 4: Navigate to each song's page and collect copyright information
aditya_music_count = 0

for song_url in song_urls:
    driver.get(song_url)
    time.sleep(2)

    try:
        # Locate copyright information
        copyright_text = driver.find_element(By.XPATH, '//div[contains(text(), "(P)") or contains(text(), "℗")]').text

        # Check if "Aditya Music" is in the copyright text (ignore case and symbols)
        if "aditya music" in copyright_text.lower():
            aditya_music_count += 1
    except Exception as e:
        print(f"Could not retrieve copyright information for {song_url}: {e}")

# Print the count of songs under "Aditya Music"
print(f"Total count of songs under 'Aditya Music': {aditya_music_count}")

# Close the browser
driver.quit()
