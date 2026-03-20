from selenium import webdriver
import time

GRID_URL = "http://localhost:4444/wd/hub"

options = webdriver.ChromeOptions()

driver = webdriver.Remote(
    command_executor=GRID_URL,
    options=options
)

driver.get("https://www.google.com")

print("Page Title:", driver.title)

# keep browser open for 15 seconds
time.sleep(15)

driver.quit()