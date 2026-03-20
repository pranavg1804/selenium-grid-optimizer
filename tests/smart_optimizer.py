import requests
from selenium import webdriver
import threading
import time

GRID_URL = "http://localhost:4444/wd/hub"
STATUS_URL = "http://localhost:4444/status"


def get_free_browser():
    response = requests.get(STATUS_URL).json()

    nodes = response["value"]["nodes"]

    for node in nodes:
        for slot in node["slots"]:
            if slot["session"] is None:
                # identify browser type
                browser = slot["stereotype"]["browserName"]
                return browser

    # fallback if all busy
    return "chrome"


def run_test(test_id):
    browser = get_free_browser()

    if browser == "chrome":
        options = webdriver.ChromeOptions()
    else:
        options = webdriver.FirefoxOptions()

    print(f"Test {test_id} assigned to {browser}")

    driver = webdriver.Remote(
        command_executor=GRID_URL,
        options=options
    )

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