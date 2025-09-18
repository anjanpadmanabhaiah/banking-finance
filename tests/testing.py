from selenium import webdriver
from selenium.webdriver.common.by import By
import sys
import time

APP_URL = "http://3.139.90.117:8085"  

try:
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # run without browser window
    driver = webdriver.Chrome(options=options)

    driver.get(APP_URL)
    time.sleep(2)

    # ✅ Test 1: Home Page Title
    assert "Customer Banking Services".upper() in driver.page_source.upper()
    print("✅ Home page loaded correctly")

    # ✅ Test 2: Navigation Menu
    nav_items = ["HOME", "ABOUT", "SERVICES", "TEAM", "CONTACT US"]
    for item in nav_items:
        assert item in driver.page_source.upper()
    print("✅ Navigation menu contains all items")

    # ✅ Test 3: Buttons
    read_more = driver.find_element(By.XPATH, "//button[contains(text(),'READ MORE')]")
    contact_us = driver.find_element(By.XPATH, "//button[contains(text(),'CONTACT US')]")
    assert read_more.is_displayed() and contact_us.is_displayed()
    print("✅ Buttons are present")

    driver.quit()
    sys.exit(0)  # success for Jenkins

except Exception as e:
    print(f"❌ Test failed: {e}")
    sys.exit(1)  # fail Jenkins stage

