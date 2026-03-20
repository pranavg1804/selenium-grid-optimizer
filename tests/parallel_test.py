from selenium import webdriver
import threading
import time

GRID_URL = "http://localhost:4444/wd/hub"

def run_test(test_id):
    options = webdriver.ChromeOptions()

    driver = webdriver.Remote(
        command_executor=GRID_URL,
        options=options
    )

    print(f"Test {test_id} started")

    driver.get("https://www.google.com")

    time.sleep(10)

    print(f"Test {test_id} completed")

    driver.quit()

# Create multiple threads (parallel tests)
threads = []

for i in range(10):   # change number to increase load
    t = threading.Thread(target=run_test, args=(i,))
    threads.append(t)
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()