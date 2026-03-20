from selenium import webdriver
import threading
import time

GRID_URL = "http://localhost:4444/wd/hub"

# simple round-robin logic
browsers = ["chrome", "firefox"]
index = 0
lock = threading.Lock()

def get_browser():
    global index
    with lock:
        browser = browsers[index]
        index = (index + 1) % len(browsers)
    return browser

def run_test(test_id):
    browser = get_browser()

    if browser == "chrome":
        options = webdriver.ChromeOptions()
    else:
        options = webdriver.FirefoxOptions()

    driver = webdriver.Remote(
        command_executor=GRID_URL,
        options=options
    )

    print(f"Test {test_id} running on {browser}")

    driver.get("https://www.google.com")

    time.sleep(10)

    driver.quit()

threads = []

for i in range(6):
    t = threading.Thread(target=run_test, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()